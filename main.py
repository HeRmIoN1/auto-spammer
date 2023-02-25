from http.client import HTTPSConnection 
from sys import stderr 
from json import dumps 
from time import sleep 
import colorama
from colorama import Fore
import json
import fade
banner = """
                           ██████╗ ██████╗ ██╗██╗   ██╗ █████╗ ████████╗███████╗
                           ██╔══██╗██╔══██╗██║██║   ██║██╔══██╗╚══██╔══╝██╔════╝
                           ██████╔╝██████╔╝██║██║   ██║███████║   ██║   █████╗  
                           ██╔═══╝ ██╔══██╗██║╚██╗ ██╔╝██╔══██║   ██║   ██╔══╝  
                           ██║     ██║  ██║██║ ╚████╔╝ ██║  ██║   ██║   ███████╗
                           ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝  ╚═╝   ╚═╝   ╚══════╝
                                     by hermione                                                                                 
  loading... 
    """
faded_banner = fade.purpleblue(banner)
print(faded_banner)
with open('./config.json') as f:
  data = json.load(f)
  for k in data['Config']:
        print('Loading...')
channelid = k['channelid'] #can be customized
token = k['token'] #can be customized
message = k['message'] #can be customized
header_data = { 
	      "content-type": "application/json", 
	      "user-agent": "discordapp.com", 
	      "authorization": token
} 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def send_message(conn, channel_id, message_data): 
    try: 
      #v9 is the best version for selbbot
        conn.request("POST", f"/api/v9/channels/{channel_id}/messages", message_data, header_data) 
        resp = conn.getresponse() 
         
        if 199 < resp.status < 300: 
            print(f'{Fore.MAGENTA}Message has been sented {Fore.RESET}') 
            pass 
 
        else: 
          #
            print(f'{Fore.RED} rate limit || \n {Fore.RESET} ') 
            sleep(0.429) #rate imit 
            pass 
    except: 
        stderr.write("Error\n") 
 
def main(): 
	message_data = { 
		"content": message, 
		"tts": "false" #you can turn on tts for fun :)
	} 
 
	send_message(get_connection(), channelid, dumps(message_data)) 
 
if __name__ == '__main__': 
	while True:    
		main()
		sleep(0.4) # 10 = 10 Secconds ,note that going under 1 sec, you will be rate limited
      #also you can set the timer to 3600 , it will be used to be an a auto message sender
