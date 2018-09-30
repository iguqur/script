import os

def collectCode(dirPath, outFilePath):
    '''将所有代码粘成一个文件，软件著作权中用到'''
    doc = open(outFilePath, "a", encoding='UTF-8')

    list = os.listdir(dirPath)
    for i in range(0, len(list)):
        path = os.path.join(dirPath, list[i])
        if os.path.isfile(path):
            if path.endswith("cpp") or path.endswith("h"):
                print(path)
                file = open(path, 'r', encoding='UTF-8')
                for eachLine in file:
                    doc.write(eachLine)
                file.close()
        elif os.path.isdir(path):
            collectCode(path, outFilePath)

if __name__ == '__main__':
    collectCode("C:\workspace\Massif\MassifClient", "I:\\a.txt")
