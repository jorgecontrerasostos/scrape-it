from imports import urlparse, requests

def get_domain(url: str) -> str:
    parsed_url = urlparse(url)
    try:
        domain = parsed_url.netloc
        return domain
    except AttributeError:
        raise ValueError("Invalid URL")
    
def get_sitemap(domain: str) -> str:
    res = requests.get(f"http://{domain}/robots.txt")
    
