from imports import sys
from helpers import get_domain, get_sitemap

def main() -> None:
    url = sys.argv[1]
    domain = get_domain(url)
    sitemap = get_sitemap(domain)
    print(sitemap)
    
if __name__ == "__main__":
    main()