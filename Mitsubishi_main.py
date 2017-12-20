#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
from optparse import OptionParser
from Mitsubishi import MSZ_GV2216

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
parser.add_option("-i", "--item",
                  dest="item_name",
                  help="item_name = MSZ_GV2216")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()

# mode        = options.mode
# temperature = options.temperature
# wind        = options.wind
# louver      = options.louver

if options.item_name == "MSZ_GV2216":
    msz_gv2216 = MSZ_GV2216()
    print msz_gv2216.get_ir_data(mode = options.mode,temperature = options.temperature,wind = options.wind,louver = options.louver ) 

