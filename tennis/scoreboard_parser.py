from playwright.sync_api import sync_playwright


def get_scoreboard_html(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=30000)

        iframe_element = page.locator("iframe").first
        iframe_src = iframe_element.get_attribute("src")

        browser.close()
        return iframe_src
