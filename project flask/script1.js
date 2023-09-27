// script.js
const weatherText = document.getElementById("weatherText");
const quoteText = document.getElementById("quoteText");

// Display the sunny message
weatherText.textContent = "It's Sunny Today!";

// Array of quotes
const quotes = [
    "Life is what happens when you're busy making other plans.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "In three words I can sum up everything I've learned about life: it goes on.",
    "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.",
    "The best time to plant a tree was 20 years ago. The second best time is now.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts."
];

// Display a random quote
const randomIndex = Math.floor(Math.random() * quotes.length);
quoteText.textContent = quotes[randomIndex];
