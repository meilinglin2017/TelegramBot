import requests 
import json
import time
from datetime import datetime,timedelta

# add other import statements here if nec

##############################################################
# global variables 
##############################################################
# Change your chat id here
chat_id = 385623042 
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

def avg_datapoints(num_list):
	if len(num_list) > 10:
		num_list.pop(0)
	print(num_list)
	len_list = len(num_list)
	average = sum(num_list)/len(num_list)
	return [len_list,average]

##############################################################
# mood_tracker 
##############################################################

def mood_tracker(chat_id, interval_sec):

	# write your code here
	my_url = getUpdates_url

	first_params = {'offset': 0}
	r = requests.get(url=my_url,params=first_params)
	try: 
		offset = r.json()['result'][-1]['update_id']
	except:
		offset = 0

	while True:
		current_time = datetime.now()
		msg_text = "Please rate your current mood: 1(poor) to 5(excellent)"
		send_msg(chat_id,msg_text)
		future_time = datetime.now() + timedelta(minutes=1)
		if current_time == future_time:
			send_msg(chat_id,msg_text)
		get_latest_text(offset)
		next_param = {'offset': offset + 1}



	print(r.json())


	return 
