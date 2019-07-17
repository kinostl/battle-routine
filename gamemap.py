from mapspace import MapSpace

class GameMap():
    map_spaces=[]

    def __init__(self, actors):
        #4 should be a setting
        map_size = 4*actors
        for x in range(map_size):
            for y in range(map_size):
                self.map_spaces.append(MapSpace(x,y))