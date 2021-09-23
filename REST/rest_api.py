import requests
import json


response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
for item in response.json()['items']:
    if item['answer_count'] == 0:
        print(item['title'])
        print(item['link'])
    else:
        print("skipped")
    # print()