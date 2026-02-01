package com.olympiad.archive.transforms;

import org.apache.kafka.common.cache.Cache;
import org.apache.kafka.common.cache.LRUCache;
import org.apache.kafka.common.cache.SynchronizedCache;
import org.apache.kafka.common.config.ConfigDef;
import org.apache.kafka.common.config.ConfigException;
import org.apache.kafka.connect.connector.ConnectRecord;
import org.apache.kafka.connect.data.Field;
import org.apache.kafka.connect.data.Schema;
import org.apache.kafka.connect.data.SchemaBuilder;
import org.apache.kafka.connect.data.Struct;
import org.apache.kafka.connect.transforms.Transformation;
import org.apache.kafka.connect.transforms.util.Requirements;
import org.apache.kafka.connect.transforms.util.SchemaUtil;
import org.apache.kafka.connect.transforms.util.SimpleConfig;

import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.ArrayList;

import static org.apache.kafka.connect.transforms.util.Requirements.requireStruct;

public class Denormalize<R extends ConnectRecord<R>> implements Transformation<R> {

    public static final String OVERVIEW_DOC =
        "Denormalize relational data into nested document structures by grouping fields with common prefixes.";

    public static final ConfigDef CONFIG_DEF = new ConfigDef()
        .define("prefixes", ConfigDef.Type.LIST, ConfigDef.NO_DEFAULT, ConfigDef.Importance.HIGH,
                "List of prefixes to group fields into nested objects. Format: prefix:field_name")
        .define("flatten", ConfigDef.Type.BOOLEAN, false, ConfigDef.Importance.MEDIUM,
                "Whether to flatten nested structures")
        .define("add.timestamp", ConfigDef.Type.BOOLEAN, false, ConfigDef.Importance.LOW,
                "Add a processing timestamp field");

    private static final String PURPOSE = "denormalize relational data";

    private List<String> prefixes;
    private boolean flatten;
    private boolean addTimestamp;

    private Cache<Schema, Schema> schemaUpdateCache;

    @Override
    public void configure(Map<String, ?> props) {
        final SimpleConfig config = new SimpleConfig(CONFIG_DEF, props);
        prefixes = config.getList("prefixes");
        flatten = config.getBoolean("flatten");
        addTimestamp = config.getBoolean("add.timestamp");

        schemaUpdateCache = new SynchronizedCache<>(new LRUCache<>(16));
    }

    @Override
    public R apply(R record) {
        if (record.value() == null) {
            return record;
        }

        Struct value = requireStruct(record.value(), PURPOSE);
        Schema schema = record.valueSchema();

        Schema updatedSchema = schemaUpdateCache.get(schema);
        if (updatedSchema == null) {
            updatedSchema = makeUpdatedSchema(schema);
            schemaUpdateCache.put(schema, updatedSchema);
        }

        Struct updatedValue = makeUpdatedValue(value, schema, updatedSchema);

        return record.newRecord(record.topic(), record.kafkaPartition(), record.keySchema(), record.key(),
                                updatedSchema, updatedValue, record.timestamp());
    }

    private Schema makeUpdatedSchema(Schema schema) {
        SchemaBuilder builder = SchemaUtil.copySchemaBasics(schema, SchemaBuilder.struct());

        // Add nested objects for prefixes
        Map<String, SchemaBuilder> nestedBuilders = new HashMap<>();
        for (String prefix : prefixes) {
            String[] parts = prefix.split(":");
            if (parts.length != 2) {
                throw new ConfigException("Invalid prefix format: " + prefix + ". Expected format: prefix:field_name");
            }
            String pref = parts[0];
            String fieldName = parts[1];
            nestedBuilders.put(pref, SchemaBuilder.struct().name(fieldName));
        }

        for (Field field : schema.fields()) {
            String fieldName = field.field();
            boolean nested = false;
            for (String prefix : nestedBuilders.keySet()) {
                if (fieldName.startsWith(prefix + "_")) {
                    String nestedField = fieldName.substring(prefix.length() + 1);
                    nestedBuilders.get(prefix).field(nestedField, field.schema());
                    nested = true;
                    break;
                }
            }
            if (!nested) {
                builder.field(fieldName, field.schema());
            }
        }

        // Add nested fields
        for (Map.Entry<String, SchemaBuilder> entry : nestedBuilders.entrySet()) {
            builder.field(entry.getKey(), entry.getValue().build());
        }

        if (addTimestamp) {
            builder.field("processed_at", Schema.OPTIONAL_INT64_SCHEMA);
        }

        return builder.build();
    }

    private Struct makeUpdatedValue(Struct value, Schema schema, Schema updatedSchema) {
        Struct updatedValue = new Struct(updatedSchema);

        // Group fields into nested objects
        Map<String, Struct> nestedValues = new HashMap<>();
        for (String prefix : prefixes) {
            String[] parts = prefix.split(":");
            String pref = parts[0];
            String fieldName = parts[1];
            nestedValues.put(pref, new Struct(updatedSchema.field(pref).schema()));
        }

        for (Field field : schema.fields()) {
            String fieldName = field.field();
            Object fieldValue = value.get(fieldName);
            boolean nested = false;
            for (String prefix : nestedValues.keySet()) {
                if (fieldName.startsWith(prefix + "_")) {
                    String nestedField = fieldName.substring(prefix.length() + 1);
                    nestedValues.get(prefix).put(nestedField, fieldValue);
                    nested = true;
                    break;
                }
            }
            if (!nested) {
                updatedValue.put(fieldName, fieldValue);
            }
        }

        // Add nested structs
        for (Map.Entry<String, Struct> entry : nestedValues.entrySet()) {
            updatedValue.put(entry.getKey(), entry.getValue());
        }

        if (addTimestamp) {
            updatedValue.put("processed_at", System.currentTimeMillis());
        }

        return updatedValue;
    }

    @Override
    public ConfigDef config() {
        return CONFIG_DEF;
    }

    @Override
    public void close() {
        schemaUpdateCache = null;
    }

    public static class Value<R extends ConnectRecord<R>> extends Denormalize<R> {
        @Override
        public R apply(R record) {
            return applyWithSchema(record);
        }
    }

    public static class Key<R extends ConnectRecord<R>> extends Denormalize<R> {
        @Override
        public R apply(R record) {
            return applyWithSchema(record);
        }
    }

    private R applyWithSchema(R record) {
        return super.apply(record);
    }
}