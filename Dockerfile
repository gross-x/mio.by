# Загрузить убунту
FROM python:3.10.1

# Добавляем контакты
# MAINTAINER DKA DEVELOP <gros@mio.by>

#Домашняя директория
WORKDIR /mio.by

# Первая "." указывает на корневую директорию где лежит докерфайл. Вторая на WORKDIR контейнера.
COPY . /mio.by

# Запустить команды
RUN apt update && apt upgrade -y && apt -y install python3-pip && pip3 install -r requirements.txt

CMD python run.py

