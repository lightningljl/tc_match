# coding: utf-8
import csv
import time
#cvs读取
def ReadCvs(filePath):
    number = 0
    dataSet = []
    csvfile = open(filePath, 'r')
    reader = csv.reader(csvfile)
    for line in reader:
        dataSet.append( line )
        number = number + 1
        if number%1000 == 0 :
            print(number)
    csvfile.close() 
    return dataSet

#初始化时间
def InitTime():
    dataSet = []
    began = "2015-03-01"
    end = "2015-08-30"
    start = time.mktime(time.strptime(began,'%Y-%m-%d'))
    end = time.mktime(time.strptime(end,'%Y-%m-%d'))
    for i in range(0,183):
        nowTime = time.localtime(start+i*86400)
        dayTime = time.strftime('%Y-%m-%d', nowTime)
        dataSet.append( dayTime )
    return dataSet

#将数据分包
def Package(singerList, actionList, dateList):
    

#读取歌曲伊人
filePath = "mars_tianchi_songs.csv"
artistAndMusic = ReadCvs( filePath )
#读取歌曲消费信息
filePath = "mars_tianchi_user_actions.csv"
musicConsume = ReadCvs( filePath)