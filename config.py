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
SESSION_NAME = getenv("SESSION_NAME", "BQAMw05Xmb9rICmp-9jrdWuX-acnkl1MI8iccbfXcVFS1EwAEqUIZBEPG69Ok5LMgUeOfyihsitpFUitSxb6UmrKcMNpmMG5jLVgcDBhxYCRmzhQZssuA6q3P4wwVtu0lVcbqozBS8ALiFwH2pOXOSHMj9uMCnDq85rzCyCy7sTboKvKsf3jO0tSO2Zd2qn_PnUXkjbJm-CJzwlJzlsUqtQb5SjoUXiQOrtENB33rRVuYOu-WAVKXV3JoOX5LY4Ykv5LHgo72WGkD3VQ4J1MwbF9y59btffo2xhFkDhm_sBCiIhQit2IRrrBTQbs8dnNeCnQbQJMlOWyK6nXKiiK7Seeds4g1QA")
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
