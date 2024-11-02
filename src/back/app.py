from flask import Flask, jsonify, request
from ticket_sdk.ticket import Ticket

app = Flask(__name__)

app.config["APPLICATION_ROOT"] = "/api/v1"

@app.route("/tickets", methods=["POST"])
def create_tickets():
    try:
        ticket_data = request.get_json()
        ticket = Ticket(**ticket_data)
        print(ticket)
        return jsonify({"message": "success"})
    except Exception as e:
        return jsonify({
            "message": "failure",
            "error"  : str(e),
        }), 400


@app.route("/tickets", methods=["GET"])
def get_tickets():
    return jsonify({ "message": "success", "tickets": [] })
