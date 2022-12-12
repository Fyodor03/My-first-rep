import moviepy.editor

video = moviepy.editor.VideoFileClip("pirates_song.mp4")
audio = video.audio
audio.write_audiofile("the song of the pirstes.mp3")

