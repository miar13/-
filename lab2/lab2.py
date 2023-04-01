from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def hello():
    user_data={
        "name":"Шаувхалова Арбита",
        "link":"@xxaviiiii",
        "img":"https://damion.club/uploads/posts/2022-11/1668399968_damion-club-p-beshenaya-chikhuakhua-instagram-90.jpg",
        "poroda":"Чихуахуа",
        "char":"Бешеный",
        "description":"Хорошо воспитана, умная, но до безумия наплевательски относится ко всему"
        }
    return render_template("sam.html", user=user_data)
app.run(debug=True)