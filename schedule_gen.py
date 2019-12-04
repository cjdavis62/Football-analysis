from analyzer import *
import random

def init_schedule():
    schedule = get_schedule()
    init_schedule = np.full_like(schedule, -1)
    return init_schedule

# Get player schedule for a season
"""def get_player_schedule(number_of_players, schedule, season_length, repeat_games, player, number_of_tries):
    number_of_tries = number_of_tries + 1
    print("starting player: ", player)

    # in case it doesn't work, save the current schedule
    start_schedule = schedule
    
    # Create schedule for a player
    list_of_available = []
    list_of_available.extend(range(player+1, number_of_players))
        
    for game in range(0,season_length - repeat_games):
        if (schedule[game, player] == -1):
            print(len(list_of_available))
            print("Available list: ", list_of_available)
            opponent = get_opponent(list_of_available, game, schedule)
            # restart if this is broken
            if opponent == 0:
                schedule = get_player_schedule(number_of_players, start_schedule, season_length, repeat_games, player, number_of_tries)
                return schedule
            list_of_available.remove(opponent)
            schedule[game,player] = opponent
            print("Schedule: ", schedule)
            if (opponent > player):
                schedule[game, opponent] = player
    for game in range(0, repeat_games):
        if (schedule[game + (season_length - repeat_games), player] == -1):
            opponent = schedule[game, player]
            schedule[game + (season_length - repeat_games), player] = opponent
            if (opponent > player):
                schedule[game + (season_length - repeat_games), opponent] = player

    return schedule
"""
                    
# Get an opponent in a week given that opponent cannot play another game in week
def get_opponent(list_of_available, week, schedule):

    weekly_list_of_available = list_of_available

    list_of_weekly_removed = []

    #print(schedule[week])
    for player in schedule[week]:
        if player in weekly_list_of_available:
            #print("removing player: ", player)
            weekly_list_of_available.remove(player)
            list_of_weekly_removed.append(player)

    if not weekly_list_of_available:
        #print("broken")
        return 0 # 0 means opponent finding doesn't work, retry
    opponent = random.choice(weekly_list_of_available)
    #print("opponent: ", opponent)
    weekly_list_of_available.extend(list_of_weekly_removed)
    return opponent
            
        
def create_schedule(number_of_players, season_length, repeat_games):

    schedule = init_schedule()

    for player in range (0, number_of_players):

        #print("starting player: ", player)
        
        # Create schedule for a player
        list_of_available = []
        list_of_available.extend(range(player+1, number_of_players))
        
        for game in range(0,season_length - repeat_games):
            if (schedule[game, player] == -1):
                #print(len(list_of_available))
                #print("Available list: ", list_of_available)
                opponent = get_opponent(list_of_available, game, schedule)
                if opponent == 0:
                    return init_schedule()
                list_of_available.remove(opponent)
                schedule[game,player] = opponent
                #print("Schedule: ", schedule)
                if (opponent > player):
                    schedule[game, opponent] = player
        for game in range(0, repeat_games):
            if (schedule[game + (season_length - repeat_games), player] == -1):
                opponent = schedule[game, player]
                schedule[game + (season_length - repeat_games), player] = opponent
                if (opponent > player):
                    schedule[game + (season_length - repeat_games), opponent] = player
                
    return schedule

def check_schedule_same(scheduleA, scheduleB, number_of_players, season_length):
    for i in range (0, season_length):
        for j in range (0, number_of_players):
            if (scheduleA[i, j] != scheduleB[i,j]):
                return False
    #print(scheduleA)
    #print(scheduleB)
    #print("")
    return True


# Creates schedules_to_make number of schedules and returns a list of good schedules
# For every 1k schedules, approximately 6 are good
def generate_schedules(schedules_to_make, number_of_players, repeat_weeks, season_length):
    schedule = init_schedule()

    list_of_good_schedules = []
    list_of_good_schedules.append(get_schedule())
    number_of_copies = 0
    schedule_number = 0

    print("Generating schedules")
    for schedules in range (0, schedules_to_make):
        new_schedule = create_schedule(number_of_players, season_length, repeat_weeks)
        if new_schedule.all() != init_schedule().all():
            # Start off assuming it's a good list. Change to False if it ends up bad
            is_good_schedule = True
            for schedule_in_list in list_of_good_schedules:
                if check_schedule_same(new_schedule, schedule_in_list, number_of_players, season_length):
                    number_of_copies = number_of_copies + 1
                    is_good_schedule = False
                    break
            if is_good_schedule:
                schedule_number = schedule_number + 1
                list_of_good_schedules.append(new_schedule)
                print("Good schedule #{schedule_number}! schedule {schedules} of {schedules_to_make} complete".format(schedules = schedules, schedules_to_make = schedules_to_make, schedule_number = schedule_number))

    #print(list_of_good_schedules)
    print("total good schedules:", len(list_of_good_schedules))
    print("number of copies deleted:", number_of_copies)

    return list_of_good_schedules

