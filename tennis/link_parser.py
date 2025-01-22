from playwright.sync_api import sync_playwright


def find_link_with_text(text):
    with sync_playwright() as p:
        # Запускаем браузер в безголовом режиме для максимальной скорости
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Загружаем сайт
        page.goto('https://sports.williamhill.com/betting/en-gb/tennis/')

        # Ищем ссылку с нужным текстом
        link = page.locator(f"a:has-text('{text}')").first
        link_url = link.get_attribute("href")  # Получаем URL ссылки

        # Закрываем браузер
        browser.close()

        return link_url.replace('/betting/en-gb/tennis/', 'https://sports.williamhill.com/betting/en-gb/tennis/')
