import requests

url = "http://localhost:8000/api/submit-scrape-job"
data = {
  "id": "",
  "url": "http://quotes.toscrape.com/",
  "elements": [
    {
      "name": "Quotes",
      "xpath": "//span[@class='text']",
      "url": "http://quotes.toscrape.com/"
    }
  ],
  "user": "",
  "time_created": "2024-11-07T17:13:55.448Z",
  "result": [],
  "job_options": {
    "multi_page_scrape": False,
    "custom_headers": {}
  },
  "status": "Queued",
  "chat": ""
}

response = requests.post(url, json=data)
print(response.json())