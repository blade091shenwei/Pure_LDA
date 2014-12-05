#encoding=utf-8
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    
    readStopWord = open('stopwords', 'r')
    writeStopWord = open('newStopWords', 'a')
    readIncrement = open('manual', 'r')
    
    for line in readStopWord.xreadlines():
        stopword = line.replace('\n','').replace('\r','')
        if cmp(stopword,'') == 0:
            pass
        else:
            writeStopWord.write(stopword + '\n') 
            '将首字母改成大写写入'
            writeStopWord.write(stopword.capitalize() + '\n')
    
    for line in readIncrement.xreadlines():
        stopword = line.split()[0]
        if cmp(stopword, '--------') == 0:
            pass
        else:
            writeStopWord.write(stopword + '\n') 
    
    readIncrement.close()
    writeStopWord.close()
    readStopWord.close()