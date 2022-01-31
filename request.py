from pprint import pprint
import requests

BASE_URL = 'https://fakestoreapi.com'

query_params = {
    "limit": 3
}

# response = requests.get(f"{BASE_URL}/products")
response_GET = requests.get(f"{BASE_URL}/products", params=query_params)
pprint(response_GET.json())
'''
1. В приведенном выше сценарии используется метод requests.get() для отправки запроса GET 
в конечную точку API /products. 
Данный запрос возвращает нам список всех продуктов. Затем мы вызываем метод .json()
2. Метод requests.get() принимает параметр с именем params, в котором 
мы можем указать параметры нашего запроса в формате словаря Python. 
Таким образом, мы создаем словарь с именем query_params и передаем limit в качестве ключа и 3 в качестве значения. 
Затем мы передаем этот словарь query_params в request.get()
'''

new_product = {
    "title": 'test product',
    "price": 13.5,
    "description": 'lorem ipsum set',
    "image": 'https://i.pravatar.cc',
    "category": 'electronic'
}

response_POST = requests.post(f"{BASE_URL}/products", json=new_product)
print(response_POST.json())
'''
Мы используем запрос POST для добавления новых данных в REST API. Данные отправляются на сервер в формате JSON, 
который выглядит как словарь Python. Согласно документации Fake Store API, у продукта есть 
следующие атрибуты: title (название), price (цена), description (описание), image (изображение) и category (категория).
'''

updated_product = {
    "title": 'updated_product',
    "category": 'clothing'
}

response_PUT = requests.put(f"{BASE_URL}/products/21", json=updated_product)
print(response_PUT.json())

'''
Используя запрос PUT, мы можем обновить данные полностью. Это означает, что, когда мы делаем запрос PUT, 
он заменяет все старые данные новыми.
'''