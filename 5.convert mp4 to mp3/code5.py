##coded by Prince!
##a script to convert mp4 to mp3 file(video-audio) using
##PYTHON

##prerequisite 
##-----------##
##pip install moviepy
##pip install ez_setup
##pip install ffmpeg

import argparse,moviepy.editor as mpy 

ap = argparse.ArgumentParser()
ap.add_argument("--path", required=True, help="Path to the video file") ##Getting video file
video_path = vars(ap.parse_args())

mpy.VideoFileClip(video_path["path"]).audio.write_audiofile(video_path["path"][:-4] + "_audio.mp3")