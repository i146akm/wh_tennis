from playwright.sync_api import sync_playwright


def get_scoreboard_html(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto(url, timeout=30000)
            page.wait_for_timeout(3000)

            element = page.locator("#scoreboard")
            if element.is_visible():
                return element.inner_html()

            for frame in page.frames:
                try:
                    element = frame.locator("#scoreboard")
                    if element.is_visible():
                        return element.inner_html()
                except Exception:
                    continue

            return None

        except Exception:
            return None

        finally:
            browser.close()
