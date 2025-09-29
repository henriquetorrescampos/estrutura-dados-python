import random
import statistics as st

weather = [random.randint(15, 40) for _ in range(5)]
days = [random.randrange(121) for _ in range(121)]

min_weather = min(weather)
max_weather = max(weather)
average_weather = st.mean(weather)
# average_weather2 = max_weather / len(weather) second way

weather_days = list(zip(days, weather))

days_bellow_mean = len([day for day, temp in weather_days if temp < average_weather])


print(f"A quantidade de dias que a temperatur foi abaixa da média foi {days_bellow_mean}")
