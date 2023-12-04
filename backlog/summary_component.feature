
Scenario: Verify followers data is updated on page refresh
    When UI: Input dvlad7909 into search field
    And UI: Click Search button
    And API: send get request to dvlad7909
    And API: verify status code is 200
    And Add 1 more follower to dvlad7909
    And API: send get request to dvlad7909
    And API: verify status code is 200
    And UI: refresh page
    Then Verify followers field values

Scenario: Verify following data is updated on page refresh
    When UI: Input dvlad7909 into search field
    And UI: Click Search button
    And API: send get request to dvlad7909
    And API: verify status code is 200
    And Add 1 more following to dvlad7909
    And API: send get request to dvlad7909
    And API: verify status code is 200
    And UI: refresh page
    Then Verify following field values