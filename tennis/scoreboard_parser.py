from playwright.sync_api import sync_playwright
from tennis.link_parser import find_link_with_text


def get_scoreboard_html(url):
    with sync_playwright() as p:
        # Инициализация браузера (используем Chromium для скорости)
        browser = p.chromium.launch(headless=True)  # Запуск в безголовом режиме для максимальной скорости
        page = browser.new_page()

        try:
            page.goto(url, timeout=60000)  # Открываем страницу с таймаутом 60 секунд

            # Проверяем наличие iframe и ищем элемент внутри него
            iframes = page.frames
            for frame in iframes:
                try:
                    # Ищем элемент #scoreboard внутри текущего iframe
                    element = frame.locator("#scoreboard")
                    if element.is_visible():
                        html_code = element.inner_html()
                        return html_code
                except Exception:
                    continue

            # Если элемент не найден в iframe, ищем на главной странице
            element = page.locator("#scoreboard")
            if element.is_visible():
                html_code = element.inner_html()
                return html_code

        except Exception as e:
            print(f"Ошибка: {e}")
            return None

        finally:
            browser.close()  # Закрываем браузер


# print(get_scoreboard_html('https://sports.williamhill.com/betting/en-gb/tennis/OB_EV34293348/peter-goldsteiner-vs-vojtech-vales'))
# print(find_link_with_text('Ben Shelton v Lorenzo Sonego'))
# print(get_scoreboard_html(find_link_with_text('Ben Shelton v Lorenzo Sonego')))
