from moviepy.editor import *
import cv2
import os
from globalvars import *

def create_one_reaction(fname):

    # Thumbnail, can customize to not be the soy image
    # Will place in webcam size and format
    base_thumb = ImageClip(THUMBNAILPATH + fname + ".jpg").set_duration(1)
    soy_thumb = ImageClip(REACTTHUMBNAILPATH).set_duration(1).resize(0.1).margin(10, color=(238, 75, 43))
    thumb = CompositeVideoClip([base_thumb,soy_thumb.set_position(("right","center"))])

    # hacky way to get jpg from mp4
    thumb.write_videofile("TMP" + fname + ".mp4", fps=24)
    vidcap = cv2.VideoCapture("TMP" + fname + ".mp4")
    _,image = vidcap.read()
    cv2.imwrite(READYTHUMBNAILSPATH + fname + ".jpg", image)
    os.remove("TMP" + fname + ".mp4")

    # Video, adds longer reaction clip in webcam size and format to a given existing youtube vid 

    reactclip = VideoFileClip(REACTVIDPATH)
    destclip = VideoFileClip(RAWVIDSPATH + fname + ".mp4")
    # destclip = destclip.subclip(0, 20) # testing

    # Trims the reaction length to the video length. Make sure you have a long react mp4 
    reactclip = reactclip.subclip(0, destclip.duration).resize(0.28).margin(10, color=(238, 75, 43))
    destclip = destclip.volumex(0.55) # adjust volumes to your liking
    reactclip = reactclip.volumex(1.8)
    video = CompositeVideoClip([destclip,reactclip.set_position(("right","center"))])
    
    video.write_videofile(READYVIDSPATH + fname + ".mp4")

    