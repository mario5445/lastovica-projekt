(async function () {
    const dataItems = document.querySelectorAll('.data-item');
    const datas = [];
    dataItems.forEach(item => {
        datas.push({ nazov: item.dataset.name, count: item.dataset.count });
    })
    const data = {
        labels: datas.map(x => x.nazov),
        datasets: [{
            label: 'Témy',
            data: datas.map(x => x.count),
            backgroundColor: [
                'rgb(142, 223, 42)',
                'rgb(83, 134, 228)',
                'rgb(201, 228, 231)'
            ],
            hoverOffset: 4
        }]
    };
    const config = {
        type: 'doughnut',
        data: data,
    };

    new Chart(
        document.getElementById('dostupnosti'),
        {
            ...config
        }
    );
})();

(async function () {
    const students = document.querySelector("#students").dataset.count;
    const teachers = document.querySelector("#teachers").dataset.count;
    const data = {
        labels: ["Študenti", "Učitelia"],
        datasets: [{
            label: 'Užívatelia',
            data: [+students, +teachers],
            backgroundColor: [
                'rgb(142, 223, 42)',
                'rgb(83, 134, 228)',
                'rgb(201, 228, 231)'
            ],
            hoverOffset: 4
        }]
    };
    const config = {
        type: 'bar',
        data: data,
    };

    new Chart(
        document.getElementById('ludia'),
        {
            ...config
        }
    );
})();
