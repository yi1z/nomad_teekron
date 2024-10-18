from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import csv

main_store_url = "https://mingrifangzhou.world.tmall.com/index.htm?from_branding=true&ali_trackid=41_ae675d40273f14961216822c92d06986"
s1_url = "https://mingrifangzhou.world.tmall.com/index.htm?from_branding=true&ali_trackid=41_ae675d40273f14961216822c92d06986"

NAME_CLASS = "title--GExDBPUi"
PRICE_CLASS = "priceUnEncode--_dE4HANk"
IMAGE_CLASS = ""

def fetch_and_parse(url):
    with sync_playwright() as p:
        # launch a browser
        browser = p.chromium.launch()
        # open a new page
        page = browser.new_page()
        # go to url
        page.goto(url)
        # wait for page to finish loading
        page.wait_for_load_state("networkidle")

        # get the content
        content = page.content()
        # close the browser
        browser.close()
        return BeautifulSoup(content, "html.parser")
    

def get_data(soup):
    if soup:
        title = soup.title.string if soup.title else "No title"
        print(f"Title: {title}")

        # get the merchandise cards
        cards = soup.find_all("div", class_="cardContainer--CwazTl0O")
        names = []
        prices = []
        images = []
        for card in cards:
            name = card.find("div", class_=NAME_CLASS)
            price = card.find("span", class_=PRICE_CLASS)
            img = card.find("img")
            names.append(name.text)
            prices.append(price.text)
            images.append(img.get("src"))

        return {"title": title, "names": names, "prices": prices, "images": images}

    else:
        print("Failed to fetch the page")
        return None
    

def write_to_csv(data: dict):
    print("Writing to file...\n")
    title = data.get("title")
    names = data.get("names")
    prices = data.get("prices")
    imgs = data.get("images")

    with open(f"src/results/{title}.csv", "w", encoding="utf-8-sig") as f:
        f.write("Product Name,Product Price,Product Image\n")
        for i in range(len(names)):
            print(f"Product Name: {names[i]}")
            print(f"Product Price: {prices[i]}")
            print(f"Product Image: {imgs[i]}")
            print("\n")
            f.write(f"{names[i]},{prices[i]},{imgs[i]}\n")

    print("File written successfully\n")


soup = fetch_and_parse(main_store_url)
data = get_data(soup)
write_to_csv(data)