### QUEST CLASS TO INITIALIZE ALL QUESTS WITHOUT HAVING TO REPEAT MYSELF
## ALSO CALCULATES END_DATE WHICH I NEED FOR MY ALGORITHM
class Quest:
    def __init__(
        self, name, start_date, duration, reward, difficulty, location, quest_giver
    ):
        self.name = name
        self.start_date = start_date
        self.duration = duration
        self.reward = reward
        self.difficulty = difficulty
        self.location = location
        self.quest_giver = quest_giver
        self.end_date = start_date + duration


### LIST OF QUESTS --> BY IGN
quests = [
    Quest("Robbie's Research", 1, 3, 750, "Hard", "Hateno Ancient Tech Lab", "Purah"),
    Quest("A Parent's Love", 2, 2, 500, "Easy", "Tarrey Town", "Ruli"),
    Quest("The Weapon Connoisseur", 1, 4, 920, "Medium", "Hateno Village", "Nebb"),
    Quest("Sunshroom Sensing", 3, 8, 1050, "Hard", "Hateno Ancient Tech Lab", "Symin"),
    Quest("Sunken Treasure", 5, 1, 200, "Easy", "Lurelin Village", "Rozel"),
    Quest("Cooking with Koko", 3, 4, 400, "Medium", "Kakariko Village", "Koko"),
    Quest(
        "Arrows of Burning Heat", 7, 5, 1200, "Very Hard", "Snowfield Stable", "Rola"
    ),
    Quest("Stalhorse: Pictured!", 12, 3, 370, "Medium", "Rito Village", "Juannelle"),
    Quest("Curry for What Ails You", 6, 8, 840, "Hard", "Goron City", "Lester"),
    Quest("The Jewel Trade", 19, 2, 165, "Easy", "Hateno Ancient Tech Lab", "Ramella"),
    Quest("Slated for Upgrades", 23, 7, 1520, "Very Hard", "Gerudo Town", "Purah"),
    Quest("Medicinal Molduga", 14, 4, 600, "Medium", "Gerudo Town", "Malena"),
    Quest("Tools of the Trade", 8, 3, 430, "Easy", "Gerudo Town", "Isha"),
    Quest(
        "A Gift for the Great Fairy",
        20,
        7,
        1100,
        "Very Hard",
        "Tabantha Bridge Stable",
        "Toren",
    ),
    Quest("A Rare Find", 28, 3, 590, "Medium", "Outskirt Stable", "Trott"),
    Quest("Frog Catching", 10, 4, 900, "Hard", "Zora's Domain", "Jihato"),
    Quest("Luminous Stone Gathering", 13, 6, 230, "Very Hard", "Zora's Domain", "Ledo"),
    Quest("A Freezing Rod", 25, 4, 1120, "Very Hard", "Great Hyrule Forest", "Kula"),
    Quest("Rushroom Rush!", 9, 1, 460, "Easy", "Gerudo Canyon Stable", "Pirou"),
    Quest("The Hero's Cache", 16, 10, 780, "Medium", "Kitano Bay", "Kass"),
    Quest("A Gift of Nightshade", 4, 5, 410, "Hard", "Tuft Mountain", "Wabbin"),
    Quest("Lynel Safari", 11, 3, 570, "Easy", "Zora's Domain", "Laflat"),
    Quest("Riddles of Hyrule", 7, 2, 1200, "Hard", "Great Hyrule Forest", "Walton"),
    Quest("An Ice Guy", 2, 23, 2100, "Very Hard", "Kara Kara Bazaar", "Guy"),
]



def getBestQuePath(arr):

    # node = {
    #   'max_reward': 0,
    #   'most_profitable_quests': [],
    #   ''
    # }
    ## SET IT UP
    days = []
    for i in range(32): #0(1)
        days.append([0, [], []])

    for quest in arr: #0(N)
        end_date = quest.end_date
        days[end_date - 1][2].append(quest)

    for i in range(len(days)):
        # print(f'before: day{i+1}: {days[i]}')
        for quest in days[i][2]:

            if days[i][0] == quest.reward + days[quest.start_date - 1][0]:
                print("")
                print(quest.reward + days[quest.start_date - 1][0])
                print("Hello i'm running")

            if days[i][0] < quest.reward + days[quest.start_date - 1][0]:
                days[i][0] = quest.reward + days[quest.start_date - 1][0]

                ### GET THE IDS
                days[i][1] = days[quest.start_date - 1][1][:]
                days[i][1].append(quest.name)
              

        ### IF THIS IS NOT A GOOD DAY, DEFAULT TO THE LAST DAY
        if i != 0 and days[i][0] <= days[i - 1][0]:
            days[i] = days[i - 1]

        # print(f'after: day{i+1}: {days[i]}')
    return days[-1]


print(getBestPath(quests))
