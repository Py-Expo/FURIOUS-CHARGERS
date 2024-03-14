// Burger menu functionality
const navLinks = document.querySelector('.nav-links');
const burger = document.querySelector('.burger');

burger.addEventListener('click', () => {
    navLinks.classList.toggle('nav-active');
    burger.classList.toggle('active');
});