import pytest
from main2 import get_github_user

def test_get_github_user(mocker):
   mock_get = mocker.patch('main2.requests.get')
   mock_get.return_value.status_code = 200
   mock_get.return_value.json.return_value = {
       'login' : 'nizavr',
       'id' : 345178,
       'name' : 'Nina'
   }

   user_data = get_github_user('cat')
   assert user_data == {
       'login' : 'nizavr',
       'id' : 345178,
       'name' : 'Nina'
   }

def test_get_github_user_with_error(mocker):
   mock_get = mocker.patch('main2.requests.get')
   mock_get.return_value.status_code = 500

   user_data = get_github_user('cat')
   assert user_data == None


