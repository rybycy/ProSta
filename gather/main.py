__author__ = 'Michal Robaszynski'

from android import Android
from time import gmtime, strftime
import sys
import os

droid = Android()

results = {}

droid.wifiDisconnect()
print('starting')
directory = '/%s/wireless_auditor' % sys.path[0]
date = strftime("%m_%d_%H_%M_%S", gmtime())
if not os.path.exists(directory):
    os.makedirs(directory)
    
while True:
    scan_success = droid.wifiStartScan()
    if scan_success:
        scan_results = droid.wifiGetScanResults()
        for ap in scan_results[1]:
            results.setdefault(ap['bssid'], (ap['ssid'], ap['capabilities']))
        print('writing %i aps' % len(results))
        file = open("%s/res_%s.txt" % (directory, date), 'w')
        file.write(str(results))
        file.close()
    eventResult = droid.eventWait(10000).result
