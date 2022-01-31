# pythonist_request-api
API (Application Programming Interface – интерфейс прикладного программирования)

API - это сервер, который позволяет извлекать и отправлять данные с помощью кода. В основном мы используем API для получения данных.
  Когда мы хотим получать данные из API, нам нужно сделать запрос. Запросы используются по всему Интернету. Например, когда вы зашли на этот сайт, ваш браузер сделал запрос на веб-сервер Pythonist, который ответил и выдал вам содержание данной веб-страницы.
  
Различные методы HTTP и коды ответов
  HTTP-метод	           Описание 
  
  GET	            Получить существующие данные
  POST	          Добавить новые данные
  PUT	            Обновить существующие данные
  PATCH	          Частично обновить существующие данные
  DELETE	        Удалить данные
  
  Как только REST API получает и обрабатывает HTTP-запрос, он возвращает ответ с кодом состояния HTTP. Этот код состояния предоставляет информацию об ответе и помогает клиентскому приложению узнать, что это за ответ
  
  Код	      Категория результата
  
  1хх     	Информационный ответ
  2хх	      Успешная операция
  3хх	      Перенаправление
  4хх	      Ошибка на стороне клиента
  5хх	      Ошибка на стороне сервера
  
Конечные точки API – это общедоступные URL-адреса, предоставляемые сервером, которые клиентское приложение использует для доступа к различным ресурсам и данным.

HTTP-методы 	Конечная точка API	                  Описание

  GET          	/products	                   Получить список продуктов
  GET	          /products?limit=x	           Получить только х товаров (к примеру, только 5 товаров)
  GET	          /products/<product_id>       Получить один конкретный продукт
  POST        	/products	                   Создать новый продукт
  PUT	          /products/<product_id>       Обновить товар
  PATCH       	/products/<product_id>       Частично обновить товар
  DELETE      	/products/<product_id>       Удалить товар
