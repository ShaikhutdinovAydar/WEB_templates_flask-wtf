from flask import Flask, render_template
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('ID Астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль Астронавта', validators=[DataRequired()])
    username_kap = StringField('ID Капитана', validators=[DataRequired()])
    password_kap = PasswordField('Пароль Капитана', validators=[DataRequired()])
    submit = SubmitField('Войти')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template('success.html')
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
