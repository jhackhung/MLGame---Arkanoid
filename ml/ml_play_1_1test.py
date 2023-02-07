"""
The template of the main script of the machine learning process
"""
# EASY 1 PASS
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
        # Make the caller to invoke `reset()` for the next round.
        # print(scene_info['ball'], scene_info['platform'])
        if (scene_info["status"] == "GAME_OVER" or
            scene_info["status"] == "GAME_PASS"):
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            command = "SERVE_TO_LEFT"
        else:
            command = "NONE"
            
            if scene_info['ball'][1] > 200:
                if scene_info['platform'][0] != scene_info['ball'][0] + 25:
                    if scene_info['platform'][0] > scene_info['ball'][0] + 25:
                        command = "MOVE_LEFT"
                    
                    elif scene_info['platform'][0] < scene_info['ball'][0] + 25:
                        command = "MOVE_RIGHT"
                    
                    else:
                        command = "NONE"

                elif scene_info['platform'][0] != scene_info['ball'][0] - 35:
                    if scene_info['ball'][1] > 300:
                        if scene_info['platform'][0] > scene_info['ball'][0]:
                            command = "NONE"
                        else:
                            command = "MOVE_LEFT"    

                    if scene_info["platform"][0] < scene_info['ball'][0] - 35:
                        command = "MOVE_RIGHT"

                    elif scene_info['platform'][0] > scene_info['ball'][0] - 35:
                        command = "MOVE_LEFT"
                    
                    else:
                        command = "NONE"
# Another is full of data (tree) to train the machine

        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
