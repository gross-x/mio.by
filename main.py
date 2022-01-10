from flask import Flask, render_template, request, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfgdfg.v,mbcvnjdfkjvn7h3u5'  # Секретный ключ для сесии.

#  Блок переменных
menu = [{"name": "Калькулятор топлива", "url": "kalk"},  # Меню сайта
        {"name": "Обратная связь", "url": "feedback"},
        {"name": "Тест", "url": "test"},
        ]
title = 'Mio.by | Портретная и жанровая фотосессия в Гомеле и Минске!'
description = "Фотограф  в Гомеле, Михаил Рельков - Гросс. Хотите фотосессию для души? Почувствуйте себя девушкой с обложки. Придумаем образ и историю." \
              "Фотосессия с мотоциклом. Фотосессия с вашим автомобилем"
keywords = "Фотосессия в Гомеле и Минске, Фотосессия в Гомеле, фотограф Гомель, портретный фотограф гомель, фотосессия в Гомеле."

title_avto = 'Фотосессия с автомобилем  в Гомеле и Минске'
description_avto = "Организуем оригинальную фотосессию с вашим или прокатным автомобилем в Гомеле или Минске.Это " \
                   "может быть индивидуальная съемка или лавстори. Вы получите яркие, интересные и креативные " \
                   "фотографии. Фотосессия с машиной - станет хорошим способом удивить своих знакомых.Так же " \
                   "фотосессия для вашего авто может понадобиться при предпродажной подготовке автомобиля. "

keywords_avto = "car, авто, фотосессия с автомобилем в Гомеле, фотосессия с автомобилем в Минске, lavstory c автомобилем"

# Первый слайд в слайдере
first_picture_index = "static/img/moto.jpg"
first_span_index = "Фотосессия с мотоциклом"


# Декоратор
@app.route("/index")
@app.route("/")  # По этому адресу будет отрабатывать функция index(). "/" - Это главная страница
def index():  # Контекст запроса
    print(url_for('index'))
    return render_template('index.html', title=title, menu=menu, description=description, keywords=keywords, first_picture=first_picture_index, first_span=first_span_index)  # По умолчанию берет шаблоны из папки 'templates'


@app.route("/avto")
def avto():  # Контекст запроса
    print(url_for('index'))
    return render_template('avto.html', title=title_avto, menu=menu,description=description_avto, keywords=keywords_avto, first_picture=first_picture_index)


@app.route("/portfolio")
def portfolio():  # Контекст запроса
    print(url_for('index'))
    return render_template('index.html', title=title, menu=menu,description=description, keywords=keywords, first_picture=first_picture_index)


@app.route("/art")
def art():  # Контекст запроса
    print(url_for('index'))
    return render_template('index.html', title=title, menu=menu,description=description, keywords=keywords, first_picture=first_picture_index)


@app.route("/contact")
def contact():  # Контекст запроса
    print(url_for('contact'))
    return render_template('contact.html', title=title, menu=menu,description=description, keywords=keywords, first_picture=first_picture_index)


@app.errorhandler(404)  # Обработка ошибки 404
def pageNotFound(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu), 404









