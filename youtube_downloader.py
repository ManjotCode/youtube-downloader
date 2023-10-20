from pytube import YouTube

def on_progress(stream, chunk, remaining_bytes):
    total_size = stream.filesize
    bytes_downloaded = total_size - remaining_bytes
    percentage = (bytes_downloaded / total_size) * 100
    print(f"Downloaded: {bytes_downloaded} bytes out of {total_size} bytes ({percentage:.2f}%)")

# Define the URL of the YouTube video you want to download
video_url = input("Enter video url:")

# Create a YouTube object
yt = YouTube(video_url)

# Choose the stream with the best video and audio quality
# Here, we select the first stream, which is typically the highest quality
stream = yt.streams.filter(progressive=True, file_extension='mp4').first()

# Specify the location where you want to save the downloaded video
output_path = 'Downloads'

# Download the video with progress tracking
stream.download(output_path=output_path, )

print(f"Video downloaded to: {output_path}")
