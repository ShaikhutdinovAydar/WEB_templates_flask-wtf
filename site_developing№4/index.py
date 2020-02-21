from flask import Flask, render_template

app = Flask(__name__)


@app.route(f'/answer')
@app.route(f'/auto_answer')
def odd():
    listt = {'title': "Анкета", "surname": "Watny", "name": "Mark",
             "education": "Выше среднего", "profession": "Штурман марсохода", "sex": "male",
             "motivation": "Всегда мечтал застрять на Марсе!",
             "ready": "True"}
    return render_template('auto_answer.html', listt=listt)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
