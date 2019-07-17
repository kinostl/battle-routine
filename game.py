#Example of Turn order
#Actions are all submitted at the same time
#A turns' actions are resolved in the order of Weighted Speed[1] from best to worst
#   [1]Weighted Speed. Actions all have weights, which are multiplied by the Actors' Speed score.


#Battle chip decks
#   Mininum deck size

#Battle chips have
#   Attack
#   Pattern
#   Weight

#Teleport resolution
#   Teleports always occur after tile conversions?
#   If a navi attempts to teleport to a space that is the wrong color they take damage and stay in place

#Tile Conversion resolution
#   Tile conversion has a lot of play with trying to be the last one to convert the tile to the color you'd like. Design should reflect this.

#Navi Stats
#   Don't really need too many stats since most of this game is going to be in loop management
#   Speed, determines turn order
#   HP?

from gamemap import GameMap
from actor import Actor

#import all the players here
class Game():
    actors=[]
    game_map=None

    def __init__(self):
        self.actors.append(Actor())
        self.game_map = GameMap(len(self.actors))

    def main(self):
        while len(self.actors) > 1:
            for actor in self.actors:
                actor.getAction()
            pass
        print("The winner is blank!")
        #iterate through every actor
            #collect their actions
        #weight the actions
        #execute the actions in weighed order
        pass

game = Game()
game.main()
