import json
import os
import requests
from flask import Flask, request,  jsonify

app = Flask(__name__)
config_file_path = "config.json"

device_states = {}

@app.route("/home/api/v1.0/status", methods=["GET"])
def getStatus():
	device_id = request.args.get('id')
	if device_id == None:
		info = json.loads(request.data)
		device_id = info["id"]
	response = {}
	response["id"] = int(device_id)
	if device_id in device_states:
		response["action"] = device_states[device_id]
	else:
		response["action"] = "light_off"
	return json.dumps(response)

@app.route("/home/api/v1.0/update", methods=["GET","POST"])
def update():
	device_id = ""
	action = ""
	if request.method == "GET":
		device_id = request.args.get('id')
		action = request.args.get('action')
	else:
		dict = json.loads(request.data)
		device_id = dict["id"]
		action = dict["action"]
	print("%s-%s" % (device_id, action))
	device_states[device_id] = action
	signal = getPilightRawSignal(int(device_id), action)
	response = {}
	if signal is not None:
		os.system("pilight-send -p raw -c '%s'" % signal)
		response["id"] = int(device_id)
		response["action"] = action
		response["success"] = 1
	else:
		response["success"] = 0
	return json.dumps(response)

def getPilightRawSignal(device_id, action):
	config_file = open(config_file_path,"r")
	config_info = config_file.read()
	config_json_info = json.loads(config_info)
	accessories = config_json_info["accessories"]
	for accessory in accessories:
		accessory_id = accessory["id"]
		if accessory_id == device_id:
			pilight_raw_signals = accessory["pilight_raw_signals"]
			for signal in pilight_raw_signals:
				signal_action = signal["action"]
				if signal_action == action:
					return signal["signal"]			
	
	return None


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
