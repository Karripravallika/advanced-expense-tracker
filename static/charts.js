document.addEventListener('DOMContentLoaded', function () {
  const ctx = document.getElementById('expenseChart').getContext('2d');

  const labels = JSON.parse(document.getElementById('chart-labels').textContent);
  const data = JSON.parse(document.getElementById('chart-data').textContent);

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Expenses by Category',
        data: data,
        backgroundColor: [
          '#4e73df', '#1cc88a', '#36b9cc', '#f6c23e', '#e74a3b'
        ],
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: true },
        title: { display: true, text: 'Expense Breakdown by Category' }
      },
      scales: {
        y: {
          beginAtZero: true,
          ticks: {
            callback: function(value) {
              return '₹' + value;
            }
          }
        }
      }
    }
  });
});
