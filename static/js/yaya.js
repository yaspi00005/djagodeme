$(document).on('click', '#lien', function () {
    var id = $(this).attr('data-id');
    var url = id;
    console.log(url)
    window.location.href = url;

});


$(document).on('click', '#lien2', function () {
    var id = $(this).attr('data-id');
    var url = 'search/' + id;
    console.log(url)
    window.location.href = url;

});