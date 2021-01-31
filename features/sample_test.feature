#noinspection CucumberUndefinedStep
Feature: Test CRUD methods with a test api framework.

  Background:
    Given the REST API url is set

  Scenario: POST example
      Given POST post api endpoint is set
      When The HEADER param request content type is set as "application/json"
      And body request is set
      And POST HTTP request is sent
      Then a valid HTTP response with code 201 for "POST" is recieved


