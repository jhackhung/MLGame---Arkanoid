"""
The template of the main script of the machine learning process
"""

class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.ball_served = False
        self.loc = (93, 395)
        self.t = 0  
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
            command = "NONE"

            # 兩點座標取斜率，預測最後與400之交點。
            # 得到預測座標
            plot = (0, 0)

            if plot == (0, 0):
                # data = scene_info["ball"] + t*(-7, -7)
                # data1 = scene_info['ball'] + t*(7, -7)
                # complex => a = 7-7j, a*3 = 21-21j, a.real = 21, a.imag = -21
                dataY = scene_info["ball"][1] + self.t * (scene_info["ball"][1] - self.loc[1])
                dataX = scene_info["ball"][0] + self.t * (scene_info["ball"][0] - self.loc[0])

                if dataY == 395 and 0 < dataX < 195:
                    plot = (dataX, dataY)#Q
                    self.t = 0

                if not(0 <= dataX <= 195 and 0 <= dataY <= 500):
                    dataX = scene_info["ball"][0]
                    dataY = scene_info["ball"][1]
                    self.t = 0
                # self.loc = scene_info['ball']
                self.t += 1

            print(dataX, dataY, scene_info["ball"], self.loc, self.t, plot, sep = ' ')

            #how to predict more and make the platform move(to keep the plot that can move platform)

            if plot[0] < scene_info["platform"][0] < plot[0] + 40:
                if scene_info['platform'][0] < plot[0] + 40:
                    command = 'MOVE_RIGHT'
                else:
                    command = "MOVE_LEFT"
                    
            self.loc = scene_info['ball'] #Last location
            return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
