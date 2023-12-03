import re
from math import prod
ints = ["0","1","2","3","4","5","6","7","8","9"]
sums = []


def main():
    lines =[]
    symb_choords = []
    symbs = ['*']
    with open("E:\AdventOfCode2023\Day03\input.txt",'r') as file:
        for y, each_line in enumerate(file,0):
            for x, each_char in enumerate(each_line,0):
                if each_char in symbs:
                    symb_choords.append((y,x))
            lines.append(list(each_line.rstrip()))
    print(lines)
    acc = 0 
    for each_choord_pair in symb_choords:
        is_val_id_gear = []
        y = each_choord_pair[0]
        x = each_choord_pair[1]
        is_val_id_gear.extend(process_top(y,x,lines))
        is_val_id_gear.extend(process_mid(y,x,lines))
        is_val_id_gear.extend(process_bot(y,x,lines))
        if len(is_val_id_gear) == 2:
            acc = acc + prod(is_val_id_gear)
    print(acc)
    # print(lines)
    
        
      
            

def process_top(y,x,lines):
        vals = []
        if lines[y-1][x-1] == "."  and lines[y-1][x] == "."  and lines[y-1][x+1]== ".":
            #print("NOTHING IN TOP")
            return vals
        if lines[y-1][x-1] in ints  and lines[y-1][x] in ints  and lines[y-1][x+1]in ints:
            #print("Top Row: ", lines[y-1][x-1],lines[y-1][x],lines[y-1][x+1])
            vals.append(conjoin(list((lines[y-1][x-1],lines[y-1][x],lines[y-1][x+1]))))
            #lines[y-1][x-1],lines[y-1][x],lines[y-1][x+1] = ".",".","."
            return vals
        if lines[y-1][x] == ".":
            # 1.1
            if lines[y-1][x-1] in ints:
                # 1.
                #print("Top Row walk left: ",lines[y-1][x-3],lines[y-1][x-2],lines[y-1][x-1])
                vals.append(conjoin(list((lines[y-1][x-3],lines[y-1][x-2],lines[y-1][x-1]))))
                #lines[y-1][x-3],lines[y-1][x-2],lines[y-1][x-1] = ".",".","."
            if lines[y-1][x+1] in ints:
                #walk right
                # ..1
                #print("Top Row walk right: ",lines[y-1][x+1],lines[y-1][x+2],lines[y-1][x+3])
                vals.append(conjoin(list((lines[y-1][x+1],lines[y-1][x+2],lines[y-1][x+3]))))
                #lines[y-1][x+1],lines[y-1][x+2],lines[y-1][x+3] = ".",".","."
        else:
            if lines[y-1][x-1] in ints:
                # 11.
                #print("Top Row walk left: ",lines[y-1][x-2],lines[y-1][x-1],lines[y-1][x])
                vals.append(conjoin(list((lines[y-1][x-2],lines[y-1][x-1],lines[y-1][x]))))
                #lines[y-1][x-2],lines[y-1][x-1],lines[y-1][x]= ".",".","."
                
            if lines[y-1][x+1] in ints:
                #walk right
                # .11
                #print("Top Row walk right: ",lines[y-1][x],lines[y-1][x+1],lines[y-1][x+2])
                vals.append(conjoin(list((lines[y-1][x],lines[y-1][x+1],lines[y-1][x+2]))))
                #lines[y-1][x],lines[y-1][x+1],lines[y-1][x+2] = ".",".","."
                
        return vals
#532495


def process_mid(y,x,lines):
    vals = []
    if lines[y][x-1] == "." and lines[y][x+1] == ".":
            return vals
    if lines[y][x-1] in ints:
        #print(lines[y][x-3],lines[y][x-2],lines[y][x-1])
        vals.append(conjoin(list((lines[y][x-3],lines[y][x-2],lines[y][x-1]))))
        lines[y][x-3],lines[y][x-2],lines[y][x-1] = ".",".","."
        
    if lines[y][x+1] in ints:
        #print(lines[y][x+1],lines[y][x+2],lines[y][x+3])
        vals.append(conjoin(list((lines[y][x+1],lines[y][x+2],lines[y][x+3]))))
        lines[y][x+1],lines[y][x+2],lines[y][x+3]= ".",".","."
    return vals

def process_bot(y,x,lines):
    vals = []

    if lines[y+1][x-1] == "."  and lines[y+1][x] == "."  and lines[y+1][x+1]== ".":
        return vals
    if lines[y+1][x-1] in ints  and lines[y+1][x] in ints  and lines[y+1][x+1]in ints:
        vals.append(conjoin(list((lines[y+1][x-1],lines[y+1][x],lines[y+1][x+1]))))
        lines[y+1][x-1],lines[y+1][x],lines[y+1][x+1] = ".",".","."
        return vals
    if lines[y+1][x] == ".":
        # 1.1
        if lines[y+1][x-1] in ints:
            # 1.
            if lines[y+1][x-2].isdigit():
                vals.append(conjoin(list((lines[y+1][x-3],lines[y+1][x-2],lines[y+1][x-1]))))
                lines[y+1][x-3],lines[y+1][x-2],lines[y+1][x-1] = ".",".","."
            else:
                vals.append(conjoin(list(lines[y+1][x-1])))
                lines[y+1][x-1] = "."
         
            
        if lines[y+1][x+1] in ints:
            # ..1
            vals.append(conjoin(list((lines[y+1][x+1],lines[y+1][x+2],lines[y+1][x+3]))))
            lines[y+1][x+1],lines[y+1][x+2],lines[y+1][x+3] = ".",".","."
        return vals
    else:
        if lines[y+1][x-1] in ints:
            # 11.
            vals.append(conjoin(list((lines[y+1][x-2],lines[y+1][x-1],lines[y+1][x]))))
            lines[y+1][x-2],lines[y+1][x-1],lines[y+1][x] = ".",".","."
            
        if lines[y+1][x+1] in ints:
            #walk right
            # .11
            vals.append(conjoin(list((lines[y+1][x],lines[y+1][x+1],lines[y+1][x+2]))))
            lines[y+1][x],lines[y+1][x+1],lines[y+1][x+2] = ".",".","."
            
        return vals
    

def conjoin(line):
    filtered_string = [eval(i) for i in list(filter(filter_ints,line))]
    ret_val = ""
    for each_element in filtered_string:
        ret_val = ret_val + str(each_element)
    
    return eval(ret_val)
        
            
            
def filter_ints(cal_val):
    return cal_val.isdigit()

if __name__ == "__main__":
     main()