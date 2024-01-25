from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def base():
    context = {'title': 'Базовый шаблон'}
    return render_template('base.html', **context)


@app.route('/index/')
def index():
    context = {'title': 'Стартовая страница'}
    return render_template('index.html', **context)


@app.route('/opportunities/')
def opportunities():
    context = {'title': 'Возможности'}
    return render_template('opportunities.html', **context)


@app.route('/reasons/')
def reasons():
    context = {'title': 'Причины'}
    return render_template('reasons.html', **context)


if __name__ == '__main__':
    app.run()
