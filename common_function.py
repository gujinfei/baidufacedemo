import os
import json

def trave_all_pic_file(dirname):
    filter = [".jpg", ".png", ".jpeg", ".bmp"]  # 设置过滤后的文件类型 当然可以设置多个类型
    result = []  # 所有的文件

    for maindir, subdir, file_name_list in os.walk(dirname):
        # print("1:",maindir) #当前主目录
        # print("2:",subdir) #当前主目录下的所有目录
        # print("3:",file_name_list)  #当前主目录下的所有文件

        for filename in file_name_list:
            apath = os.path.join(maindir, filename)  # 合并成一个完整路径
            ext = os.path.splitext(apath)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容
            if ext in filter:
                result.append(apath)

    return result


def loadJsonConfig(jsonPath):
    try:
        with open(jsonPath) as f:
            data = json.load(f)
            return data
    except:
        print("WARING:file open as json failed")


def saveJsonConfig(jsonPath, dataDict):
    data = loadJsonConfig(jsonPath)
    if not data is None:
        for key in dataDict:
            data[key] = dataDict[key]
    else:
        data = dataDict

    try:
        with open(jsonPath, 'w') as json_file:
            json_file.write(json.dumps(data, indent=4))
    except:
        print("ERROR:json file write failed")

    return True

