describe('Testing Distance', function() {
  it('Calculates distance between two points', function(){
    cy.visit('/distance')

    cy.get('input#x1')
      .type('0')

    cy.get('input#y1')
      .type('0')

    cy.get('input#x2')
      .type('5')

    cy.get('input#y2')
      .type('5')

    cy.contains("Submit")
      .click()

    cy.get('h5')
      .should('contain', 'The shortest distance between your two points is:')

  })
})

describe('Testing e-mail', function() {
  it('Checks to see if an email is vailid', function(){
    cy.visit('/email')

    cy.get('input#email_input')
      .type('ajm712@msstate.edu')

    cy.contains("Submit")
      .click()

    cy.get('h5')
      .should('contain', 'Email is Validated')

  })
})

describe('Testing BMI', function() {
  it('Calculates BMI given height and weight', function(){
    cy.visit('/bmi')

    cy.get('input#f')
      .type('5')

    cy.get('input#i')
      .type('7')

    cy.get('input#p')
      .type('150')

    cy.contains("Submit")
      .click()

    cy.get('h5')
      .should('contain', 'Your BMI:')

  })
})

describe('Testing Retirement Savings', function() {
  it('Calculates the age you will be to save up a certain amount', function(){
    cy.visit('/retirement')

    cy.get('input#age')
      .type('23')

    cy.get('input#salary')
      .type('60000')

    cy.get('input#percent')
      .type('10')

    cy.get('input#goal')
      .type('100000')

    cy.contains("Submit")
      .click()

    cy.get('h5')
      .should('contain', 'You will meet your savings goal at age 35')

  })
})

describe('Testing Split the Tip', function() {
  it('Calculates what each guest need to pay given the bill amoutn and number of guests', function(){
    cy.visit('/tip')

    cy.get('input#bill')
      .type('6000')

    cy.get('input#guests')
      .type('15')

    cy.contains("Submit")
      .click()

    cy.get('h5')
      .should('contain', 'These are the bills for each guest.')

  })
})
