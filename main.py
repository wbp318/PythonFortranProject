import numpy as np
import matplotlib.pyplot as plt
from weather_data import get_weather_data, extract_temperatures

# This line compiles the Fortran code and makes it available as a Python module
import numpy.f2py
with open('weather_calc.f90') as f:
    source = f.read()
    numpy.f2py.compile(source, modulename='weather_calc', extension='.f90')

import weather_calc

def plot_forecast(dates, temps, avg_temp, max_temp, min_temp):
    plt.figure(figsize=(12, 6))
    plt.plot(dates, temps, marker='o')
    plt.axhline(y=avg_temp, color='r', linestyle='--', label=f'Avg Temp: {avg_temp:.2f}°C')
    plt.axhline(y=max_temp, color='g', linestyle='--', label=f'Max Temp: {max_temp:.2f}°C')
    plt.axhline(y=min_temp, color='b', linestyle='--', label=f'Min Temp: {min_temp:.2f}°C')
    plt.title(f"Temperature Forecast for {city}")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    city = input("Enter city name: ")
    data = get_weather_data(city)
    if data:
        temperatures = extract_temperatures(data)
        dates = [item['dt_txt'] for item in data['list']]
        
        # Use the Fortran subroutine to process temperatures
        avg_temp, max_temp, min_temp = weather_calc.weather_calc.process_temperatures(
            np.array(temperatures, dtype=np.float32), 
            len(temperatures)
        )
        
        plot_forecast(dates, temperatures, avg_temp, max_temp, min_temp)
    else:
        print("Failed to retrieve weather data.")