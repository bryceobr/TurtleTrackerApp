#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: John Fay (john.fay@duke.edu)
# Date:   Fall 2022
#----

# Ask the user for a date, specifying the format
user_date = input("Enter a date (M/D/YYYY):")

# # Copy and paste a line of data as the lineString variable value
# lineString = "20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0"

# # Use the split command to parse the items in lineString into a list object
# lineData = lineString.split()

# # Assign variables to specfic items in the list
# record_id = lineData[0]   # ARGOS tracking record ID
# obs_date = lineData[2]   # Observation date
# ob_lc = lineData[4]       # Observation Location Class
# obs_lat = lineData[6]     # Observation Latitude
# obs_lon = lineData[7]     # Observation Longitude

# # Print information to the use
# print (f"Record {record_id} indicates Sara was seen at {obs_lat}N, and {obs_lon}W on {obs_date}.")

# #exploring sara.txt in read mode
# fileObj = open('data/raw/sara.txt','r')
# print(fileObj.readline())
# print(fileObj.readlines())
# lineList = fileObj.readlines()
# print(lineList[0])
# fileObj.close()

# #writing to text files
# newFile = open('newfile.txt','w')
# newFile.write("Hello world\nIt's me")
# newFile.close()

# #appending text file
# open('newfile.txt','a').write("\nsee what I did here homie?")

#Create a variable pointing to the data file
file_name = 'data/raw/sara.txt'

#Create a file object from the file
file_object = open(file=file_name,mode='r')

#Read contents of file into a list
line_list = file_object.readlines()

#close the file object
file_object.close() 

#create dictionaries
date_dict = {}
location_dict = {}

#Extract one data line into a variable
for lineString in line_list:
    
    #check to see if the lineString is a data line
    if lineString[0] in ('#','u'):
        continue
    
    #Split the string into a list of data items
    lineData = lineString.split()
    
    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    #filter records based on location classification
    if obs_lc in ("1", "2", "3"):    
        #add items to the dictionary
        date_dict[record_id] = obs_date
        location_dict[record_id] = (obs_lat,obs_lon)

#testing script
#list(location_dict.keys())[0] 
#print (location_dict['20616'])
#print(date_dict['24719'])
print(len(location_dict))

#Create an empty key list
matching_keys = []

# Loop through all key, value pairs in the date_dictionary
for the_key, the_value in date_dict.items():
    #See if the date (the value) matches the user date
    if the_value == user_date:
        #print(the key,the_value)
        matching_keys.append(the_key)

#report whether no keys were found
if len(matching_keys) == 0:
    print(f"Sara was not located on {user date}")

#Reveal locations for each key in matching_keys
for matching_key in matching_keys:
    obs_lat, obs_lon = location_dict[matching_key]
    print(f"Record {matching_key} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {user_date}")
