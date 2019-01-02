import time
import Car
import math
#停车信息类
class Record:
    #time1为进入停车场，time2为到达车位，time3为离开车位，time4为到达出口
    def __init__(self,time1=0,time2=0,time3=0,time4=0):
        self.time1 = time1
        self.time2 = time2
        self.time3 = time3
        self.time4 = time4
    #获取停车时间
    def gettime(self):
                
        return  math.ceil(float((self.time4 - self.time1) / 3600))
        
        
        
        

        