"""  Problem statment Reworded

We will receive a list of calibration values.
These will have numbers in them
We want to combine the first and alst digit to form a number

What is the sum of all the calibration values

"""

ints = ["0","1","2","3","4","5","6","7","8","9"]

mapping = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"    
}


def main():
    acc = 0
    with open("input.txt",'r') as file:
        for each_line in file:
            acc = acc + get_ints_from_cal(each_line.lower().rstrip())
    print(acc)
    
    
def get_ints_from_cal(cal_val):
    first = None
    last = None
    # Easy checks first
    if cal_val[0] in ints :
        first = cal_val[0]
    if cal_val[-1] in ints :
        last = cal_val[-1]
    # Otherwise put effort in    
    indexes = []
    for each_key in mapping:
        if each_key in cal_val:
            indexes.append((cal_val.index(each_key),mapping[each_key]))
            indexes.append((cal_val.rindex(each_key),mapping[each_key]))
    filtered_cal = [i for i in list(filter(filter_ints,cal_val))]    
    for each_int in filtered_cal:
        indexes.append((cal_val.index(each_int),each_int))
        indexes.append((cal_val.rindex(each_int),each_int))
    indexes = sorted(indexes)
    if first == None:
        first = indexes[0][1]
    if last == None:
        last = indexes[-1][1]
    combined = first + last
    return int(combined)
 
     
def filter_ints(cal_val):
    return True if cal_val in ints else False
  
  
if __name__ == "__main__":
     main()