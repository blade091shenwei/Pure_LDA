#encoding=utf-8
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

import string

if __name__=="__main__":
    
    '读入字典文件'
    dict = []
    readWordMap = open('wordmap.txt')
    readWordMap.readline()
    for line in readWordMap.xreadlines():
        word = line.split()[0]
        ID = line.split()[1]
        dict.append([word,string.atoi(ID)])
    '对字典文件按照ID进行排序'
    dict_sorted = sorted(dict, key=lambda s:s[1])
#     for word in dict_sorted:
#         print word
    dict_inUse = []
    for word in dict_sorted:
        dict_inUse.append(word[0])
#     for word in dict_inUse:
#         print word
        
#     for word in dict:
#         print word
    
    '''
        对读入phi文件的每一行topic并进行排序
        将排序后的前10个词及其对应的概率写入文件
    '''
    writeTopicWord = open('TopicWords', 'a')
    readPhi = open('model-final.phi')
    TopicCount = 0
    for topic in readPhi.xreadlines():
        ID_Probs = []
        eachWordProbs = topic.split()
        ID = 0
        for eachWordProb in eachWordProbs:
            ID_Probs.append([ID,string.atof(eachWordProb)])
            ID = ID + 1
        ID_Probs_Sorted = \
        sorted(ID_Probs, key=lambda s:s[1], reverse=True)
        '写入前20个词及其对应的概率'
        writeTopicWord.write('Topic' + str(TopicCount) + ': ')
        TopicCount = TopicCount + 1
        count = 0
        while count < 100:
            writeTopicWord.write(dict_inUse[ID_Probs_Sorted[count][0]]\
                                 + ' ' + str(ID_Probs_Sorted[count][1]) \
                                 + ' ')
            count = count + 1
        writeTopicWord.write('\n')
    writeTopicWord.close()