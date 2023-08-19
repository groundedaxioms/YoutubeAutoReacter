import os

CHANNELHANDLE = "destiny" # youtube.com/@CHANNELHANDLEHERE
PREFIX = "Mr. Soy REACTS TO"
REACTVIDPATH = "Raw/React/origreact.mp4"
REACTTHUMBNAILPATH = "Raw/React/origreactthumbnail.jpg"
SECRETSPATH = "Scripts/Keys/client_secrets.json"
OAUTHPATH = "Scripts/Keys/oauth.json"
ORIGREACTPATH = "Raw/React/origreact.mp4"
CLEAN = False # Will remove all used files after successful upload
MAXUPLOADS = 6 # Due to api limits

def get_init_vid_no():
    if not os.path.exists("Scripts/.batchcounter.txt"):
        with open("Scripts/.batchcounter.txt", "w") as f:
            f.write(str(0))
            return 0
    else:
        with open("Scripts/.batchcounter.txt", "r") as f:
            return int(f.read())
        
def update_vid_no(n):
    with open("Scripts/.batchcounter.txt", "w") as f:
            f.write(str(n + 1))

CHANNELVIDSURL = "https://www.youtube.com/@" + CHANNELHANDLE + "/videos"
_RAWPATH = "Raw/" + CHANNELHANDLE + "/"
METADATAPATH = _RAWPATH + "Metadata/"
THUMBNAILPATH = _RAWPATH + "Thumbnails/"
RAWVIDSPATH = _RAWPATH + "Vids/"
READYTHUMBNAILSPATH = "Ready/Thumbnails/"
READYVIDSPATH = "Ready/Vids/"
VIDLISTPATH = _RAWPATH + "allvids.txt"
INITVIDNO = get_init_vid_no()
