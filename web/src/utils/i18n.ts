import mk from '../data/locales/mk.json';

const translations: Record<string, any> = {
  mk
};

export type Locale = 'mk';

export function t(key: string, locale: Locale = 'mk'): string {
  const keys = key.split('.');
  let current: any = translations[locale];
  
  for (const k of keys) {
    if (current && current[k]) {
      current = current[k];
    } else {
      return key; // Return key as fallback
    }
  }
  
  return typeof current === 'string' ? current : key;
}

export function formatNumber(num: number, locale: Locale = 'mk'): string {
  return new Intl.NumberFormat(locale === 'mk' ? 'mk-MK' : 'en-US').format(num);
}

export function formatDate(date: Date, locale: Locale = 'mk'): string {
  return new Intl.DateTimeFormat(locale === 'mk' ? 'mk-MK' : 'en-US', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  }).format(date);
}

export function formatCurrency(amount: number, currency: string = 'MKD', locale: Locale = 'mk'): string {
  return new Intl.NumberFormat(locale === 'mk' ? 'mk-MK' : 'en-US', {
    style: 'currency',
    currency
  }).format(amount);
}
