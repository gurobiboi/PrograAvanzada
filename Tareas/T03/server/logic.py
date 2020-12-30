

class Logic:
    
    def __init__(self):
        self.game_in_progress = False
        self.actual_player_list = []
    
    def update_player_list(self, player):
        self.actual_player_list.append(player.username)
