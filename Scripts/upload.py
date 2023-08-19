from youtube_upload.client import YoutubeUploader
import json
from globalvars import *

def upload_one_vid(fname):
    json_path = METADATAPATH + fname + ".json"
    vid_path = READYVIDSPATH + fname + ".mp4"
    uploader = YoutubeUploader(secrets_file_path=SECRETSPATH)

    uploader.authenticate(oauth_path=OAUTHPATH)

    # Video options to add thumbnail, tags, title, etc
    with open(json_path, 'r') as jf:
        options = json.load(jf)
        options["thumbnailLink"] = READYTHUMBNAILSPATH + fname + ".jpg"

        # upload video
        uploader.upload(vid_path, options) 