import requests
import FBLogin
import FBSend
import FBGet

class FBObject:
    def __init__(self, headers):
        self.session = requests.session()
        self.headers = headers
    
    def login(self, username, password):
        self.FBData = FBLogin.initSession(self.session, self.headers, username, password)
    
    def sendMessage(self, message, other_user_id, attachmentID=""):
        FBSend.sendMessage(self.session, self.headers, self.FBData, message, other_user_id, attachmentID)
    
    def logout(self):
        data = {"fb_dtsg":self.FBData['fb_dtsg']}
        self.session.post("https://www.messenger.com/logout/", data, headers=self.headers)
    
    def getMessages(self, other_user_id, count):
        print "MOO"
        
    def getImages(self, other_user_id):
        return FBGet.getImages(self.session, self.headers, self.FBData, other_user_id)
    
    def sendImage(self, imageLocation, other_user_id):
        FBSend.sendImage(self.session, self.headers, self.FBData, imageLocation, other_user_id)
