import requests 
import json
import time
from datetime import datetime,timedelta

# add other import statements here if nec

##############################################################
# global variables 
##############################################################

chat_id = 385623042 # fill in your chat id here
api_token = '1026444413:AAGgoFtrF4hAdQw3cWhKRKhtCPpr_bLxajU' # fill in your api token here 

base_url = 'https://api.telegram.org/bot{}/'.format(api_token)
sendMsg_url = base_url + 'sendMessage'
editMsg_url = base_url + 'editMessageText'
sendPhoto_url = base_url + 'sendPhoto'

getUpdates_url = base_url + 'getUpdates'

# add other global variables here 
def send_msg(chat_id,msg_text):
	my_params = {"chat_id": chat_id, "text":msg_text}
	r = requests.get(sendMsg_url, params=my_params)
	if r.status_code == 200:
		return r.json()['result']['message_id']
	return r.status_code

def get_latest_text(offset):
	my_params = {"offset": offset}
	r = requests.get(url=getUpdates_url,params=my_params)
	text = r.json()['result'][0]['message']['text']
	return text 

def process_input(input):
	try: 
		number = float(input)
		if 0 <= number <= 3:
			output = 'Oh dear, hope you are feeling better soon!'
		elif 3 <= number <= 4:
			output = 'Holy shit NUBBAD!'
		else:
			output = 'YOU DA BOSS MAN DATS RITE'
	except:
		output = 'Please key in a **NUMBER** from 1 to 5'
	return output	


##############################################################
# mood_tracker 
##############################################################

def mood_tracker(chat_id, interval_sec):

	# write your code here

	my_url = getUpdates_url

	first_params = {'offset': 0}

	r = requests.get(url=my_url,params=first_params)
	try: 
		starting_id = r.json()['result'][-1]['update_id']

	except:
		starting_id = 0

	current_time = datetime.now()
	# print(current_time)
	future_time = datetime.now() + timedelta(hours=1)
	# print(future_time)
	next_param = {'offset': starting_id + 1}
	msg_text = "Please rate your current mood: 1(poor) to 5(excellent)"
	send_msg(chat_id,msg_text)
	r = requests.get(url=my_url,params=next_param)

	print(r.json())


	return 

# mood_tracker(chat_id, 2)


# get latest update id before this echobot 
# params = {'offset': 0}
# r = requests.get(url=getUpdates_url, params=params)
# we use try except here, because r.json()['result'] may be an empty list
# alternatively, you can use IF-THEN to check that list is not empty 
# latest_update = 881346053
# print(json.dumps(r.json(),indent = 2, sort_keys=True))
# text = retrieve_msg(chat_id)

# sleep(interval_sec)
# try:
# 	previous_id = r.json()['result'][-1]['update_id']
# except:
# 	previous_id = 0 
# print(r.status_code)
# print('previous_id', previous_id)

# while True:
# 	number = retrieve_msg(chat_id) 
# 	if number in range (1,6)

# # Time Tracker? To check every interval, while statement
# # If-else statement defining enter number range and the message that you want to send
# # send_msg parameter need to be used
# # Handle exceptions where the user keyed in something else
# # Of if user keyed in three/3
# # GET AVERAGE OF THE LAST 10 Datapoints that was keyed in by the user

# 	sleep(3600)