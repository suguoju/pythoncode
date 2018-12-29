#使用面向对象的思路实现『停车收费』场景：
#1. 车主开车进入停车场，产生停车记录，
#2. 车主开车继续向前，将车停到车位上，修改前面的停车记录，
#3. 车主停车完成，
#一段时间(购物、吃饭...)之后，车主驾车准备离开停车场，
#4. 车主开车离开车位，修改停车记录，
#5. 车主开车到达出口，系统根据停车的时间生成订单，
#6. 车主缴纳停车费，
#7. 车主离开停车场。
#至此，整个停车收费的场景完成。

import time
import math



car_lst = []


class car():
    def __init__(self, platenumber, owner, contantway, time1=0, time2=0, time3=0):
        self.platenumber = platenumber
        self.owner = owner
        self.contantway = contantway
        self.time1 = time1
        self.time2 = time2
        self.time3 = time3
        
    
    def goin(self):
        self.time1 = time.time()
        car_lst.append(self)
        print("欢迎光临，您已经进入停车场")


    def park(self):
        self.time2 = time.time()
        car_lst.append(self)
        print('您已经到达车位停车成功，开始计费')

    
    def leave(self):
        self.time3 = time.time()
        car_lst.append(self)
        print('您已经驶离车位')
        
       

    def exit(self):
        a = len(car_lst)-1
        for i in range(0, a):
            if car_lst[i].platenumber == self.platenumber:
                carex = car_lst[i]
                car_lst.remove(car_lst[i])
                carex.time3 = time.time()
                tt = float((carex.time3 - carex.time2) / 3600)
                if tt < 1:
                    tt = 1
                else:
                    tt = math.ceil(tt)

                print('停车时间%f小时,停车费用%f元.' % (tt, float(tt * 5)))
            else:
                print('该汽车从未进入， 请联系管理员.')
                
                    


while True:
    cho = input(
        '''
        请选择功能：
        1.停车
        2.驶离车位
        3.出车
        4.退出系统   
        '''
    )
    if cho == '4':
        break
    elif cho == '1':

        
        pla = input('输入车牌号：')
        own = input('输入车主名：')
        cw = input('输入联系方式：')
        c = car(pla, own, cw)
        c.goin()
        #time.sleep(4)
        c.park()
    elif cho == '2':
        c.leave()
    elif cho == '3':
        if len(car_lst) == 0:
            print('车库为空， 请联系管理员.')
        else:
            pl = input('输入车牌号：')
            carr = car(pl, 0, 0)
            carr.exit()
    else:
        print('输入错误，请重新选择.')
    time.sleep(2)
    continue
