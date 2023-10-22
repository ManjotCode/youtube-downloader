from pytube import YouTube
video_url = input("Enter video url:")
yt = YouTube(video_url)
stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
output_path = 'Downloads'

stream.download(output_path=output_path, )

print(f"Video downloaded to: {output_path}")
