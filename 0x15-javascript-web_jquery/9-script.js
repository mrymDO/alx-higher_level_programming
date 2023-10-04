$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    const helloTranslation = data.hello;
    $('#hello').text(helloTranslation);
  });
});
