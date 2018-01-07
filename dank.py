from BeautifulSoup import BeautifulSoup
import requests
import shutil
from urllib import quote

headers = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","DNT": "1","Connection": "keep-alive","Upgrade-Insecure-Requests": "1"}

def memes(dankCache, location):
    if location > len(dankCache):
        return "null"
    
    r = requests.get(dankCache[location], stream=True)
    if r.status_code == 200:
        with open("Memes/" + quote(dankCache[location], safe=''), 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    return "Memes/" + quote(dankCache[location], safe='')

def getMemes():
    urmom = ["https://www.reddit.com/r/youdontsurf/","https://www.reddit.com/r/dankmemes/", "https://www.reddit.com/r/youdontsurf/top/?sort=top&t=all", "https://www.reddit.com/r/dankmemes/top/?sort=top&t=all"]
    
    dankArray = []
    
    for dicks in urmom:
        r = requests.get(dicks, headers=headers)
        soup = BeautifulSoup(r.text)
        
        for penis in soup.findAll("div"):
            if penis.get('class') == "sitetable linklisting":
                for penisssss in penis.findAll("div", {"data-type":"link"}):
                    moo = str(penisssss.get('data-url'))
                    if moo.find("http") == 0:
                        dankArray.append(moo)
    
    return dankArray
    
    
