import threading

def someFunc():
    print "someFunc was called"




t1 = threading.Thread(target=someFunc)
t1.start()
t1.join()
