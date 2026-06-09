from flask import Flask, jsonify
import requests

app = Flask(__name__)

orders = {
    1: {
        "id": 1,
        "user_id": 1,
        "product": "Laptop"
    },
    2: {
        "id": 2,
        "user_id": 2,
        "product": "Keyboard"
    }
}

@app.route("/orders/<int:order_id>")
def get_order(order_id):

    order = orders.get(order_id)

    if not order:
        return jsonify({
            "message": "Order not found"
        })

    user = requests.get(
        f"http://127.0.0.1:5001/users/{order['user_id']}"
    ).json()

    return jsonify({
        "order": order,
        "user": user
    })

if __name__ == "__main__":
    app.run(
        port=5002,
        debug=True
    )
