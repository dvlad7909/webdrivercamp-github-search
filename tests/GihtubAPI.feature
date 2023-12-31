# Created by dvlad at 12/19/2023
@no_browser
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
      | No of Repos | 13  |

  Scenario: Create Gist
    Given Load payload from gist_payload.json file with updated values
      | description | Gist created with api 2 |
      | public      | true                    |
    When Send POST request with authentication to https://api.github.com/gists
      | scope | gist |
    And Save gist id
    Then Verify response value
      | status code | 201 |

  Scenario: Delete Gist
    When Send DELETE Gist request with authentication to https://api.github.com/gists/
    Then Verify response value
      | status code | 204 |

  Scenario: Create Repo
    Given Load payload from repo_payload.json file with updated values
      | name     | repo-created-with-api |
      | private  | true                  |
      | has_wiki | false                 |
    When Send POST request with authentication to https://api.github.com/user/repos
    Then Verify response value
      | status code | 201 |

  Scenario: Get created Repo
    When Send GET request with authentication to https://api.github.com/repos/{owner}/{repo}
    Then Verify response value
      | status code | 200 |

  Scenario: Update created Repo
    Given Load payload from repo_payload.json file with added values
      | description | I know Python Requests! |
    When Send PATCH request with authentication to https://api.github.com/repos/{owner}/{repo}
    Then Verify response value
      | status code | 200 |

  Scenario: Delete Repo
    When Send DELETE Repo request with authentication to https://api.github.com/repos/{owner}/{repo}
    Then Verify response value
      | status code | 204 |

  Scenario: Planets data verification
    When Send GET request to https://swapi.dev/api/planets/
    Then Verify response value
      | status code | 200 |