# coding=utf-8
#!/usr/bin/python
# <ErosXD@qq.com>
"""
Created by IDLE.
File:               TTSpy.py
User:               Er0s
Create Date:        2016/9/25
Create Time:        00:30
"""
from __future__ import unicode_literals
from BGtext import BGtext
from sys import argv
import prompt
import ctypes
import urllib2
import urllib
import os

class TTSPY:

    def TTS(self,lan,text):
        self.text = urllib.quote(text)
        self.lan = lan
        self.filename ='temp.mp3'
        self.url = 'http://fanyi.baidu.com/gettts?lan='+lan+'&text='+text+'&source=web'
        urllib2.urlopen(self.url)
        urllib.urlretrieve(self.url, filename=self.filename, reporthook=None, data=None)
        ctypes.windll.winmm.mciSendStringA(b"play temp.mp3", 0, 0, 0)
        os.remove(self.filename)

BGtext()
prompt.prompt()

if __name__ == '__main__':
    app = TTSPY()
    if len(argv) ==1:
        app.lan = 'zh'
        app.text ='abcdefghijklmnopqrstuvwxyz'
        app.lan = raw_input("L:")
        if app.lan == 'en':
            app.text='HH'
            
        app.TTS(app.lan,app.text)
    else:
        app.lan = argv[2];app.text=argv[4]
        app.TTS(app.lan,app.text)
