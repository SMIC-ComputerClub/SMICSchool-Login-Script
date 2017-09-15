import json
with open('response.txt', 'r') as file:
    calendar = json.loads(file.read())

events = calendar['result']
for event in events:
    print("{} from {}".format(event['title'], event['calName']))

    
