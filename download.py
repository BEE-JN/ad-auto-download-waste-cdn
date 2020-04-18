# -*- coding:utf-8 -*-
# writer: GCS


import requests
import keyboard
import threading
import sys
import time


url = "https://lf3-adcdn-tos.pstatp.com/obj/ad-advertiser-package/adapk_adv_1640629539887116_ts_1586432904769.apk"
isExit = 0
num = 0


class dlThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        downloadT(self.threadID, self.name)



def downloadT(i, threadName):
    global url
    global isExit
    global num
    print("下载线程" + threadName + "启动")
    while not isExit:
        res = requests.get(url=url)
        num += 1
        with open("./download_apk_" + str(i) + ".apk", "wb") as file:
            file.write(res.content)
    return 0


def listenT():
    global isExit
    print("按q退出程序")
    keyboard.wait('q')
    print("监听结束，等待下载进程结束")
    isExit = 1
    sys.exit(0)


if __name__ == "__main__":
    t1 = dlThread(1, "download-1", 1)
    t2 = dlThread(2, "download-2", 2)
    t3 = dlThread(3, "download-3", 3)
    t4 = dlThread(4, "download-4", 4)
    t5 = threading.Thread(target=listenT)
    print("开始循环下载垃圾软件apk，路径为程序所在目录")
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    print("下载结束，共下载" + str(num) + "次，5秒后程序退出")
    time.sleep(5)
    sys.exit(0)
