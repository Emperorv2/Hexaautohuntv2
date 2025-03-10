from utils.config import POKEMON_TO_CATCH
from utils.logger import logger

class Scraper:
    def __init__(self):
        self.pokemon_list = POKEMON_TO_CATCH

    def run(self):
        logger.info(f"Pokémon to catch: {', '.join(self.pokemon_list)}")