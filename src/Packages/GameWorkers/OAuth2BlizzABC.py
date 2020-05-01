from abc import ABC, abstractmethod

class OAuth2BlizzABC(ABC):
    
    #return string
    @abstractmethod
    def get_token(self): pass

    # #return boolean
    # @abstractmethod
    # def is_token_invalid(self): pass

    #return boolean
    @abstractmethod
    def _check_connection(self): pass