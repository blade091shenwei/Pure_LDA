#encoding=utf-8
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    
    '统计文件的个数'
    readFile = open('comments','r')
    readFile.readline()
    fileNumber = 0
    for line in readFile.xreadlines():
        if cmp(line,'\n') == 0:
            pass
        else:
            fileNumber = fileNumber + 1
    readFile.close()
    
    '写入新的文件个数和文件'
    writeFile = open('newComments', 'a')
    writeFile.write(str(fileNumber) + '\n')
    readFile = open('comments','r')
    readFile.readline()
    for line in readFile.xreadlines():
        if cmp(line,'\n') == 0:
            pass
        else:
            writeFile.write(line)
    
    readFile.close()
    writeFile.close()
    