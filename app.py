from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:15931@localhost/my_database'
db = SQLAlchemy(app)
Bootstrap(app)


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(500), nullable=False)


class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')


def extract_data_to_file():
    feedback_data = Feedback.query.all()
    project_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(project_directory, 'bd.txt')

    with open(file_path, 'w') as file:
        for feedback in feedback_data:
            file.write(
                f"ID: {feedback.id}, Name: {feedback.name}, Email: {feedback.email}, Message: {feedback.message}\n")


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Домашняя страница")


@app.route('/examples')
def examples():
    return render_template('examples.html', title="Примеры работ")


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        feedback = Feedback(name=form.name.data, email=form.email.data, message=form.message.data)
        db.session.add(feedback)
        db.session.commit()
        flash('Feedback submitted successfully!')
        extract_data_to_file()
    return render_template('feedback.html', form=form, title="Обратная связь")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
