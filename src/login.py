from playwright.sync_api import sync_playwright

def login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.set_default_timeout(100000)
        page.goto("https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fi.taobao.com%2Fmy_taobao.htm%3Fspm%3Da21n57.1.754894437.1.663d523cLDyL4u%26pm_id%3D1501036000a02c5c3739")

        input("Press Enter after logging in manually...")

        page.context.storage_state(path="storage.json")
        browser.close()