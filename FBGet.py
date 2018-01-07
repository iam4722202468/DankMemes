import json

def getMessages():
    return

def getImages(session, headers, FBData, other_user_id):
    url = "https://www.messenger.com/api/graphqlbatch/"

    query = '{"query1":{"priority":0,"q":"Query MessengerSharedPhotosContainerRoute {message_thread(' + other_user_id + ') {id,@F4}} QueryFragment F0 : Node {id,__typename} QueryFragment F1 : MessageImage {legacy_attachment_id,image.width(500).height(500) as _image2LC0nl {uri},original_dimensions {x,y},id} QueryFragment F2 : MessageVideo {legacy_attachment_id,image.width(500).height(500) as _image2LC0nl {uri},original_dimensions {x,y},id} QueryFragment F3 : MessageSharedPhotoAndVideoConnection {edges {node {__typename,@F0,@F1,@F2},cursor},count,page_info {has_next_page,has_previous_page}} QueryFragment F4 : MessageThread {message_shared_photo_and_video.first(10) as message_shared_photo_and_video {page_info {has_next_page,has_previous_page},count,@F3},id}","query_params":{}}}'
    
    data = {"fb_dtsg":FBData['fb_dtsg'],"method":"GET","queries":query}
    
    r = session.post(url, data, headers=headers).text
    beginOfReport = r.rfind("{")
    rJSON = json.loads(r[:beginOfReport-1])
    
    count = rJSON['query1']['response'][other_user_id]['message_shared_photo_and_video']['count']
    print rJSON['query1']['response'][other_user_id]['message_shared_photo_and_video']
    
    return "MOO"
