const ctx = document.getElementById("myChart").getContext("2d");
let chart = new Chart(ctx, {
  type: "line",
  data: {
    labels: [],
    datasets: [
      {
        label: "Sensor",
        data: [],
        borderColor: "rgb(255, 99, 132)",
        tension: 0.4,
      },
    ],
  },
  options: {
    scales: {
      x: { title: { display: true, text: "Hora" } },
      y: { title: { display: true, text: "Valor" }, min: 0, max: 100 },
    },
  },
});

function updateChart() {
  fetch("/api/data")
    .then((response) => response.json())
    .then((data) => {
      chart.data.labels = data.map((item) => item.timestamp);
      chart.data.datasets[0].data = data.map((item) => item.value);
      chart.update();
    });
}

setInterval(updateChart, 2000);
