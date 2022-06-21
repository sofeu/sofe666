## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBu5PRojnDY3DuZgBLThW-8_GuIR5cYANgpWRXLpcsJNVOe_VVyOyAHhuWdOWdyzVAaGKV_OxkDPm_Cpw-GE5gaRP26Mj1lQbOlA1e36i13bsR5TyYK5Z3SEabA-AefhAH1Msnwx325oDa1UnU2aRcMiNMfvSJvFvSJ0bTKJYB1HW-OrNnNRxlnzIQWcL5XnVOnrXKFHEcqm4uPEkbyIu1V0rvasfbIQky7Gi9NqiM-xG1LOk7F-x9fr2ldenYCVn8wJsVLTmTMvm-smmDeHrvQP951dewMLuUje9klS_BBnUzBhJc4ODxmFFvBOkfzw4CwtrjGa4tC0o_fJN4kWTzcW4=")
BOT_TOKEN = getenv("BOT_TOKEN", "5583750786:AAEs4aDmPwfugGJ3SUSWfGsl02nar1m78G4")
BOT_NAME = getenv("BOT_NAME", "song")
API_ID = int(getenv("API_ID", "6440669"))
API_HASH = getenv("API_HASH", "fec788c7d1ccdfc9ec507b63818d0970")
OWNER_NAME = getenv("OWNER_NAME", "sofe")
OWNER_USERNAME = getenv("OWNER_USERNAME", "no_nn")
ALIVE_NAME = getenv("ALIVE_NAME", "sofe")
BOT_USERNAME = getenv("BOT_USERNAME", "musicf7sbot")
OWNER_ID = getenv("OWNER_ID", "1686444936")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "no_nn")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "bc_cb")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "bc_cb")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1686444936").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
