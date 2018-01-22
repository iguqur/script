import os
import codecs

def utf8SigToUtf8(dirPath):
    '''½«UTF8-ÎÞBOMÌí¼ÓBOM'''
    list = os.listdir(dirPath)
    for i in range(0, len(list)):
        path = os.path.join(dirPath, list[i])
        if os.path.isfile(path):
            if path.endswith(".cpp") or path.endswith(".h") or path.endswith(".hpp"):
                # print(path)

                BOM = b'\xef\xbb\xbf'

                f = open(path, 'rb')
                fbody = f.read()
                f.close()
                if not fbody.startswith(BOM):
                    f = open(path, 'wb')
                    f.write(BOM)
                    f.write(fbody)
                    f.close()

        elif os.path.isdir(path):
            utf8SigToUtf8(path)

if __name__ == '__main__':
    utf8SigToUtf8("I:\some")