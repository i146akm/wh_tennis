from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import data_parser
from tennis.link_parser import find_link_with_text
from tennis.scoreboard_parser import get_scoreboard_html


@login_required(login_url='/login')
def tennis_view(request):
    live_events = data_parser.live_tennis_data()
    highlights = data_parser.highlights_data()

    context = {
        'live_events': live_events,
        'highlights': highlights,
    }

    return render(request, "tennis.html", context=context)

@login_required(login_url='/login')
def detail_view(request, id):
    if request.method == 'GET':
        for i in data_parser.live_tennis_data():
            if i['id'] == id:
                return render(request, 'detail.html', context={'parsed_html': get_scoreboard_html(find_link_with_text(i['title']))})
