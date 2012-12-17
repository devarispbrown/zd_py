#!/usr/bin/python

import requests, json, os

################################################################
## TICKETS
################################################################

# Get Tickets
get_url = 'https://thegizzle.zendesk.com/api/v2/tickets.json'
headers = {'Accept':'application/json'}
get = requests.get(get_url, auth=(os.environ['ZD_USER'], os.environ['ZD_PASS']), headers=headers)
print get.headers
print get.text

# Create Ticket
create_url = 'https://thegizzle.zendesk.com/api/v2/tickets.json'
headers = {'Accept':'application/json', 'Content-Type':'application/json'}
create_data = {"ticket":{"subject":"My printer is on fire!", "comment": { "body": "The smoke is very colorful." }}}
create = requests.post(create_url, auth=(os.environ['ZD_USER'], os.environ['ZD_PASS']), data=json.dumps(create_data), headers=headers)
print create.headers
print create.text

# Update Ticket
update_url = 'https://thegizzle.zendesk.com/api/v2/tickets/123.json'
headers = {'Accept':'application/json', 'Content-Type':'application/json'}
update_data = {"ticket":{"status":"pending","comment":{"public":"true", "body": "Thanks, this is now updated!"}}}
update = requests.put(update_url, auth=(os.environ['ZD_USER'], os.environ['ZD_PASS']), data=json.dumps(update_data), headers=headers)
print update.headers
print update.text

# Create Ticket w/ New Requester
request_url = 'https://thegizzle.zendesk.com/api/v2/tickets.json'
headers = {'Accept':'application/json', 'Content-Type':'application/json'}
request_data = {"ticket": {"subject": "Hello","comment": { "body": "Some question" },"requester": { "locale_id": 8, "name": "Pablo", "email": "pablito@example.org" }}}
request = requests.post(request_url, auth=(os.environ['ZD_USER'], os.environ['ZD_PASS']), data=json.dumps(request_data), headers=headers)
print request.headers
print request.text

################################################################
## USERS
################################################################
