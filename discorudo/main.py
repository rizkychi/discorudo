def hello():
    print('Hello from Discorudo!')

def hi():
    print('Hi bro! wassup!')

from http.client import HTTPSConnection 
from sys import stderr 
from json import dumps 
import json

# send message to discord channel
def send_message(channel_id, message, token): 
    conn = HTTPSConnection("discordapp.com", 443)
    header_data = { 
        "content-type": "application/json", 
        "user-agent": "discordapp.com", 
        "authorization": token
    }
    message_data = { 
		"content": message, 
		"tts": "false"
	}
    ids = ''
    try: 
        conn.request("POST", f"/api/v7/channels/{channel_id}/messages", message_data, header_data) 
        resp = conn.getresponse() 
         
        if 199 < resp.status < 300: 
            print("     - Message Sent!")
            rs = json.loads(resp.read())
            ids = rs['id']
            pass 
 
        else: 
            stderr.write(f"HTTP {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n")

    return ids

# send message from discord channel
def del_message(channel_id, message_id, token):
    conn = HTTPSConnection("discordapp.com", 443)
    header_data = { 
        "content-type": "application/json", 
        "user-agent": "discordapp.com", 
        "authorization": token
    }
	try: 
		conn.request("DELETE", f"/api/v7/channels/{channel_id}/messages/{message_id}", headers = header_data) 
		resp = conn.getresponse() 
		 
		if 199 < resp.status < 300: 
			print("     - Deleted!")
			pass 
 
		else:
			stderr.write(f"HTTP {resp.status}: {resp.reason}\n")
			pass
            
	except: 
        stderr.write("Error\n")