async function loadDetails(gameId) {
    try {
        const response = await fetch(`/api/details/${gameId}/`);
        const data = await response.json();
        displayDetails(data);  // Обновляем отображение на странице
    } catch (error) {
        console.error('Ошибка загрузки деталей:', error);
    }
}

function displayDetails(event) {
    const container = document.getElementById('detail-container');
    // Обновляем содержимое контейнера с новыми данными
    container.innerHTML = `
        <p>${event.results[0].home.name} - ${event.results[0].away.name}</p>
        <span>Aces (Home): ${event.results[0].stats.aces[0]}</span>
        <span>Aces (Away): ${event.results[0].stats.aces[1]}</span>
        <p>Points: ${event.results[0].points}</p>
    `;
}

// Получаем game_id из data-атрибута
window.onload = () => {
    const gameId = document.getElementById('detail-container').dataset.gameId;

    // Загрузка данных сразу при загрузке страницы
    loadDetails(gameId);

    // Запуск периодической загрузки данных каждые 5 секунд
    setInterval(() => loadDetails(gameId), 1000);  // Каждые 1 секунд
};