from flask import Flask, jsonify

app = Flask(__name__)

users = {
    1: {
        "id": 1,
        "name": "Rahul"
    },
    2: {
        "id": 2,
        "name": "Amit"
    }
}

@app.route("/users/<int:user_id>")
def get_user(user_id):

    return jsonify(
        users.get(
            user_id,
            {"message": "Not Found"}
        )
    )

if __name__ == "__main__":
    app.run(
        port=5001,
        debug=True
    )
