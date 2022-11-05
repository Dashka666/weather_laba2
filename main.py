import requests
city ="Moscow,RU"
appid ="8485fae7c17e6ada8f411f6b3432d35a"
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city,'units':'metric','lang':'ru','APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'],"> \r\nТемпература<",
          '{0:+3.0f}'.format(i['main']['temp']),"> \r\nПогодныеусловия <",
          i['weather'][0]['description'],"> \r\nВидимость <",
          i['visibility'], "> \r\nСкорость ветра <",
          i['wind']['speed'], ">")
    print("____________________________")
