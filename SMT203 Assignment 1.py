import requests 
import json

# add other import statements here if nec

##############################################################
# global variables 
##############################################################

chat_id = 385623042 # fill in your chat id here
api_token = '1026444413:AAGgoFtrF4hAdQw3cWhKRKhtCPpr_bLxajU' # fill in your api token here 

# add other global variables here 
def send_msg(chat_id,msg_text):
	my_url = "https://api.telegram.org/bot" + api_token + "/sendMessage"
	my_params = {"chat_id": chat_id, "text":msg_text}
	r = requests.get(my_url, params=my_params)
	if r.status_code == 200:
		return r.json()['result']['message_id']
	return r.status_code
	
##############################################################
# mood_tracker 
##############################################################

def mood_tracker(chat_id, interval_sec):

	# write your code here
	# Time Tracker? To check every interval, while statement
	# If-else statement defining enter number range and the message that you want to send
	# send_msg parameter need to be used


	return