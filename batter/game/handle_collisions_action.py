import sys
import random
from game import constants
from game.point import Point
from game.action import Action


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
       
        # ball - just one character changing"
        
        ball = cast ["ball"][0]
        ball_position = ball.get_position()
       
        paddle = cast["paddle"][0] # there's only one
        paddle_position = paddle.get_position()
        
        
        bricks = cast["brick"]
        # brick_position = bricks.get_position()
        
        for brick in bricks:
            if paddle.get_position().equals(brick.get_position()):
                description = brick.get_description()
                brick.set_text(description) 
        #PADDLE CODE 
        if paddle_position.get_y() -1 == ball_position.get_y():
            min_x = paddle_position.get_x()
            # beginning of paddle
            max_x = min_x + len(paddle.get_text())
            # total length of paddle because it adds min (beg) with total len.
          
            if ball_position.get_x() >= min_x and ball_position.get_x() <= max_x:
                old_velocity = ball.get_velocity()
                new_velocity = Point(old_velocity.get_x(), (old_velocity.get_y() * -1))
                ball.set_velocity(new_velocity)
        #BALL CODE
        # don't forget your lovely parenthesis c:
        if ball_position.get_x() == constants.MAX_X -1 or ball_position.get_x() == 1:
            old_velocity = ball.get_velocity()
            new_velocity = Point((old_velocity.get_x() * -1), old_velocity.get_y())
            ball.set_velocity(new_velocity)
            # total length of paddle because it adds min (beg) with total len.
          
    
        elif ball_position.get_y() == constants.MAX_Y -1 or ball_position.get_y() == 1:
            old_velocity = ball.get_velocity()
            new_velocity = Point((old_velocity.get_y() * -1), old_velocity.get_x())
            ball.set_velocity(new_velocity)
            sys.exit(print("""

             >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
             >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>               
                            GAME OVER
            <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            
            """
                           ))   
        #BRICKS CODE
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                # remove brick and have it bounce back 
                bricks.remove(brick)
                
                # have it bounce off now - use reverse method from  point
                ball.set_velocity(ball.get_velocity().reverse())
                # ball.set_position(ball.get_position().reverse())
                # write code here
                
        
        
        
                

        
      
    
        

        
        
        
    # fix your for loop here 
    # check if ball collides with paddle 
    # if collide , reverse y velocity
    # x normal
    # -y up +y down 
        