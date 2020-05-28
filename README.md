# Описание
Микро-сервис для скачивания информации с ftp.zakupki.gov.ru, работающий на связке flask+uWSGI+NGINX.
1. Api для скачивания архивов с информацией по аукциону с ftp за заданный период
# Описание
Микро-сервис является коннектором с несколькими сервисами, работающий на связке flask+uWSGI+NGINX.
1. Api для сохранения данных в БД с id аукционов;
2. Api для получение всех данных по номеру аукциона, которые сервис получает от подключенных к нему парсер микро-сервисов.

# Структура
* app/ - директория с flask приложением
* congigs/ - директория с настройками пакетов, приложения, api. Все настройки можно получить от ConfigDealer
* wsgi.py - файл точки входа
* service.ini - файл настройками uWSGI сервиса
* afiller.sock - файл сокет для соеденения сервера NGINX  с сервисом uWSGI
* setup.py - файл установки. Временно не работает
* .env - файл с переменными окружения, необходимые для работы сериса

# Установка
1. Скачать с репозитория
2. Созздать venv и установить в него требуемые пакеты из requirements.txt
3. Настроить файл .env
4. Настроить файл .service
5. Создать uWSGI сервис в ОС.
6. Создать связть uWSGI и NGINX через файл afiller.sock

# Настройка Configs(.env) - файл переменных виртуального окружения
* API_XML_URL - ссылка на Api по предоставлению информации из XmlFile по URL
* API_XML_ID - ссылка на Api по предоставлению информации из XmlFile по локальной ссылке
* DEFAULT_LOCAL_PATH - стандартный путь с локальными файлами
* PREFIX_URL - префикс ссылки на XmlFile
* APP_MODE - режим в котором включить приложение
* DB_DIR - директория расположения локальной БД(sqlite3), используется для режима development 
* SQLALCHEMY_TRACK_MODIFICATIONS - модификатор для оповещения, используется для режима production
* SQLALCHEMY_DATABASE_URI - ссылка на базу данных, используется для режима production
