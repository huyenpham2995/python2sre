### Question
- Input: a file with asset info (Model# Created Assignee)
- Output:  sort the items by Model# and Created date, after that, add a new first column with distinct asset number started at 000001

### Thoughts
- The entries are sorted by model and created date, so the model should be the key and value would be the array of created date (in sorted order)
- Once we have done sorting the dictionary, each asset should be assign an id. the ID has 6 digits, so we need to format the string. example: first ID starts at 1, then format it to be 000001, ID 15 would be 000015. Basically create a format to take a number and return a string of 6 digit represents that number.
- Cnvert the Created date into datetime object for sorting, but later on have to convert back to string to write to output file. To avoid this converting back step, store both datetime converted string and original string.

### Pseudocode
1.  Create an assets dictionary to store each line information. The key will be model#, value is the list of [date in datetime object, original date time string, assignee].
2.  Open files and check for validity.
3.  Loop through all lines in file. For each line:\
    3.1.    First line is the header\
    3.2.    After that, split each line using space.\
    3.3.    Convert date string into datetime object. Append the array of [date in datetime object, original date time string, assignee] to the value of assets[model]
4.  Write to output file:\
    4.1.    Set the header of the output file first. Set num=1 (for asset ID).\
    4.2.    Sort the dictionary by key (model number). Loop through all items\
        4.2.1.  Sort the value of assets[model] by the 1st element of the value array (date in datetime format). Loop through each value\
            - Format the assetID string (a string of 6 character, contains the num).\
            - Append the asset ID + model# (key) + assets[model][1:] (skip the date in datetime, which is in index 0)\
            -   Join them with " " as delimeter and write it to output file.\
            -   Increment the ID number.

### BigO
- Looping through all lines of input file: O(N)
- Sort the dictionary by key (model): O(NlogN) (worst case scenario, there are N models, each model has 1 asset entry). The inner for loop will run 1 time.
- If there are K models (0 < K < N), then worst case a model has N-K assets. Sorting based on date time takes O((N-K)log(N-K)).
   - If K=1: O(Nlog(N-1) - log(N-1)) -> O(Nlog(N-1))
   - If K=N-1: O((N-N+1)log(N-N+1)) = O(log1)
=> O(NlogN)