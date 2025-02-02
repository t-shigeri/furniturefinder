$(document).ready(function() {
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



// // リザルトのときのみ
// $(document).ready(function() {
//     $('form.search-form').on('submit', function(event) {
//         event.preventDefault(); // フォームのデフォルトの送信動作を防ぐ
//         var form = $(this);
//         $.get(form.attr('action'), form.serialize(), function(data) {
//             var newContent = $(data).find('#results').parent().html();
//             $('#results').parent().html(newContent);
//             $('html, body').animate({
//                 scrollTop: $('#results').offset().top
//             }, 500); // 500ミリ秒でスクロール
//         });
//     });
// });
