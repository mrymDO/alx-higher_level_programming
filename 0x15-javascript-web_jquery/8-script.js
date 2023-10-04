$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movies = data.results;
    movies.forEach(function (movie) {
      const title = movie.title;
      // Create an <li> element for each movie title
      const listMovie = $('<li>').text(title);
      // Append the <li> element to the UL
      $('#list_movies').append(listMovie);
    });
  });
});
