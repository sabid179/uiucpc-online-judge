// script.js for uiucpcOJ homepage
"use strict";
// Navbar blur and scroll effect with debounce
function debounce(fn, delay) {
  let timer = null;
  return function () {
    clearTimeout(timer);
    timer = setTimeout(fn, delay);
  };
}

const navbar = document.getElementById('navbar');
window.addEventListener('scroll', debounce(function () {
  if (!navbar) return;
  if (window.scrollY > 20) {
    navbar.classList.add('navbar-scrolled');
  } else {
    navbar.classList.remove('navbar-scrolled');
  }
}, 50));
