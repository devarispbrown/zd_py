These are simple examples for using Python to consume the Zendesk API. Make sure your ZD_USER and ZD_PASS environment variables are set before using this.

## On Mac

```
export ZD_USER='user@example.com'
export ZD_PASS='password'
```

## On Windows

```
set ZD_USER=user@example.com
set ZD_PASS=password
```

I've used the Requests library to do all my HTTP communication so if you need to do more complex operations check it out: <http://docs.python-requests.org/en/latest/>.

In the code, I've done basic CRUD operations for Tickets and Users. If you'd like to see more, email me at <api@zendesk.com>. These should be pretty self explanatory.

Make sure you change up all the variable names to your instance inside the code before running 

## Usage:

```
python zdTicketOperations.py
```

## Sample Output:

```
{"url":"https://thegizzle.zendesk.com/api/v2/users/311469541.json","id":311469541,"external_id":null,"name":"Pablo","alias":null,"created_at":"2012-12-17T23:42:48Z","updated_at":"2012-12-17T23:42:48Z","active":true,"verified":false,"shared":false,"locale_id":null,"locale":"en-US","time_zone":"Pacific Time (US & Canada)","last_login_at":null,"email":"pablito@example.org","phone":null,"signature":null,"details":null,"notes":null,"organization_id":null,"role":"end-user","custom_role_id":null,"moderator":false,"ticket_restriction":"requested","only_private_comments":false,"tags":[],"suspended":false,"photo":null}],"next_page":null,"previous_page":null,"count":13}
{'status': '201 Created', 'x-zendesk-api-version': 'v2', 'content-length': '622', 'server': 'nginx/1.0.15', 'x-zendesk-user-id': '244792127', 'connection': 'keep-alive', 'location': 'https://thegizzle.zendesk.com/api/v2/users/309162917.json', 'cache-control': 'no-cache', 'date': 'Tue, 18 Dec 2012 00:37:11 GMT', 'x-zendesk-origin-server': 'app14.sys.zendesk.com', 'content-type': 'application/json; charset=utf-8', 'x-runtime': '489'}
{"user":{"url":"https://thegizzle.zendesk.com/api/v2/users/309162917.json","id":309162917,"external_id":null,"name":"Zendesk Dev Team","alias":null,"created_at":"2012-12-18T00:37:10Z","updated_at":"2012-12-18T00:37:10Z","active":true,"verified":false,"shared":false,"locale_id":null,"locale":"en-US","time_zone":"Pacific Time (US & Canada)","last_login_at":null,"email":"api@zendesk.com","phone":null,"signature":null,"details":null,"notes":null,"organization_id":null,"role":"agent","custom_role_id":null,"moderator":false,"ticket_restriction":null,"only_private_comments":false,"tags":[],"suspended":false,"photo":null}}
{'status': '200 OK', 'x-zendesk-api-version': 'v2', 'x-content-type-options': 'nosniff', 'content-encoding': 'gzip', 'transfer-encoding': 'chunked', 'x-runtime': '53', 'server': 'nginx/1.0.15', 'x-zendesk-user-id': '244792127', 'connection': 'keep-alive', 'etag': '"825947fe73243005f72e30ea47095d7d"', 'x-zendesk-origin-server': 'app34.sys.zendesk.com', 'cache-control': 'private, max-age=0, must-revalidate', 'date': 'Tue, 18 Dec 2012 00:37:11 GMT', 'content-type': 'application/json; charset=utf-8'}
{"user":{"url":"https://thegizzle.zendesk.com/api/v2/users/244792127.json","id":244792127,"external_id":null,"name":"DeVaris Brown","alias":"Master of the Universe","created_at":"2012-08-06T19:56:20Z","updated_at":"2012-11-01T03:43:06Z","active":true,"verified":true,"shared":false,"locale_id":null,"locale":"en-US","time_zone":"America/Denver","last_login_at":"2012-12-18T00:36:06Z","email":"dbrown@zendesk.com","phone":"","signature":"You've just been helped by the Master...Your Master... Master doesn't have a phone number so don't even ask chump","details":"","notes":"","organization_id":22140487,"role":"admin","custom_role_id":null,"moderator":true,"ticket_restriction":null,"only_private_comments":false,"tags":["redirect_to_lotus"],"suspended":false,"photo":{"id":47898237,"file_name":"5542293400_5415a5334f_b.jpg","content_url":"https://thegizzle.zendesk.com/system/photos/4789/8237/5542293400_5415a5334f_b.jpg","content_type":"image/jpeg","size":1854,"thumbnails":[{"id":47898247,"file_name":"5542293400_5415a5334f_b_thumb.jpg","content_url":"https://thegizzle.zendesk.com/system/photos/4789/8237/5542293400_5415a5334f_b_thumb.jpg","content_type":"image/jpeg","size":1857}]}}}
```