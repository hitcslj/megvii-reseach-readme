import requests
import json
import time

personal_access_token = "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" # your_personal_access_token
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f"token {personal_access_token}"
}

def get_github_user_repos(user):
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{user}/repos?per_page=200&page={page}"
        time.sleep(2)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            current_page_repos = json.loads(response.text)
            if len(current_page_repos) == 0:
                break
            repos.extend(current_page_repos)
            page += 1
        else:
            print(f"请求失败，状态码：{response.status_code}，响应文本：{response.text}")
            break
    return repos


def get_github_repo_description(user, repo):
    url = f"https://api.github.com/repos/{user}/{repo}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        repo_data = json.loads(response.text)
        return repo_data['description'], repo_data['stargazers_count']
    else:
        return "Error: Unable to fetch the repository data.", 0


def generate_markdown_table(user):
    repos = get_github_user_repos(user)
    markdown_table = "| 仓库名 | 爬取的简介 |\n|-------|-----------|\n"
    print(f'{user}:{len(repos)}')
    for repo in repos:
        repo_name = repo['name']
        description, stars_count = get_github_repo_description(user, repo_name)
        repo_url = f"https://github.com/{user}/{repo_name}"
        star_badge_url = f"https://img.shields.io/github/stars/{user}/{repo_name}?style=social"
        markdown_table += f"| [{repo_name}]({repo_url}) <a href='{repo_url}'><img src='{star_badge_url}' /></a> | {description} |\n"
    return markdown_table


def save_to_md_file(user, content):
    file_name = f"{user}.md"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Markdown内容已保存到 {file_name}")


if __name__ == "__main__":
    # users_input = input("请输入多个GitHub用户名（以逗号分隔）：")
    # users = [user.strip() for user in users_input.split(',')]
    users = ['megvii-research','megvii-model','Megvii-BaseDetection','MegEngine','MegviiRobot']
    for user in users:
        markdown_table = generate_markdown_table(user)
        print(markdown_table)
        save_to_md_file(user, markdown_table)