document.addEventListener("DOMContentLoaded", function () {
    const pagination = document.querySelector(".pagination");
    const footer = document.querySelector("footer");

    if (pagination && footer) {
        const adjustPagination = () => {
            const footerRect = footer.getBoundingClientRect();
            const paginationRect = pagination.getBoundingClientRect();

            if (footerRect.top < window.innerHeight) {
                pagination.style.bottom = `${window.innerHeight - footerRect.top + 10}px`; // Dostosowanie paginacji
            } else {
                pagination.style.bottom = "0px"; // Normalna pozycja
            }
        };

        window.addEventListener("scroll", adjustPagination);
        window.addEventListener("resize", adjustPagination);
        adjustPagination(); // Wywołaj funkcję po załadowaniu strony
    }
});
