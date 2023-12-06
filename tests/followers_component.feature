# Created by Dmitrii Vladimirov at 12/5/2023

Feature: Followers component

  Background: Test prerequisites
    Given Navigate to https://gh-users-search.netlify.app/

  Scenario Outline: Verify max number of followers UI vs API
    When UI: Input <user_name> into search field
    And UI: Click Search button
    And API: send get request to <user_name>/followers?per_page=100
    And API: verify status code is 200
    Then Verify number of followers

    Examples:
      | user_name   |
    #  | dvlad7909   |
    #  | dmitriivlad |
      | ab054       |
    #  |stas00       |

  Scenario Outline: Verify each follower has user name UI vs API
    When UI: Input <user_name> into search field
    And UI: Click Search button
    And API: send get request to <user_name>/followers?per_page=100
    And API: verify status code is 200
    Then Verify logins of followers

    Examples:
      | user_name   |
      | dvlad7909   |
      | dmitriivlad |
      # | ab054       |
      |stas00       |

  Scenario Outline: Verify each follower has user link UI vs API
    When UI: Input <user_name> into search field
    And UI: Click Search button
    And API: send get request to <user_name>/followers?per_page=100
    And API: verify status code is 200
    Then Verify links_text of followers

    Examples:
      | user_name   |
      | dvlad7909   |
      | dmitriivlad |
      | ab054       |
      |stas00       |

  Scenario Outline: Verify each link redirects to correspondent url UI vs API
    When UI: Input <user_name> into search field
    And UI: Click Search button
    And API: send get request to <user_name>/followers?per_page=100
    And API: verify status code is 200
    Then Verify links_value of followers

    Examples:
      | user_name   |
      | dvlad7909   |
      | dmitriivlad |
      # | ab054       |
      |stas00       |

  Scenario: Verify followers data is updated on page refresh
    When UI: Input dmitriivlad into search field
    And UI: Click Search button
    And API: send get request to dmitriivlad
    And API: verify status code is 200
    And API: add dvlad7909 follows dmitriivlad
    And API: verify status code is 204
    And API: send get request to dmitriivlad
    And API: verify status code is 200
    And UI: refresh page
    Then Verify number of followers