document.addEventListener('DOMContentLoaded', function () {
    const dropdownToggle = document.querySelector('.dropdown-toggle');
    const dropdownMenu = document.querySelector('.dropdown-menu');
  
    if (dropdownToggle && dropdownMenu) {
      dropdownToggle.addEventListener('click', function (e) {
        e.preventDefault();
        dropdownMenu.classList.toggle('show');
      });
  
      // Close the dropdown when clicking outside
      document.addEventListener('click', function (e) {
        if (!dropdownToggle.contains(e.target) && !dropdownMenu.contains(e.target)) {
          dropdownMenu.classList.remove('show');
        }
      });
    }
  });

document.addEventListener('DOMContentLoaded', function () {
  const container = document.getElementById('customerLogos');
  if (!container) return;

  const totalCustomers = 36; // change this when you add more logos

  for (let i = 1; i <= totalCustomers; i++) {
    const card = document.createElement('div');
    card.className = 'logo-card';

    const img = document.createElement('img');
    img.src = `customers (${i}).png`;
    img.alt = `Customer ${i}`;
    img.loading = 'lazy';

    card.appendChild(img);
    container.appendChild(card);
  }
});