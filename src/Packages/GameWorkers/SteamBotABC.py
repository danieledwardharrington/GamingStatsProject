from abc import ABC, abstractmethod

class SteamBotABC(ABC):

    @abstractmethod
    @classmethod
    def set_grenre(cls, game):
        pass