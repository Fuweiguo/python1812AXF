$(function () {
    $('.home').width(innerWidth-20)

    var swiper = new Swiper('.swiper-container', {
        pagination: '.swiper-pagination',
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        slidesPerView: 1,
        paginationClickable: true,
        autoplay: 2500,
        spaceBetween: 30,
        loop: true
    });
})
