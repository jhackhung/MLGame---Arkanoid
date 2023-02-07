"""
The template of the main script of the machine learning process
"""

class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.ball_served = False
        self.loc = (93, 125)

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
            p = 0
            if (self.loc[0] != scene_info["ball"][0]):
                p = TARGET(*self.loc, *scene_info["ball"])  #Another METHOD * 解包
                
            if p < scene_info["platform"][0] + 15:
                command = "MOVE_LEFT"
            elif p > scene_info["platform"][0] + 35:
                command = "MOVE_RIGHT"
            else:
                command = "NONE" 


            self.loc = scene_info["ball"]
        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
def TARGET(x1, y1, x2, y2):
    a = (y1-y2) / (x1-x2)
    b = y1 - (a*x2)
    x = ((400-b) / a) % 400
    return 200 - abs(200 - x)

# a = (self.loc[1] - scene_info["ball"][1]) / (self.loc[0] - scene_info["ball"][0])
# b = scene_info["ball"][1] - (a * scene_info["ball"][0])
# x = ((400 - b) / a) % 400
# p = 200 - abs(200 - x)