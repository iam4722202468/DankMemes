from randomID import randomMessageID
from FBLogin import getFromInitialHTML
import magic

def sendMessage(session, headers, FBData, message, other_user_id, attachmentID):
    
    if other_user_id != "1526338537641003":
        messageType = "single"
    else:
        messageType = "group"
    
    url = "https://www.messenger.com/messaging/send/?dpr=1"
    
    msgID = randomMessageID()
    data = {"client":"mercury","action_type":"ma-type:user-generated-message","body":message,"ephemeral_ttl_mode":"0","has_attachment":"false","message_id":msgID,"offline_threading_id":msgID,"source":"source:messenger:web","timestamp":"1477433223060","__user":FBData['user_id'],"__a":"1","__be":"-1","__pc":"PHASED:messengerdotcom_pkg","fb_dtsg":FBData['fb_dtsg'], "other_user_fbid":other_user_id}

    if messageType == "single":
        data["specific_to_list[0]"] = "fbid:"+str(other_user_id)
        data["specific_to_list[1]"] = "fbid:"+FBData['user_id']
    else:
        data["thread_fbid"] = str(other_user_id)
        del data['other_user_fbid']
    
    if attachmentID != "":
        data['has_attachment'] = "true"
        data['image_ids[0]'] = attachmentID
        del data["body"]
    
    r = session.post(url, data, headers=headers)
    
    print r.text

def sendImage(session, headers, FBData, imageLocation, other_user_id):
    data = {"__user":FBData['user_id'], "__a":"1", "__be":"-1","__pc":"PHASED:messengerdotcom_pkg","fb_dtsg":FBData['fb_dtsg']}
    
    url = "https://upload.messenger.com/ajax/mercury/upload.php?dpr=1"
    
    mimeType = magic.Magic(mime=True).from_file(imageLocation)
    
    files = {'upload_1024': (imageLocation, open(imageLocation, 'rb'), mimeType)}
    
    r = session.post(url, data, files=files, headers=headers)
    
    file_id = getFromInitialHTML('image_id":', r.text)[:-1]
    
    sendMessage(session, headers, FBData, "", other_user_id, file_id)
