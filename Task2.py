"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def longest_call_duration(calls):
    """Function that returns the index of maximum call duration """
    
    time_dict = {}    
    for i in range(len(calls)):
        call_duration = int(calls[i][-1])
        
        if calls[i][0] in time_dict:  # calling telephone number
            time_dict[calls[i][0]] += call_duration

        else:
            time_dict[calls[i][0]] = call_duration
 
        if calls[i][1] in time_dict:  # receiving telephone number
            time_dict[calls[i][1]] += call_duration 
                
        else: 
            time_dict[calls[i][1]] = call_duration
    
    phone_number = max(time_dict, key = time_dict.get)
    
    return phone_number, time_dict[phone_number] 
    
phone_num, duration = longest_call_duration(calls)
    
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone_num, duration))
