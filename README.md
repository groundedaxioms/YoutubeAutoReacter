# Automated Youtube Channel Reacter

This program is deisgned to automatically "react" to every video from a given channel. It will scrape all of their video links, then to every video, download it, automatically edit in a set reaction video, and then upload it to your youtube channel (this involves some API setup on Google Cloud)

Designed with Python3 on Ubuntu

## Instructions for use
1. Clone this repo and `cd` into the directory
2. Setup the venv environment with this script: `./setup.sh`, and activate it with `source venv/bin/activate`
3. Set up your youtube channel API following these [instructions](https://github.com/pillargg/youtube-upload#getting-a-youtube-api-key)
    - Make sure that you have [`Scripts/Keys/client_secrets.json`](https://github.com/groundedaxioms/YoutubeAutoReacter/blob/e3bc9f8979b352cf352380e9e7a5c9a3c1acddbf/Scripts/Keys/client_secrets.json) replaced with your secrets file
    - This application will authenticate oauth in your browser, but you should only have to long in manually once
    - Ensure that these urls are listed under *Authorized redirect URIs*
        + <https://www.googleapis.com/auth/youtube.upload>
        + <http://localhost:8080/>
        + Google can be fussy with these urls, make sure slashes are in the right places etc.
4. At this point, the application can be ran with `./main.sh` to react to Destiny automatically
   - See command line output for any updates
   - Make sure you are in the python virtual environment
4. To add your own reaction video, replace [`Raw/React/origreact.mp4`](https://github.com/groundedaxioms/YoutubeAutoReacter/blob/e3bc9f8979b352cf352380e9e7a5c9a3c1acddbf/Raw/React/origreact.mp4) with a video of the same filename and path
    - Note that this will be trimmed down to the other video's length each time, so make it long (5-6 hours for Destiny content)
    - You can also replace the default reaction image in thumbnails in similar fashion by changing [`Raw/React/origreactthumbnail.mp4`](https://github.com/groundedaxioms/YoutubeAutoReacter/blob/e3bc9f8979b352cf352380e9e7a5c9a3c1acddbf/Raw/React/origreactthumbnail.jpg) 
    - Further customization can be accomplished in [`Scripts/globalvars.py`](https://github.com/groundedaxioms/YoutubeAutoReacter/blob/e3bc9f8979b352cf352380e9e7a5c9a3c1acddbf/Scripts/globalvars.py), explore and have fun!
    - If you change the channel you are scraping from, delete the pre-scraped [`Raw/destiny/allvids.txt`](https://github.com/groundedaxioms/YoutubeAutoReacter/blob/e3bc9f8979b352cf352380e9e7a5c9a3c1acddbf/Raw/destiny/allvids.txt) urls file and you will need to rename that [`destiny`](https://github.com/groundedaxioms/YoutubeAutoReacter/tree/e3bc9f8979b352cf352380e9e7a5c9a3c1acddbf/Raw/destiny) directory to the new handle. The scraping requires Selenium set up, see the comments in [`Scripts/grab_all_vids.py`](https://github.com/groundedaxioms/YoutubeAutoReacter/blob/e3bc9f8979b352cf352380e9e7a5c9a3c1acddbf/Scripts/grab_all_vids.py)

DGG4Lyfe
