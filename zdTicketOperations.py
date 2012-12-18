#!/usr/bin/python

import requests, json, os

################################################################
## TICKETS
################################################################

# Get Tickets
get_tickets_url = 'https://thegizzle.zendesk.com/api/v2/tickets.json'
headers = {'Accept':'application/json'}
get_tickets = requests.get(get_tickets_url, auth=(os.environ['ZD_USER'], os.environ['ZD_PASS']), headers=headers)
print get_tickets.headers
print get_tickets.text

# Create Ticket
create_ticket_url = 'https://thegizzle.zendesk.com/api/v2/tickets.json'
headers = {'Accept':'application/json', 'Content-Type':'application/json'}
create_ticket_data = {"ticket":{"subject":"My printer is on fire!", "comment": { "body": "The smoke is very colorful." }}}
create_ticket = requests.post(create_ticket_url, auth=(os.environ['ZD_USER'], os.environ['ZD_PASS']), data=json.dumps(create_ticket_data), headers=headers)
print create_ticket.headers
print create_ticket.text

# Show Ticket
show_ticket_url = 'https://thegizzle.zendesk.com/api/v2/tickets/123.json'
headers = {'Accept':'application/json'}
show_ticket = requests.get(show_ticket_url, auth=(os.environ['ZD_USER'], os.environ['ZD_PASS']), headers=headers)
print show_ticket.headers
print show_ticket.text

# Update Ticket
update_ticket_url = 'https://thegizzle.zendesk.com/api/v2/tickets/123.json'
headers = {'Accept':'application/json', 'Content-Type':'application/json'}
update_ticket_data = {"ticket":{"status":"pending","comment":{"public":"true", "body": "Thanks, this is now updated!"}}}
update_ticket = requests.put(update_ticket_url, auth=(os.environ['ZD_USER'], os.environ['ZD_PASS']), data=json.dumps(update_ticket_data), headers=headers)
print update_ticket.headers
print update_ticket.text

# Create Ticket w/ New Requester
ticket_request_url = 'https://thegizzle.zendesk.com/api/v2/tickets.json'
headers = {'Accept':'application/json', 'Content-Type':'application/json'}
ticket_request_data = {"ticket": {"subject": "Hello","comment": { "body": "Some question" },"requester": { "locale_id": 8, "name": "Pablo", "email": "pablito@example.org" }}}
ticket_request = requests.post(ticket_request_url, auth=(os.environ['ZD_USER'], os.environ['ZD_PASS']), data=json.dumps(ticket_request_data), headers=headers)
print ticket_request.headers
print ticket_request.text

################################################################
## USERS
################################################################

# Get All Users
get_users_url = 'https://thegizzle.zendesk.com/api/v2/users.json'
headers = {'Accept':'application/json'}
get_users = requests.get(get_users_url, auth=(os.environ['ZD_USER'], os.environ['ZD_PASS']), headers=headers)
print get_users.headers
print get_users.text

# Create User w/ Multiple Identities
create_user_url = 'https://thegizzle.zendesk.com/api/v2/users.json'
headers = {'Accept':'application/json', 'Content-Type':'application/json'}
create_user_data = {"user": {"name": "Zendesk Dev Team", "role":"agent", "identities": [{ "type": "email", "value": "api@zendesk.com"}, {"type": "twitter", "value": "zendeskdevteam" }]}}
create_user = requests.post(create_user_url, auth=(os.environ['ZD_USER'], os.environ['ZD_PASS']), data=json.dumps(create_user_data), headers=headers)
print create_user.headers
print create_user.text

# Show User
show_user_url = 'https://thegizzle.zendesk.com/api/v2/users/244792127.json'
headers = {'Accept':'application/json'}
show_user = requests.get(show_user_url, auth=(os.environ['ZD_USER'], os.environ['ZD_PASS']), headers=headers)
print show_user.headers
print show_user.text