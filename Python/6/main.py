import requests
import matplotlib.pyplot as plt

def get_data(country):
    url = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv"
    response = requests.get(url)
    data = response.text.splitlines()

    header = data[0].split(",")
    country_index = header.index("Country/Region")
    dates = header[4:]

    country_data = {}
    for line in data[1:]:
        values = line.split(",")
        if values[country_index] == country:
            country_data = {date: int(value) for date, value in zip(dates, values[4:])}
            break

    return country_data

def plot_graph(data, category, show_increase=False, x_step=90):
    x = list(data.keys())
    y = list(data.values())

    if show_increase:
        y = [y[i] - y[i-1] if i > 0 else y[i] for i in range(len(y))]

    plt.plot(x, y)
    plt.xlabel("Date")
    plt.ylabel(category)
    plt.title(f"COVID-19 {category} in {country}")
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(x_step))
    plt.show()


# Пример использования
country = "Belarus"  # Выбранная страна
category = "Confirmed"  # Выбранная категория: "Confirmed" (заболевшие), "Recovered" (выздоровевшие), "Deaths" (смерти)

data = get_data(country)
plot_graph(data, category, show_increase=True)