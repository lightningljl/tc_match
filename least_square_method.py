# coding: utf-8
#最小二乘法
#传入的是时间(转化为排序数字，1,2,3)和下载量为数组的二维数组
def calc(dataList):
    t1,t2,t3,t4=0,0,0,0
    number = len(dataList)
    for key,value in enumerate(dataList):
        t1 = t1 + value[0]*value[0]
        t2 = t2 + value[0] 
        t3 = value[0]*value[1]
        t4 = t4 + value[1]
    a = ( (t3*number)-t2*t4 ) / ( t1*number-t2*t2 )
    b = ( t1*t4-t2*t3 )/(t1*number-t2*t2)
    return a,b