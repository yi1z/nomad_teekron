from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import csv

import argparse

HANDLE_INDEX = 0
TITLE_INDEX = 1
BODY_INDEX = 2
VENDOR_INDEX = 3
PRODUCT_CATEGORY_INDEX = 4
TYPE_INDEX = 5
TAGS_INDEX = 6
PUBLISHED_INDEX = 7
OPTION1_NAME_INDEX = 8
OPTION1_VALUE_INDEX = 9
OPTION2_NAME_INDEX = 10
OPTION2_VALUE_INDEX = 11
OPTION3_NAME_INDEX = 12
OPTION3_VALUE_INDEX = 13
VARIANT_SKU_INDEX = 14
VARIANT_GRAMS_INDEX = 15
VARIANT_INVENTORY_TRACKER_INDEX = 16
VARIANT_INVENTORY_QTY_INDEX = 17
VARIANT_INVENTORY_POLICY_INDEX = 18
VARIANT_FULFILLMENT_SERVICE_INDEX = 19
VARIANT_PRICE_INDEX = 20
VARIANT_COMPARE_AT_PRICE_INDEX = 21
VARIANT_REQUIRE_SHIPPING_INDEX = 22
VARIANT_TAXABLE_INDEX = 23
VARIANT_BARCODE_INDEX = 24
IMAGE_SRC_INDEX = 25
IMAGE_POSITION_INDEX = 26
IMAGE_ALT_TEXT_INDEX = 27
GIFT_CARD_INDEX = 28
SEO_TITLE_INDEX = 29
SEO_DESCRIPTION_INDEX = 30
GOOGLE_SHOPPING_GOOGLE_PRODUCT_CATEGORY_INDEX = 31
GOOGLE_SHOPPING_GENDER_INDEX = 32
GOOGLE_SHOPPING_AGE_GROUP_INDEX = 33
GOOGLE_SHOPPING_MPN_INDEX = 34
GOOGLE_SHOPPING_ADWORDS_GROUPING_INDEX = 35
GOOGLE_SHOPPING_ADWORDS_LABELS_INDEX = 36
GOOGLE_SHOPPING_CONDITION_INDEX = 37
GOOGLE_SHOPPING_CUSTOM_PRODUCT_INDEX = 38
GOOGLE_SHOPPING_CUSTOM_LABEL_0_INDEX = 39
GOOGLE_SHOPPING_CUSTOM_LABEL_1_INDEX = 40
GOOGLE_SHOPPING_CUSTOM_LABEL_2_INDEX = 41
GOOGLE_SHOPPING_CUSTOM_LABEL_3_INDEX = 42
GOOGLE_SHOPPING_CUSTOM_LABEL_4_INDEX = 43
VARIANT_IMAGE_INDEX = 44
VARIANT_WEIGHT_UNIT_INDEX = 45
VARIANT_TAX_CODE_INDEX = 46
COST_PER_ITEM_INDEX = 47
PRICE_INTERNAIONAL_INDEX = 48
COMPARE_AT_PRICE_INTERNATIONAL_INDEX = 49
STATUS_INDEX = 50
OPTION4_NAME_INDEX = 51
OPTION4_VALUE_INDEX = 52
OPTION5_NAME_INDEX = 53
OPTION5_VALUE_INDEX = 54
OPTION6_NAME_INDEX = 55
OPTION6_VALUE_INDEX = 56
OPTION7_NAME_INDEX = 57
OPTION7_VALUE_INDEX = 58
OPTIONS_NAME_INDEX = [OPTION1_NAME_INDEX, OPTION2_NAME_INDEX, OPTION3_NAME_INDEX, OPTION4_NAME_INDEX, OPTION5_NAME_INDEX, OPTION6_NAME_INDEX, OPTION7_NAME_INDEX]
OPTIONS_VALUE_INDEX = [OPTION1_VALUE_INDEX, OPTION2_VALUE_INDEX, OPTION3_VALUE_INDEX, OPTION4_VALUE_INDEX, OPTION5_VALUE_INDEX, OPTION6_VALUE_INDEX, OPTION7_VALUE_INDEX]
TOTAL_COLUMNS = 59

VENDOR = "Nomad Teekron"
PRODUCT_CATEGORY = "Arts & Entertainment > Hobbies & Creative Arts > Collectibles"
PUBLISED = "TRUE"
VARIANT_INVENTORY_POLICY = "deny"
VARIANT_FULFILLMENT_SERVICE = "manual"
PRICE_MULTIPLIER = 4.5
COMPARE_AT_PRICE_MULTIPLIER = 5
BASE = 5
VARIANT_REQUIRE_SHIPPING = "TRUE"
VARIANT_TAXABLE = "TRUE"
IMAGE_POSITION = 1
VARIANT_WEIGHT_UNIT = "g"
STATUS = "active"

IMAGE_CLASS = "thumbnailPic--QasTmWDm"
PRICE_CLASS = "text--fZ9NUhyQ"
OPTION_BUTTON_CLASS = "valueItem--GzWd2LsV"
OPTION_NAME_CLASS = "valueItemText--HiKnUqGa"

# parser = argparse.ArgumentParser(description="Fetch and parse a page")
# parser.add_argument("url", help="The URL of the page to fetch")
# parser.add_argument("file", help="The file to write the data to")

