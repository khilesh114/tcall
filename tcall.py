import os
import sys
import json
import time

def looper():
    os.system("bash tcall.sh")
    while True: 
        filters = ("call me")  # add your massage and filter 
        filter_s = filters.split(",")
        jdata = os.popen("termux-sms-list -l 1").read() # Cheking massage in your massage android phone
        jd = json.loads(jdata)
        for j in jd:
            jd = json.loads(jdata)
            n  = (j['number']) # massage me se numder nikalale ka prosses
            m = (j['body']) # massage ka pura body 
            for f in filter_s: # yaha message ko f me stor kiya ja raha hai
                
        #
                if  f in j['body'].lower() and j['type'] == "inbox": # cheking massage filter se eq ha kee nahi
                    print(f)
                    os.system(f"termux-telephony-call  {n} ") # call your destnessin numder
                    time.sleep(5)
                    sys.exit()
                         
                else:
                    print(m)
                    print("run agane 30 seconds")
                    time.sleep(23)
                    
looper()
