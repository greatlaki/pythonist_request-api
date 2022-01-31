import requests

BASE_URL = 'https://fakestoreapi.com'

query_params = {
    "limit": 3
}

# response = requests.get(f"{BASE_URL}/products")
response = requests.get(f"{BASE_URL}/products", params=query_params)
print(response.json())
'''
1. В приведенном выше сценарии используется метод requests.get() для отправки запроса GET 
в конечную точку API /products. 
Данный запрос возвращает нам список всех продуктов. Затем мы вызываем метод .json()
2. Метод requests.get() принимает параметр с именем params, в котором 
мы можем указать параметры нашего запроса в формате словаря Python. 
Таким образом, мы создаем словарь с именем query_params и передаем limit в качестве ключа и 3 в качестве значения. 
Затем мы передаем этот словарь query_params в request.get()
'''
print(response.status_code)