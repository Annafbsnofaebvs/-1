'''停车计费系统：
进入停车场记录进入时间，如果出去则记录出去时间，停车时间是： 出去-进入时间
停车场的数据结构是：
[{'车牌'：[进入时间，0]}，{‘车牌’：[进入时间，出去时间]}，...]
15分钟 1块
1个小时4块
停车场变量 --->全局变量
'''

import random

#没有车辆
car_park = []

def enter():
    print('欢迎进入xxxx停车场')
    number = input('输入车牌号码：')
    # 构建结构{'车牌'：[0,5]}
    car = {}
    car[number] = [0]
    #添加到car_park
    car_park.append(car)
    print('{}已进场'.format(number))


def go_out():
    number = input('输入车牌号码：')
    #判断汽车是否进场
    for car in car_park:
        if number in car:
            #记录结束时间
            time = random.randint(0, 24)
            time_record = car.get(number)
            time_record.append(time)
            #计算花费
            total = time * 4
            print('{}停车{}小时，应缴费：{}'.format(number,time,total))
            break
    else:
        print('此车未进场！')

#进场
enter()
go_out()