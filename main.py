from FBObject import FBObject
from dank import memes
from dank import getMemes
from urllib import quote
import time

headers = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","DNT": "1","Connection": "keep-alive","Upgrade-Insecure-Requests": "1"}

username = 'aparen01@mail.uoguelph.ca'
password = open("psswd").readline().rstrip()

FBobj = FBObject(headers)
FBobj.login(username, password)

#FBobj.sendMessage("Test", "1526338537641003")
#images = FBobj.getImages("100002661911773")

memers = open("sendTo").read().splitlines()
dankMemes = getMemes()

memersArray = []

def writeFile(memersArray):
    f = open("sendTo",'w')
    for z in memersArray:
        f.write(str(z['id']) + "|" + str(z['time']) + "|" + str(z['lastUpdated']) + "|" + str(z['atMeme']) + "\n")
    
    f.close()

for x in memers:
    memersArray.append({"id":int(x.split('|')[0]), "time":int(x.split('|')[1]), "lastUpdated":int(x.split('|')[2]), "atMeme":int(x.split('|')[3])})

while(True):
    currentTime = int(time.time())
    
    for x in xrange(0,len(memersArray)):
        if currentTime - memersArray[x]['lastUpdated'] > memersArray[x]['time']:
            memersArray[x]['lastUpdated'] = currentTime
            
            memersArray[x]['atMeme'] += 1
            writeFile(memersArray)
            memeLocation = memes(dankMemes, memersArray[x]['atMeme'])
            
            if memeLocation != "null":
                print memeLocation
                print str(memersArray[x]['id'])
                FBobj.sendImage(memeLocation, str(memersArray[x]['id']))
            
    
    if len(open("sendTo").read().splitlines()) > len(memersArray):
        a = open("sendTo").read().splitlines()
        for x in a[len(memersArray):]:
            memersArray.append({"id":int(x.split('|')[0]), "time":int(x.split('|')[1]), "lastUpdated":int(x.split('|')[2]), "atMeme":int(x.split('|')[3])})
            print "added user"
            print memersArray
    
    time.sleep(1)

FBobj.logout()
