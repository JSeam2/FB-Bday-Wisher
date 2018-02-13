from facepy import GraphAPI
import datetime
import json

# FB oauth stuff
# store oauth token in ./oauth.txt
with open('key.json', 'r') as f:
    data = json.load(f)


graph = GraphAPI(data["oauth"])

# This doesn't work
#friend_list = graph.get("me/friends?fields=birthday,name")
#print(friend_list)

birthday_wishes = ["Happy Bday!"]

#Get today's day and month
now = datetime.datetime.now().strftime("%m-%d")
month_day = now.split('-')

# sync sqllite db with
# webcal://www.facebook.com/ical/b.php?uid=YYYY&key=XXXX
# TODO check if YYYY and XXXX changes over time

# Check sqllite db with birthdays today

#Iterate through friend list birthday's and wish a random message
#graph.post(friend['id']+ '/feed', 0, message = bday_wishes[0])
