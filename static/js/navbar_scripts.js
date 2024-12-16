// Obsługuje rozwijanie i zwijanie dropdown menu
$(document).ready(function() {
    $('.dropdown-toggle').on('click', function() {
        $(this).parent().toggleClass('show');
        $(this).next('.dropdown-menu').toggleClass('show');
    });

    // Zamknij dropdown po kliknięciu poza nim
    $(document).on('click', function(e) {
        if (!$(e.target).closest('.dropdown').length) {
            $('.dropdown-menu').removeClass('show');
            $('.dropdown').removeClass('show');
        }
    });
});

