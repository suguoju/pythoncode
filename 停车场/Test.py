import time
from Car import Car
from Record import Record
from Order import Order
from Record import Record
from Park import Park
#测试类
class Test():
   
    while True:
        cho = input(
        '''
        请选择功能：
        1.停车
        2.出车
        3.退出系统   
        '''
    )
        if cho == '3':
            break
        
        if cho == '1':
            print('欢迎光临',Park.park_name,'停车场')
            time1 = time.time()
            carnumber = input('请输入车牌号')
            carowner = input('请输入车主姓名')
            carmodel = input('请输入车型')
            car = Car(carnumber,carowner,carmodel)
            record = Record()
            record.time1 = time1
            #进车时调用停车厂类的进车方法，把车的相关信息存入列表，由于不需要传订单所以用0代替
            park = Park(car,record,0)
            park.goin()


            
        if cho == '2':
            carnumber1 = input('请输入车牌号')
            b = False
            #判断列表是否存在这个车牌
            for i in range(0,len(Park.car_list)-1):
                if Park.car_list[i].car.carnum == carnumber1:
                    carwoner1 = Park.car_list[i].car.carowner
                    carmodel1 = Park.car_list[i].car.carmodel
                    #根据列表获得进车时间
                    cartime1 = Park.car_list[i].record.time1
                    #出车时间
                    time4 =time.time()
                    car2 = Car(carnumber1,carwoner1,carmodel1)
                    record1 = Record()
                    record1.time4 = time.time()
                    record1.time1 = cartime1
                    order1 = Order()
                    #调用停车场类的出车方法计算车费，然后打印出来
                    park1 = Park(car2,record1,order1)
                    a = park1.getexit(carnumber)
                    print(a)
                    #出车后移除信息
                    Park.car_list.remove(Park.car_list[i])
                    b = True
            
            if b ==  False:
                print('查无此车')
            
            
            
            
               
                
            
            



         
            
           
            


            
