from playwright.sync_api import sync_playwright


def find_link_with_text(text):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto('https://sports.williamhill.com/betting/en-gb/in-play/tennis', timeout=30000)
            page.wait_for_selector(f"a:has-text('{text}')", timeout=5000)

            link = page.locator(f"a:has-text('{text}')").first
            link_url = link.get_attribute("href")

            if link_url:
                return link_url.replace('/betting/en-gb/tennis/', 'https://sports.williamhill.com/betting/en-gb/tennis/')
            return None

        except Exception:
            return None

        finally:
            browser.close()
