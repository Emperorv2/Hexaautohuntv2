from telethon.sync import TelegramClient
from utils.config import API_ID, API_HASH, PHONE_NUMBER

# Create a session file named "session"
client = TelegramClient("session", API_ID, API_HASH)

async def login():
    await client.start(PHONE_NUMBER)
    print("Logged in successfully!")
    me = await client.get_me()
    print(f"Logged in as: {me.first_name} ({me.id})")

# Run the login process
with client:
    client.loop.run_until_complete(login())