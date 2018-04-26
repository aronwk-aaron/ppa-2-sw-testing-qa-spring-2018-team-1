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
