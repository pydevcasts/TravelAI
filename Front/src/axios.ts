// src/axios.ts
import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000/', // آدرس API خود را وارد کنید
});

// افزودن interceptor برای درخواست
instance.interceptors.request.use((config) => {
  const token = localStorage.getItem('access'); // توکن را از storage دریافت کنید
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
}, (error) => {
  return Promise.reject(error);
});

// افزودن interceptor برای پاسخ
instance.interceptors.response.use((response) => {
  return response;
}, async (error) => {
  const originalRequest = error.config;

  // بررسی اینکه آیا خطا به دلیل توکن نامعتبر است
  if (error.response && error.response.data.code === 'token_not_valid') {
    const refreshToken = localStorage.getItem('refresh'); // توکن تازه را از storage بگیرید

    if (refreshToken) {
      try {
        const response = await axios.post('/rest-auth/token/refresh/', { refresh: refreshToken });
        localStorage.setItem('access', response.data.access); // توکن جدید را ذخیره کنید
console.log(response, 1111111111111111)
        // به روز رسانی هدر Authorization در درخواست اصلی
        originalRequest.headers.Authorization = `Bearer ${response.data.access}`;
        
        // دوباره درخواست اصلی را ارسال کنید
        return instance(originalRequest);
      } catch (refreshError) {
        console.error('Failed to refresh token:', refreshError);
        // کاربر را به صفحه ورود هدایت کنید
        // Redirect to login page or handle accordingly
      }
    }
  }
  
  return Promise.reject(error);
});

export default instance;
