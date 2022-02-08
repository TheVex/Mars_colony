from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/image_mars')
def image_mars():

    return f'''<h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/mars.jpg')}" alt="здесь должна была быть картинка, но не нашлась">
    <br>Это - как выглядит Марс сейчас.</br>
    <img src="{url_for('static', filename='img/future_city.jpg')}" alt="здесь должна была быть картинка, но не нашлась">
    <br>А это - Марс, когда на него прибудем мы.</br>
    <br>Понравилось? Присоединяйся!</br>'''


@app.route('/promotion')
def promotion():
    speech = ['Человечество вырастает из детства.',
              'Человечеству мала одна планета.',
              'Мы сделаем обитаемыми безжизненные пока планеты.',
              'И начнем с Марса!',
              'Присоединяйся!',
              'Земляне всех стран, объединяйтесь!']
    return '</br>'.join(speech)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')