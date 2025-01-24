from playwright.sync_api import sync_playwright


def get_scoreboard_html(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url, timeout=30000)
        page.wait_for_timeout(3000)

        iframe_src = page.locator("iframe").nth(0).get_attribute("src")
        return iframe_src
