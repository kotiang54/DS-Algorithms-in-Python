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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def telemarketers(calls, texts):
    """Function to identify a list of possible telemarketers"""
    
    outgoing_calls = []
    in_calls_texts = []  # list of incoming calls and all texts contacts
    
    for i in range(len(calls)): 
        outgoing_calls.append(calls[i][0]) # append calling contacts
        in_calls_texts.append(calls[i][1])  # append receiving contacts 
        
    for i in range(len(texts)): # append texts contacts
        in_calls_texts.append(texts[i][0])
        in_calls_texts.append(texts[i][1])
           
    telemarketers_list = []
    
    for num in range(len(outgoing_calls)):
        if outgoing_calls[num] not in in_calls_texts:
            if outgoing_calls[num] not in telemarketers_list:
                telemarketers_list.append(outgoing_calls[num])
            
    telemarketers_list.sort()
    
    return telemarketers_list
        
         
phone_records = telemarketers(calls, texts)    
print("These numbers could be telemarketers: ")

for item in phone_records:
    print(item)
