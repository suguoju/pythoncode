#停车厂类
class Park:
    #car_list列表为存放车辆的所有心理
    car_list = []
    park_name = '智慧停车场'
    #车型1收费5元
    park_prize1 = 5
    #车型2收费10元
    park_prize2 = 10
    def __init__(self,car,record,order):
        self.car = car
        self.record = record
        self.order = order
        
        
    #车主进车的动作同时把车主的信息存入car_list集合中
    def goin(self):
        Park.car_list.append(self)
        
    #车主退车的动作，number为验证的车牌号
    def getexit(self,number):
        for i in range(0,len(Park.car_list)):
            if number == Park.car_list[i].car.carnum:
                return self.order.getmoney(self.car,self.record)
        
       
       
        

        