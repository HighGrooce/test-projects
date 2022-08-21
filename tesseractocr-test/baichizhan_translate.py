import pyautogui
import tesserocr
from PIL import Image
import PIL.ImageOps
from PIL import ImageFilter
import requests
import json
import os
import keyboard
import sys
import time
# screenWidth, screenHeight = pyautogui.size()
# pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
# pyautogui.moveTo(20,650)
# pyautogui.moveTo(18,650)
# img_path = r'D:\baichi\env.png'
# im = pyautogui.screenshot(region=(80, 255, 220 ,50))
# im.save(img_path)
# x,y = pyautogui.position()
# print(x,y)
# a = pyautogui.locateOnScreen(r'D:\baichi\one.png',grayscale=True)
# print(a)
# im.convert('L')

def img_change(img):
    img = img.convert('L')
    pixdata = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if pixdata[x, y] == 109 or pixdata[x, y] == 115 or pixdata[x, y] == 112:
                pixdata[x, y] = 0
    img = img.filter(ImageFilter.SMOOTH)
    img = PIL.ImageOps.invert(img)
    return img


URL = "https://fanyi.baidu.com/sug"
i =0
os.chdir('D:\\baichi\\data_pic')
while True:
    #confirm_result = pyautogui.confirm("开始翻译")
    i = i + 1
    print("press Space to translate\n")
    keyboard.wait("Space")
    os.system("cls")
    im = pyautogui.screenshot(region=(49,268,270,70))
    im = im.convert('L')
    im = img_change(im)
    img_name = str(i) + '.png'
    img_path = 'D:\\baichi\\data_pic\\' + img_name
    im.save(img_path,dpi=(500.0,500.0))
    text = tesserocr.image_to_text(Image.open(img_path),lang='eng')
    text = text.split('\n')[0]
    DATA = {'kw': text}
    response = requests.post(URL, data=DATA).content.decode("utf-8")
    myjson = json.loads(response)
    #print(myjson)
    try:
        print(myjson['data'][0]['k'])
        print(myjson['data'][0]['v'])
    except IndexError as e:
        print(e)
    except KeyError as a:
        print(a)
    try:
        print(myjson['data'][1]['v'])
        print(myjson['data'][2]['v'])
    except IndexError as e:
        print(e)
    except KeyError as a:
        print(a)
    if(text != ""):
        text_name = text + '.png'
        os.rename(img_name,text_name)
    #     os.remove(text_name)
    # else:
    #     os.remove(img_name)
    # log_record = str(i) + '  ' + text
    # log_file = open('D:\\baichi\\translate_log.txt','w',encoding='utf-8')
    # log_file.write(log_record)
    # log_file.close()

# import pyautogui
# x,y = pyautogui.position()
# print(x,y)
# # 左上 59 268
# # 右上 319 268
# # 左下 59 348
# # 右下 319 348
# # 59,268,260,80

