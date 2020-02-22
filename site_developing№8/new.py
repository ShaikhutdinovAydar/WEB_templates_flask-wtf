from flask import Flask, request, render_template

app = Flask(__name__)

a = 3
pictures = ["static/img/mars-2.jpg", "static/img/mars-3.jpg"]


@app.route('/', methods=['POST', 'GET'])
def bootstrap_carousel():
    global a, pictures
    if request.method == 'GET':
        return render_template('base.html', pictures=pictures)
    elif request.method == 'POST':
        a += 1
        f = request.files['file']
        file = f"static/img/mars-{a}.jpg"
        with open(file, "wb") as fil:
            fil.write(f.read())
        pictures.append(file)
        return render_template('base.html', pictures=pictures)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
