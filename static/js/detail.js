async function loadDetails(gameId) {
    try {
        const response = await fetch(`/api/details/${gameId}/`);
        const data = await response.json();
        displayDetails(data);
    } catch (error) {
        console.error('Ошибка загрузки деталей:', error);
    }
}

function displayDetails(event) {
    const container = document.getElementById('detail-container');
    container.innerHTML = `
        <p>${event.results[0].home.name} - ${event.results[0].away.name}</p>
        <span>${event.results[0].stats.aces[0]}</span>
        <span>${event.results[0].stats.aces[1]}</span>
    `;
}

// Получаем game_id из data-атрибута
window.onload = () => {
    const gameId = document.getElementById('detail-container').dataset.gameId;
    loadDetails(gameId);
};