import os
from pydub import AudioSegment

def mp3_to_wav(mp3_file, output_dir):
    audio = AudioSegment.from_mp3(mp3_file)
    audio = audio.set_channels(1)  # Set to mono
    audio = audio.set_frame_rate(22050)  # Set the sample rate to 22050 Hz
    
    wav_file = os.path.join(output_dir, os.path.splitext(os.path.basename(mp3_file))[0] + ".wav")
    audio.export(wav_file, format="wav")
    return wav_file

def convert_and_remove_mp3_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".mp3"):
                mp3_file = os.path.join(root, file)
                wav_file = mp3_to_wav(mp3_file, root)
                os.remove(mp3_file)
                print(f"Converted {mp3_file} to {wav_file} and removed the original mp3.")

if __name__ == "__main__":
    input_directory = "put_audio_files_here"
    convert_and_remove_mp3_files(input_directory)