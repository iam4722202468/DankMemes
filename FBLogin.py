def getFromInitialHTML(toFind, findIn):
    start = findIn.find(toFind)
    end = findIn.find('"', start + len(toFind))
    return findIn[start + len(toFind):end]

def initSession(session, headers, username, password):
    r = session.get('https://www.messenger.com/', headers=headers)
    
    FBData = {}
    
    FBData['initial_request_id'] = getFromInitialHTML('name="initial_request_id" value="', r.text)
    FBData['identifier'] = getFromInitialHTML('"identifier":"', r.text)
    FBData['_js_datr'] = getFromInitialHTML('"_js_datr","', r.text)
    FBData['lsd'] = getFromInitialHTML('["LSD",[],{"token":"', r.text)

    cookies = {"_js_datr" : FBData['_js_datr']}
    data = {"lsd" : FBData['lsd'], "initial_request_id" : FBData['initial_request_id'], "lgnjs" : "n", "email" : username, "pass" : password, "login" : "1", "default_persistent" : "0"}

    r = session.post("https://www.messenger.com/login/password/", data, cookies=cookies, headers=headers)

    FBData['fb_dtsg'] = getFromInitialHTML('["DTSGInitialData",[],{"token":"', r.text)
    FBData['user_id'] = session.cookies.get_dict()['c_user']

    cookies = {"p":"-2"}
    r = session.get('https://www.messenger.com/', headers=headers, cookies=cookies)
    
    return FBData
