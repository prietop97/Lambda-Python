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


## Creates a hashmap with day nodes -- Can be reused for other games or used in February or months that have 30 days
def create_quests_calendar(days_in_the_month, quests_arr):
    days = []
    for i in range(days_in_the_month):
        days.append(
            {
                "max_profit": 0,
                "most_profitable_quests": [],
                "quests_ending_this_day": [],
            }
        )

    for quest in quests_arr:
        end_date = quest.end_date
        days[end_date - 1]["quests_ending_this_day"].append(quest)

    return days


def get_max_reward_quest_list(quests_arr):
    calendar = create_quests_calendar(31, quests_arr)

    for i in range(1, len(calendar)):
        current_day_node = calendar[i]

        ## LOOPING THROUGH ALL THE QUESTS THAT ENDS ON THE CURRENT DATE
        for quest in current_day_node["quests_ending_this_day"]:
            quest_start_node = calendar[quest.start_date - 1]

            ## EDGE CASE, DOES NOT AFFECT ANSWER BUT CAN HELP BY GIVING LINK DIFFERENT OPTIONS WHILE GETTING THE SAME AMMOUNT RUPEES
            if (
                current_day_node["max_profit"]
                == quest.reward + quest_start_node["max_profit"]
            ):
                print("TODO")

            ## EDGE CASE, DOES NOT AFFECT ANSWER BUT CAN HELP BY GIVING LINK DIFFERENT OPTIONS WHILE GETTING THE SAME AMMOUNT RUPEES
            if (
                current_day_node["max_profit"]
                < quest.reward + quest_start_node["max_profit"]
            ):
                current_day_node["max_profit"] = (
                    quest.reward + quest_start_node["max_profit"]
                )

                ### GET THE MOST PROFITABLE QUESTS FOR EASY REACH
                current_day_node["most_profitable_quests"] = quest_start_node[
                    "most_profitable_quests"
                ][:]
                current_day_node["most_profitable_quests"].append(quest.name)

        ### IF YESTERDAY HAD A BETTER OUTCOME THAT TODAY THERE IS NO REASON TO KEEP TODAY STATS
        day_before_node = calendar[i - 1]
        if current_day_node["max_profit"] <= day_before_node["max_profit"]:
            calendar[i] = day_before_node


    ## RETURNING THE LAST DAY WHICH SHOULD HAVE EVERYTHING WE NEED
    return f"{calendar[i]['max_profit']} rupees by completing this quests: {calendar[i]['most_profitable_quests']}"


print(get_max_reward_quest_list(quests))
