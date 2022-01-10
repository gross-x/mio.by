# Загрузить убунту
FROM python

# Добавляем контакты
# MAINTAINER DKA DEVELOP <gros@mio.by>

#Домашняя директория
WORKDIR /mio.by

# Первая "." указывает на корневую директорию где лежит докерфайл. Вторая на WORKDIR контейнера.
COPY . /mio.by

# Указываем на каком порту работает программа.(Открываем порт в контейнере)
EXPOSE 9091

# Запустить команды
RUN apt update && apt upgrade -y && apt -y install python3-pip && pip3 install -r requirements.txt

CMD python run.py
#CMD ['run.py']
