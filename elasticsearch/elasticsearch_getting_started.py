import requests
import json


def add_single():
    url = "http://localhost:9200/logs-my_app-default/_doc?pretty"
    payload = {
        "@timestamp": "2021-05-06T16:21:15.000Z",
        "event": {
            "original": "192.0.2.42 - - [06/May/2021:16:21:15 +0000] \"GET /images/bg.jpg HTTP/1.0\" 200 24736"
        }
    }

    headers = {'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    return response.json()


def add_multiple():
    url = "http://localhost:9200/logs-my_app-default/_bulk"

    payload = [{'create': {}},
               {
                   '@timestamp': '2099-05-07T16:24:32.000Z',
                   'event': {
                       'original': '192.0.2.242 - - [07/May/2020:16:24:32 -0500]'
                                   ' \\\"GET /images/hm_nbg.jpg HTTP/1.0\\\" 304 0'
                   }
               },
               {'create': {}},
               {
                   '@timestamp': '2099-05-08T16:25:42.000Z',
                   'event': {
                       'original': '192.0.2.255 - - [08/May/2099:16:25:42 +0000]'
                                   ' \\\"GET /favicon.ico HTTP/1.0\\\" 200 3638'
                   }
               }]

    payload_dump = ''
    for document in payload:
        payload_dump += f'{document}\n'
    payload_dump += '\n'

    headers = {'Content-Type': 'application/json'}

    response = requests.request("PUT", url, headers=headers, data=payload_dump)
    return response.json()


def search():
    url = "http://localhost:9200/logs-my_app-default/_search?pretty"

    payload = {
        "query": {
            "match_all": {}
        },
        "sort": [
            {
                "@timestamp": "desc"
            }
        ]
    }

    headers = {'Content-Type': 'application/json'}

    response = requests.request("GET", url, headers=headers, data=json.dumps(payload))
    return response.json()


def search_date_range():
    url = "http://localhost:9200/logs-my_app-default/_search?pretty"

    payload = {
        "query": {
            "range": {
                "@timestamp": {
                    "gte": "2099-05-05",
                    "lt": "2099-05-08"
                }
            }
        },
        "fields": [
            "@timestamp"
        ],
        "_source": False,
        "sort": [
            {
                "@timestamp": "desc"
            }
        ]
    }

    headers = {'Content-Type': 'application/json'}

    response = requests.request("GET", url, headers=headers, data=json.dumps(payload))
    return response.json()


def search_specific_fields():
    url = "http://localhost:9200/logs-my_app-default/_search?pretty"

    payload = {
        "query": {
            "match_all": {}
        },
        "fields": [
            "@timestamp"
        ],
        "_source": False,
        "sort": [
            {
                "@timestamp": "desc"
            }
        ]
    }

    headers = {'Content-Type': 'application/json'}

    response = requests.request("GET", url, headers=headers, data=json.dumps(payload))

    return response.json()


if __name__ == '__main__':
    # print(add_single())
    # print(add_multiple())
    # print(search())
    # print(search_date_range())
    print(search_specific_fields())
