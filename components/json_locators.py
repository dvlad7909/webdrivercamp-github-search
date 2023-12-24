class JsonLocators:
    file_name = "json_response.json"
    number_of_repos_json = "$.public_repos"
    number_of_followers_json = "$.followers"
    number_of_following_json = "following"
    number_of_gists_json = "public_gists"
    followers_logins_json = "$[*].login"
    followers_links_json = "$[*].html_url"

    all_repos = "$.items"
    number_of_repos = "$..owner.login" # "$.total_count"
    owners_logins = "$..owner.login"
