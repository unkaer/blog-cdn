# -*- coding: utf-8 -*-
import sys

reload(sys)

sys.setdefaultencoding('utf-8')
# 录音
import speech_recognition as sr

def rec(rate=16000):
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        print("please say something")
        audio = r.listen(source)

    with open("recording.wav", "wb") as f:
        f.write(audio.get_wav_data())

# 百度API
from aip import AipSpeech

APP_ID = '17894422'
API_KEY = 'fOsiZBGNvcHEBZHQfNbn51zS'
SECRET_KEY = '2PyRdp4GzorbtZycONGk6ISoGCgyUe8i'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 百度语音识别
def listen():
    with open('recording.wav', 'rb') as f:
        audio_data = f.read()

    result = client.asr(audio_data, 'wav', 16000, {
        'dev_pid': 1837,
    })

    result_text = result["result"][0]

    print("you said: " + result_text)

    return result_text

# 百度语音合成
def speak(text=""):
    result = client.synthesis(text, 'zh', 1, {
        'spd': 4,
        'vol': 5,
        'per': 4,
    })

    if not isinstance(result, dict):
        with open('audio.mp3', 'wb') as f:
            f.write(result)

# 播放音频
import pyaudio
import wave
import os
import time
def play():
    os.system('sox audio.mp3 audio.wav')
    wf = wave.open('audio.wav', 'rb')
    p = pyaudio.PyAudio()

    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    stream.start_stream()

    while stream.is_active():
        time.sleep(0.1)

    stream.stop_stream()
    stream.close()
    wf.close()

    p.terminate()

# 写入到文件233.txt
def xier():
    filename = '233.txt'
    with open(filename,'a') as f: #'a'表示append,即在原来文件内容后继续写数据
        f.write(request)
        f.write("\n")

# 退出循环
import re
def guanbi(text=""):
    pandu1 = "退"
    pandu3 = 1
    print text
    print pandu1
    pandu5 = re.search(pandu1, text)
    print pandu5
    if pandu5:
        print pandu5.group()
        pandu3 = 0
        print "即将退出"
    pandu2 = pandu3
    return pandu2

# 循环调用
pandu = 1
while (pandu == 1):
    rec()
    request = listen()
    speak(request)
    play()
    xier()
    pandu=guanbi(request)
    print pandu

