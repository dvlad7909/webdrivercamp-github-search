class Locators:
    search_input = "//input[@data-testid='search-bar']"

    search_button = "//button[@type='submit']"

    number_of_repos = "//p[contains(text(), 'repos')]//preceding-sibling::h3"

    number_of_followers = "//p[contains(text(), 'followers')]//preceding-sibling::h3"

    number_of_following = "//p[contains(text(), 'following')]//preceding-sibling::h3"

    number_of_gists = "//p[contains(text(), 'gists')]//preceding-sibling::h3"

    user_name = "//p[@class='bio']//preceding-sibling::header//child::h4"

    user_twitter = "//p[@class='bio']//preceding-sibling::header//child::p"

    user_bio = "//p[@class='bio']"

    user_company_name = "//div[@class='links']/p[1]"

    user_location = "//div[@class='links']/p[2]"

    user_blog = "//div[@class='links']/a"

    user_follow_button = "//a[contains(text(), 'follow')]"

    followers_list = "//div[@class='followers']/article"

    follower_name = "//div[@class='followers']/article[1]//child::h4"

    follower_link = "//div[@class='followers']/article[1]//child::a"
