import os

# Telegram API Credentials
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
PHONE_NUMBER = os.getenv("PHONE_NUMBER", "")
CHAT_ID = int(os.getenv("CHAT_ID", 0))

# List of Pokémon to Catch
POKEMON_TO_CATCH = [
    "Eternatus", "Zacian", "Dialga", "Palkia", "Mewtwo", "Arceus", "Zamazenta",
    "Glastrier", "Calyrex", "Kyurem", "Lunala", "Necrozma", "Rayquaza",
    "Cosmoem", "Yveltal", "Kyogre", "Xerneas", "Cosmog", "Groudon", "Giratina",
    "Zeraora", "Marshadow", "Buzzwole", "Solgaleo", "Zygarde", "Slaking",
    "Metagross", "Beldum", "Slakoth", "Vigoroth", "Garchomp", "Gallade",
    "Gardevoir", "Dragapult", "Ho-oh", "Lugia", "Reshiram", "Regigigas",
    "Gengar", "Alakazam", "Greninja", "Salamence", "Charizard", "Blastoise",
    "Lucario", "Darmanitan"
]

# Scraper & Automation Configuration
CONFIG = {
    "SCRAPER_URL": "https://example.com",
    "HEADLESS": True,
    "USE_PROXY": False  # Set to True if using a proxy
}