from abc import ABC, abstractmethod

class UserABC:

    #Arguments will change in various subclasses depending on what it required from each gaming platform
    #ie: SteamUser has steam_id and steam_api assigned in init, BlizzardUser has real_id
    @abstractmethod
    def __init__(self): pass