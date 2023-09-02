// script.js

// Add your JavaScript code here
// You can interact with the HTML elements and add functionality

// Example: Change the background color of the content div
const contentDiv = document.querySelector('.content');
contentDiv.style.backgroundColor = 'lightblue';

// Get all the navigation links
const navLinks = document.querySelectorAll('.menu ul li a');

// Add click event listener to each navigation link
navLinks.forEach(link => {
  link.addEventListener('click', (event) => {
    event.preventDefault(); // Prevent the default link behavior

    const targetId = link.getAttribute('about.html'); // Get the target section ID
    const targetSection = document.querySelector(targetId); // Get the target section element

    // Scroll to the target section smoothly
    targetSection.scrollIntoView({
      behavior: 'smooth'
    });
  });
});