# Reddit Headline Analyzer

A Python script that fetches top posts from the r/technology subreddit and analyzes their headlines for word frequency, upvote statistics, and posting patterns.

## What It Does

- Fetches the top 50 posts from r/technology using Reddit's JSON API
- Analyzes word frequency across all post titles (excluding common stopwords)
- Identifies the most upvoted post and calculates average upvotes
- Categorizes posts by whether they were posted today or on previous dates
- Saves all results to a `report.json` file

## How to Run

1. Make sure you have Python 3 installed
2. Install the required dependency:
   ```bash
   pip install requests
   ```
3. Run the script:
   ```bash
   python3 reddit-analyzer.py
   ```

The script will generate a `report.json` file in the same directory with the analysis results.

## Example Output

```json
{
    "top_words": [
        ["ai", 8],
        ["new", 7],
        ["says", 6],
        ["into", 5],
        ["foreign-made", 4],
        ["routers", 4],
        ["apple", 4],
        ["tech", 4],
        ["just", 3],
        ["bans", 3],
        ["now", 3],
        ["fcc", 3],
        ["about", 3],
        ["out", 3],
        ["online", 2],
        ["pay", 2],
        ["billion", 2],
        ["wind", 2],
        ["internet", 2],
        ["intuit", 2]
    ],
    "upvotes_stats": {
        "most_upvoted_title": "A High School Student Just Built a Water Filter That Removes 96% of Microplastics, Without Expensive Equipment",
        "most_upvotes": 23886,
        "average_upvotes": 1675.26
    },
    "posts_by_date": {
        "today": 22,
        "older": 28
    }
}
```

## Functions

- `fetch_reddit_posts()`: Fetches posts from Reddit API with error handling
- `parse_posts()`: Extracts relevant data (title, upvotes, timestamp) from posts
- `word_frequency()`: Counts word frequency across titles, excluding stopwords
- `analyze_upvotes()`: Calculates upvote statistics
- `posts_today()`: Categorizes posts by date
- `generate_report()`: Creates and saves the analysis report

## Error Handling

The script includes comprehensive error handling for:
- API response errors
- Empty data sets
- File writing operations

If any errors occur during data fetching, the script will print an informative message and exit gracefully.
