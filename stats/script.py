import os

list = {}

for fn in os.listdir('res/'):
    print("no %s" % fn)
    file = open('res/%s' % fn)
    while True:
        str = file.readline()
        if not str:
            break;
        list.update(eval( str ))
    #print(list)
print("Wczytano %i sieci " % (len(list)) )

banned = ["FON_NETIA_FREE_INTERNET", "Orange_FunSpot", "FreeCityInternet", "MiejskiInternet" ]

filtered_list = [ a for a in list.values() if a[0] not in banned ]

#sprint("Wczytano %i sieci " % (len(filtered_list)))

print("%i out of %i supports WPA2" % (len([ a[1] for a in list.values() if 'WPA2' in (a[1]) ]), len(list)))
print("%i out of %i supports WEP" % (len([ a[1] for a in list.values() if 'WEP' in (a[1]) ]), len(list)))
print("%i out of %i supports WPS" % (len([ a[1] for a in list.values() if 'WPS' in (a[1]) ]), len(list)))

