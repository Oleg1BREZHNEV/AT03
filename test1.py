import pytest
from main1 import get_weather  # замените my_module на имя вашего модуля


def test_get_weather_success(mocker):
   mock_get = mocker.patch('main1.requests.get')

   # Создаем мок-ответ для успешного запроса
   mock_get.return_value.status_code = 200
   mock_get.return_value.json.return_value = {
       'weather': [{'description': 'clear sky'}],
       'main1': {'temp': 282.55}
   }

   api_key = '01d60d241916f5d850574139c275f457'
   city = 'London'
   weather_data = get_weather(api_key, city)

   assert weather_data == {
       'weather': [{'description': 'clear sky'}],
       'main1': {'temp': 282.55}
   }

def test_get_weather_failure(mocker):
   mock_get = mocker.patch('main1.requests.get')

   # Создаем мок-ответ для неуспешного запроса
   mock_get.return_value.status_code = 404

   api_key = '01d60d241916f5d850574139c275f457'
   city = 'UnknownCity'
   weather_data = get_weather(api_key, city)

   assert weather_data is None
