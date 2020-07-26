from datetime import datetime
import os
import time
time_format='%Y-%m-%d %H:%M:%S'
time_1=input(time_format)
target = datetime.strptime(time_1,time_format)
while True:
    #清屏 windows下使用'cls',mac下使用'clear'
    os.system('clear')
    now=datetime.now()
    timedelta=target-now
    days=timedelta.days
    secs=timedelta.seconds
    hours=secs//3600
    secs=secs%3600
    mins=secs//60
    secs=secs%60
    print(f'{days}天{hours}时{mins}分{secs}秒')
    time.sleep(1)

