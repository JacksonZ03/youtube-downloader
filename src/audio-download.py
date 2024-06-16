import yt_dlp
import os
import uuid

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Assumes that this file is in <project_dir>/src
download_dir = os.path.join(project_dir, 'download')
os.makedirs(download_dir, exist_ok=True)  # Create the download directory if it doesn't exist

def download_best_audio(url):
    unique_id = str(uuid.uuid4())[:8]  # Generate a short UUID (first 8 characters)
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_dir, '%(title)s_' + unique_id + '.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',  # '0' indicates best quality
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    url = input("Enter the YouTube video URL: ").strip()
    if not url:
        print("Error: No URL entered.")
        return

    try:
        download_best_audio(url)
    except yt_dlp.utils.DownloadError as e:
        print(f"Error downloading audio: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()