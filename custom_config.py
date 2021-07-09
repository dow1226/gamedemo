import sys
import os
import datetime
import platform

sys.path.append('..')

from utils import ReadJson, UpdateJson

LOCAL_DATA_PATH = os.path.join(os.pathe.dirname(__file__), 'data')
LOCAL_INITINFO_PATH = os.path.join(LOCAL_DATA_PATH, 'init_info.json')
LOCAL_USERINFO_PATH = os.path.join(LOCAL_DATA_PATH, 'user_info.json')
LOCAL_DAILYINFO_PATH = os.path.join(LOCAL_DATA_PATH, 'daily_info.json')
LOCAL_MASTERINFO_PATH = os.path.join(LOCAL_DATA_PATH, 'master_info.json')

LOCAL_CUSTOM_DATA_PATH = os.path.join(os.path.dirname(__file__), 'custom_data')
LOCAL_QUERYINFO_DIR_PATH = os.path.join(LOCAL_CUSTOM_DATA_PATH, 'query_info')
LOCAL_PRODUCTINFO_DIR_PATH = os.path.join(LOCAL_CUSTOM_DATA_PATH, 'product_info')
LOCAL_MENUINFO_DIR_PATH = os.path.join(LOCAL_CUSTOM_DATA_PATH, 'menu_info')
LOCAL_NAMEINFO_PATH = os.path.join(LOCAL_CUSTOM_DATA_PATH, 'name.json')

ALL_LOCAL_DATA_PATH = [LOCAL_INITINFO_PATH, LOCAL_USERINFO_PATH, LOCAL_DAILYINFO_PATH, LOCAL_MASTERINFO_PATH]

ALL_LOCAL_DIR_PATH = [LOCAL_DATA_PATH, LOCAL_CUSTOM_DATA_PATH, LOCAL_QUERYINFO_DIR_PATH, LOCAL_PRODUCTINFO_DIR_PATH, LOCAL_MENUINFO_DIR_PATH]

for dirPath in ALL_LOCAL_DIR_PATH:
    if os.path.exists(dirPath) == False:
        os.makedirs(dirPath)
        print("Make dir: " + dirPath)

for path in ALL_LOCAL_DATA_PATH:
    if os.path.exists(path) == False:
        UpdateJson({}, path)
        print("Create file: " + path)