from telethon.sync import TelegramClient
import time

# Your Telegram API credentials
API_ID = 21293406
API_HASH = "dbaa72e10301db2908f08347c6333602"
CHAT_ID = -1002433318417  # Hexa game bot chat ID

client = TelegramClient("session", API_ID, API_HASH)

async def auto_hunt():
    await client.start()
    print("✅ Auto-Hunt Started!")

    while True:
        await client.send_message(CHAT_ID, "/hunt")
        print("📨 Sent /hunt command!")
        time.sleep(15)  # Adjust delay if needed

# Run auto-hunt
with client:
    client.loop.run_until_complete(auto_hunt())