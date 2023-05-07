const apiUrl = 'https://fourtonfish.com/hellosalut/?lang=fr';

$.get(apiUrl, (data) => $('div#hello').html(data.hello));