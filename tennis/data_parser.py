from playwright.sync_api import sync_playwright


def live_tennis_data():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://sports.williamhill.com/betting/en-gb/tennis')
        page.wait_for_selector('#in-play-now', timeout=10000)

        in_play_now = page.query_selector('#in-play-now')
        live_events = in_play_now.query_selector_all('.event') if in_play_now else []

        data = []
        for event in live_events:
            title_elem = event.query_selector('.show-for-desktop-medium')
            event_status = event.query_selector_all('.event__status')
            btmarket_selection = event.query_selector_all('.btmarket__selection')

            if title_elem and len(event_status) >= 2 and len(btmarket_selection) >= 2:
                data.append({
                    'title': title_elem.inner_text(),
                    'score': [
                        [
                            event_status[0].query_selector('.team-a').inner_text(),
                            event_status[0].query_selector('.team-b').inner_text()
                        ],
                        [
                            event_status[1].query_selector('.team-a').inner_text(),
                            event_status[1].query_selector('.team-b').inner_text()
                        ]
                    ]
                    if event.query_selector('.btmarket__more-bets-counter') else "0"
                })

        browser.close()
        for index, item in enumerate(data, start=1):
            item['id'] = index

        return data


def highlights_data():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://sports.williamhill.com/betting/en-gb/tennis')
        page.wait_for_selector('#match-highlights', timeout=10000)

        match_highlights_block = page.query_selector('#match-highlights')
        match_highlights = match_highlights_block.query_selector_all('.event') if match_highlights_block else []

        data = []
        for event in match_highlights:
            title_elem = event.query_selector('.show-for-desktop-medium')
            btmarket_selection = event.query_selector_all('.btmarket__selection')

            if title_elem and len(btmarket_selection) >= 2:
                data.append({
                    'start_time': event.query_selector('.eventStartTime').inner_text(),
                    'title': title_elem.inner_text(),
                    'btn_home': btmarket_selection[0].query_selector('.betbutton__odds').inner_text(),
                    'btn_away': btmarket_selection[1].query_selector('.betbutton__odds').inner_text(),
                    'bets_counter': event.query_selector('.btmarket__more-bets-counter').inner_text()
                    if event.query_selector('.btmarket__more-bets-counter') else "0"
                })

        browser.close()
        return data
