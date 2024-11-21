import random

from flask import Flask, render_template


app = Flask(__name__)


CONTACT = "+380731570901"


@app.get("/")
def index():
    pizzanames = [
        "Маргарита", "Пепероні", "Гавайська", "Чотири Сира",
        "Веганська", "Куряча", "Любителі М'яса", "П'ять Сирів",
        "Курка Буффало", "Песто"
    ]

    pizzas = [
        {"name": random.choice(pizzanames), "price": random.randint(50, 400)}
        for _ in range(10)
    ]

    return render_template("index.html", contact=CONTACT, pizzas=pizzas)

@app.get('/results-ababagalamaga/')
def results():
    context = {
        "max_score": 100,
        "test_name": "Python Challenge",
        "students": [
        {"name": "Vlad", "score": 100},
        {"name": "Vlad", "score": 42},
        {"name": "Sviatoslav", "score": 99},
        {"name": "Юстин", "score": 100},
        {"name": "Viktor", "score": 79},
        {"name": "Ярослав", "score": 93},
        ],
        "title": "Результати тестування",
        "contact": CONTACT
    }

    return render_template("results.html", **context)


if __name__ == "__main__":
    app.run(debug=True)