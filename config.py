import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6309843542:AAHFK5XqY502SbpJ8ObqqAPG1aXp8ZwIyTE")

    APP_ID = int(os.environ.get("APP_ID", 24447363))

    API_HASH = os.environ.get("API_HASH", "5400d05077ad972cd19fb317af63abec")
