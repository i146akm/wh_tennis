async function loadEvents() {
    try {
        const response = await fetch('/api/events/');
        const data = await response.json();
        displayEvents(data.events);
    } catch (error) {
        console.error('Ошибка загрузки событий:', error);
    }
}

// Отображаем события
function displayEvents(events) {
    const container = document.getElementById('events-container');
    container.innerHTML = ''; // Очищаем контейнер

    events.forEach(event => {
        const eventDiv = document.createElement('div');
        eventDiv.innerHTML = `
            <p>
                <a href="/details/${event.game_id}/">${event.home.name} - ${event.away.name}</a>
                <span>${event.score}</span>
            </p>`;
        container.appendChild(eventDiv);
    });
}

// Загружаем события каждые 5 секунд
setInterval(loadEvents, 5000);

// Начальная загрузка событий
window.onload = loadEvents;