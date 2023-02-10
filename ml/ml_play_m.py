"""
The template of the main script of the machine learning process
"""

class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.ball_served = False
        self.loc = (93, 125) # 設置初始球的位置

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
            # a = (scene_info["ball"][1] - self.loc[1]) / (scene_info["ball"][0] - self.loc[0])
            if (self.loc[0] != scene_info["ball"][0]):
                a = (self.loc[1] - scene_info["ball"][1]) / (self.loc[0] - scene_info["ball"][0])
                b = scene_info["ball"][1] - (a * scene_info["ball"][0])
                x = (393 - b) / a

                if(x < 0 or x > 200):   #反摺
                    b = scene_info["ball"][1] - ((-1/a) * scene_info["ball"][0])
                    x = (393 - b) * a * (-1)
            
            # if 0 < x < 200:  # debug
            #     print(f"y = {a}x + {b}")
            #     print(x)
            #     print("                                ")
            # print(scene_info["ball"], " ", self.loc, " ", scene_info["platform"])

            if (0 < x < 200):
                if scene_info["platform"][0] + 20 < x:
                    command = "MOVE_RIGHT"
                elif scene_info["platform"][0] + 20 > x:
                    command = "MOVE_LEFT"
                else:
                    command = "NONE"
            else:   # 其他處理
                command = "NONE"
              
        self.loc = scene_info["ball"] # 紀錄此幀的球位置，以便下幀的斜率計算

        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
