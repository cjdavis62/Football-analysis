import sys
import argparse
import numpy as np

class player:
    record_of_records = []

    def __init__(self, player_real, player_pseudo, player_name):
        self.real = player_real
        self.pseudo = player_pseudo
        self.name = player_name

    def set_pseudo(self, new_pseudo):
        self.pseudo = new_pseudo

# initialize all the players with their default values
def get_players():
    
    Chris = player(0, 0, "Chris")
    Todd = player(1, 1, "Todd")
    Andy = player(2, 2, "Andy")
    Greg = player(3, 3, "Greg")
    Aaron = player(4, 4, "Aaron")
    Robert = player(5, 5, "Robert")
    Tyler = player(6, 6, "Tyler")
    Stephen = player(7, 7, "Stephen")
    Travis = player(8, 8, "Travis")
    Mark = player(9, 9, "Mark")
    Noel = player(10, 10, "Noel")
    Eric = player(11, 11, "Eric")

    array_of_players = np.array([Chris, Todd, Andy, Greg, Aaron, Robert, Tyler, Stephen, Travis, Mark, Noel, Eric])
    return array_of_players

# shuffle up the player's pseudo schedule
def shuffle_player_pseudo(array_of_players):

    shuffled_pseudo = np.random.permutation(12)
    return_array = np.empty_like(array_of_players)
    i = 0
    for player in array_of_players:
        player.set_pseudo(shuffled_pseudo[i])
        return_array[i] = player
        i = i + 1
    return return_array
        
# Calculate score for win/loss/tie. Win = 1, Loss = 0, Tie = 0.5
def win_loss_tie(scoreA, scoreB):
    if (scoreA > scoreB):
        return 1;
    if (scoreA < scoreB):
        return 0;
    else:
        return 0.5

# Grab the schedule from the text file
def get_schedule():
    return np.loadtxt("2018FantasySchedules.txt", dtype=int, delimiter="\t")

# Grab the scores from the text file
def get_scores():
    return np.loadtxt("2018FantasyScores.txt", dtype=float, delimiter="\t")

# Parse the arguments
def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--player", type=int, help="number of player to simulate", required=True)
    parser.add_argument("-l", "--list", help="displays player numbers and exits", action="store_true")

    args = parser.parse_args()

    if(args.list):
        names_numbers = ("Chris\t0\n"
                         "Todd\t1\n"
                         "Andy\t2\n"
                         "Greg\t3\n"
                         "Aaron\t4\n"
                         "Robert\t5\n"
                         "Tyler\t6\n"
                         "Stephen\t7\n"
                         "Travis\t8\n"
                         "Mark\t9\n"
                         "Noel\t10\n"
                         "Eric\t11")

        print(names_numbers)
        sys.exit()
    return args

# Get the scores for a player in a season
def get_player_scores(player, scores):
    return scores[:, player]

# Get the score for a player in a particular week
def get_player_week_score(player, week, scores):
    return scores[week, player]

def get_player_schedule(player, schedule):
    return schedule[:, player]

# Calculate the number of wins and losses for a player in a season
def calculate_schedule(player, schedule, scores, season_length):
    player_scores = get_player_scores(player, scores)
    player_schedule = get_player_schedule(player, schedule)
    
    record = 0
    for week in range(0, season_length):
        team_score = get_player_week_score(player, week, scores)
        opposing_player = player_schedule[week]
        opposing_score = get_player_week_score(opposing_player, week, scores)
        result = win_loss_tie(team_score, opposing_score)
        record = record + result
    return record


# See if player wins a tiebreaker against another player. True if player wins tiebreaker, False if they lose
def tiebreaker(player, some_player, scores):
    player_sum_score = sum(get_player_scores(player, scores))
    some_player_sum_score = sum(get_player_scores(some_player, scores))
    if (player_sum_score > some_player_sum_score):
        return True
    elif (player_sum_score < some_player_sum_score):
        return False
    else:
        print("Geez, tiebreakers can get pretty complicated, huh? Especially when two teams have both the same points for and record in a season.")
        sys.exit(1)

# Calculate rank of player based on wins and losses of their and other teams
def calculate_rank(player, schedule, scores, season_length, number_of_players):
    # Get the player's record
    player_record = calculate_schedule(player, schedule, scores, season_length)
    # Will calculate the record based on all the other players' scores
    # Initialize rank to 1
    rank = 1
    # Get the record of the other players
    for some_player in range (0, number_of_players):
        if (some_player == player):
            continue
        some_player_record = calculate_schedule(some_player, schedule, scores, season_length)
        if ((some_player_record - player_record) > 0.1 ):
            rank = rank + 1
        elif ((some_player_record - player_record) < -0.1):
            rank = rank
        else:
            if tiebreaker(player, some_player, scores):
                rank = rank
            else:
                rank = rank + 1
    return rank

def main():
     season_length = 13
     number_of_players = 12
     args = parse()
     schedule = get_schedule()
     scores = get_scores()

     print(calculate_rank(args.player, schedule, scores, season_length, number_of_players))

