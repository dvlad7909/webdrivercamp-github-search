# Created by D. Vladimirov at 11/30/2023
Feature: Summary fields

  Background: Test prerequisites
    Given Navigate to https://gh-users-search.netlify.app/

  Scenario Outline: Verify number of repos UI vs API
    When UI: Input <user_name> into search field
    And UI: Click Search button
    And API: send get request to <user_name>
    And API: verify status code is 200
    Then Verify repos field values

    Examples:
      | user_name   |
      | dvlad7909   |
      | dmitriivlad |
      # | ab054       |

  Scenario: Verify data is updated on page refresh
    When UI: Input dvlad7909 into search field
    And UI: Click Search button
    And API: send get request to dvlad7909
    And API: verify status code is 200
    And API: send post request to dvlad7909 to add 1 more repo
    And API: verify status code is 201
    And API: send get request to dvlad7909
    And API: verify status code is 200
    And UI: refresh page
    Then Verify repos field values