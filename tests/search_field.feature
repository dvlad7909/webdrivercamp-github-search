# Created by dvlad at 11/30/2023
Feature: Search field

  Background: Test prerequisites
    Given Navigate to https://gh-users-search.netlify.app/

  Scenario Outline: Search performed by click:
    When UI: Input <user_name> into search field
    And UI: Click Search button
    And API: send get request to <user_name> repo
    And API: verify status code is 200
    Then Verify repos field values

    Examples:
      | user_name   |
      | dvlad7909   |
      | ab054       |
      | roboflow    |

  Scenario Outline: Search performed by Enter key:
    When UI: Input <user_name> into search field
    And UI: Push Enter key
    And API: send get request to <user_name> repo
    And API: verify status code is 200
    Then Verify repos field values

    Examples:
      | user_name   |
      | dvlad7909   |

  Scenario Outline: Not valid search data
    When UI: Input <not_valid_data> into search field
    And API: send get request to user_name repo
    And API: verify status code is 404
    Then Varify empty results: no article element on the page

    Examples:
      | not_valid_data  |
      | #$%87^          |
#      | #$%87^bla       |
