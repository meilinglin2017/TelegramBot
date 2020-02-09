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

# fill in your api token here 
api_token = '1026444413:AAGgoFtrF4hAdQw3cWhKRKhtCPpr_bLxajU' 

base_url = 'https://api.telegram.org/bot{}/'.format(api_token)
sendMsg_url = base_url + 'sendMessage'
sendPhoto_url = base_url + 'sendPhoto'

getUpdates_url = base_url + 'getUpdates'

# FYI this api may return quotes that contains sensitive language (SORRY!!)
quotes_url = 'https://api.kanye.rest/'

cat_url = 'https://aws.random.cat/meow?ref=apilist.fun'

# add other global variables here 
# Trigger to send message
def send_msg(chat_id,msg_text):
	my_params = {"chat_id": chat_id, "text":msg_text, 'parse_mode':'Markdown'}
	r = requests.get(url=sendMsg_url, params=my_params)
	if r.status_code == 200:
		return r.json()['result']['message_id']
	return r.status_code

def get_latest_offset():
	r = requests.get(url=getUpdates_url)
	try:
		offset = r.json()['result'][-1]['update_id']
	except:
		offset = 0
	return offset

# Obtain the text of offset that was given
def get_latest_text(offset):
	my_params = {"offset": offset}
	r = requests.get(url=getUpdates_url,params=my_params)
	text = r.json()['result'][0]['message']['text']
	# print(text)
	return text 

# Check if the input is a float/number then if it is a string ask user to enter a number
def process_input(input):
	try: 
		number = float(input)
		if number > 5 or number < 0:
			output = 'Please key in a *NUMBER* from *1* to *5*'
			verification = 0
		else:
			if 0 <= number < 3:
				output = '_Oh dear_, *hope you are feeling better soon!* Here is a cat pic to brighten up yurrr day!'
			elif 3 <= number < 4:
				output = '_Meowwww_ *WOW NUBBAD!* Here is a cat pic to brighten up yurrr day further!'
			else:	
				output = '_RAWRRRRR_! *Keep it up!* Here is a cat pic to make your day brighter than yurrr future!'
			verification = 1
	except:
		output = 'Please key in a *NUMBER* from *1* to *5*'
		verification = 0
	return [output,verification]

def avg_datapoints(num_list):
	if len(num_list) > 10:
		num_list.pop(0)
	# print(num_list)
	len_list = len(num_list)
	average = round(sum(num_list)/len(num_list),2)
	return [str(len_list),str(average)]

def retreive_quote():
	r = requests.get(url=quotes_url)
	text = 'As the famous *Kanye West* says \n(*WARNING*: THERE MAYBE SOME PROFANITIES):\n_' + r.json()['quote'] + '_'
	return text

def retrieve_imgurl():
	r = requests.get(url=cat_url)
	img_url = r.json()['file']
	return img_url

def send_image(chat_id,photo_url):
	photo_url = retrieve_imgurl()
	my_params = {'chat_id': chat_id, 'photo':photo_url}
	r = requests.get(url=sendPhoto_url,params=my_params)
	# print(json.dumps(r.json(),indent=2,sort_keys=True))
	if r.status_code == 200:
		return r.json()['result']['message_id']
	return r.status_code

##############################################################
# mood_tracker 
##############################################################

def mood_tracker(chat_id, interval_sec):
	# write your code here

	current_time = datetime.now()
	msg_text = "Please rate your current mood: 1(poor) to 5(excellent)"
	future_time = current_time + timedelta(seconds=interval_sec)
	halftime_mark = future_time - timedelta(seconds=interval_sec/2)
	current_offset = get_latest_offset()
	num_list = []
	count_response = 0
	reminder = 0
	send_msg(chat_id,msg_text)
	

	while True:
		try:
			if datetime.now() >= future_time:
				send_msg(chat_id,msg_text)
				future_time = datetime.now() + timedelta(seconds=interval_sec)
				halftime_mark = future_time - timedelta(seconds=interval_sec/2)
				count_response = 0
				reminder = 0

			if datetime.now() >= halftime_mark and reminder == 0 and count_response == 0:
				output_response = "Please remember to send in your mood by _" + str(future_time)[:19] + "_ !"
				send_msg(chat_id,output_response)
				reminder += 1

			if current_offset < get_latest_offset(): 
				current_offset = get_latest_offset()
				user_response = get_latest_text(current_offset)
				output_response = process_input(user_response)

				if count_response >= 1:
					output_response = "You have already sent in your mood, please try again at _" + str(future_time)[:19] + "_"
					send_msg(chat_id,output_response)

				elif count_response == 0:
					if output_response[1] == 1:
						count_response += 1
						num_list.append(float(user_response))
						output_datapoints = " Your avg mood for the last *" + avg_datapoints(num_list)[0] + "* data points is _" + avg_datapoints(num_list)[1] + "_"
						send_msg(chat_id,output_response[0])
						send_image(chat_id,retrieve_imgurl())
						send_msg(chat_id,retreive_quote())
						send_msg(chat_id,output_datapoints)
					else:
						send_msg(chat_id,output_response[0])

		except KeyboardInterrupt:
			output_response = "Thank you for using YORBOOTIFUL! Have a great day ahead!"
			print(output_response)
			send_msg(chat_id,output_response)
			exit()
	return 

mood_tracker(chat_id,30)