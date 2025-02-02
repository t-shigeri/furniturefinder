$(document).ready(function () {
    var previousTop = 0;

    $(window).bind('scroll', function () {
        var currentTop = $(window).scrollTop();
        if (currentTop < previousTop) {
            $('header').addClass('visible');
        } else {
            $('header').removeClass('visible');
        }
        previousTop = currentTop;
    });
});
document.querySelector('#contact-form').addEventListener('submit', (e) => {
    e.preventDefault();
    e.target.elements.name.value = '';
    e.target.elements.email.value = '';
    e.target.elements.message.value = '';
});
