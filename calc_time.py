import time
import phix

def calc_time():
    local_time = time.asctime(time.localtime(time.time()))
    print(local_time)
    phix.speak(local_time)