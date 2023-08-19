import create_react
import download_vids
import upload
import grab_all_vids
from globalvars import *
import os

def main():
    if not os.path.exists(VIDLISTPATH):
        print("You don't have the list of videos from this channel yet. ")
        print("Scraping all videos from " + CHANNELVIDSURL + " . . .\n")
        grab_all_vids.grab_all_vids()
        print("Successfully wrote url list to " + VIDLISTPATH + "\n")
    else:
        print("Detected url list.", end=' ')

    print("Initiating react process . . . \n")    

    for i in range(MAXUPLOADS):
        vid_no = INITVIDNO + i
        str_cvd = str(vid_no)
        fname = CHANNELHANDLE + str_cvd

        print("Now processing video number " + str_cvd + ".\n")

        print("Downloading (May take a minute or two) . . . ")    
        download_vids.download_one_vid(vid_no, fname)
        print("Successfully downloaded!\n")

        print("Reacting and editing . . . ")    
        create_react.create_one_reaction(fname)
        print("Successfully reacted!\n")


        print("Uploading . . . ")    
        upload.upload_one_vid(fname)
        print("Succcessfully uploaded! Check your youtube dashboard.")
        print("----" * 20) 
        print()   

        if CLEAN:
            print("Cleaning all files created . . . ")
            files = [METADATAPATH + fname + ".json",
                     THUMBNAILPATH + fname + ".jpg",
                     RAWVIDSPATH + fname + ".mp4",
                     READYTHUMBNAILSPATH + fname + ".jpg",
                     READYVIDSPATH + fname + ".mp4"]
            for f in files:
                if os.path.exists(f):
                    os.remove(f)
            print("Succesfully cleaned up!\n")
        # Should be removed everytime to refresh creds
        if os.path.exists(OAUTHPATH):
            os.remove(OAUTHPATH)

        # increment in file to keep track of vids already reacted to
        update_vid_no(vid_no)

    print("Youtube API quota has been met. Goodbye!")

if __name__ == '__main__':
    main()