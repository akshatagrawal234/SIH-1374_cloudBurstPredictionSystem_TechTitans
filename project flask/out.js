// JavaScript code to enable smooth scrolling for the navigation links

// Function to scroll to a specific element by its ID
function scrollToElement(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
      element.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
    }
  }
  
  // Add an event listener to the navigation links
  
  document.addEventListener("DOMContentLoaded", function () {
    const purposeLink = document.querySelector(".ps a");
    const benefitsLink = document.querySelector(".be a");
    const teamLink = document.querySelector(".ot a");
  
    purposeLink.addEventListener("click", function (e) {
      e.preventDefault();
      scrollToElement("purpose-section");
    });
  
    benefitsLink.addEventListener("click", function (e) {
      e.preventDefault();
      scrollToElement("benefits-section");
    });
  
    teamLink.addEventListener("click", function (e) {
      e.preventDefault();
      scrollToElement("team-section");
    });
  });
  