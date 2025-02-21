const dishes = document.querySelectorAll('.card');
const filter = (event) => {

    dishes.forEach((card) => {
        const name = card.getAttribute("data-name").toLowerCase();
        const category = card.getAttribute("data-category").toLowerCase();
        card.style.display = name.includes(event.target.value.toLowerCase()) || category.includes(event.target.value.toLowerCase()) ? "block" : "none";
    });
    
}

const filters = document.getElementById('filters');

const category = (name) => {
    filters.innerText = name + ';';
    dishes.forEach((card) => {
        const category = card.getAttribute("data-category").toLowerCase();
        card.style.display = category.includes(name.toLowerCase()) ? "block" : "none";
    });
}

const clearFilter = () => {
    filters.innerText = '';
    dishes.forEach((card) => {
        card.style.display = "block";
    })        
}