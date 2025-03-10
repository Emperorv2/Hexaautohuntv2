from utils.config import POKEMON_TO_CATCH
from utils.logger import logger

class Automation:
    def __init__(self):
        self.target_pokemon = POKEMON_TO_CATCH

    def run(self):
        logger.info(f"Starting automation for: {', '.join(self.target_pokemon)}")