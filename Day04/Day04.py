import re
import itertools

games = []
filtered_games=[]


def main():
    with open("E:\AdventOfCode2023\Day04\input.txt",'r') as file:
        for each_line in file:
            a,cleaned_line = re.split(':', each_line.rstrip())
            cleaned_line =  re.split(' ', cleaned_line)
            condition = lambda x: x != '|'
            # takewhile = populate while conditions is true
            # dropwhile = put elements in to list while conition is true
            winning = list(itertools.takewhile(condition, cleaned_line))
            winning = [i for i in list(filter(lambda x: (x.isdigit()),winning))]
            pulled = list(itertools.dropwhile(condition, cleaned_line))[1:]
            pulled = [i for i in list(filter(lambda x: (x.isdigit()),pulled))]
            game = tuple((winning,pulled))
            games.append(game)
    for each_game in games:
        a_filtered_game = [i for i in list(filter(lambda x: (x in each_game[0]),each_game[1]))]
        if len(a_filtered_game) >= 1:
            filtered_games.append(a_filtered_game)

    points = 0
    for each_game in filtered_games:
        points = points + pow(2,(len(each_game)-1))
    print(points)
    
    
if __name__ == "__main__":
     main()