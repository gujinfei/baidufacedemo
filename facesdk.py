# -*- coding: utf-8 -*-
import time
import base64
import baidu as bd
import const

initialize = None
faceDetect = None
persistent = None

const.BAIDU = 1
const.RETRYNUM = 6

def initsdk(sdktype):
    result = True
    global initialize
    global faceDetect
    global persistent
    if sdktype == const.BAIDU:
        initialize = bd.initialize
        faceDetect = bd.faceDetect
        persistent = bd.persistent
    else:
        result = False
    return result


def prepare():
    if initialize is None:
        print("ERROR:initialize is None")
        return False
    else:
        ret = False;
        i = 0;
        while i < const.RETRYNUM and not ret:
            ret = initialize()
            if i > 1:
                time.sleep(i)
            i = i + 1
        return ret

def dispose_all_file(xlxsFile, txtFile, allPicFiles):
    resultList = []
    errorFileList = []
    for i in range(len(allPicFiles)):
        print("***** procee all count is %d, current is %d ******" % (len(allPicFiles), i + 1))
        file = allPicFiles[i]
        # print("process file:%s" % file)
        with open(file, 'rb') as f:  # 以二进制读取图片
            data = f.read()
            encodestr = base64.b64encode(data)  # 得到 byte 编码的数据
            result = faceDetect(encodestr)
            if result is None:
                count = 0
                while count < const.RETRYNUM and result is None:
                    count = count + 1
                    time.sleep(count)
                    result = faceDetect(encodestr)
            if result is None:
                print("ERROR:net error! open or read faild")
                info = file + ' ERROR:net error! open or read faild\n'
                errorFileList.append(info)
            elif result['error_code'] == 0:
                result['name'] = file
                resultList.append(result)
            else:
                info = file + " ERROR:error code is " + str(result['error_code']) + '\n'
                errorFileList.append(info)

    persistent(xlxsFile, txtFile, resultList, errorFileList)
    return len(resultList), len(errorFileList)




