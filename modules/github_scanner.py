# modules/github_scanner.py

import requests

SENSITIVE_KEYWORDS = ["apikey", "secret", "token", "password", "aws_access_key_id"]


def scan_github(target, token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    repos_url = f"https://api.github.com/users/{target}/repos"
    repos_response = requests.get(repos_url, headers=headers)

    if repos_response.status_code != 200:
        print("[!] Failed to retrieve repositories.")
        return []

    repos = repos_response.json()
    findings = []

    for repo in repos:
        repo_name = repo['name']
        contents_url = f"https://api.github.com/repos/{target}/{repo_name}/contents"
        contents_response = requests.get(contents_url, headers=headers)

        if contents_response.status_code != 200:
            continue

        contents = contents_response.json()
        for file in contents:
            if file['type'] != 'file':
                continue
            filename = file['name'].lower()
            match_in_name = any(keyword in filename for keyword in SENSITIVE_KEYWORDS)
            file_url = file['download_url']

            match_in_content = False
            try:
                content_response = requests.get(file_url)
                if content_response.status_code == 200:
                    content_text = content_response.text.lower()
                    if any(keyword in content_text for keyword in SENSITIVE_KEYWORDS):
                        match_in_content = True
            except:
                pass

            if match_in_name or match_in_content:
                findings.append({
                    'repository': repo_name,
                    'file': file['name'],
                    'url': file['html_url']
                })

    return findings
