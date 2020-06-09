# Интерактивная карта 

Этот сайт, создан для того, чтобы лучше узнать про интересные места в Москве и Московской области. 
Ссылка на [сайт](http://djeck1432.pythonanywhere.com/)

## Переменные окружения
`SECRET_KEY`- это ключ шифрования данных вашего проекта в `Django`;

## Как запустить

Чтобы развернуть на `Pythonanywhere` нужно: 
- Пройдите туториал по `pythonanywhere` [здесь](https://tutorial.djangogirls.org/ru/deploy/index.html#%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-%D0%B1%D0%BB%D0%BE%D0%B3%D0%B0-%D0%BD%D0%B0-pythonanywhere)
- Не забудь вставить ссылку на этот репозиторий или скопируйте этот код:
```bash
pa_autoconfigure_django.py https://github.com/djeck1432/interactive_map.git
```
- После успешной настройки виртуального окружения и установки проекта, добавьте `SECRET_KEY`:
```bash 
echo SECRET_KEY=[your secret key] > .env
```
- Cоздайте базу данных: 
```bash 
cd [name of project].pythonanywhere.com

python3 manage.py migrate
```
- Создайте акк для админ панель:
```bash
python3 manage.py createsuperuser
```
- Загрузите локации в формате `json` следующей командой : 
```bash 
python3 manage.py load_place [url]
```
