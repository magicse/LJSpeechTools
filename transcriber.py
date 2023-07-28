# -*- coding: utf-8 -*-
import glob
import os

import speech_recognition as sr
from os import path, rename

def transcribe ():
    r = sr.Recognizer()

    # get a list of audio files from the juice/wavs directory
    #wav_files = glob.glob('./wavs/*.wav')
    wav_files = glob.glob('./wavs_split_final/*.wav')

    # Sort the files based on their names
    wav_files = sorted(wav_files)

    metadata = []

    # for each wav file
    for fpath in wav_files:
        with sr.AudioFile(fpath) as source:
            print()
            audio = r.record(source)  # read the entire audio file
            transcription = ''
            try:
                transcription = r.recognize_google(audio, language='ru')
                #transcription = transcription.replace('\r', '').replace('\r\n', '')
                file_name = os.path.splitext(os.path.basename(fpath))[0]  # Get the file name without extension
                metadata_entry = os.path.join(os.path.dirname(fpath), f"{file_name}|{transcription}")
                #print(fpath + "|" + transcription)
                print(f"{file_name}|{transcription}")
                #metadata.append(fpath + "|" + transcription)
                #metadata.append(f"{file_name}|{transcription}")
                #metadata.append(metadata_entry.strip())
                metadata.append(metadata_entry)
            except:
                print('Skipping ' + fpath)
                #metadata.append(fpath + "|" + "<ERROR>")
                #new_fpath = './ignore/' + path.basename(fpath)
                
                #metadata.append(f"{os.path.basename(fpath)}|<ERROR>")
                #new_fpath = './ignore/' + os.path.basename(fpath)
                
                metadata_entry = os.path.join(os.path.dirname(fpath), f"{os.path.basename(fpath)}|<ERROR>")
                metadata.append(metadata_entry)
                new_fpath = os.path.join('./ignore', os.path.basename(fpath))
                
                # now move the file to the skipped directory
                rename(fpath, new_fpath)
                continue

    l = ['Line1', 'Line2', 'Line3']
    s_n = '\n'.join(l)
    print(metadata)
    metadata_txt = '\n'.join(metadata)
    print(s_n)

    #with open("metadata.csv", "w", encoding="utf-8", newline='') as text_file:
    with open("metadata.csv", "w", encoding="utf-8", newline='\n') as text_file:
        text_file.write(metadata_txt)


if __name__ == "__main__":
    transcribe()