$(document).ready(function () {// ожидаем после загрузки
    $('a#activeOffers').click(function (event) {// отлавливаем клик по id
        event.preventDefault();
        $('#overlay').ready(
            function () {
                $('#activeOffers')
                    .css('display', 'block')
            });
    });
});