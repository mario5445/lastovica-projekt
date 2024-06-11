const overview = document.querySelector('.overview');

function getSibling(el, cls) {
    const parent = el.parentElement;

    return parent.querySelector(`.${cls}`);
}

overview.addEventListener('click', function(e) {
    let element = e.target;

    while (element && !element.classList.contains('overview-item') && !element.classList.contains('active')) {
        element = element.parentElement;
    }

    if (!element) return;
    if (element.classList.contains('active')) {
        const form = element.closest('.consultations-form');
        const consultationsInput = getSibling(element.parentElement, 'topic-consultations');
        const consultations = +consultationsInput.value;
        if (element.parentElement.classList.contains('plus-button')) {
            consultationsInput.value = consultations + 1;
        }
        else if (element.parentElement.classList.contains('minus-button')){
            consultationsInput.value = consultations - 1;
        }
        form.submit();
    }
})
