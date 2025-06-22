// You can add optional dynamic features here
// Example: clear flash messages after 5 seconds
setTimeout(() => {
  document.querySelectorAll('.alert').forEach(alert => {
    alert.classList.add('fade');
    setTimeout(() => alert.remove(), 500);
  });
}, 5000);
