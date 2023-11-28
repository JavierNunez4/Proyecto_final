/* global bootstrap: false */
(() => {
  'use strict'
  const tooltipTriggerList = Array.from(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  tooltipTriggerList.forEach(tooltipTriggerEl => {
    new bootstrap.Tooltip(tooltipTriggerEl)
  })
})()


document.addEventListener("DOMContentLoaded", function () {
  const sidebar = document.querySelector(".sidebar");
  const content = document.querySelector(".content");
  const toggleButton = document.getElementById("sidebar-toggle");

  toggleButton.addEventListener("click", function () {
      sidebar.classList.toggle("open");
      content.classList.toggle("shift");
  });
});
