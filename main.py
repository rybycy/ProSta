__author__ = 'Michal Robaszynski'

from android import Android
import sys

droid = Android()

results = {}

#droid.wifiDisconnect()
print('starting')
while True:
    scan_success = droid.wifiStartScan()
    if scan_success:
        scan_results = droid.wifiGetScanResults()
        for ap in scan_results[1]:
            results.setdefault(ap['bssid'], (ap['ssid'], ap['capabilities']))
        print('writing')
        file = open('/sdcard/res.txt', 'w')
        file.write(str(results))
        file.close()
    eventResult = droid.eventWait(10000).result
