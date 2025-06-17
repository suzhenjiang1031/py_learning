import os
import random
import pygame
import speech_recognition as sr

# === 初始化音乐播放器 ===
MUSIC_FOLDER = "music"  # 将你的MP3放在这个目录
pygame.mixer.init()

# === 加载音乐文件 ===
def get_music_files():
    return [file for file in os.listdir(MUSIC_FOLDER) if file.endswith(".mp3")]

playlist = get_music_files()
current_index = 0

def play_music(index):
    if 0 <= index < len(playlist):
        pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, playlist[index]))
        pygame.mixer.music.play()
        print(f"🎶 正在播放: {playlist[index]}")

# === 语音识别部分 ===
def recognize_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ 请说指令：播放、暂停、下一首、退出")
        audio = r.listen(source, phrase_time_limit=5)
        try:
            command = r.recognize_google(audio, language="zh-CN")  # 中文
            print(f"🗣️ 识别结果：{command}")
            return command.lower()
        except sr.UnknownValueError:
            print("😅 没听清楚，请再试一次。")
        except sr.RequestError:
            print("❌ 无法连接识别服务。")
    return ""

# === 控制逻辑 ===
def voice_control_loop():
    global current_index
    if not playlist:
        print("⚠️ 没有找到任何 mp3 文件")
        return

    play_music(current_index)

    while True:
        command = recognize_voice()

        if "暂停" in command:
            pygame.mixer.music.pause()
            print("⏸️ 已暂停")
        elif "播放" in command:
            pygame.mixer.music.unpause()
            print("▶️ 继续播放")
        elif "下一首" in command:
            current_index = (current_index + 1) % len(playlist)
            play_music(current_index)
        elif "退出" in command or "停止" in command:
            pygame.mixer.music.stop()
            print("👋 已退出音乐播放器")
            break
        else:
            print("🤔 未识别的命令（试试：播放、暂停、下一首、退出）")

if __name__ == "__main__":
    voice_control_loop()
