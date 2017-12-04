#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-m", "--mode",
                  dest="mode",
                  help="mode = warm|cool|off|dehumidify|dehumidify-|dehumidify+")
parser.add_option("-t", "--temperature",
                  dest="temperature",
                  help="16 <= temperaturemode <= 31")
parser.add_option("-w", "--wind",
                  dest="wind",
                  help="wind speed = Auto|1|2|3")
parser.add_option("-l", "--louver",
                  dest="louver",
                  help="louver angle = Auto|0|1|2|3|4|All")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()

mode        ="warm"
temperature = 18
wind        = 2
louver      = 0
mode        = options.mode
temperature = options.temperature
wind        = options.wind
louver      = options.louver

data = {}
data['postscale'] = 100
data['freq']      = 38
data['format']    = 'raw'
data['data']      = []

modes = {
    "cool"      :"10000011000",
    "dehumidify":"10000001000",
    "warm"      :"10000010000",
    "off"       :"00000010000",
}
modes2 = {
    "cool"       :"000001101100",
    "dehumidify+":"000000001100",
    "dehumidify-":"000000101100",
    "dehumidify" :"000001001100",
    "warm"       :"000000001100",
    "off"        :"000000001100",
}
winds = {
    "Auto": 0,
    "1"   : 1,
    "2"   : 2,
    "3"   : 3,
}
louvers = {
    "Auto": 0,
    "0"   : 1,
    "1"   : 2,
    "2"   : 3,
    "3"   : 4,
    "4"   : 5,
    "All" : 6,
}

header       = [120, 53, 24, 7]
data_delta   = [190, 53, 24, 7]
on_duration  = 18
off_duration = 5

data['data'] += header

#mode temp wind louver                                        ヘッダ        機能 温度       機能２ 風量角度                                                      不明 checksum
#cool   16    2      0 110001001101001101100100100000000000000000000 10000011000 0000 000001101100 010 1001 000000000000000000000000000000000001000000000000000000000 10001011
#cool   17    2      0 110001001101001101100100100000000000000000000 10000011000 1000 000001101100 010 1001 000000000000000000000000000000000001000000000000000000000 01001011
#cool   31    2      0 110001001101001101100100100000000000000000000 10000011000 1111 000001101100 010 1001 000000000000000000000000000000000001000000000000000000000 00000111
#除湿強       2      0 110001001101001101100100100000000000000000000 10000001000 0001 000000001100 010 1001 000000000000000000000000000000000001000000000000000000000 11010011
#除湿弱       2      0 110001001101001101100100100000000000000000000 10000001000 0001 000000101100 010 1001 000000000000000000000000000000000001000000000000000000000 11110011
#除湿         2      0 110001001101001101100100100000000000000000000 10000001000 0001 000001001100 010 1001 000000000000000000000000000000000001000000000000000000000 10110011
#off                   110001001101001101100100100000000000000000000 00000010000 1110 000000001100 010 0001 000000000000000000000000000000000001000000000000000000000 01011001
#warm   16    2      0 110001001101001101100100100000000000000000000 10000010000 0000 000000001100 010 1001 000000000000000000000000000000000001000000000000000000000 11011101
#warm   17    2      0 110001001101001101100100100000000000000000000 10000010000 1000 000000001100 010 1001 000000000000000000000000000000000001000000000000000000000 00111101
#warm   23 Auto   Auto 110001001101001101100100100000000000000000000 10000010000 1110 000000001100 000 0001 000000000000000000000000000000000001000000000000000000000 00011101
#warm   23    1   Auto 110001001101001101100100100000000000000000000 10000010000 1110 000000001100 100 0001 000000000000000000000000000000000001000000000000000000000 10011101
#warm   23    2   Auto 110001001101001101100100100000000000000000000 10000010000 1110 000000001100 010 0001 000000000000000000000000000000000001000000000000000000000 01011101
#warm   23    3   Auto 110001001101001101100100100000000000000000000 10000010000 1110 000000001100 110 0001 000000000000000000000000000000000001000000000000000000000 11011101
#warm   23    2   Auto 110001001101001101100100100000000000000000000 10000010000 1110 000000001100 010 0001 000000000000000000000000000000000001000000000000000000000 01011101
#warm   23    2      0 110001001101001101100100100000000000000000000 00000010000 1110 000000001100 010 1001 000000000000000000000000000000000001000000000000000000000 01000101
#warm   23    2      1 110001001101001101100100100000000000000000000 10000010000 1110 000000001100 010 0101 000000000000000000000000000000000001000000000000000000000 01010011
#warm   23    2      2 110001001101001101100100100000000000000000000 10000010000 1110 000000001100 010 1101 000000000000000000000000000000000001000000000000000000000 01001011
#warm   23    2      3 110001001101001101100100100000000000000000000 00000010000 1110 000000001100 010 0011 000000000000000000000000000000000001000000000000000000000 01011101
#warm   23    2      4 110001001101001101100100100000000000000000000 10000010000 1110 000000001100 010 1011 000000000000000000000000000000000001000000000000000000000 01000111
#warm   23    2    All 110001001101001101100100100000000000000000000 10000010000 1110 000000001100 010 1111 000000000000000000000000000000000001000000000000000000000 01001111
#warm   31    2      0 110001001101001101100100100000000000000000000 10000010000 1111 000000001100 010 1001 000000000000000000000000000000000001000000000000000000000 01010011 

