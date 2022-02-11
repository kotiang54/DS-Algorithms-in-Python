"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def count_num_telephones(texts, calls):
    
    phone_records = []
    
    for i in range(len(texts)):  # append texts to phone_records list
        phone_records.append(texts[i][0])
        phone_records.append(texts[i][1])
        
    for i in range(len(calls)):   # append calls to phone_records list
        phone_records.append(calls[i][0])
        phone_records.append(calls[i][1])
        
        
    count = len(set(phone_records))
    return count

print("There are {} different telephone numbers in the records.".format(count_num_telephones(texts, calls)))
    
   
