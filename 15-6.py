import threading
import time
class myThread(threading.Thread):
    def run(self):
        global x
        #lock.acquire()
        for i in range(3):
            x+=10
        time.sleep(1)
        print(x)
        #lock.release()
x=0
lock=threading.RLock()
def main():
    thrs=[]
    for itme in range(5):
        thrs.append(myThread())#list  中存的是线程
        #print(thrs)
    for item in thrs:
        item.start()
if __name__=="__main__":
    main()
