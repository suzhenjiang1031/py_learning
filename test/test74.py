import speech_recognition as sr
import pyttsx3
import webbrowser

# 初始化语音识别器和语音引擎
r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # 语速调节

def speak(text):
    """朗读文字"""
    print(f"助手：{text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """监听麦克风输入"""
    with sr.Microphone() as source:
        print("请说话（安静点等 1 秒）...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language='zh-CN')  # 识别中文
        print("你说的是：", command)
        return command
    except sr.UnknownValueError:
        speak("我没听清楚，请再说一遍。")
        return ""
    except sr.RequestError:
        speak("语音识别服务出错了。")
        return ""

def handle_command(command):
    """处理指令"""
    if "百度" in command:
        speak("正在为你打开百度。")
        webbrowser.open("https://www.baidu.com")
    elif "播放音乐" in command:
        speak("为你播放一首BGM。")
        webbrowser.open("https://music.163.com")
    elif "退出" in command:
        speak("好的，退出语音助手。")
        return False
    else:
        speak("抱歉，我暂时不明白这条指令。你可以说：打开百度、播放音乐、退出等。")
    return True

if __name__ == '__main__':
    speak("你好，我是你的语音助手。请说出你的指令。")
    while True:
        cmd = listen()
        if cmd:
            if not handle_command(cmd):
                break
