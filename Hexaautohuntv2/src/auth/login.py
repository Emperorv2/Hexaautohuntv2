from telethon.sync import TelegramClient
import time

# Your Telegram API credentials
API_ID = 21293406
API_HASH = "dbaa72e10301db2908f08347c6333602"
PHONE_NUMBER = "+251716958387"

# Create a client session
client = TelegramClient("session", API_ID, API_HASH)

async def login():
    await client.start(PHONE_NUMBER)
    print("✅ Logged in successfully!")
    
    # Fetch user details
    me = await client.get_me()
    print(f"Logged in as: {me.first_name} ({me.id})")
    
    # Wait for confirmation before exiting
    time.sleep(3)

# Run the login process
with client:
    client.loop.run_until_complete(login())