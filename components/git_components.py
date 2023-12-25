import requests
import components.git_token_and_user


class GitComponents:

    def delete_repo(self):
        token = f'token {components.git_token.GitToken.git_token}'
        header_content = {'Authorization': token}
        owner = 'dvlad7909'
        repo = 'repo-created-with-api'
        url = f'https://api.github.com/repos/{owner}/{repo}'
        response = requests.delete(url, headers=header_content)

    def delete_gist(self, context):
        g_id = context.feature.gist_id
        token = f'token {components.git_token.GitToken.gists_token}'
        url = f'https://api.github.com/gists/{g_id}'
        header_content = {'Authorization': token}
        response = requests.delete(url, headers=header_content)

    def delete_following(self):
        username = 'dmitriivlad'
        gists_url = f'https://api.github.com/user/following/{username}'
        token = f'token {components.git_token.GitToken.follow_token}'
        header_content = {'Authorization': token}
        response = requests.delete(gists_url, headers=header_content)
