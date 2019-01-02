from Park import Park
import math
#订单类
class Order:
    
       
    #根据车型和停车时间计算费用
    def getmoney(self,Car,Record):
        self.Car = Car
        self.Record = Record
        if Car.carmodel == '1':
            return Record.gettime() * Park.park_prize1
        else:
            return Record.gettime() * Park.park_prize2
        


        