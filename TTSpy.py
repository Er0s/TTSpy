# coding=utf-8
#!/usr/bin/python
# <ErosXD@qq.com>
"""
Created by IDLE.
File:               TTSpy.py
User:               Er0s
Create Date:        2016/9/26
Create Time:        15:30
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
    def Error(slef):
        print 'Error!'
        exit()
    def TTS(self,lan,text):
        self.text = text
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
        app.lan = 'en'
        app.text = 'HHH'
        app.lan = raw_input("Language:").lower()
        if app.lan == 'zh':
            n = input("Number(1-10):")
            if n == 1:
                app.text = urllib.quote("鹅鹅鹅鹅鹅鹅鹅鹅鹅鹅鹅鹅鹅嗯~鹅鹅鹅鹅鹅鹅鹅鹅鹅鹅鹅鹅鹅嗯~鹅鹅鹅鹅鹅鹅鹅鹅鹅鹅鹅鹅鹅嗯！淦！妈的烂机车发不动~鹅鹅鹅鹅鹅鹅鹅鹅鹅鹅鹅鹅鹅嗯~鹅鹅鹅鹅鹅鹅鹅鹅鹅鹅鹅鹅鹅嗯".encode('utf-8'))
            elif n == 2:
                app.text = urllib.quote("因为，绳命，是剁么的回晃；绳命，是入刺的井猜。壤窝们，巩痛嘱咐碰优。田下冯广宰饿妹，饿妹冯广宰呲处。壤窝们，嘱咐这缩优类缩优。开心的一小，火大的一小，壤绳命，梗楤容，壤绳命，梗秤巩，壤绳命，梗回晃。".encode('utf-8'))
            elif n == 3:
                app.text = urllib.quote("哦嘿菇狗翻溢，雷啊雷啊，抬举丽抖啦！，哦u汞滴猴嘿搞羞滴许哇，虽瘾哦母还猴歇汞广东娃，蛋嗨哦u汞呗雷听！哦丢雷过漏谋嗨！雷破该，累哼噶残，累哼噶玩允！".encode('utf-8'))
            elif n == 4:
                app.text = urllib.quote("桑伯奇怎的桑伯奇，偶桑你桑你桑到舔很案底，丹哈大格尼没怒有窄你还理，偶喊你喊你哈妮哈到刑辱鞋底".encode('utf-8'))
            elif n == 5:
                app.text = "du du du du du du du du du du du du du aaaaaaaaaaaaaaaadu du du du du du du du du du du duaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.fuck you!the motor cannot be use!!!!! damn it"
            elif n == 6:
                app.text = "wo z ni ma mai ma pee"
            elif n == 7:
                app.text = "chuie ni mala ger beee de G F W, wo ciao ni daaaaaah yea"
            elif n == 8:
                app.text = "haha tai hao wan la hia hia hia hiaa"
            elif n == 9:
                app.text = "abcdefghijklmnopqrstuvwxyz"
            elif n == 10:
                app.text = "Need yo ben shir chang nan ren,Need yo ben shir kai men na。kai men na,kai men na,kai men kai men kai men na,food when pe,food when pe,bie duzei li mian boochoosheng,wo zhi dao need zai zhia."
            else:
                app.Error()
        elif app.lan == 'en':
            n = input("Number(1-5):")
            if n == 1:
                app.text = "rinmin hao sheuundee."
            elif n == 2:
                app.text = "chee put out buu tue putout pee,buu chee put out doll"
            elif n == 3:
                app.text = "more zombie, zombiebay lay pee"
            elif n == 4:
                app.text = "ne ma be ne ma be,ne shi da sha be,song bo qi a song bo qi,you mu you you mu you"
            elif n == 5:
                app.text = "nimabi nimabi niseudasabi sangbochiasangbochi yomoyoyomoyo"
            else:
                app.Error()
        elif app.lan == 'de':
            n = input("Number(1-2):")
            if n == 1:
                app.text = "choon ger choon yermern"
            elif n == 2:
                app.text = "pv zk bschk pv zk pv bschk zk pv zk bschk pv zk pv bschk zk bschk pv bschk bschk pv kkkkkkkkkk bschk bschk bschk pv zk bschk pv zk pv bschk zk pv zk bschk pv zk pv bschk zk bschk pv bschk bschk pv kkkkkkkkkk bschk bschk bschk pv zk bschk pv zk pv bschk zk pv zk bschk pv zk pv bschk zk bschk pv bschk bschk pv kkkkkkkkkk bschk bschk bschk pv zk bschk pv zk pv bschk zk pv zk bschk pv zk pv bschk zk bschk pv bschk"
            else:
                app.Error()
        elif app.lan == 'kor':
            app.text = '%EB%8B%88%EB%A7%88%EB%B9%84%20%EB%8B%88%EB%A7%88%EB%B9%84%20%EB%8B%88%EC%8A%A4%EB%8B%A4%EC%82%AC%EB%B9%84%20%EC%83%81%EB%B3%B4%EC%B9%98%EC%95%84%EC%83%81%EB%B3%B4%EC%B9%98%20%EC%9A%94%EB%AA%A8%EC%9A%94%EC%9A%94%EB%AA%A8%EC%9A%94'
        elif app.lan == 'jp':
            n = input("Number(1-5):")
            if n == 1:
                app.text = "%E3%83%8B%E3%83%9E%E3%83%93%E3%83%8B%E3%83%9E%E3%83%93%E3%83%8B%E3%83%BC%E3%82%B9%E3%81%BE%E3%81%99"
            elif n == 2:
                app.text = "%E3%81%AB%E3%81%BE%E3%81%B3%20%E3%81%AB%E3%81%BE%E3%81%B3%20%E3%81%AB%E3%81%97%E3%81%A0%E3%81%97%E3%82%83%E3%81%B3"
            elif n == 3:
                app.text = "%E3%81%AB%E3%81%BE%E3%81%B3%E3%81%82%E3%81%AB%E3%81%BE%E3%81%B3,%E3%81%95%E3%82%93%E3%81%B6%E3%81%A1%E3%81%82%E3%81%95%E3%82%93%E3%81%B6%E3%81%A1,%E3%81%95%E3%82%93%E3%81%B6%E3%81%A1%E3%81%82%E3%81%82%E3%81%82%E3%81%82%E3%81%82%E3%81%82,%E3%82%88%E3%82%80%E3%82%88%E3%82%88%E3%82%80%E3%82%88"
            elif n == 4:
                app.text = "%E3%83%91%E3%83%81%E3%83%91%E3%83%81%E3%83%91%E3%83%81%E3%83%91%E3%83%81%E3%83%91%E3%83%81%E3%83%91%E3%83%81"
            elif n == 5:
                app.text = "%D0%BD%D0%B8%20ma%20%D0%B1%D0%B8%20%D0%BD%D0%B8%20ma%20%D0%B1%D0%B8%20%D0%BD%D0%B8%20%D1%88%D0%B8%20%D0%B3e%20%D0%B4a%20%D1%88a%20%D0%B1%D0%B8%20%D1%88a%D0%BD%20%D0%B1%D1%83%20%D1%9B%D0%B8%20%D1%88a%D0%BD%20%D0%B1%D1%83%20%D1%9B%D0%B8%20j%D1%83%20m%D1%83%20j%D1%83%20j%D1%83%20m%D1%83%20j%D1%83"
            else:
                app.Error()
        elif app.lan == 'yue':
            n = input("Number(1-3):")
            if n == 1:
                app.text = urllib.quote("嗯嗯嗯嫩嗯嗯嗯讷讷恩恩嫩恩恩恩呢嫩嗯嗯嗯嫩嗯嗯嗯恩恩呢嫩嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嗯嫩嗯嗯嗯嗯呢嫩嗯嗯嗯呢嫩嫩恩额恩恩谔谔".encode('utf-8'))
            elif n == 2:
                app.text = urllib.quote("苟利国家生死以 岂能祸福趋避之".encode('uft-8'))
            elif n == 3:
                app.text = urllib.quote("你们造的这个句子啊,excited".encode('utf-8'))
            else:
                app.Error()
        app.TTS(app.lan,app.text)
    else:
        app.Error()
    #TODO
    '''
    else:
        app.lan = argv[2];app.text=argv[4]
        app.TTS(app.lan,app.text)
    '''
