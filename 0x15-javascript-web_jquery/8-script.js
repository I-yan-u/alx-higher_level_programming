$.ajax({
	method: 'GET',
	url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
	dataType: 'json',
	success: function (data) {
		$.map(data.results, function (movie) {
			$('UL#list_movies').append(`<li>${movie.title}</li>`);
		});
	}
});