import json
import requests
import random

latest = requests.get('https://xkcd.com/info.0.json').json()
num = random.randint(1, latest['num'])
comic = requests.get('https://xkcd.com/' + str(num) + '/info.0.json').json()
print("")
print("click the link for the image")
print("")
print(comic['img'])
print("")
print( '_' + comic['alt'] + '_')



