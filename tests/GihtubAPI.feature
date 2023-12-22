# Created by dvlad at 12/19/2023
Feature: GitHub API
  # Enter feature description here

  Scenario: Get all repos
    When Send GET request to https://api.github.com/search/repositories
      | q | webdrivercamp-learning-python |
    And Verify response value
      | status code | 200       |
      | No of Repos | 23        |
      | name        | dvlad7909 |

  Scenario: Get repo with authentication
    When Send GET request with authentication to https://api.github.com/user/repos
    Then Verify response value
      | status code | 200 |
      | No of Repos | 11  |

  Scenario: Create Gist
    Given Load payload from <string> file with updated values
      | description | Gist created with api |
      | public      | True                  |
    When Send POST request with authentication to https://api.github.com/gists
      | scope | gist |
    Then Verify response value
      | status code | 201 |

  Scenario: Create Repo
    Given Load payload from payload.json file with updated values
      | name     | repo-created-with-api |
      | private  | True                  |
      | has_wiki | False                 |
    When Send POST request with authentication to https://api.github.com/user/repos
    Then Verify response value
      | status code | 201 |

  Scenario: Get created Repo
    When Send GET request with authentication to https://api.github.com/repos/{owner}/{repo}
      | owner  | dvlad7909                                                           |
      | repo   | repo-created-with-api                                               |
    Then Verify response value
      | status code | 200 |

  Scenario: Update created Repo
    Given Load payload from payload.json file with updated values
      | description | I know Python Requests! |
    When Send PATCH request with authentication to https://api.github.com/repos/{owner}/{repo}
      | owner  | dvlad7909                                                              |
      | repo   | repo-created-with-api                                                  |
    Then Verify response value
      | status code | 201 |

  Scenario: Delete Gist
    When Send DELETE request with authentication to https://api.github.com/gists/{id}
    Then Verify response value
      | status code | 204 |

  Scenario: Delete Repo
    When Send DELETE request with authentication to https://api.github.com/repos/{owner}/{repo}
      | owner     | dvlad7909             |
      | repo      | repo-created-with-api |
    Then Verify response value
      | status code | 204 |

  Scenario: Planets data verification
    When Send GET request to https://swapi.dev/api/planets/
    Then Verify response value
      | status code | 200 |