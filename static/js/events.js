function loadEvents() {
    const eventSource = new EventSource('/sse/events/');

    eventSource.onmessage = function(event) {
        const data = JSON.parse(event.data);
        displayEvents(data);
    };

    eventSource.onerror = function(event) {
        console.error("Ошибка SSE:", event);
    };
}

function displayEvents(events) {
    const container = document.getElementById('events-list').getElementsByTagName('tbody')[0];
    container.innerHTML = '';

    events.forEach(event => {
        const eventRow = document.createElement('tr');
        eventRow.classList.add('eventsItem')
        eventRow.innerHTML = `
            <td class="liveNote">LIVE</td>
            <td class="competition">${event.league.name}</td>
            <td class="eventName">
                <a href="/details/${event.game_id}/">${event.home.name} - ${event.away.name}</a>
            </td>
            <td class="score">${event.score}</td>`;
        container.appendChild(eventRow);
    });
}
window.onload = loadEvents;