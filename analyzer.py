import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--player", type=int, help="number of player to simulate")
parser.add_argument("-s", "--schedule", type=int, help="number of player's schedule to simulate");
parser.add_argument("-l", "--list", help="displays player numbers and exits", action="store_true")

args = parser.parse_args()

if ((args.player or args.schedule) is None) and args.list is False:
    parser.error("Need to include --player and --schedule options")

if ((args.player or args.schedule) > 11 or (args.player or args.schedule)<0) and args.list is False:
    parser.error("--player and --schedule need to be between 0 and 11")

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

    print names_numbers
    sys.exit()

# make list of schedule
schedule0 = [4,6,7,8,10,1,5,3,2,9,11,4,6] # Chris
schedule1 = [11,5,3,2,9,0,4,6,7,8,10,11,5] # Todd
schedule2 = [7,8,10,1,5,3,11,9,0,4,6,7,8] # Andy
schedule3 = [8,10,1,5,11,2,9,0,4,6,7,8,10] # Greg
schedule4 = [0,11,6,7,8,10,1,5,3,2,9,0,11] # Aaron
schedule5 = [10,1,11,3,2,9,0,4,6,7,8,10,1] # Robert
schedule6 = [9,0,4,11,7,8,10,1,5,3,2,9,0] # Tyler
schedule7 = [2,9,0,4,6,11,8,10,1,5,3,2,9] # Stephen
schedule8 = [3,2,9,0,4,6,7,11,10,1,5,3,2] # Travis
schedule9 = [6,7,8,10,1,5,3,2,11,0,4,6,7] # Mark
schedule10 = [5,3,2,9,0,4,6,7,8,11,1,5,3] # Robert
schedule11 = [1,4,5,6,3,7,2,8,9,10,0,1,4] # Eric

schedules = [schedule0,schedule1,schedule2,schedule3,schedule4,schedule5,schedule6,schedule7,schedule8,schedule9,schedule10,schedule11]

# list of scores
score0 = [62.7,92.2,92.2,69.2,53.7,97.9,111.1,75.9,89.5,95.2,85,114.5,0]
score1 = [123.7,72.4,82,72.4,105.5,127.4,132.8,86.8,106.9,66.7,119.5,105,0]
score2 = [90.2,99,80.6,63,72.8,64.1,71.2,72.5,78.2,95,106.8,75.5,0]
score3 = [128.1,95.5,72.2,90.2,56.4,77.7,69,89.3,92.2,83.2,65.8,85.7,0]
score4 = [61.1,76.4,53.2,83.4,105.6,105.6,80.2,131.6,51.5,87.9,57.8,116.4,0]
score5 = [89,82.9,94.5,133.7,84.7,88.4,113.2,102.5,89.3,78.5,99.2,114.8,0]
score6 = [79.5,58.1,78.1,95.6,86.1,78.6,56.9,85.1,87.5,101,128.6,71.9,0]
score7 = [80.4,127.9,122.2,118.5,60.2,93.8,98.8,145.9,98.8,88.5,104.5,93.8,0]
score8 = [71,83.7,64.3,72.3,92.2,76.3,76.7,53.1,103.9,70.5,74,99.7,0]
score9 = [61,63,110.4,77.1,67.3,77.6,68.5,67.3,72.7,92.7,102.1,112.4,0]
score10 = [87.3,121.3,82.5,64.2,128.7,107.5,103.4,80.4,52.1,96,66.3,61.7,0]
score11 = [58.2,76.1,105.9,92.5,70.6,105.3,83.6,65,60.4,102.9,112.9,83.1,0]

scores = [score0,score1,score2,score3,score4,score5,score6,score7,score8,score9,score10,score11]

#print scores
    
# calculate win-loss

def winlosstie(a,b):
    diff = a-b
    if diff > 0.09:
        score = 1
    elif diff < -0.09:
        score = 0
    else:
        score = 0.5
    return score

week = 0
record = 0

print "You", "Opp", "W/L/T", "Record"
for a in schedules[args.schedule]:

    current_score = int(scores[args.player][week])
    opponent_score = int(scores[a][week])

    outcome = winlosstie(current_score, opponent_score)
    record = record + outcome
    print current_score, opponent_score, outcome, record
    week = week+1




