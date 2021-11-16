from flask import Flask, jsonify, request
app = Flask(__name__)

tasks = [
    {'id': 1,
     'title': "tution",
     "discription": "Early Morning I go for maths tution and I studied their Trignometry",
     'done': True
     },
    {
        'id': 2,
        'title': "Tifine",
        "discription": "After Coming From Tution I goes for breakfast And I have eaten Chapati And Curry"
    }
]


@app.route("/knowAboutme")
def helloworld():
    return 'Hii I am Adarsh Tiwari From West Bengal'


@app.route("/gettask")
def showtasks():
    return jsonify({
        "data": tasks
    })


@app.route("/addTask", methods=["POST"])
def addTask():
    if not request.json:
        return jsonify({
            "status": "success",
            "message": "add some data"
        })
    t={
        "id":tasks[-1]["id"]+1,
        "title":request.json["title"],
        "discription":request.json["discription"]
    }


if(__name__ == "__main__"):
    app.run(debug=True)
