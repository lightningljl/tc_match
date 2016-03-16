# coding: utf-8
import csv
import time
#cvs读取
def ReadCvs(filePath, switch=0):
    number = 0
    dataSet = []
    csvfile = open(filePath, 'r')
    reader = csv.reader(csvfile)
    for line in reader:
        dataSet.append( line )
        if number > 10000 and switch == 1 : 
            break
        number = number + 1
    csvfile.close() 
    return dataSet
#将数据规整
def FormateData(artistAndMusic, musicConsume):
    dataSet = {}
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
        day  = time.strftime('%Y-%m-%d', time.localtime( int(music[2]) ) )
        print(day)
        if len( dataSet[auth][key] ) == 0 :
            dataSet[auth][key].append([day, 1])
        else :
            number = 0
            for useData in dataSet[auth][key]:
                #如果已经存在时间，则时间对应的的值加一
                if useData[0] == day:
                    useData[1] = useData[1] + 1
                    dataSet[auth][key][number] = useData
                else :
                    dataSet[auth][key].append([day, 1])
                number = number + 1
    return dataSet

#读取歌曲伊人
filePath = "mars_tianchi_songs.csv"
artistAndMusic = ReadCvs( filePath )
#读取歌曲消费信息
filePath = "mars_tianchi_user_actions.csv"
musicConsume = ReadCvs( filePath, 1 )
#将数据规整
formateData = FormateData(artistAndMusic, musicConsume)
#print(formateData)


    