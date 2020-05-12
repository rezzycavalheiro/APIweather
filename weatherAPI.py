import requests
import json

cidade = input("Digite a cidade: ")
pais = input("Digite o país: ")

url = "http://api.openweathermap.org/data/2.5/weather?q=" + cidade + "," + pais + "&appid=442de31b43491aba83051131ecfeffe3"

response = requests.get(url)
# print(response.status_code)
# print(response.content)
weather = response.content.decode('utf8')
weather = json.loads(weather)
temp = weather['main']['temp'] - 273.15
sensacao = weather['main']['feels_like'] - 273.15 
minima = weather['main']['temp_min'] - 273.15 
maxima = weather['main']['temp_max'] - 273.15  

print("Temperatura atual em", cidade, '%2.2f' % temp, "º C")
print("Sensação de ", '%2.2f' % sensacao, "º C, com mínima de", '%2.2f' % minima, "º C, e máxima de", '%2.2f' % maxima, "º C")
