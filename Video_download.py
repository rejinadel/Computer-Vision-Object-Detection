import yt_dlp

video_url = 'https://www.youtube.com/watch?v=qQAvbbv78-c'

options = {
'format': 'bestvideo', # Download the best video and audio quality
'outtmpl': r'C:\Users\prashant\Desktop\CV project\Downloaded_video\Downloaded_video.%(ext)s',
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([video_url])
    print("Download complete!")