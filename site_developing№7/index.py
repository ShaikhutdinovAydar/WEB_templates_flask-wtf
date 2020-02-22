import random

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/table/<sex>/<age>')
def table(sex, age):
    color = ""
    if sex == "female":
        random_nums = random.randint(0, 255)
        random_nums1 = random.randint(1, 50)
        random_nums2 = random.randint(1, 50)
        color = f"{random_nums}, {random_nums1}, {random_nums2}"
    elif sex == "male":
        random_nums = random.randint(1, 50)
        random_nums1 = random.randint(1, 50)
        random_nums2 = random.randint(1, 255)
        color = f"{random_nums}, {random_nums1}, {random_nums2}"
    if int(age) < 21:
        src = 'baby.jpg'
    else:
        src = 'adult.jpg'
    return render_template('index.html', color=color, src=url_for('static', filename=f'img/{src}'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
