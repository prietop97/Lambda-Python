class Quest:
    def __init__(self,name,start_date,duration,reward,difficulty,location,quest_giver):
        self.name = name
        self.start_date = start_date
        self.duration = duration
        self.reward = reward
        self.difficulty = difficulty
        self.location = location
        self.quest_giver = quest_giver
        self.end_date = start_date + duration