command_header      = "110001001101001101100100100000000000000000000"
command_mode        = modes[mode]
command_temperature = format(int(temperature) - 16, '04b')[::-1]
command_mode2       = modes2[mode]
command_wind        = format(winds[wind],      '03b')[::-1]
command_louver      = format(louvers[louver],  '03b')[::-1] + "1"
command_footer      = "000000000000000000000000000000000001000000000000000000000"
#
bin_command =  command_header + command_mode + command_temperature + command_mode2 + command_wind + command_louver + command_footer
#
sum = 0
while len(bin_command) > 0:
    b = bin_command[:8]
    i = int(b[::-1], 2)
    #print i, '(' , b , ') + ', sum  
    sum += i
    #print "\t", sum
    bin_command = bin_command[8:]
#print sum
checksum = format(sum, '0b')
checksum = checksum[::-1][:8] # 逆順にして８桁までにする
#print command_header, command_mode, command_temperature, command_mode2, command_wind, command_louver, command_footer + checksum
bin_command =  command_header + command_mode + command_temperature + command_mode2 + command_wind + command_louver + command_footer + checksum
#
sys.stderr.write(u"mode:%s , temperature:%s , wind:%s , louver:%s\n" % (mode, temperature, wind, louver))
#print len(bin_command)
sys.stderr.write(bin_command + "\n")
#print "warm17_wind2_louver0"
#print "110001001101001101100100100000000000000000000100000100001000000000001100010100100000000000000000000000000000000000100000000000000000000000111101"
#print "warm18_wind2_louver0"
#print "110001001101001101100100100000000000000000000100000100000100000000001100010100100000000000000000000000000000000000100000000000000000000010111101"
#print mode, temperature, wind, louver
sys.stderr.write("|-------------------------------------------||---------||--||----------||-||--||-------------------------------------------------------||------|\n")
sys.stderr.write("                   HEADER                        MODE          MODE2    WIND                       UNKNOWN                              checksum\n")
sys.stderr.write("                                                     TEMPERATURE          LOUVER\n")

header       = [120, 53, 24, 7]
data_delta   = [190, 53, 24, 7]
one_duration  = 18
zero_duration = 5
off_duration  = 7

data['data'] += header
for b in bin_command:
    if b == '0':
        data['data'] += [zero_duration, off_duration]
    elif b == '1':
        data['data'] += [one_duration,  off_duration]
data['data'] += data_delta
for b in bin_command:
    if b == '0':
        data['data'] += [zero_duration, off_duration]
    elif b == '1':
        data['data'] += [one_duration,  off_duration]
print json.dumps(data)
