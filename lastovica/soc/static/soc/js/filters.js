const topicInput = document.querySelector('#topic-input');
const teacherSelect = document.querySelector('#teacher-select');
const departmentSelect = document.querySelector('#department-select');
const availabilitySelect = document.querySelector('#availability-select');
const overviewItems = document.querySelectorAll('.overview-item');
const resetBtn = document.querySelector('.reset-btn');

function filterItems(){
    const topicFilter = topicInput.value.toLowerCase().trim();
    const teacherFilter = teacherSelect.value;
    const departmentFilter = departmentSelect.value;
    const availabilityFilter = availabilitySelect.value;

    overviewItems.forEach(element => {
        const topic = element.querySelector('.topic').textContent.toLowerCase();
        const teacher = element.querySelector('.teacher').dataset.id;
        const department = element.querySelector('.department').dataset.id;
        const availability = element.querySelector('.availability').dataset.id;

        const topicMatch = topicFilter.lenght === 0 ? true : topic.includes(topicFilter);
        const teacherMatch = teacherFilter === "all" || teacherFilter === teacher;
        const departmentMatch = departmentFilter === "all" || departmentFilter === department;
        const availabilityMatch = availabilityFilter === "all" || availabilityFilter === availability;

        if(topicMatch && teacherMatch && departmentMatch && availabilityMatch){
            element.style.display = "block";
        }
        else {
            element.style.display = "none";
        }
    });
}

topicInput.addEventListener('input', filterItems);
topicInput.addEventListener('keydown', function(e){
    if (e.key === "Enter") {
        filterItems()
    }
});
teacherSelect.addEventListener('change', filterItems);
departmentSelect.addEventListener('change', filterItems);
availabilitySelect.addEventListener('change', filterItems);

resetBtn.addEventListener('click', function(){
    topicInput.value = "";
    teacherSelect.selectedIndex = 0;
    departmentSelect.selectedIndex = 0;
    availabilitySelect.selectedIndex = 0;
    filterItems();
})