const apiUrl = 'http://127.0.0.1:8000/animes';

const animeList = document.getElementById('anilist');

function fetchAnimes(){
    fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
        animeList.innerHTML = '';
        data.forEach((movie, index) => {
            const paragraph = document.createElement('div')
            paragraph.innerHTML = `<p> ${movie.title} </p>`
            animeList.appendChild(paragraph)
        })
    })
}

window.addEventListener('load', fetchAnimes);