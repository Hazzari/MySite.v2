$(document).ready(function () {

    $('#blog-menu a').each(function () {


        let location = window.location.protocol + '//' + window.location.host + window.location.pathname;
        let link = this.href;

        if (location === link) {
            $(this).addClass('active');
        }
    });

    $('#ssd a').each(function () {


        let location = window.location.protocol + '//' + window.location.host + window.location.pathname;
        let link = this.href;
        if (location === link) {

            $(this).addClass('active');
        }
    });


});