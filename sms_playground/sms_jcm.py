# Request
from twilio.rest import Client

account_sid = '[AcctSID]'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+TwilioGivenNumber',
    body='HELLLLLLOOOOOOO! XD',
    to='+YourNumber'
)

# print(message.sid)

# Response
# 201 - CREATED - The request was successful. We created a new resource and the response body contains the representation.
# {
#     "sid": "SM3922f43fa45e461c8b70634be1691cf3",
#     "date_created": "Thu, 23 Jul 2020 06:41:24 +0000",
#     "date_updated": "Thu, 23 Jul 2020 06:41:24 +0000",
#     "date_sent": null,
#     "account_sid": "ACaea47d8a8c635df8c3f710f1d7883e39",
#     "to": "+YourNumber",
#     "from": "+TwilioGivenNumber",
#     "messaging_service_sid": null,
#     "body": "Sent from your Twilio trial account - HELLLLLLOOOOOOO! XD",
#     "status": "queued",
#     "num_segments": "1",
#     "num_media": "0",
#     "direction": "outbound-api",
#     "api_version": "2010-04-01",
#     "price": null,
#     "price_unit": "USD",
#     "error_code": null,
#     "error_message": null,
#     "uri": "/2010-04-01/Accounts/ACaea47d8a8c635df8c3f710f1d7883e39/Messages/SM3922f43fa45e461c8b70634be1691cf3.json",
#     "subresource_uris": {
#         "media": "/2010-04-01/Accounts/ACaea47d8a8c635df8c3f710f1d7883e39/Messages/SM3922f43fa45e461c8b70634be1691cf3/Media.json"
#     }
# }
