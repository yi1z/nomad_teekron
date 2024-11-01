from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    # Launch browser and use the saved authentication state
    browser = p.chromium.launch()
    context = browser.new_context(storage_state="storage.json")  # Load saved state
    page = context.new_page()
    
    # Go to a page that requires login
    url = "https://detail.tmall.com/item.htm?abbucket=4&id=848965857802&rn=aa2576e94d82215c33d193e624abc1c8&spm=a1z10.5-b-s.w4011-22044789678.28.1b9e2140PbrbsD&sku_properties=134942334%3A25351185550"
    page.goto(url)

    soup = BeautifulSoup(page.content(), "html.parser")
    print(soup.prettify())
    # Continue with automated tasks as an authenticated user
    browser.close()