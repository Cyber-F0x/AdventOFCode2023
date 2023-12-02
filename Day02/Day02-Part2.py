import re
from math import prod        

def main():
    acc = 0
    power_acc = 0 
    with open("E:\AdventOfCode2023\Day02\input.txt",'r') as file:
        for num,each_line in enumerate(file, 1):
            each_line = each_line.rstrip()
            cleaned_line = re.split('[:, ; ]', each_line)
            cleaned_line.pop(0)
            cleaned_line.pop(0)
            non_white_space = [ele for ele in cleaned_line if ele.strip()]
            l,c = list_split(non_white_space)
            pos, power = check_line(l,c)
            if pos:
                acc = acc + num
            power_acc = power_acc + power
        print(power_acc)
        
    
def check_line(ints,colours):
#    red = 12
#    blue = 14
#    green = 13
    maxes = {
        "red":1,
        "blue":1,
        "green":1
    }
    possible = True
    for dex, each_element in enumerate(ints, 0):
        if int(each_element) > maxes[colours[dex]]:
            maxes[colours[dex]] = int(each_element)
        if int(each_element) >= 15:
            possible = False
        # Advanced Checks
        if int(each_element) == 14 and colours[dex] != "blue":
            possible = False
        if int(each_element) == 13 and colours[dex] == "red":
            possible = False
    power = prod(maxes.values())
    return possible,power
                      
                      
    
def list_split(list):  
    return list[::2], list[1::2]


if __name__ == "__main__":
     main()