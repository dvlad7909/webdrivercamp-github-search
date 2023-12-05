# Created by Dmitrii Vladimirov at 12/5/2023

Feature: Followers component

  Scenario Outline: Verify max number of followers UI vs API
    When UI: Input <user_name> into search field
    And UI: Click Search button

    Examples:
      | user_name   |
      | dvlad7909   |
      | dmitriivlad |
      # | ab054       |
      |stas00       |

  Scenario Outline: Verify each follower has user name UI vs API
    When UI: Input <user_name> into search field
    And UI: Click Search button

    Examples:
      | user_name   |
      | dvlad7909   |
      | dmitriivlad |
      # | ab054       |
      |stas00       |

  Scenario Outline: Verify each follower has user link UI vs API
    When UI: Input <user_name> into search field
    And UI: Click Search button

    Examples:
      | user_name   |
      | dvlad7909   |
      | dmitriivlad |
      # | ab054       |
      |stas00       |

  Scenario Outline: Verify each link redirects to correspondent url UI vs API
    When UI: Input <user_name> into search field
    And UI: Click Search button

    Examples:
      | user_name   |
      | dvlad7909   |
      | dmitriivlad |
      # | ab054       |
      |stas00       |

  Scenario: Verify followers data is updated on page refresh
    When UI: Input dvlad7909 into search field
    And UI: Click Search button