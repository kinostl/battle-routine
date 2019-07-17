from mapspace import MapSpace

class GameMap():
    map_spaces=[]
    map_size = None

    def __init__(self, actors):
        #4 should be a setting
        self.map_size = 4*actors
        for x in range(self.map_size):
            for y in range(self.map_size):
                self.map_spaces.append(MapSpace(x,y))
    
    def __str__(self):
        game_map_string=""
        for map_id in range(len(self.map_spaces)):
            if map_id % self.map_size == 0:
                game_map_string = game_map_string + "\n"
            game_map_string = game_map_string + str(self.map_spaces[map_id])
        return game_map_string