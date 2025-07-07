from flask import Flask, jsonify, request
import pprint
import logging
import pytest
import argparse

###############################################################################

app = Flask(__name__)
logger = logging.getLogger(__name__)

# Sample data
tickets = [
    { "id": 1, "title": "AAA" },
    { "id": 2, "title": "BBB" },
    { "id": 3, "title": "CCC" }
]

###############################################################################

parser = argparse.ArgumentParser(description='This is my help')
args = parser.parse_args()

###############################################################################

# Get all tickets
@app.route('/tickets', methods=['GET'])
def get_tickets():
    """
        Get All op
    """
    print("In get_tickets()")
    logger.info('"In get_tickets()')
    #http://127.0.0.1:5000/tickets
    return jsonify(tickets)

# Get a single ticket by ID
@app.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    """
        Get op
    """
    print("In get_ticket()")
    logger.info('"In get_ticket()')
    #http://127.0.0.1:5000/tickets/1
    ticket = next((ticket for ticket in tickets if ticket["id"] == ticket_id), None)
    return jsonify(ticket) if ticket else (jsonify({"error": "ticket not found"}), 404)

# Add a new ticket
@app.route('/tickets', methods=['POST'])
def add_ticket():
    """
        Post op
    """
    print("In add_ticket()")
    new_ticket = request.json
    tickets.append(new_ticket)
    return jsonify(new_ticket), 201

# Update a ticket
@app.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    print("In update_ticket()")
    ticket = next((ticket for ticket in tickets if ticket["id"] == ticket_id), None)
    if not ticket:
        return jsonify({"error": "ticket not found"}), 404
    data = request.json
    ticket.update(data)
    return jsonify(ticket)

# Delete a ticket
@app.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    print("In delete_ticket()")
    global tickets
    tickets = [ticket for ticket in tickets if ticket["id"] != ticket_id]
    return jsonify({"message": "ticket deleted"})

###############################################################################

#@pytest.fixture
def get_address() -> str:
    return "http://127.0.0.1:5000/"

def test_get_address() -> None:
    """Test web server address"""
    assert get_address() == "http://127.0.0.1:5000/"

###############################################################################

if __name__ == '__main__':
    logging.basicConfig(filename='tmp.log', level=logging.INFO)
    logger.info('Started')
    #app.run(host='127.0.0.1', port=5000, debug=True)
    app.run(debug=True)
