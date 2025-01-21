from django.shortcuts import render
from . import data_parser  # Импортируйте ваш парсер
from . import scoreboard_parser


def tennis_view(request):
    live_events = data_parser.live_tennis_data()
    highlights = data_parser.highlights_data()

    context = {
        'live_events': live_events,
        'highlights': highlights,
    }

    return render(request, "tennis.html", context)


def detail_view(request):
    element = scoreboard_parser.get_scoreboard_html('https://sports.williamhill.com/betting/en-gb/tennis/OB_EV34282471/julia-adams-vs-emma-wilson')

    context = {
        'element': element,
    }

    return render(request, "detail.html", context)
