import whisper
import moviepy.editor as mp

model = whisper.load_model("base")

def video_to_text(video_path):
    clip = mp.VideoFileClip(video_path)
    clip.audio.write_audiofile("audio.wav")
    result = model.transcribe("audio.wav")
    return result["text"]
