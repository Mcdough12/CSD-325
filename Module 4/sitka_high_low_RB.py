import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

def read_weather_data(choice):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates, temps = [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                if choice == 'highs':
                    temp = int(row[5])
                elif choice == 'lows':
                    temp = int(row[6])
            except ValueError:
                continue
            else:
                dates.append(current_date)
                temps.append(temp)
        return dates, temps

def plot_temperatures(dates, temps, label, color):
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)
    plt.title(f"Daily {label} Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

while True:
    print("\nMenu:")
    print("1 - View High Temperatures")
    print("2 - View Low Temperatures")
    print("3 - Exit")
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == '1':
        dates, highs = read_weather_data('highs')
        plot_temperatures(dates, highs, "High", 'red')
    elif choice == '2':
        dates, lows = read_weather_data('lows')
        plot_temperatures(dates, lows, "Low", 'blue')
    elif choice == '3':
        print("Thank you for using the Sitka Weather Viewer. Goodbye!")
        sys.exit()
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
