from abc import ABC, abstractmethod

class SteamBotABC(ABC):

    @abstractmethod
    def _set_grenre(self, game): pass