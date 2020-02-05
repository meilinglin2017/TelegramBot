import requests 
import json
import time

# add other import statements here if nec

##############################################################
# global variables 
##############################################################

chat_id = 153754183 # fill in your chat id here
api_token = '1026444413:AAGgoFtrF4hAdQw3cWhKRKhtCPpr_bLxajU' # fill in your api token here 

base_url = 'https://api.telegram.org/bot{}/'.format(api_token)
sendMsg_url = base_url + 'sendMessage'
editMsg_url = base_url + 'editMessageText'
sendPhoto_url = base_url + 'sendPhoto'

getUpdates_url = base_url + 'getUpdates'

# add other global variables here 
def send_msg(chat_id,msg_text):
	my_url = "https://api.telegram.org/bot" + api_token + "/sendMessage"
	my_params = {"chat_id": chat_id, "text":msg_text}
	r = requests.get(my_url, params=my_params)
	if r.status_code == 200:
		return r.json()['result']['message_id']
	return r.status_code

# def retrieve_latest(chat_id):
# 	my_url = getUpdates_url 
# 	first_params = {'offeset': 0}

# 	r = requests.get(url=my_url,params=first_params)

# 	try: 
# 		previous_id = r.json()['result'][-1]['update_id']

# 	except:
# 		previous_id = 0


# 	latest_param = {'offset': previous_id + 1}
# 	print(r.json()['result'][-1]['message']['text'])
# 	return r.json()['result'][0]['message']['text']


##############################################################
# mood_tracker 
##############################################################

def mood_tracker(chat_id, interval_sec):

	# write your code here

	# get latest update id before this echobot 
	# params = {'offset': 0}
	# r = requests.get(url=getUpdates_url, params=params)
	# we use try except here, because r.json()['result'] may be an empty list
	# alternatively, you can use IF-THEN to check that list is not empty 
	my_url = getUpdates_url
	latest_update = 881346053

	my_url = getUpdates_url 
	first_params = {'offeset': 0}

	r = requests.get(url=my_url,params=first_params)

	try: 
		previous_id = r.json()['result'][-1]['update_id']

	except:
		previous_id = 0

	while True:
		latest_param = {'offset': previous_id + 1}
		msg_text = "Please rate your current mood: 1(poor) to 5(excellent)"
		send_msg(chat_id,msg_text)
		r = requests.get(url=my_url,params=latest_param)
		print(json.dumps(r.json(),indent = 2, sort_keys=True))
		sleep(30)
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
	return 

mood_tracker(chat_id, 2)