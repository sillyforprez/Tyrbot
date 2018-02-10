from registry import instance
from character_manager import CharacterManager


@instance
class BuddyManager:
    def __init__(self):
        self.buddy_list = {}
        self.buddy_list_size = 1000

    def inject(self, registry):
        self.character_manager: CharacterManager = registry.get_instance("charactermanager")

    def start(self):
        pass

    def update(self, packet):
        self.buddy_list[packet.character_id] = {"online": packet.online}

    def get_buddy(self, char):
        char_id = self.character_manager.resolve_char_to_id(char)
        return self.buddy_list.get(char_id, None)

    def is_online(self, char):
        char_id = self.character_manager.resolve_char_to_id(char)
        buddy = self.get_buddy(char_id)
        if buddy is None:
            return None
        else:
            return buddy["online"] == 1
