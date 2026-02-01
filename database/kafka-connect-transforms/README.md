# Kafka Connect Custom Transforms

This module contains custom Single Message Transforms (SMTs) for the Olympiad Math Archive Kafka Connect setup.

## Denormalize Transform

The `Denormalize` transform groups fields with common prefixes into nested objects, facilitating relational-to-document mapping and denormalization.

### Configuration

- `prefixes`: List of prefixes to group fields. Format: `prefix:field_name` where `prefix` is the field prefix (e.g., "competition_") and `field_name` is the name of the nested object field.
- `flatten`: Boolean to flatten nested structures (not implemented yet).
- `add.timestamp`: Boolean to add a `processed_at` timestamp field.

### Example

If the input record has fields:
- `competition_id`
- `competition_name`
- `competition_year`
- `problem_title`

With `prefixes: ["competition:competition_details"]`, the output will have:
- `competition_details`: { id, name, year }
- `problem_title`

### Building

Run `mvn clean package` to build the JAR. Place the JAR in the Kafka Connect classpath.