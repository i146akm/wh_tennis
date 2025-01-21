const closeButton = document.querySelector('#close');
const scoreboard = document.querySelector('#scoreboard_container');

closeButton.addEventListener('click', () => {
    scoreboard.style.display = 'none';
})