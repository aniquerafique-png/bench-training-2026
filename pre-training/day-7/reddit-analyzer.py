import requests
import json
from collections import Counter
from datetime import datetime, timezone

STOPWORDS = {"the", "a", "to","in","of","for","and","on","is","with","at","by","are","was","as","it","that","this","these","those","he","she","they","we","you","i","us","them","their","our","your","my","his","her","its","its","it's","from","an","what","have"}

URL = "https://reddit.com/r/technology/top.json?limit=50"

def fetch_reddit_posts(url=URL):
    headers = {"User-Agent": "RedditHeadlineAnalyser/0.1"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data["data"]["children"]
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def parse_posts(posts):
    result = []
    for post in posts:
        data = post["data"]
        result.append({
            "title": data["title"],
            "ups": data["ups"],
            "created_utc": data["created_utc"]
        })
    return result

def word_frequency(posts):
    counter = Counter()
    for post in posts:
        words = post["title"].lower().split()
        words = [w.strip(".,!?()[]") for w in words if w not in STOPWORDS]
        counter.update(words)
    return counter.most_common(20)

def analyze_upvotes(posts):
    if not posts:
        return {}
    most_upvoted = max(posts, key=lambda x: x["ups"])
    avg_upvotes = sum(p["ups"] for p in posts) / len(posts)
    return {
        "most_upvoted_title": most_upvoted["title"],
        "most_upvotes": most_upvoted["ups"],
        "average_upvotes": avg_upvotes
    }

def posts_today(posts):
    today_count = 0
    now = datetime.now(timezone.utc)
    for p in posts:
        post_date = datetime.fromtimestamp(p["created_utc"], tz=timezone.utc)
        if post_date.date() == now.date():
            today_count += 1
    return {
        "today": today_count,
        "older": len(posts) - today_count
    }

def generate_report(posts):
    report = {
        "top_words": word_frequency(posts),
        "upvotes_stats": analyze_upvotes(posts),
        "posts_by_date": posts_today(posts),
        "generated_at": datetime.now(timezone.utc).isoformat()
    }
    try:
        with open("report.json", "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)
        print("Report generated: report.json")
    except IOError as e:
        print(f"Error saving report: {e}")

def main():
    posts = fetch_reddit_posts()
    if not posts:
        print("No posts fetched. Exiting.")
        return
    parsed_posts = parse_posts(posts)
    generate_report(parsed_posts)

if __name__ == "__main__":
    main()