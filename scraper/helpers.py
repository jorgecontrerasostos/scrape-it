
from imports import os, FirecrawlApp

app = FirecrawlApp(api_key=os.environ.get('FIRE_CRAWL_API_KEY'))

print(app)