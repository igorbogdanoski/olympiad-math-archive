import mkTranslations from '../data/locales/mk.json';
import { t } from './i18n';

interface TestResult {
  key: string;
  status: 'pass' | 'fail' | 'missing';
  message?: string;
}

export function testLocalizationCompleteness(): TestResult[] {
  const results: TestResult[] = [];

  // Test all keys in mk.json are accessible via t()
  function testKeys(obj: any, prefix = ''): void {
    for (const key in obj) {
      const fullKey = prefix ? `${prefix}.${key}` : key;
      if (typeof obj[key] === 'object' && obj[key] !== null) {
        testKeys(obj[key], fullKey);
      } else {
        const translated = t(fullKey);
        if (translated === fullKey) {
          results.push({
            key: fullKey,
            status: 'missing',
            message: 'Translation key not found or returns key as fallback'
          });
        } else {
          results.push({
            key: fullKey,
            status: 'pass'
          });
        }
      }
    }
  }

  testKeys(mkTranslations);

  return results;
}

export function testPlaceholderConsistency(): TestResult[] {
  const results: TestResult[] = [];
  const placeholderRegex = /\{\{(\w+)\}\}/g;

  function checkPlaceholders(obj: any, prefix = ''): void {
    for (const key in obj) {
      const fullKey = prefix ? `${prefix}.${key}` : key;
      if (typeof obj[key] === 'object' && obj[key] !== null) {
        checkPlaceholders(obj[key], fullKey);
      } else {
        const matches = obj[key].match(placeholderRegex);
        if (matches) {
          const translated = t(fullKey);
          const translatedMatches = translated.match(placeholderRegex);
          if (!translatedMatches || matches.length !== translatedMatches.length) {
            results.push({
              key: fullKey,
              status: 'fail',
              message: 'Placeholder mismatch between source and translation'
            });
          } else {
            results.push({
              key: fullKey,
              status: 'pass'
            });
          }
        }
      }
    }
  }

  checkPlaceholders(mkTranslations);

  return results;
}

export function testMacedonianSpecific(): TestResult[] {
  const results: TestResult[] = [];

  // Test number formatting
  const testNumber = 1234.56;
  const formatted = new Intl.NumberFormat('mk-MK').format(testNumber);
  if (formatted) {
    results.push({
      key: 'number_formatting',
      status: 'pass',
      message: `Number formatted as: ${formatted}`
    });
  }

  // Test date formatting
  const testDate = new Date('2025-01-01');
  const formattedDate = new Intl.DateTimeFormat('mk-MK', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  }).format(testDate);
  if (formattedDate) {
    results.push({
      key: 'date_formatting',
      status: 'pass',
      message: `Date formatted as: ${formattedDate}`
    });
  }

  // Test cultural elements presence
  const culturalKeys = ['cultural.olympiad_reference', 'cultural.macedonian_math_tradition'];
  culturalKeys.forEach(key => {
    const translated = t(key);
    if (translated !== key) {
      results.push({
        key,
        status: 'pass',
        message: `Cultural element present: ${translated}`
      });
    } else {
      results.push({
        key,
        status: 'fail',
        message: 'Cultural element missing'
      });
    }
  });

  return results;
}

export function runLocalizationTests(): { completeness: TestResult[], placeholders: TestResult[], macedonian: TestResult[] } {
  return {
    completeness: testLocalizationCompleteness(),
    placeholders: testPlaceholderConsistency(),
    macedonian: testMacedonianSpecific()
  };
}

export function printTestResults(results: TestResult[]): void {
  console.log('Localization Test Results:');
  console.log('=========================');

  const passed = results.filter(r => r.status === 'pass').length;
  const failed = results.filter(r => r.status === 'fail').length;
  const missing = results.filter(r => r.status === 'missing').length;

  console.log(`Passed: ${passed}, Failed: ${failed}, Missing: ${missing}`);

  results.forEach(result => {
    const icon = result.status === 'pass' ? '✅' : result.status === 'fail' ? '❌' : '⚠️';
    console.log(`${icon} ${result.key}: ${result.message || result.status}`);
  });
}