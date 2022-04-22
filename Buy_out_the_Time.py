
class Player:
    def __init__(self, name, quality_dict):
        self.name = name
        self.quality_dict = quality_dict
              
    def choose(self, choice):
        for key in self.quality_dict:
            if key in choice.cost_dict:
                self.quality_dict[key] += choice.cost_dict[key]
            else:
                print("bye")
        
        print(self.quality_dict)
                
    def check_available_actions(self):
        for item in actions:
            #for key in self.quality_dict.keys():
                if self.quality_dict.keys() in item.cost_dict.keys():
                    print("bruh")
                    if self.quality_dict[key] + item.cost_dict[key] >= 0:
                        available_actions.append(item.name)
                        print(item.name, self.quality_dict[key], item.cost_dict[key])
                    else:
                        continue
        print(available_actions)
                
                    
                    
        
class Choice:
    def __init__(self, name, cost_dict):
        self.cost_dict = cost_dict
        self.name = name
        
    def print_dict(quality):
        print(f"Choice's dictionary: {quality.cost_dict}")
        
        
player_one = Player("Anthony", {"Knowledge": 0, "Faith": 1, "Love": 2, "Peace": 3, "Joy":4, "Money": 5, "Health": 6, "Energy": 7})
player_two = Player("Priscilla", {"Knowledge": 0, "Faith": 5, "Love": 5, "Peace": 5, "Joy":5, "Money": 5, "Health": 5, "Energy": 5})

personal_study = Choice("personal study", {"Knowledge": 2, "Faith": 2, "Energy": -1})
secular_education = Choice("school", {"Knowledge": 5, "Faith": -5, "Money": -5, "Love": -3})
prayer = Choice("pray", {"Faith": 5, "Joy": 1, "Peace": 5})
exercise = Choice("exercise", {"Energy": 2, "Joy": 2, "Health": 5})
attend_meeting = Choice("meeting", {"Knowledge": 1, "Faith": 1, "Love": 2, "Joy": 1, "Money": -1})
work = Choice("work", {"Money": 5, "Energy": -3, "Love": -2, "Joy": -3, "Peace": -2})
ministry = Choice("preach", {"Faith": 2, "Love": 5, "Joy": 1, "Health": 1, "Energy": -2, "Money": -3})
entertainment = Choice("relax", {"Energy": 5, "Joy": 3, "Knowledge": -3, "Faith": -2, "Money": -2, "Health": -3})

actions = [personal_study, secular_education, prayer, exercise, attend_meeting, work, ministry, entertainment]
available_actions = []
actions_dict = {"personal study": personal_study, "school": secular_education, "pray": prayer, 
                "exercise": exercise, "meeting": attend_meeting, "work": work, 
                "preach": ministry, "relax": entertainment,
    }
player_marker = 0
def make_choice():
    global player_marker
    while True:
        if player_marker == 0:
            print(player_one.quality_dict)
            player_one.check_available_actions()
            action = input(f" {player_one.name}, What would you like to do?")
            player_marker += 1
            for thing in actions_dict:
                if action == thing:
                    player_one.choose(actions_dict[thing])
            
            
        elif player_marker == 1:
            print(player_two.quality_dict)
            player_two.check_available_actions()
            action = input(f" {player_two.name}, What would you like to do?")
            player_marker -= 1
            for thing in actions_dict:
                if action == thing:
                    player_two.choose(actions_dict[thing])


make_choice()