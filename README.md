#Automated FB birthday wisher
## Smarter and Better Insincerity in the 21th Century

1. We won't use facebook graph api as it is currently quite restrictive in the information you can access. You can't get all your friends birthday from what I have tried via "me/friends?fields=id,name,birthday". The second alternative is to follow https://www.facebook.com/help/152652248136178 to get the birthday data. I recommend exploring the functionalities of the graph api via "https://developers.facebook.com/tools/explorer/"

2. Right click and copy link, you will get a link "webcal://www.facebook.com/ical/b.php?uid=XXXX&key=XXXX" in this format". To download the ics file simply change the welcal to http and input to a web browser it should prompt you to download the file. Eg. "http://www.facebook.com/ical/b.php?uid=XXXX&key=XXXX" 


TODO:
Turn the ics to a sql database


