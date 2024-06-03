import yt_dlp
import os

def get_video_formats(url):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        return ydl.extract_info(url, download=False)

def extract_resolutions(info_dict):
    formats = info_dict.get('formats', [])
    resolutions = {}
    for f in formats:
        vcodec = f.get('vcodec', 'none')
        if vcodec != 'none':  # Check if the format has a video codec
            resolution = f.get('format_note', 'Unknown')
            if resolution != 'Unknown':  # Check if the resolution is known
                if resolution not in resolutions:
                    resolutions[resolution] = []
                resolutions[resolution].append(f)
    return resolutions

def select_resolution(resolutions):
    # Sort resolutions by the numeric part before 'p', in descending order
    resolution_keys = sorted(resolutions.keys(), key=lambda x: (int(x.split('p')[0]) if x.split('p')[0].isdigit() else 0), reverse=True)
    
    print("\nAvailable resolutions and codecs for selection:")
    for i, res in enumerate(resolution_keys):
        print(f"{i + 1}. {res}")
    
    try:
        selected_option = int(input("Enter the number corresponding to the resolution you wish to download (default is highest resolution): "))
        if 1 <= selected_option <= len(resolution_keys):
            return resolution_keys[selected_option - 1]
    except ValueError:
        # Default to the highest resolution if input is invalid
        pass
    
    return resolution_keys[0]

def select_codec(resolutions, selected_resolution):
    # Sort codecs by the highest bitrate available for each codec, in descending order
    available_codecs = sorted(set(f['vcodec'] for f in resolutions[selected_resolution]), key=lambda c: max(f['tbr'] for f in resolutions[selected_resolution] if f['vcodec'] == c), reverse=True)
    
    print("\nAvailable codecs for the selected resolution:")
    for i, codec in enumerate(available_codecs):
        bitrates = [f['tbr'] for f in resolutions[selected_resolution] if f['vcodec'] == codec]
        max_bitrate = max(bitrates) if bitrates else 0
        print(f"{i + 1}. {codec} (Max Bitrate: {max_bitrate} Kbps)")
    
    try:
        selected_codec_option = int(input("Enter the number corresponding to the codec you wish to download (default is highest bitrate): "))
        if 1 <= selected_codec_option <= len(available_codecs):
            return available_codecs[selected_codec_option - 1]
    except ValueError:
        # Default to the highest bitrate codec if input is invalid
        pass
    
    return available_codecs[0]

def download_video(url, video_format_code):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ydl_opts = {
        'format': f"{video_format_code}+bestaudio/best",
        'outtmpl': os.path.join(script_dir, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    url = input("Enter the YouTube video URL: ")
    info_dict = get_video_formats(url)
    resolutions = extract_resolutions(info_dict)
    
    if not resolutions:
        print("No video resolutions found.")
        return
    
    selected_resolution = select_resolution(resolutions)
    selected_codec = select_codec(resolutions, selected_resolution)
    
    selected_codec_formats = [f for f in resolutions[selected_resolution] if selected_codec in f.get('vcodec', '')]
    if selected_codec_formats:
        selected_video_format = max(selected_codec_formats, key=lambda x: x.get('tbr', 0))['format_id']
    else:
        print(f"No format available for the selected resolution with codec {selected_codec}.")
        return

    download_video(url, selected_video_format)

if __name__ == "__main__":
    main()
