import sys
from game import constants
from asciimatics.widgets import Frame
# DON'T CHANGE ANYTHING HERE c; 
class OutputService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self, screen):
        """The class constructor.
        
        Args:
            screen (Screen): An Asciimatics Screen.
        """
        self._screen = screen
    # DON'T CHANGE ANYTHING HERE c;     
    def clear_screen(self):
        """Clears the Asciimatics buffer for the next rendering.""" 
        self._screen.clear_buffer(7, 0, 0)
        self._screen.print_at("" * constants.MAX_X, 0, 0, 7)
        self._screen.print_at("-" * constants.MAX_X, 0, constants.MAX_Y, 7)
        
    def draw_actor(self, actor):
        """Renders the given actor's text on the screen.

        Args:
            actor (Actor): The actor to render.
        """ 
        text = actor.get_text()
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        self._screen.print_at(text, x, y, 7) # WHITE

    def draw_actors(self, actors):
        """Renders the given list of actors on the screen.

        Args:
            actors (list): The actors to render.
        """ 
        for actor in actors:
            self.draw_actor(actor)
    
    def flush_buffer(self):
        """Renders the screen.""" 
        self._screen.refresh()    