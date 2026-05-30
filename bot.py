import requests
# Instead of file-polling, use the API:
def trigger_search(query):
    url = "http://slskd:5030/api/v1/search"
    payload = {"query": query}
    requests.post(url, json=payload)
