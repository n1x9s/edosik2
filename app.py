from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)

Bootstrap(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Домашняя страница")


@app.route('/examples')
def examples():
    return render_template('examples.html', title="Примеры работ")


@app.route('/feedback')
def feedback():
    return render_template('feedback.html', title="Обратная связь")


if __name__ == '__main__':
    app.run()
