import json
import datetime
import numpy as np
from enum import Enum, IntEnum, unique

tw_tz = datetime.timezone(datetime.timedelta(hours=8), '台灣時間')

# Json資料更新
def UpdateJson(jsonFile, path):
    with open(path, "w", encoding='utf-8') as f:
        json.dump(jsonFile, f, ensure_ascii=False)

# Json資料讀取
def ReadJson(path):
    with open(path, "r", encoding='utf-8') as f:
        js = f.read()
        jsonFile = json.loads(js)
        return jsonFile

# 非同步更新Json資料
async def UpdateJsonAsync(jsonFile, path):
    with open(path, "w", encoding='utf-8') as f:
        json.dump(jsonFile, f, ensure_ascii=False)

def GetCurrentDateStr():
    current_date = datetime.datetime.now(tw_tz)
    return current_date.strftime('%Y_%m_%d_%H_%M_%S')

def GetCurrentDateRaw():
    current_date = datetime.datetime.now(tw_tz)
    return current_date

def Str2Datetime(inputStr):
    result = datetime.datetime.strptime(inputStr, '%Y_%m_%d_%H_%M_%S')
    result = result.replace(tzinfo=tw_tz)
    return result

def Datetime2Str(inputDatetime):
    return inputDatetime.strftime('%Y_%m_%d_%H_%M_%S')

def PairSubstring(substring, strList) -> list:
    # 子串匹配
    possibleResult = []
    for strCur in strList:
        if strCur.find(substring) != -1:
            possibleResult.append(strCur)
    return possibleResult


def PairSubstringList(substringList, strList) -> list:
    # 多子串匹配
    possResult = []
    for strCur in strList:
        isPoss = True
        for keyword in substringList:
            if strCur.find(keyword) == -1:
                isPoss = False
                break
        if isPoss:
            possResult.append(strCur)
    return possResult


def DeleteInvalidInfo(targetDict, sourceKeys):
    # 只保留键在sourceKeys中的targetDict条目
    invalidGroupId = []
    for gId in targetDict.keys():
        if not gId in sourceKeys:
            invalidGroupId.append(gId)
    for gId in invalidGroupId:
        del targetDict[gId]

