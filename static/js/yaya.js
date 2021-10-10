$(document).on('click', '#lien', function () {
    var id = $(this).attr('data-id');
    var url = id;
    console.log(url)
    window.location.href = url;

});