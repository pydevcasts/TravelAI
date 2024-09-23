// src/axios.ts
import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000/', // آدرس API خود را وارد کنید
});

instance.interceptors.request.use((config) => {
  const token = localStorage.getItem('access'); // توکن را از storage دریافت کنید
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default instance;
