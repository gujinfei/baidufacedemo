# -*- coding: utf-8 -*-
from datetime import datetime
import common_function as cf
import const
import facesdk as fs

const.JSON_CONF = 'conf.json'

def loadConfig():
    jsondata = cf.loadJsonConfig(const.JSON_CONF)
    if jsondata is None:
        picture_path = input("please input the picture path:")
        xlsx_file = input("please input the result xlsx file name:")
        error_txt = input("please input the error txt file name:")
        alg_type = int(input("please input the algorithm type[1:BAIDU]:"))
    else:
        picture_path = jsondata['picture_path']
        xlsx_file = jsondata['xlsx_file']
        error_txt = jsondata['error_txt']
        alg_type = jsondata['alg_type']

    return picture_path, xlsx_file, error_txt, alg_type

def saveConfig(picture_path, xlsx_file, error_txt, alg_type):
    dict_data = {}
    dict_data['picture_path'] = picture_path
    dict_data['xlsx_file'] = xlsx_file
    dict_data['error_txt'] = error_txt
    dict_data['alg_type'] = alg_type

    cf.saveJsonConfig(const.JSON_CONF, dict_data)

if __name__ == '__main__':
    start_time = datetime.now()

    picture_path, xlsx_file, error_txt, alg_type = loadConfig()
    if not fs.initsdk(alg_type):
        print("ERROR:fasdk initsdk failed")
        sys.exit("Goodbye!");
    if not fs.prepare():
        print("ERROR:fasdk prepare failed")
        sys.exit("Goodbye!");

    all_pic_files = cf.trave_all_pic_file(picture_path)
    success_count, failed_count = fs.dispose_all_file(xlsx_file, error_txt, all_pic_files)

    saveConfig(picture_path, xlsx_file, error_txt, alg_type)
    end_time = datetime.now()

    print("all success!![all:%d, success:%d, failed:%d]" % (len(all_pic_files), success_count, failed_count))
    print("The program cost %d second"% (end_time-start_time).seconds)