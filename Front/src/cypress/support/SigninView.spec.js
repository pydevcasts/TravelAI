// cypress/support/component.js
import { mount } from '@cypress/vue';
import { createApp } from 'vue';
import { createPinia } from 'pinia';

Cypress.Commands.add('mount', (component) => {
  const pinia = createPinia(); // Create a new Pinia instance
  const app = createApp({});
  app.use(pinia); // Use Pinia in the app
  return mount(component, { app });
});