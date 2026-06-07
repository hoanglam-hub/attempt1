from configs import *

class Rule:
    def __init__(self):
        self.mar_dict = {"num_of_yawn_frame": 0, "num_of_yawn": 0, 'moment_of_yawn': []}
        self.ear_dict = {"num_of_ear_frame": 0, "num_of_ear": 0, "moment_of_ear1": [], "moment_of_ear": []}
        self.pitch_dict = {"num_of_pitch_frame": 0, "num_of_pitch": 0, "moment_of_pitch_lower1": [], "moment_of_pitch": []}
        self.yaw_dict = {"num_of_yaw_frame": 0, "num_of_yaw": 0, "moment_of_yaw_lower1": [], "moment_of_yaw": []}
        self.roll_dict = {"num_of_roll_frame": 0, "num_of_roll": 0, "moment_of_roll_lower1": [], "moment_of_roll": []}

    def process():
        #rule meme,


    def mar_rule(self, mar):
        if mar > mar_threshold:
            self.mar_dict["num_of_yawn_frame"] += 1
        else:
            if self.mar_dict["num_of_yawn_frame"] >5:
                self.mar_dict["num_of_yawn"] += 1
                self.mar_dict["moment_of_yawn"].append(time.time())
            self.mar_dict["num_of_yawn_frame"] = 0
        if len(self.mar_dict["moment_of_yawn"]) > 0 and time.time() - self.mar_dict["moment_of_yawn"][0] >= 60:
            if len(self.mar_dict["moment_of_yawn"]) >= 2:
                self.mar_dict["moment_of_yawn"].remove(self.mar_dict["moment_of_yawn"][0])
                rule_score += self.config["Score"]["MAR_score"]

            else:
                self.moment_of_yawn.remove(self.moment_of_yawn[0])


    def ear_rule(self, ear):
        if ear < ear_threshold:
            self.ear_dict["num_of_ear_frame"] += 1
            self.ear_dict["moment_of_ear1"].append(time.time())
            if self.ear_dict["moment_of_ear1"][-1] - self.ear_dict["moment_of_ear1"][0] >= 7:
                rule_score_intense += self.config["Score"]["EAR_score1"]


        else:
            self.ear_dict["moment_of_ear1"] = []
            if self.ear_dict["num_of_ear_frame"] > 5:
                self.ear_dict["num_of_ear"] += 1
                self.ear_dict["moment_of_ear"].append(time.time())
            self.ear_dict["num_of_ear_frame"] = 0
        if len(self.ear_dict["moment_of_ear"]) > 0 and time.time() - self.ear_dict["moment_of_ear"][0] >= 300:
            if len(self.ear_dict["moment_of_ear"]) >= 100:
                self.ear_dict["moment_of_ear"].remove(self.ear_dict["moment_of_ear"][0])
                rule_score += self.config["Score"]["EAR_score1"]
            else:
                self.ear_dict["moment_of_ear"].remove(self.ear_dict["moment_of_ear"][0])


    def pitch_rule(self, pitch):
        if pitch < pitch_lower_threshold or pitch > pitch_upper_threshold:
            self.pitch_dict["num_of_pitch_frame"] += 1
            self.pitch_dict["moment_of_pitch_lower1"].append(time.time())
            if self.pitch_dict["moment_of_pitch_lower1"][-1] - self.pitch_dict["moment_of_pitch_lower1"][0] >= 7:
                rule_score_intense += self.config["Score"]["pitch_score"]


        else:
            self.pitch_dict["moment_of_pitch_lower1"] = []
            if self.pitch_dict["num_of_pitch_frame"] > 30:
                self.pitch_dict["num_of_pitch"] += 1
                self.pitch_dict["moment_of_pitch"].append(time.time())
            self.pitch_dict["num_of_pitch_frame"] = 0

        # check gật gù ngủ gật
        # nếu thời gian lần gục cuồi và lần gục đầu >=60 thì xét số lần gục có lớn hơn 3 không, >=3 --> ngủ gật, <3 --> bình thường
        if len(self.pitch_dict["moment_of_pitch"]) > 0 and time.time() - self.pitch_dict["moment_of_pitch"][0] >= 60:
            if len(self.pitch_dict["moment_of_pitch"]) >= 3:
                rule_score += self.config["Score"]["pitch_score"]
                self.pitch_dict["moment_of_pitch"].remove(self.pitch_dict["moment_of_pitch"][0])
            else:
                self.pitch_dict["moment_of_pitch"].remove(self.pitch_dict["moment_of_pitch"][0])


    def yaw_rule(self, yaw):
        if yaw < yaw_lower_threshold or yaw > yaw_upper_threshold:
            self.yaw_dict["num_of_yaw_frame"] += 1
            self.yaw_dict["moment_of_yaw_lower1"].append(time.time())
            if self.yaw_dict["moment_of_yaw_lower1"][-1] - self.yaw_dict["moment_of_yaw_lower1"][0] >= 7:
                rule_score_intense += self.config["Score"]["yaw_score"]


        else:
            self.yaw_dict["moment_of_yaw_lower1"] = []
            if self.yaw_dict["num_of_yaw_frame"] > 30:
                self.yaw_dict["num_of_yaw"] += 1
                self.yaw_dict["moment_of_yaw"].append(time.time())
            self.yaw_dict["num_of_yaw_frame"] = 0

        if len(self.yaw_dict["moment_of_yaw"]) > 0 and time.time() - self.yaw_dict["moment_of_yaw"][0] >= 60:
            if len(self.yaw_dict["moment_of_yaw"]) >= 3:
                self.yaw_dict["moment_of_yaw"].remove(self.yaw_dict["moment_of_yaw"][0])
                rule_score += self.config["Score"]["yaw_score"]
            else:
                self.yaw_dict["moment_of_yaw"].remove(self.yaw_dict["moment_of_yaw"][0])


    def roll_rule(self, roll):
        if roll < roll_lower_threshold or roll > roll_upper_threshold:
            self.roll_dict["num_of_roll_frame"] += 1
            self.roll_dict["moment_of_roll_lower1"].append(time.time())
            if self.roll_dict["moment_of_roll_lower1"][-1] - self.roll_dict["moment_of_roll_lower1"][0] >= 5:
                rule_score_intense += self.config["Score"]["roll_score"]


        else:
            self.roll_dict["moment_of_roll_lower1"] = []
            if self.roll_dict["num_of_roll_frame"] > 30:
                self.roll_dict["num_of_roll"] += 1
                self.roll_dict["moment_of_roll"].append(time.time())
            self.roll_dict["num_of_roll_frame"] = 0

        if len(self.roll_dict["moment_of_roll"]) > 0 and time.time() - self.roll_dict["moment_of_roll"][0] >= 60:
            if len(self.roll_dict["moment_of_roll"]) >= 3:
                rule_score += self.config["Score"]["roll_score"]
                self.roll_dict["moment_of_roll"].remove(self.roll_dict["moment_of_roll"][0])
            else:
                self.roll_dict["moment_of_roll"].remove(self.roll_dict["moment_of_roll"][0])


                







