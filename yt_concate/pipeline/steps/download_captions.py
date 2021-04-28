# 匯入內建套件
import os
import time
# 匯入第三方套件
from pytube import YouTube
# 匯入自製套件
from yt_concate.pipeline.steps.step import Step
from yt_concate.pipeline.steps.step import StepException


# 繼承Step class
class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for url in data:
            print('Downloading caption for ', url, '\n')
            if utils.caption_file_exists(url):  # 若檔案存在且大於0為真,跳過本次執行
                print('Found existing caption file: ', url)
                continue

            print(url)
            try:
                source = YouTube(url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (KeyError, TypeError):
                print('Error when downloading caption for ', url)
                continue
            text_file = open(utils.get_caption_filepath(url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()


        end = time.time()
        print('Took ', end - start, ' seconds.\n')

        return data

