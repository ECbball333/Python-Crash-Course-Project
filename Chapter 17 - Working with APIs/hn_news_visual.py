from operator import itemgetter
import requests
import matplotlib.pyplot as plt

# Get top story IDs
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
submission_ids = r.json()

submission_dicts = []

# Get details for top 30 stories
for submission_id in submission_ids[:30]:
    item_url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(item_url)
    response_dict = r.json()

    if response_dict is None:
        continue

    submission_dict = {
        'title': response_dict.get('title', 'No Title'),
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants', 0),
    }
    submission_dicts.append(submission_dict)

# Sort by comment count
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Plot the results
titles = [d['title'] for d in submission_dicts]
comments = [d['comments'] for d in submission_dicts]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(titles, comments)
ax.set_title("Top Hacker News Stories by Comment Count")
ax.set_xlabel("Number of Comments")
ax.set_ylabel("Story Title")
ax.invert_yaxis()  # Highest first
plt.tight_layout()
plt.show()
