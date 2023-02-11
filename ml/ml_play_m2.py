"""
The template of the main script of the machine learning process
"""

class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.ball_served = False
        self.loc = (93, 125)  # initialize the location

    def update(self, scene_info):
        """
        Generate the command according to the received `scene_info`.
        """
        # Make the caller to invoke `reset()` for the next round.
        if (scene_info["status"] == "GAME_OVER" or
            scene_info["status"] == "GAME_PASS"):
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            command = "SERVE_TO_LEFT"
        else:
            # y = ax + b    [1] = y ,[0] = x
            x = 0
            a = 0
            b = 0
            p = 0
            # a = (scene_info["ball"][1] - self.loc[1]) / (scene_info["ball"][0] - self.loc[0])
            if (self.loc[0] != scene_info["ball"][0]):
                a = (self.loc[1] - scene_info["ball"][1]) / (self.loc[0] - scene_info["ball"][0])
                b = scene_info["ball"][1] - (a * scene_info["ball"][0])
                x = ((400 - b) / a) % 400
                p = 200 - abs(200 - x) # p 為預測位置

            if p < scene_info["platform"][0] + 20:
                command = "MOVE_LEFT"
            elif p > scene_info["platform"][0] + 20:
                command = "MOVE_RIGHT"
            else:
                command = "NONE" 

            self.loc = scene_info["ball"]   # Record previous ball location
        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
