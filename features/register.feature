Feature: register feature

  Background:
    Given I am on the https://automationexercise.com/ page

  Scenario: Verify that home page is visible
    Then Home page should be visible successfully

  Scenario: Check Signup/Login button
    When I click on "Signup / Login" button
    Then "New User Signup!" should be visible

  Scenario: Signup with new name and email
    When I click on "Signup / Login" button
    And I enter name
    And I enter email
    And I click "Signup" button
    Then "ENTER ACCOUNT INFORMATION" should be visible
    When I fill details: Title, Name, Email, Password, Date of birth
    And I select checkbox "Sign up for our newsletter!"
    And I select checkbox "Receive special offers from our partners!"
    And I fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    And I click "Create Account button"
    Then "ACCOUNT CREATED!" should be visible
    When I click "Continue" button
    Then "Logged in as username" should visible
    When I click "Delete Account" button
    Then "ACCOUNT DELETED!" should be visible

  Scenario: Register user with existing email
    Then Home page should be visible successfully
    When I click on "Signup / Login" button
    And I enter name
    And I enter email
    And I click "Signup" button
    Then "ENTER ACCOUNT INFORMATION" should be visible
    When I fill details: Title, Name, Email, Password, Date of birth
    And I select checkbox "Sign up for our newsletter!"
    And I select checkbox "Receive special offers from our partners!"
    And I fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    And I click "Create Account button"
    And I delete cookies
    And I go to main page
    And I click on "Signup / Login" button
    Then "New User Signup!" should be visible
    When I Enter name and already registered email address
    And I click "Signup" button
    Then "Email Address already exist!" should be visible
