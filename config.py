import os
import aiohttp
from Python_ARQ import ARQ
from os import getenv
from dotenv import load_dotenv
from helpers.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAhP0SW5LanDKOVWWDlQHU8TMDgJU_sKrADGDw9J75LZKMDWty4vRAGyYSvzL_nb1g6bO9ot8T5FgA0ERaILZfZJGodTwykyeiwFxd4Os1mNxZfImrvoUkGrqEnDGIjNfDJLM2eDhRGQdnNDIltxQOKfEynm0IxG0ORiEdpcAKC4RNH0Vx9uxUwy5D7LemjXAD_TgB40giDO0AQ5KC-7THivVRBTBBRs4AqO1NYRoax1vf8Htr_uGnQdXd0MfmyIVOHqzR2SVRFxOCfwQD9THCUexTIbOymLSkVsIb3GPhwJcmD8HMysKyYYYxK-R7TbWrBvcztQ2qx3Vml8Zrz2_2mds4g1QA")
ARQ_API_KEY = getenv("ARQ_API_KEY")
BOT_TOKEN = getenv("BOT_TOKEN", "2049904848:AAE6raTlxx9RWgp_22355kTVWJZQzPV9fp8")
BOT_NAME = getenv("BOT_NAME", "𝐕rⓄs 𝐌𝐮₴𝐢𝐜")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/ca8af7378500099b78075.png")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/64114ef627bfbb87451a9.png")
BOT_IMG = getenv("BOT_IMG", "https://telegra.ph/file/1fe1780becadd6b7f7c2d.jpg")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "VrosMusicBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "VrosAssistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "sanki_bots_support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "sanki_bots")
OWNER_NAME = getenv("OWNER_NAME", "sanki_manager") # isi dengan username kamu tanpa simbol @
DEV_NAME = getenv("DEV_NAME", "sanki_manager")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/KennedyProject/KennedyXMusic")
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)

aiohttpsession = aiohttp.ClientSession()
arq = ARQ("https://thearq.tech", ARQ_API_KEY, aiohttpsession)
