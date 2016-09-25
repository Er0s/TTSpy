import time
def  BGtext():
    option = 'TTSpy.txt'
    print file(option).read()[:]
    print time.asctime(time.localtime(time.time()))
