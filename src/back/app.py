from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/tickets": {"origins": "*"}})

@app.route("/tickets", methods=["POST"])
def create_tickets():
    return jsonify({"message": "success"})

@app.route("/tickets", methods=["GET"])
def get_tickets():
    return jsonify(
        {
            "message": "success",
            "tickets": [
                {
                    "consumed": False,
                    "event_date": "Tue, 05 Nov 2024 00:00:00 GMT",
                    "event_name": "La fête du slip",
                    "id": "0e5fff3f-c93e-4b1f-820c-eee101b73ad5",
                    "price": 1.0
                },
                {
                    "consumed": False,
                    "event_date": "Tue, 05 Nov 2024 00:00:00 GMT",
                    "event_name": "La fête du slip",
                    "id": "dde695f0-cea2-429f-bb3f-fb5279affb4f",
                    "price": 1.0
                },
                {
                    "consumed": False,
                    "event_date": "Tue, 05 Nov 2024 00:00:00 GMT",
                    "event_name": "La fête du slip",
                    "id": "2ef46d32-f3dc-4ee8-8bf7-34ae4c7d47a7",
                    "price": 1.0
                },
                {
                    "consumed": False,
                    "event_date": "Tue, 05 Nov 2024 00:00:00 GMT",
                    "event_name": "La fête du slip",
                    "id": "5b8a10f3-4fcc-4aae-85ad-0105cbbc863d",
                    "price": 1.0
                },
                {
                    "consumed": False,
                    "event_date": "Tue, 05 Nov 2024 00:00:00 GMT",
                    "event_name": "La fête du slip",
                    "id": "3942120e-584c-41af-a2be-9742fa7889ba",
                    "price": 1.0
                }
            ]
        }
    )


app.run(debug=True)
