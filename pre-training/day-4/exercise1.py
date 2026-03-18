# github_fetcher.py

import requests
import sys

def fetch_github_user(username):
    try:
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url)

        if response.status_code == 404:
            print("User not found.")
            return

        if response.status_code == 403:
            print("Rate limit exceeded. Try again later.")
            return

        response.raise_for_status()

        data = response.json()

        print("Username:", data["login"])
        print("Bio:", data["bio"])
        print("Public Repos:", data["public_repos"])
        print("Followers:", data["followers"])

        
        repos_url = f"https://api.github.com/users/{username}/repos?per_page=100&sort=stars"
        repos_response = requests.get(repos_url)
        repos = repos_response.json()

        top_repos = sorted(repos, key=lambda r: r["stargazers_count"], reverse=True)[:5]

        print("\nTop 5 Repositories:")
        for repo in top_repos:
            print(f"- {repo['name']} {repo['stargazers_count']} | {repo['language']}")

    except requests.exceptions.RequestException:
        print("Network error. Check your internet connection.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python github_fetcher.py <username>")
    else:
        fetch_github_user(sys.argv[1])