from flask import Flask, jsonify, request
from flask_cors import CORS
from ticket_sdk.ticket import TicketEmitterDto, TicketsManager

app = Flask(__name__)
CORS(app)

app.config["APPLICATION_ROOT"] = "/api/v1"

# Global state
# Yes this is shit, it ain't much but it's honest work!
tickets_manager = TicketsManager()

@app.route("/tickets", methods=["POST"])
def create_tickets():
    print("GOT REQUEST")
    try:
        ticket_data = request.get_json()
        ticket_dto = TicketEmitterDto(**ticket_data)

        emitted_tickets = tickets_manager.emit(ticket_dto)

        return jsonify({
            "message": "success",
            "tickets": [ticket.to_dict() for ticket in emitted_tickets],
        })
    except Exception as e:
        return jsonify({
            "message": "failure",
            "error"  : str(e),
        }), 400


@app.route("/tickets", methods=["GET"])
def get_tickets():
    try:
        return jsonify({
            "message": "success",
            "tickets": [ticket.to_dict() for ticket in tickets_manager.get_tickets("emitter")],
        })
    except Exception:
        return jsonify({
            "message": "failure",
            "error": "no tickets has been created",
        }), 400