# args = parser.parse_args()

def fetch_and_parse(url):
    # print(f"Fetching...\n")
    with sync_playwright() as p:
        # launch a browser
        browser = p.chromium.launch()
        # Load saved state
        context = browser.new_context(storage_state="storage.json")
        # open a new page
        page = context.new_page()
        page.set_default_timeout(100000)
        # go to url
        page.goto(url)
        # wait for page to finish loading
        page.wait_for_load_state("networkidle")

        # get the content
        content = page.content()
        # close the browser
        # browser.close()
        soup = BeautifulSoup(content, "html.parser")
        if soup:
            print("Page fetched successfully\n")
        else:
            print("Failed to fetch the page")
        
        print("Reading data...\n")
        page_title = soup.title.string if soup.title else "No title"
        print(f"Title: {page_title}")

        # get the title of the product
        title = soup.find("h1").text
        image = soup.find("img", class_=IMAGE_CLASS).get("src")
        base_price = soup.find("span", class_=PRICE_CLASS).text

        # get all the options listed
        options = soup.find_all("div", class_=OPTION_BUTTON_CLASS)
        option_names = soup.find_all("span", class_=OPTION_NAME_CLASS)
        option_data = {}

        for name in option_names:
            page.click(f'text="{name.text}"')
            page.wait_for_load_state("networkidle")
            print(f"Clicked on {name.text}")
            soup = BeautifulSoup(page.content(), "html.parser")
            option_data[name.text] = soup.find("span", class_=PRICE_CLASS).text
            print(f"Price: {option_data[name.text]}")

        handle = title.replace(" ", "-")
        handle = handle.encode('unicode_escape').decode('utf-8')
        print("Data read successfully")
        result = {"title": title, "image": image, "base_price": base_price, "handle": handle, "options": option_data}
        print(result)
        return result
        
def read_to_data(soup, page):
    print("Reading data...\n")
    page_title = soup.title.string if soup.title else "No title"
    print(f"Title: {page_title}")

    # get the title of the product
    title = soup.find("h1").text
    image = soup.find("img", class_=IMAGE_CLASS).get("src")
    base_price = soup.find("span", class_=PRICE_CLASS).text

    # get all the options listed
    option_names = soup.find_all("span", class_=OPTION_NAME_CLASS)
    option_data = {}

    for name in option_names:
        page.wait_for_load_state("networkidle")
        print(f"Clicked on {name.text}")
        soup = BeautifulSoup(page.content(), "html.parser")
        option_data[name.text] = soup.find("span", class_=PRICE_CLASS).text
        print(f"Price: {option_data[name.text]}")

    handle = title.replace(" ", "-")
    handle = handle.encode('unicode_escape').decode('utf-8')
    print("Data read successfully")
    result = {"title": title, "image": image, "base_price": base_price, "handle": handle, "options": option_data}
    print(result)
    return result

    
def write_to_file(data, filepath):
    title = data["title"]
    image = data["image"]
    price = data["base_price"]
    handle = data["handle"]
    options = data["options"]

    print("Writing to file...")
    with open(filepath, "a", encoding="utf-8-sig", newline='') as f:
        new_line = [""] * (TOTAL_COLUMNS + 1)
        new_line[HANDLE_INDEX] = handle
        new_line[TITLE_INDEX] = title
        new_line[VARIANT_PRICE_INDEX] = float(price) * PRICE_MULTIPLIER / BASE
        new_line[VARIANT_COMPARE_AT_PRICE_INDEX] = float(price) * COMPARE_AT_PRICE_MULTIPLIER / BASE
        new_line[IMAGE_SRC_INDEX] = image

        new_line[VENDOR_INDEX] = VENDOR
        new_line[PRODUCT_CATEGORY_INDEX] = PRODUCT_CATEGORY
        new_line[PUBLISHED_INDEX] = PUBLISED
        new_line[VARIANT_INVENTORY_POLICY_INDEX] = VARIANT_INVENTORY_POLICY
        new_line[VARIANT_FULFILLMENT_SERVICE_INDEX] = VARIANT_FULFILLMENT_SERVICE
        new_line[VARIANT_REQUIRE_SHIPPING_INDEX] = VARIANT_REQUIRE_SHIPPING
        new_line[VARIANT_TAXABLE_INDEX] = VARIANT_TAXABLE
        new_line[VARIANT_WEIGHT_UNIT_INDEX] = VARIANT_WEIGHT_UNIT
        new_line[STATUS_INDEX] = STATUS

        for i, (name, value) in enumerate(options.items()):
            print(i)
            new_line[OPTIONS_NAME_INDEX[i]] = name
            new_line[OPTIONS_VALUE_INDEX[i]] = value

        writer = csv.writer(f)
        writer.writerow(new_line)

    print("Finished writing to file")
    print(f"Product Name: {title}")
    print(f"Product Price: {price}")
    print(f"Product Image: {image}")
    print("------------------------------------")
    print("\n")

# url = "https://detail.tmall.com/item.htm?abbucket=4&id=810837883100&rn=9a3955472dc2b198240b0768039d3076&spm=a1z10.5-b-s.w4011-22044789678.12.6ecc7300twYOB8&sku_properties=134942334%3A25351185550"
# soup = fetch_and_parse(url)
# print(soup.prettify())