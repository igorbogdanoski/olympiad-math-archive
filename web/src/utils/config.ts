const getBaseUrl = () => {
  if (typeof window !== 'undefined') {
    return `${window.location.protocol}//${window.location.hostname}:8000`;
  }
  return 'http://localhost:8000';
};

const getAiBaseUrl = () => {
  if (typeof window !== 'undefined') {
    return `${window.location.protocol}//${window.location.hostname}:8001`;
  }
  return 'http://localhost:8001';
};

export const API_BASE_URL = import.meta.env.PUBLIC_API_URL || getBaseUrl();
export const AI_API_BASE_URL = import.meta.env.PUBLIC_AI_API_URL || getAiBaseUrl();
