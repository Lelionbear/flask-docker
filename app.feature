Feature: Deployable Flask webpage
  A webpage that shows the number of visits it has obtained

  Scenario: Requesting basic response from the Flask app
    When the flask app is requested
    Then the response status code is 200
    And the response content has data


  Scenario: Ensure that the count is changing
    When the flask app is imported
    Then the current count is read
    And count is incremented by a value of one