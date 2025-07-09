#!/usr/bin/env python

from flask import Flask, jsonify, request
import pprint
import logging
import pytest
import argparse
import sqlite3
from sqlite3 import Error as Err

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

def get_port() -> int:
    return 5000

def get_address() -> str:
    return '127.0.0.1'

###############################################################################

def sqlite_try():
    try:
        print()
        print("SQLite:")
        connection = sqlite3.connect(':memory:')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE ticket (
                          id INTEGER PRIMARY KEY,
                          name TEXT )''')
        cursor.execute("INSERT INTO ticket VALUES (20, 'WWWWW')")
        cursor.execute("SELECT * FROM ticket")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print()
    # if any interruption or error occurs
    except Err: print(Err)
    # terminate the connection    
    finally: connection.close()

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
    #request.get_json()
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

def test_get_full_address() -> None:
    """Test web server address"""
    assert get_address() == '127.0.0.1'
    assert get_port() == 5000

###############################################################################

if __name__ == '__main__':
    sqlite_try()

    parser = argparse.ArgumentParser(description='Current server')
    args = parser.parse_args()
    logging.basicConfig(filename='tmp.log', level=logging.INFO)
    logger.info('Started')
    print(get_tickets.__doc__)
    #app.run(host='127.0.0.1', port=5000, debug=True)
    #app.run(debug=True)
    app.run(host=get_address(), port=get_port(), debug=True)
