import os
from pprint import pprint

from .step import Step
from yt_concate.settings import CAPTIONS_DIR


# 繼承Step抽象class的框架
class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {}  # 建立以個別字幕檔為單位的字典檔
        for caption_file in os.listdir(CAPTIONS_DIR):  # 逐清單中的檔案進行處裡
            captions = {}  # 建立字幕字典檔
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r') as f:  # 讀取字幕檔
                time_line = False  # 設定條件式,用來辨識時間軸所在的行
                time = None  # 時間變數
                caption = None  # 字幕變數
                for line in f:
                    line = line.strip()  # 處裡每行的\n字元
                    if '-->' in line:
                        time_line = True
                        time = line  # 將該時間軸存成變數time
                        continue  # 跳至下一行
                    if time_line:  # 當上一行是時間軸(True)
                        caption = line  # 將該字幕存成變數time
                        captions[caption] = time # 新增一筆caption:time pair存進captions字典變數
                        time_line = False  # 改回預設值,用以判斷下一行時間軸
            data[caption_file] = captions  # 新增一筆caption_file:captions pair存進data字典變數
        pprint(data)

        return data

