#!/usr/bin/python

import requests, json, os, argparse, ast

parser = argparse.ArgumentParser(add_help=True, description='Create and get Zendesk tickets with Python')
parser.add_argument("-g", "--get", action='store_true', help="Gets tickets from your Zendesk instance")

subparsers = parser.add_subparsers(help='commands')

# Create Ticket
create_parser = subparsers.add_parser('create', help='Creates new Zendesk ticket')
create_parser.add_argument("-d", "--create-data", action='store', type=ast.literal_eval, required=True, help="JSON string that stores ticket data. Remember to escape your quotation marks with a backslash(\).")

args = parser.parse_args()

if args.get:
  get_url = 'https://thegizzle.zendesk.com/api/v2/tickets.json'
  headers = {'Accept':'application/json'}
  get = requests.get(get_url, auth=(os.environ['ZD_USER'], os.environ['ZD_PASS']), headers=headers)
  print get.status_code
  print get.text

elif args.create_data:
  create_url = 'https://thegizzle.zendesk.com/api/v2/tickets.json'
  headers = {'Accept':'application/json', 'Content-Type':'application/json'}
  create_data = args.create_data
  create = requests.post(create_url, auth=(os.environ['ZD_USER'], os.environ['ZD_PASS']), data=json.dumps(create_data), headers=headers)
  print create.status_code
  print create.text