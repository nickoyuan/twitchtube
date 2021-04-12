import pathlib

# Note:
# Changing FRAMES and or RESOULTION will heavily impact load on CPU.
# If you have a powerful enough computer you may set it to 1080p60

# Secrets
# Twitch Client ID
CLIENT_ID = "700c79e2148ufw0shb2t36pqbejz8f"

# Twitch OAuth Token
OAUTH_TOKEN = "lbjn02zshyayqgm993gpy07jtubsp0"

# Path to the Firefox profile where you are logged into YouTube
ROOT_PROFILE_PATH = "C:\\Users\\nicko\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\8zlud8gd.ihatemylife"

# Selenium
# How many seconds Firefox should sleep for when uploading
SLEEP = 3

# If True Firefox will be hidden (True/False)
HEADLESS = True

# If information when uploading should be printed (True/False)
DEBUG = True


# Paths
PATH = str(pathlib.Path().absolute()).replace("\\", "/")
CLIP_PATH = PATH + "/clips/{}/{}"


# Video
# Set the mode (game/channel)
MODE = "game"

# If mode is channel put channel names e.g. ["trainwreckstv", "xqcow"]
# If mode is game put game names e.g. ["Team Fortress 2", "Just Chatting"]
LIST = ["VALORANT"]

# If clips should be rendered into one video (True/False)
# If set to False everything else under Video will be ignored
RENDER_VIDEO = True

# Resoultion of the rendered video (height, width) for 1080p: ((1080, 1920))
RESOLUTION = (1080, 1920)

# Frames per second (30/60)
FRAMES = 30

# Minumum video length in minutes (doesn't always work)
VIDEO_LENGTH = 10.5
#VIDEO_LENGTH = 0.5

# Resize clips to fit RESOLUTION (True/False)
# If any RESIZE option is set to False the video might end up having a weird resolution
RESIZE_CLIPS = True

# Name of the rendered videor
FILE_NAME = "rendered"

# Name of downloaded clip (slug/title)
CLIP_TITLE = "slug"

# Enable (True/False)
# Resize (True/False) read RESIZE_CLIPS
# Path to video file (str)
ENABLE_INTRO = False
RESIZE_INTRO = True
INTRO_FILE_PATH = PATH + "/assets/intro.mp4"

ENABLE_TRANSITION = True
RESIZE_TRANSITION = True
TRANSITION_FILE_PATH = PATH + "/assets/transition.mp4"

ENABLE_OUTRO = False
RESIZE_OUTRO = True
OUTRO_FILE_PATH = PATH + "/assets/outro.mp4"


# Other
# If YouTube stuff should be saved to a separate file e.g. title, description & tags (True/False)
SAVE_TO_FILE = True

# Name of the file YouTube stuff should be saved to
SAVE_FILE_NAME = "youtube"

# If the rendered video should be uploaded to YouTube after rendering (True/False)
UPLOAD_TO_YOUTUBE = True

# If the downloaded clips should be deleted after rendering the video (True/False)
DELETE_CLIPS = True

# How often it should check if it has made a video today (in seconds)
TIMEOUT = 3600


# Twitch
RETRIES = 5

# Twitch API Request Options
HEADERS = {"Accept": "application/vnd.twitchtv.v5+json", "Client-ID": CLIENT_ID}
PARAMS = {"period": "all", "language": "en", "limit": 100}  # 100 is max


# YouTube
# If empty, it would take the title of the first clip, and add "- *category* Highlights Twitch"
TITLE = ""

# Category
# Not supported yet
CATEGORY = 20  # 20 for gaming

# Descriptions
# {} will be replaced with a list of streamer names
DESCRIPTIONS = {
    "VALORANT": "Valorant most viewed twitch clips \n\n{}\n"
}

# Thumbnails
THUMBNAILS = {
    "VALORANT": "path/to/file.jpg",
}

# Tags
# Not supported yet
TAGS = {
    "VALORANT": "valorant montage,valorant plays,valorant funny moments,valorant best highlights,valorant pro plays,twitch moments valorant,twitch stream valorant,twitch most viewed valorant,twitch highlights valorant,valorant best moments,valorant moment,valorant funny,valorant best,valorant epic,valorant funny highlights,valorant best plays,valorant viral,valorant viral moments,valorant viral clips,valorant epic moments,valorant funniest moments,valorant top fails"
}
