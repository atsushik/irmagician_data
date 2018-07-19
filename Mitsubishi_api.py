# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, make_response, request
# import peewee
# import json
from Mitsubishi import MSZ_GV2216
# import irmcli
import json
import serial

api = Flask(__name__)

ir_serial = serial.Serial("/dev/ttyACM0", 9600, timeout = 1)
#ir_serial = serial.Serial("/dev/tty.usbmodem01231", 9600, timeout = 1)
def send_with_irmagician(json_string):
	# originally from https://github.com/netbuffalo/irmcli
	data = json.loads(json_string)
	# print data
	recNumber = len(data['data'])
	rawX = data['data']

	ir_serial.write("n,%d\r\n" % recNumber)
	ir_serial.readline()

	postScale = data['postscale']
	ir_serial.write("k,%d\r\n" % postScale)
	#time.sleep(1.0)
	msg = ir_serial.readline()
	#print msg

	for n in range(recNumber):
		bank = n / 64
		pos = n % 64
		if (pos == 0):
			ir_serial.write("b,%d\r\n" % bank)

		ir_serial.write("w,%d,%d\n\r" % (pos, rawX[n]))

	ir_serial.write("p\r\n")
	msg = ir_serial.readline()
	# print msg
	

# @api.route('/msz_gv2216/<string:userId>', methods=['GET','POST'])
@api.route('/msz_gv2216', methods=['GET','POST'])
def send_ir_data_msz_gv2216():
	mode = 'warm'
	temperature = 18
	wind = 'Auto'
	louver = 'Auto'
	# print request.args
	if 'mode' in request.args.keys():
		mode = request.args['mode']
	if 'temperature' in request.args.keys():
		temperature = request.args['temperature']
	if 'wind' in request.args.keys():
		wind = request.args['wind']
	if 'louver' in request.args.keys():
		louver = request.args['louver']
	msz_gv2216 = MSZ_GV2216()
	result = msz_gv2216.get_ir_data(mode = mode,temperature = temperature,wind = wind,louver = louver )
        import datetime
        if not wind in ["Auto", "All"]:
                wind = int(wind)
        if not louver in ["Auto", "All"]:
                louver = int(louver)
        d = {"timestamp":datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"), "mode":mode, "temperature":int(temperature), "wind":wind, "louver":louver}
        write_log(d)
	# print result
	send_with_irmagician(result)

	return make_response(jsonify(result))
	# Unicodeにしたくない場合は↓
	# return make_response(json.dumps(result, ensure_ascii=False))

import json
def write_log(json_data):
	log_file = "Mitsubishi_api.log"
        with open(log_file, mode="a") as f:
                f.write(json.dumps(json_data) + "\n")

@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=8080, debug = True)
