import pdb
import pprint
import requests
import json
import random
from requests.auth import HTTPBasicAuth

#GET: curl http://127.0.0.1:5000/api/items
#POST: curl -X POST -H "Content-Type: application/json" -d '{"name": "This is item 3"}' http://127.0.0.1:5000/api/items
#PUT: curl -X PUT -H "Content-Type: application/json" -d '{"name": "This is updated item 1"}' http://127.0.0.1:5000/api/items/1
#DELETE: curl -X DELETE http://127.0.0.1:5000/api/items/1

server_address_full = 'http://127.0.0.1:5000/tickets/'

def main():

    print("For server->get_tickets()")
    try:
        print()
        session = requests.Session()
        session.allow_redirects = True
        session.max_redirects = 3
        response = session.get(server_address_full + '1')
        response.raise_for_status()
        print()
        response1 = requests.get(server_address_full + '1', timeout=5)
        response1.raise_for_status()
        #pdb.set_trace()
        print()
        pprint.pprint(response.json())
        print(response.text)
        print(response.json())
        print(response.status_code)
        print()
        pprint.pprint(response1.json())
        print(response1.text)
        print(response1.json())
        print(response1.status_code)
        print()
    # If the request fails (404) then print the error.
    except requests.exceptions.HTTPError as error:
        print(error)
    except requests.exceptions.TooManyRedirects as error:
        print(error)
    except requests.ConnectionError as error:
        print(error)
    except requests.Timeout as error:
        print(error)
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
    print()
    #private_url_response = requests.get( url="https://api.github.com/user", auth=HTTPBasicAuth("username", "token") )

    print("For server->add_ticket()")
    list1 = [8, 5, 10, 4, 5, 6, 12, 14, 16]
    id = random.choice(list1)
    print(id)
    # Composing a payload for API
    payload = { "id": id, "title": "EEEEE" }
    # Defining content type for our payload
    header = { 'Content-type': 'application/json' }
    try:
        # Sending a post request to the server (API)
        #response = requests.post(url=server_address_full, data=json.dumps(payload), headers=header)
        response = requests.post(server_address_full, json=payload, headers=header)
        # Printing out the response of API
        print(response.text)
        print(response.json())
        print(response.status_code)
    # If the request fails (404) then print the error.
    except requests.exceptions.HTTPError as error:
        print(error)
    except requests.exceptions.TooManyRedirects as error:
        print(error)
    except requests.ConnectionError as error:
        print(error)
    except requests.Timeout as error:
        print(error)
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")

if __name__ == "__main__":
    main()
