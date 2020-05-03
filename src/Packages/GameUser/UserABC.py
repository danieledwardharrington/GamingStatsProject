from abc import ABC, abstractmethod

class UserABC(ABC):
    blizz_real_id = None
    blizz_region = None
    blizz_realm_id = None
    blizz_region_id = None
    blizz_games = None
    steam_id = None
    steam_api_key = None

    @abstractmethod
    def set_steam_info(self, user_id, user_api):
        pass

    @abstractmethod
    def set_blizz_info(self, real_id, region, games):
        pass