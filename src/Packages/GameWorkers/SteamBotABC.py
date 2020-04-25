from abc import ABC, abstractmethod

class SteamBotABC(ABC):

    @abstractmethod
    def set_grenre(self, game): pass