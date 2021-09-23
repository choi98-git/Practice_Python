# 네이버 날씨 크롤링

import requests
from bs4 import BeautifulSoup

url = 'https://weather.naver.com'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print()
else : 
    print(response.status_code)

# 지역 정보
location = soup.find('div',{'class':'location_area'})
location_name = location.find('strong',{'class':'location_name'}).text

# html중 날씨 관련 area 
weather = soup.find('div',{'class':'weather_area'})

# 현재 온도
now_degree = weather.find('strong',{'class':'current'}).text

# 온도 비교
compare_degree = weather.find('p',{'class':'summary'}).text

# 날씨 정보 리스트
weather_info_list = weather.find('dl',{'class':'summary_list'})
weather_info = weather_info_list.findAll('dd',{'class':'desc'})

# 습도
humidity = weather_info[0].text

# 바람
wind = weather_info[1].text

# 체감 온도
feel_degree = weather_info[2].text

print('현재위치: ' + location_name)
print(now_degree)
print(compare_degree)
print('습도: ' + humidity)
print('북동풍: ' + wind)
print('체감온도: ' + feel_degree)
