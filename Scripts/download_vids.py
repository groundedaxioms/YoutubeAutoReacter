from pytube import YouTube
import json
import requests
from globalvars import *

def download_one_vid(vid_no, fname):

    def get_metadata(yt):
        return { "description": yt.description, 
                "tags": yt.keywords,
                "title": "Mr. Soy REACTS TO " + yt.title,
                "kids": False
                # "privacyStatus" : "public"
                }

    with open(VIDLISTPATH, 'r') as vids, open(METADATAPATH + fname + ".json", 'w') as meta:
        line = vids.readlines()[vid_no]
        yt = YouTube(line)
        streams = yt.streams.filter(progressive=True, file_extension="mp4") 
        if streams:
            json.dump(get_metadata(yt), meta, indent=4)

            # Download thumbnail for editing, assumes jpg
            data = requests.get(yt.thumbnail_url).content
            with open(THUMBNAILPATH + fname + ".jpg", 'wb') as tf:
                tf.write(data)

            # Should get highest quality mp4 I think
            streams.last().download(output_path=RAWVIDSPATH, filename=fname + ".mp4")
