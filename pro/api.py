# import requests 
# import json
# # r=requests.get(url="http://127.0.0.1:8000/savedet/",headers={"Authorization":"token f1f2b6e26a821ba73c66198db405e7140ead05ed"})
# r=requests.post(url="http://127.0.0.1:8000/savedet/",headers={"Authorization":"token f1f2b6e26a821ba73c66198db405e7140ead05ed"},data={'temp':100,'img':'http://127.0.0.1:8000/media/pics/wifi-icon-260nw-329468402.webp'})
# print(r.json())
import base64
import json                    
import requests
from datetime import datetime
api = 'http://127.0.0.1:8000/savedet/'
image_file = './media/pics/download_dhR2xUV.png'
with open(image_file, "rb") as f:
    im_bytes = f.read()        
im_b64 = base64.b64encode(im_bytes).decode("utf8")
r=requests.post(url=api,headers={"Authorization":"token f1f2b6e26a821ba73c66198db405e7140ead05ed",'Content-type': 'application/json'},data=json.dumps({'temp':99.9,'img':im_b64}))
print(r.json())