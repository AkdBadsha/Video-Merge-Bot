import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", "f0f35dbb5b0081cdc8d3c9d5383c4628")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6460761520:AAFWxbuFxn60sdkupPQzSt3sYQDiv2JL94c")
    TELEGRAM_API = os.environ["TELEGRAM_API", "25502576"]
    OWNER = os.environ.get("OWNER", "6093431204")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "Sujan_Ch)
    PASSWORD = os.environ.get("PASSWORD", "Sujanchy12")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://liris0826:A2aVOBzdIDiPptzn@cluster0.mc4rn8m.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("LOGCHANNEL", "-1001962988893")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
