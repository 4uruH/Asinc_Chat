import subprocess
import chardet


def ping(source):
    input = ['ping', source]
    png = subprocess.Popen(input, stdout=subprocess.PIPE)
    for i in png.stdout:
        result = chardet.detect(i)
        i = i.decode(result['encoding']).encode('utf-8')
        print(i.decode('utf-8'))


ping('yandex.ru')
ping('youtube.com')
