"""
The template of the main script of the machine learning process
"""

class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.ball_served = False

    def update(self, scene_info):
        """
        Generate the command according to the received `scene_info`.
        """
        print(scene_info['ball'])
        # Make the caller to invoke `reset()` for the next round.
        if (scene_info["status"] == "GAME_OVER" or
            scene_info["status"] == "GAME_PASS"):
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            command = "SERVE_TO_LEFT"
        else:
            # Follow the ball
            
            # if scene_info['platform'][0] >= scene_info['ball'][0]:
            #     command = "MOVE_LEFT"
            #     if scene_info['ball'][1] > 150:
            # elif scene_info['platform'][0] <= scene_info['ball'][0]:
            #     command = "MOVE_RIGHT"
            # else:
            #     command = "NONE"

            command = 'NONE'

            if scene_info['platform'][0] >= scene_info['ball'][0]:
                command = "MOVE_LEFT"

            elif scene_info['platform'][0] <= scene_info['ball'][0]:
                command = "MOVE_RIGHT"

            else: 
                command = "NONE"

        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False




# elif scene_info['ball'][1] > 250:
            #     if 0 < scene_info['ball'][0] < 80:
            #         command = "MOVE_LEFT"
            #     else:
            #         command = "MOVE_RIGHT"
                
            
            # if 20 < scene_info["frame"] < 100:
            #     command = "MOVE_RIGHT"
            
            # if 180 < scene_info["frame"] < 200:
            #     command = "MOVE_RIGHT"

            # if scene_info["platform"][0] == 0 or scene_info["platform"][0] < 400:
            #     command = "MOVE_RIGHT"
            # elif scene_info["platform"][0] == 400 or scene_info["platform"][0] > 0:
            #     command = "MOVE_LEFT"
             