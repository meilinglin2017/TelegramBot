import requests 
import json
import time

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

def retrieve_msg(chat_id):
	return r.json()['result'][0]['message']['text']
##############################################################
# mood_tracker 
##############################################################

def mood_tracker(chat_id, interval_sec):

	# write your code here
	while True:
		number = retrieve_msg(chat_id) 
		if number in range (,)

	# Time Tracker? To check every interval, while statement
	# If-else statement defining enter number range and the message that you want to send
	# send_msg parameter need to be used
	# Handle exceptions where the user keyed in something else
	# Of if user keyed in three/3
	# GET AVERAGE OF THE LAST 10 Datapoints that was keyed in by the user

		sleep(3600)


	return