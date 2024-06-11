(function () {

    const btnEliminacion = document.querySelectorAll(".btnDelete");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('Are zou sure zou want to delete this course?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
    
})();

