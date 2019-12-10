export var GenderChartTemplate = {
  type: 'pie',
  data: {
    labels: ['Male','Female'],
    datasets: [
      {
        data: [],
        label: 'Population Gender Distribution',
        backgroundColor: [
          'rgba(54,73,93,.5)'
        ],
        borderColor: [
          '#36495d',
        ],
        borderWidth: 3
      },
    ]
  },
  options: {
    responsive: true,
  }
}

export default GenderChartTemplate;
