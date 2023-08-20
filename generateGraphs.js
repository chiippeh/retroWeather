export function createGraphs(year) {
    destroyCharts(); // Destroy existing charts before creating new ones
    graph1(year);
    graph2(year);
}

function destroyCharts() {
    // Destroy the temperatureChart
    const temperatureChartCanvas = document.getElementById("temperatureChart");
    if (temperatureChartCanvas) {
        const temperatureChart = Chart.getChart(temperatureChartCanvas);
        if (temperatureChart) {
            temperatureChart.destroy();
        }
    }

    // Destroy the rhodesTemperatureChart
    const rhodesTemperatureChartCanvas = document.getElementById("rhodesTemperatureChart");
    if (rhodesTemperatureChartCanvas) {
        const rhodesTemperatureChart = Chart.getChart(rhodesTemperatureChartCanvas);
        if (rhodesTemperatureChart) {
            rhodesTemperatureChart.destroy();
        }
    }
}


function graph1(year) {
    const baseUrl = "https://archive-api.open-meteo.com/v1/archive?latitude=-33.3042&longitude=26.5328&start_date=2018-01-01&end_date=2018-12-31&daily=temperature_2m_mean&timezone=Africa%2FCairo";
    const updatedUrl = baseUrl.replace(/start_date=[^&]+/, `start_date=${year}-01-01`)
    .replace(/end_date=[^&]+/, `end_date=${year}-12-31`);

    // Fetch the JSON data from the URL
    fetch(updatedUrl)
        .then(response => response.json())
        .then(data => {
            // Extract dates and temperature data
            const dates = data.daily.time;
            const temperatureData = data.daily.temperature_2m_mean;
    
            // Create a line chart using Chart.js
            const ctx = document.getElementById("temperatureChart").getContext("2d");
            const myChart = new Chart(ctx, {
                type: "line",
                data: {
                    labels: dates,
                    datasets: [
                        {
                            label: ``,
                            data: temperatureData,
                            fill: false,
                            borderWidth: 2
                        }
                    ]
                },
                options: {
                    scales: {
                        x: {
                            grid: {
                                color: 'rgba(124, 124, 124, 0.8)'
                            },
                            type: "time",
                            time: {
                                unit: "day",
                                tooltipFormat: "MMM D, YYYY",
                                displayFormats: {
                                    day: "MMM D"
                                }
                            },
                            title: {
                                display: true,
                                text: "Date"
                            }
                        },
                        y: {
                            grid: {
                                color: 'rgba(124, 124, 124, 0.8)'
                            },
                            beginAtZero: false,
                            title: {
                                display: true,
                                text: "Temperature (°C)"
                            }
                        }
                    },
                    plugins: {
                        title: {
                          display: true,
                          text: `API datasource (https://open-meteo.com) - Average Temperature in Grahamstown (Makhanda) - ${year}`,
                          font: {
                            size: 25
                          }
                        }
                    }                    
                }
            });
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

function graph2(year) {
    // Fetch the JSON data from local file depending on the year
    const directory = `./cleanedRhodesWeatherData/rhodesWeatherStation_${year}.json`;

    fetch(directory)
    .then(response => response.json())
    .then(data => {
        // Extract dates and temperature data
        const dates = data.date;
        const temperatureData = data.temp;

        // Create a line chart using Chart.js
        const ctx = document.getElementById("rhodesTemperatureChart").getContext("2d");
        const myChart = new Chart(ctx, {
            type: "line",
            data: {
                labels: dates,
                datasets: [
                    {
                        label: "Temperature (°C)",
                        data: temperatureData,
                        fill: false,
                        borderColor: "rgba(250, 100, 192, 1)",
                        borderWidth: 2
                    }
                ]
            },
            options: {
                scales: {
                    x: {
                        grid: {
                            color: 'rgba(124, 124, 124, 0.8)'
                        },
                        type: "time",
                        time: {
                            unit: "day",
                            tooltipFormat: "MMM D, YYYY",
                            displayFormats: {
                                day: "MMM D"
                            }
                        },
                        title: {
                            display: true,
                            text: "Date"
                        }
                    },
                    y: {
                        grid: {
                            color: 'rgba(124, 124, 124, 0.8)'
                        },
                        beginAtZero: false,
                        title: {
                            display: true,
                            text: "Temperature (°C)"
                        }
                    }
                },
                plugins: {
                    title: {
                      display: true,
                      text: `Rhodes Weather Data Store - Average Temperature in Grahamstown (Makhanda) - ${year}`,
                      font: {
                        size: 25
                      }
                    }
                }            
            }
        });
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
}