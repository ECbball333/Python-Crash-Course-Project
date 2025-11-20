from operator import itemgetter
import requests

# Get list of top story IDs
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")
submission_ids = r.json()

submission_dicts = []

for submission_id in submission_ids[:30]:  # Limit to top 30
    item_url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(item_url)
    print(f"Status code: {r.status_code}")
    response_dict = r.json()

    # Handle missing data safely
    if response_dict is None:
        continue

    submission_dict = {
        'title': response_dict.get('title', 'No Title'),
        'hn_link': f'https://news.ycombinator.com/item?id={submission_id}',
        'comments': response_dict.get('descendants', 0),
    }
    submission_dicts.append(submission_dict)

# Sort by number of comments
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Print top stories
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
