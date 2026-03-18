# Day 4: GitHub Fetcher + Weather CLI

Two command-line tools that interact with external APIs to fetch real-world data.

## Example Outputs

### GitHub Fetcher
```bash
$ python3 exercise1.py octocat
Username: octocat
Bio: None
Public Repos: 8
Followers: 22086

Top 5 Repositories:
- Spoon-Knife 13675 | HTML
- Hello-World 3531 | None
- octocat.github.io 1063 | CSS
- hello-worId 723 | None
- linguist 699 | Ruby
```

### Weather CLI
```bash
$ python3 exercise2.py "New York"
Raw Geocoding Response:
{'results': [{'id': 5128581, 'name': 'New York', 'latitude': 40.71427, 'longitude': -74.00597, 'elevation': 10.0, 'feature_code': 'PPL', 'country_code': 'US', 'admin1_id': 5128638, 'timezone': 'America/New_York', 'population': 8804190, 'postcodes': ['10001', '10002', '10003', '10004', '10005', '10006', '10007', '10008', '10009', '10010', '10011', '10012', '10013', '10014', '10016', '10017', '10018', '10019', '10020', '10021', '10022', '10023', '10024', '10025', '10026', '10027', '10028', '10029', '10030', '10031', '10032', '10033', '10034', '10035', '10036', '10037', '10038', '10039', '10040', '10041', '10043', '10044', '10045', '10055', '10060', '10065', '10069', '10080', '10081', '10087', '10090', '10101', '10102', '10103', '10104', '10105', '10106', '10107', '10108', '10109', '10110', '10111', '10112', '10113', '10114', '10115', '10116', '10117', '10118', '10119', '10120', '10121', '10122', '10123', '10124', '10025', '10126', '10128', '10129', '10130', '10131', '10132', '10133', '10138', '10150', '10151', '10152', '10153', '10154', '10155', '10156', '10157', '10158', '10159', '10160', '10161', '10162', '10163', '10164', '10165', '10166', '10167', '10168', '10169', '10170', '10171', '10172', '10173', '10174', '10175', '10176', '10177', '10178', '10179', '10185', '10199', '10203', '10211', '10212', '10213', '10242', '10249', '10256', '10258', '10259', '10260', '10261', '10265', '10268', '10269', '10270', '10271', '10272', '10273', '10274', '10275', '10276', '10277', '10278', '10279', '10280', '10281', '10282', '10285', '10286'], 'country_id': 6252001, 'country': 'United States', 'admin1': 'New York'}, ...]

Raw Weather Response:
{'latitude': 40.710335, 'longitude': -73.99308, 'generationtime_ms': 0.0985860824584961, 'utc_offset_seconds': 0, 'timezone': 'GMT', 'timezone_abbreviation': 'GMT', 'elevation': 51.0, 'current_weather_units': {'time': 'iso8601', 'interval': 'seconds', 'temperature': '°C', 'windspeed': 'km/h', 'winddirection': '°', 'is_day': '', 'weathercode': 'wmo code'}, 'current_weather': {'time': '2026-03-18T16:45', 'interval': 900, 'temperature': 1.3, 'windspeed': 6.6, 'winddirection': 13, 'is_day': 1, 'weathercode': 3}}

City: New York
Temperature: 1.3 °C / 34.34 °F
Wind Speed: 6.6 km/h
```

## What Was the Hardest Part of Reading the API Response?

The hardest part was **navigating the nested JSON structure and identifying the exact fields needed**:

### GitHub API Challenges:
- **Multiple API calls**: Had to make two separate requests (user info + repos) and combine the data
- **Repository sorting**: Needed to understand the `stargazers_count` field and implement proper sorting
- **Null values**: Some repositories had `null` for language, requiring graceful handling

### Weather API Challenges:
- **Two-step process**: First geocoding to get coordinates, then weather data using those coordinates
- **Nested structure**: Weather data was buried under `current_weather` within the response
- **Multiple results**: Geocoding returned multiple cities with the same name, had to pick the first result
- **Field names**: Had to dig through the response to find `temperature` and `windspeed` fields

### Key Learning:
API documentation is crucial, but sometimes you need to **print the raw response** to understand the actual structure. The debug prints in the weather script helped identify the correct path to the data.