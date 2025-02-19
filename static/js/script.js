const getCurrentYear = () => new Date().getFullYear();

const yearHTML = document.getElementById('year')
yearHTML.innerText = getCurrentYear();