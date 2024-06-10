const topicInput = document.querySelector('#topic-name');
const overviewItems = document.querySelectorAll('.overview-item');

function filterTopics() {
    const topicFilter = topicInput.value.toLowerCase().trim();

    overviewItems.forEach(element => {
        const topic = element.querySelector('.topic').textContent.toLowerCase();
        
        const topicMatch = topicFilter.length === 0 ? true : topic.includes(topicFilter);

        if(topicMatch){
            element.style.display = "block"; 
        }
        else {
            element.style.display = "none";
        }
    })
}

topicInput.addEventListener('input', filterTopics);