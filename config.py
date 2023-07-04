import os

API_ID = 25121788
API_HASH = "097ef348f14f4beab2d579f6fc70d170"
BOT_TOKEN = "6190627535:AAFWun6w6OtvX545Vib-Rhjh14EY1xvI55w"
DB_CHANNEL_ID = -1001978353486
IS_PRIVATE = os.environ.get("True",False) # any input is ok But True preferable
OWNER_ID = 6063430281
UPDATE_CHANNEL = -1001978353486
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
