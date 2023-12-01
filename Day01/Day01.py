"""  Problem statment Reworded

We will receive a list of calibration values.
These will have numbers in them
We want to combine the first and alst digit to form a number

What is the sum of all the calibration values

"""
import argparse
import os

def main():
    acc = 0
    with open("input.txt",'r') as file:
        for each_line in file:
            acc = acc + get_ints_from_cal(each_line)
    print(acc)
    
def get_ints_from_cal(cal_val):
    filtered_cal = [eval(i) for i in list(filter(filter_ints,cal_val))]
    combined = eval(str(filtered_cal[0]) + str(filtered_cal[-1]))
    return combined
      
    
    
def filter_ints(cal_val):
    ints = ["0","1","2","3","4","5","6","7","8","9"]
    return True if cal_val in ints else False
  
if __name__ == "__main__":
 
    main()