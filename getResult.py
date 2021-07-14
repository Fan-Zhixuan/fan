import json
import os


objDict = {'knife': 1, 'scissors': 2, 'sharpTools': 3, 'expandableBaton': 4, 'smallGlassBottle': 5, 'electricBaton': 6, 'plasticBeverageBottle': 7, 'plasticBottleWithaNozzle': 8, 'electronicEquipment': 9, 'battery': 10, 'seal': 11, 'umbrella': 12 }

def writeOnePic(path):
    pic = [[], [], [], [], [], [], [], [], [], [], [], []]
    dict_obj = {}
    with open(path, "r") as f:  # 打开文件
        for line in f.readlines():
            line = line.strip('\n')  # 去掉列表中每一个元素的换行符
            oneObject = line.split(' ')
            name = oneObject[0]
            confidence = float(oneObject[1])
            xmin = float(oneObject[2])
            ymin = float(oneObject[3])
            xmax = xmin + float(oneObject[4])
            ymax = ymin + float(oneObject[5])
            if name not in dict_obj.keys():  # 该类别第一次加入
                dict_obj[name] = {}

            key = len(dict_obj[name])
            dict_obj[name][key] = [xmin, ymin, xmax, ymax, confidence]

    for nameKey, obj in dict_obj.items():
        if nameKey not in objDict.keys():  # 找不到类别
            print(nameKey + ' is not find')
        else:
            index = objDict[nameKey] - 1
            for value in obj.values():
                pic[index].append(value)

    return pic

def wirtePictures(folderPath,num):
    #path = 'ppyolov2_epoch=57_txt'
    # 读取文件夹内容
    fileList = os.walk(folderPath)
    txtFileList = []
    for root, dirs, files in fileList:
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        # print(files)  # 当前路径下所有非目录子文件
        for file in files:
            if os.path.splitext(file)[1] == '.txt':
                txtFileList.append(folderPath + '/' + file)

    # 遍历文件
    result = []
    for path in txtFileList:
        pic = writeOnePic(path)
        result.append(pic)

    jsObj = json.dumps(result)
    result_path = os.path.join(folderPath,'result')+str(num)+'.json'
    fileObject = open(result_path, 'w')
    fileObject.write(jsObj)
    fileObject.close()

if __name__ == '__main__':
    path = 'infer_output/200/txt'
    wirtePictures(path,200)