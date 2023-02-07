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
        # Make the caller to invoke `reset()` for the next round.

        print(scene_info['ball'])

        if (scene_info["status"] == "GAME_OVER" or
            scene_info["status"] == "GAME_PASS"):
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            command = "SERVE_TO_LEFT"
        else:
            command = "NONE"

            lb = [(0, 287),(7, 294),(14, 301),(21, 308),(28, 315),(35, 322),(42, 329),(49, 336),(56, 343),(63, 350),(70, 357),(77, 364),(84, 371),(91, 378),(98, 385)]
            lb2 = [(195, 259),(188, 266),(181, 273),(174, 280),(167, 287),(160, 294),(153, 301),(146, 308),(139, 315),(132, 322),(125, 329),(118, 336),
                    (111, 343),(104, 350),(97, 357)]
            lb3 = [(0, 247),(7, 254),(14, 261),(21, 268),(28, 275),(35, 282),(42, 289),(49, 296),(56, 303),(63, 310),(70, 317),(77, 324),(84, 331),(91, 338),(98, 345),(105, 352),(112, 359),(119, 366),(126, 373),(133, 380),(140, 387),
                (147, 394)]
            lb4 = [(140, 177),(147, 184),(154, 191),(161, 198),(168, 205),(175, 212),(182, 219),
            (189, 226),(195, 233),(188, 240),(181, 247),(174, 254),(167, 261),(160, 268),(153, 275),(146, 282),(139, 289),(132, 296),(125, 303),
                (118, 310),(111, 317),(104, 324),(97, 331),(90, 338),(83, 345),(76, 352),(69, 359)]
            lb5 = [(0, 219),(7, 226),(14, 233),(21, 240),(28, 247),(35, 254),(42, 261),(49, 268),(56, 275),(63, 282),(70, 289),(77, 296),(84, 303),
(91, 310),(98, 317),(105, 324),(112, 331),(119, 338),(126, 345),(133, 352),(140, 359),(147, 366)]

            lb6 = [(195, 205),(188, 212),(181, 219),(174, 226),(167, 233),(160, 240),(153, 247),(146, 254),(139, 261),(132, 268),(125, 275),(118, 282),
(111, 289),(104, 296),(97, 303),(90, 310),(83, 317),(76, 324),(69, 331),(62, 338),(55, 345),(48, 352),(41, 359),(34, 366),(27, 373),(20, 380)]

            lp = [(112,400), (59, 400),(152,400),(34, 394),(175, 400), (6, 400)]

            # if 100 < scene_info['ball'][1] < 400:
            #     dot = 2
            #     if scene_info['ball'][1] == 195:
            #         dot = 1
            #     elif scene_info['ball'][1] == 0:
            #         dot = 0
                
            #     if dot == 1:
            #         command = 'MOVE_LEFT'
            #     elif dot == 0:
            #         command = 'MOVE_RIGHT'
            #     else:
            #         command = "NONE"

            if scene_info['ball'] in lb:
                if scene_info['platform'] <= lp[0]:
                    command = "MOVE_RIGHT"
                elif scene_info["platform"] >= lp[0]:
                    command = "MOVE_LEFT"
                else:
                    command = "NONE"
            if scene_info['ball'] in lb2:
                if scene_info['platform'] <= lp[1]:
                    command = "MOVE_RIGHT"
                elif scene_info["platform"] >= lp[1]:
                    command = "MOVE_LEFT"
                else:
                    command = "NONE"
            if scene_info['ball'] in lb3:
                if scene_info['platform'] <= lp[2]:
                    command = "MOVE_RIGHT"
                elif scene_info["platform"] >= lp[2]:
                    command = "MOVE_LEFT"
                else:
                    command = "NONE"
            
            if scene_info['ball'] in lb4:
                if scene_info['platform'] <= lp[3]:
                    command = "MOVE_RIGHT"
                elif scene_info["platform"] >= lp[3]:
                    command = "MOVE_LEFT"
                else:
                    command = "NONE"
            if scene_info['ball'] in lb5:
                if scene_info['platform'] <= lp[4]:
                    command = "MOVE_RIGHT"
                elif scene_info["platform"] >= lp[4]:
                    command = "MOVE_LEFT"
                else:
                    command = "NONE"

            if scene_info['ball'] in lb6:
                if scene_info['platform'] <= lp[5]:
                    command = "MOVE_RIGHT"
                elif scene_info["platform"] >= lp[5]:
                    command = "MOVE_LEFT"
                else:
                    command = "NONE"


        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
