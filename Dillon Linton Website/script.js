// Get the current mode from local storage (if available)
const currentMode = localStorage.getItem("mode");

// Set the initial mode based on local storage or default to light mode
document.body.classList.toggle("dark-mode", currentMode === "dark");

// Event listener for the toggle button
const toggleButton = document.getElementById("toggleButton");
toggleButton.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
  // Save the mode to local storage
  localStorage.setItem("mode", document.body.classList.contains("dark-mode") ? "dark" : "light");
});

// Event listener for the Read More button
document.getElementById('read-more-button').addEventListener('click', function() {
  var moreText = document.getElementById('more-text');
  var button = document.getElementById('read-more-button');
  
  if (moreText.classList.contains('collapsed')) {
    moreText.classList.remove('collapsed');
    button.textContent = 'Read Less';
  } else {
    moreText.classList.add('collapsed');
    button.textContent = 'Read More';
  }
});
