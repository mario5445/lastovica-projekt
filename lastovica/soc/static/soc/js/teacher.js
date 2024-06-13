const overview = document.querySelector('.overview');
const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
const greenColor = "#0A8754";
const grayColor = "#95A3A4";

function updateButton(element, color) {
    const paths = element.querySelectorAll('.path');
    paths.forEach(path => {
        path.setAttribute('stroke', color);
    });
}

function updateDots(container, value) {
    container.querySelectorAll('.consultation-icon').forEach((element, index) => {
        if (value > index) {
            element.style.fill = greenColor;
        }
        else {
            element.style.fill = grayColor
        }
    })
}

function checkPlusBtn(btn, value) {
    if (value < 3) {
        if (!btn.classList.contains('active')) {
            btn.classList.add('active');
        }
        return true;
    }
    if (btn.classList.contains('active')) {
        btn.classList.remove('active');
    }
    return false;
}

function checkMinusButton(btn, value) {
    if (value > 0) {
        if (!btn.classList.contains('active')) {
            btn.classList.add('active');
        }
        return true;
    }
    if (btn.classList.contains('active')) {
        btn.classList.remove('active');
    }
    return false;
}

async function updateRecord(id, value) {
    const url = '/update_konzultacie/';
    const data = {
        "id": id,
        "value": value
    }

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (!response.ok) {
            console.error("Error: ", result);
        }
    } catch (error) {
        console.error("Error: ", error);
    }

}

function getSibling(el, cls) {
    const parent = el.parentElement;
    return parent.querySelector(`.${cls}`);
}

function checkAndUpdateButtons(plusButton, minusButton, value) {
    if (checkPlusBtn(plusButton, value)) {
        updateButton(plusButton, greenColor);
    }
    else {
        updateButton(plusButton, grayColor);
    }
    if (checkMinusButton(minusButton, value)) {
        updateButton(minusButton, greenColor);
    }
    else {
        updateButton(minusButton, grayColor);
    }
}

overview.addEventListener('click', function (e) {
    let element = e.target;

    while (element && !element.classList.contains('overview-item') && !element.classList.contains('active')) {
        element = element.parentElement;
    }

    if (!element || element.classList.contains('overview-item')) return;
    if (element.classList.contains('active')) {
        const form = element.closest('.consultations-form');
        const consultationsInput = form.querySelector('.topic-consultations');
        const topicID = form.querySelector('.topic-id').value;
        const consultations = +consultationsInput.value;
        if (element.parentElement.classList.contains('plus-button') && consultationsInput.value < 3) {
            consultationsInput.value = consultations + 1;
            checkAndUpdateButtons(element, form.querySelector('.minus-button svg'), consultationsInput.value);
        }
        else if (element.parentElement.classList.contains('minus-button')) {
            consultationsInput.value = consultations - 1;
            checkAndUpdateButtons(form.querySelector('.plus-button svg'), element, consultationsInput.value);
        }
        updateDots(form.closest('.consultations'), consultationsInput.value);
        updateRecord(topicID, consultationsInput.value);
    }
})
