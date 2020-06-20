# Сайт по доставке продуктов на дом

## Клонирование проекта
    
    git clone https://github.com/Smirnoff2019/delivery.git
    cd Delivery
    
## Деплой проекта
    
    cd backend
    python -m venv django_delivery
    delivery\Scripts\activate.bat
    python -m pip instal -r requirements.txt
    cd django_delivery
    python manage.py migrate

## Запуск сервера разработки

    cd backend
    delivery\Scripts\activate.bat
    cd django_delivery
    python manage.py runserver 8080 

##Установка питона 3.6 на Windows 10

    https://python-scripts.com/install-python-windows