
import { createPinia, setActivePinia } from 'pinia';
import { mount } from '@cypress/vue';
import SigninView from './SigninView.vue'; // Adjust the path as necessary
import { useUserStore } from '../../stores/userStore.ts'; // Adjust the path as necessary

describe('<SigninView />', () => {
  beforeEach(() => {
    setActivePinia(createPinia()); // Set active Pinia before each test

    // Mock API for successful login
    cy.intercept('POST', '/rest-auth/login/', (req) => {
      req.reply((res) => {
        res.send({
          user: { pk: 1, email: 's@gmail.com' }, // Mock user data
          access: 'access',
          refresh: 'refresh',
        });
      });
    }).as('loginRequest'); // Intercept the login request
    cy.intercept('GET', '/api/users/*', {
      statusCode: 200,
      body: { /* your mock user data */ }
    }).as('getUserRequest');
  });


  it('renders the login form', () => {
    mount(SigninView);

    cy.get('input[type="email"]')
      .should('exist')
      .and('have.attr', 'placeholder', 'Enter your email');

    cy.get('input[type="password"]')
      .should('exist')
      .and('have.attr', 'placeholder', '6+ Characters, 1 Capital letter');

    cy.get('input[type="submit"]')
      .should('exist')
      .and('have.value', 'Sign In');
  });

  it('logs in the user successfully', () => {
    mount(SigninView);

    cy.get('input[type="email"]').type('s@gmail.com');
    cy.get('input[type="password"]').type('s'); // Use valid password
    cy.get('input[type="submit"]').click();

    cy.wait('@loginRequest'); // Wait for the login request to complete

    // Confirm that user data is stored properly in Pinia store
    cy.window().then(() => {
      const userStore = useUserStore();
      expect(userStore.user).to.deep.equal({ pk: 1, email: 's@gmail.com' }); // Expect the user in store
    });

    // Confirm that user data is stored in localStorage
    cy.window().then((win) => {
      expect(win.localStorage.getItem('access')).to.equal('access');
      expect(win.localStorage.getItem('refresh')).to.equal('refresh');
      expect(JSON.parse(win.localStorage.getItem('user'))).to.deep.equal({ pk: 1, email: 's@gmail.com' });
    });

    cy.url().should('include', '/'); // Check redirection to profile page
  });

  it('shows error message on login failure', () => {
    cy.intercept('POST', '/rest-auth/login/', {
      statusCode: 401,
      body: { message: 'Unauthorized' },
    }).as('loginRequestFailed');

    mount(SigninView);

    cy.get('input[type="email"]').type('s@gmail.com');
    cy.get('input[type="password"]').type('s');
    cy.get('input[type="submit"]').click();

    cy.wait('@loginRequestFailed');


  });
});
