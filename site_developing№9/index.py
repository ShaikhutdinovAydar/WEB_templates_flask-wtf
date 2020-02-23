import random

from flask import Flask, json, render_template

app = Flask(__name__)


@app.route('/member')
def members():
    with open("templates/database.json", "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
        rand_int = random.randint(0, len(data['crew-members']) - 1)
        data = data["crew-members"][rand_int]
        name = data["name"]
        image_src = data["image_src"]
        prof = sorted(data["professions"].split(","))
        print(prof)
        return render_template('index.html', name=name, image_src=image_src, prof=", ".join(prof))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
