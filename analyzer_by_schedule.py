from analyzer import *
from schedule_gen import *
import matplotlib.pyplot as plt

schedules_to_make = 10000
number_of_players = 12
repeat_weeks = 2
season_length = 13

list_of_schedules = generate_schedules(schedules_to_make, number_of_players, repeat_weeks, season_length)

scores = get_scores()
player = 0

player_ranks = []
for schedule in list_of_schedules:

    #print(schedule)


    player_ranks.append(calculate_rank(player, schedule, scores, season_length, number_of_players))

    
# Make plot
plt.hist(player_ranks, normed=True, bins = 10)
plt.ylabel('Probability')
