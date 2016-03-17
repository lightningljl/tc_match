# coding: utf-8
import csv
import time
import draw
#cvs读取
def ReadCvs(filePath, switch=0):
    number = 0
    dataSet = []
    csvfile = open(filePath, 'r')
    reader = csv.reader(csvfile)
    for line in reader:
        dataSet.append( line )
        if number > 100000 and switch == 1 : 
            break
        number = number + 1
    csvfile.close() 
    return dataSet
#将数据规整
def FormateData(artistAndMusic, musicConsume):
    dataSet = {}
    dayList = []
    #附上歌曲作者
    for music in musicConsume:
        auth = ''
        for artist in artistAndMusic:
            if music[1] == artist[0]:
                auth = artist[1]
                break
        if auth == "" :
            continue
        
        if auth not in dataSet.keys():
            dataSet[auth] = [[],[],[]]
        #1播放对应key0,2下载对应key1,3收藏对应key2
        key  = int(music[3]) - 1
        day  = time.strftime('%Y%m%d', time.localtime( int(music[2]) ) )
        day  = int(day)
        if day not in dayList :
            dayList.append(day)
        count = len( dataSet[auth][key] )
        if count == 0 :
            dataSet[auth][key].append([day, 1])
        else :
            number = 0
            calcNumber = 0
            for useData in dataSet[auth][key]:
                #如果已经存在时间，则时间对应的的值加一
                if useData[0] == day:
                    number = 1
                    dataSet[auth][key][calcNumber][1] = useData[1]+1
                    break
                calcNumber = calcNumber + 1
            #如果不存在时间，则再加数据
            #print(day)
            if number == 0 :
                dataSet[auth][key].append([day, 1])
    dayList.sort()
    return dataSet, dayList

#做图
def showLine(dataSet, dayList):
    #暂时只显示一个用户的曲线
    xList = []
    yList = []
    for (key, user) in dataSet.items():
        #只显示下载量
        x = []
        y = []
        find = 0
        number = 0
        for day in dayList:
            find = 0
            number = number + 1
            x.append(number)
            for downLoadNumber in user[0]:
                if downLoadNumber[0] == day :
                    find = 1
                    y.append(downLoadNumber[1])
            if find == 0 :
                y.append(0)
        if len(x) > 1 :
            #print(dayList)
            #print(key)
            #print(x)
            #print(y)
            xList.append(x)
            yList.append(y)
    draw.DrawImage(xList, yList)
#读取歌曲伊人
filePath = "mars_tianchi_songs.csv"
artistAndMusic = ReadCvs( filePath )
#读取歌曲消费信息
filePath = "mars_tianchi_user_actions.csv"
musicConsume = ReadCvs( filePath, 1 )
#将数据规整
formateData,dayList = FormateData(artistAndMusic, musicConsume)

#画图
showLine(formateData, dayList)


    