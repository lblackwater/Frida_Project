#Task 1 

#First, create a list called paintings and add the following titles to it:

# The Two Fridas, My Dress Hangs Here, Tree of Hope, Self Portrait With Monkeys

paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']



# Task 2

# Next, create a second list called dates and give it the following values: 1939, 1933, 1946, 1940

dates = ['1939', '1933', '1946', '1940']



# Task 3

# It doesn't do much good to have the paintings without their dates, and vice versa. Zip together the two lists so that each painting is paired with its date and resave it to the paintings variable. Make sure to convert the zipped object into a list using the list() function. Print the results to the terminal to check your work.

paintings = list(zip(paintings, dates))
updatedpaintings = paintings


# Task 4
# There were some last minute additions to the show that we need to add to our list. Append the following paintings to our paintings list then re-print to check they were added correctly:

# 'The Broken Column', 1944
# 'The Wounded Deer', 1946
# 'Me and My Doll', 1937


updatedpaintings.append(('The Broken Column', 1944))
updatedpaintings.append(('The Wounded Deer', 1946))
updatedpaintings.append(('Me and My Doll', 1937))


print(list(paintings))

# Task 5
# Since each of these paintings is going to be in the audio tour, they each need a unique identification number. But before we assign them a number, we first need to check how many paintings there are in total.

# Find the length of the paintings list.

length_of_paintings = print(len(updatedpaintings))


# Task 6
# Use the range method to generate a list of identification numbers that starts at 1 and is equal in length to our list of items. Save the list to the variable audio_tour_number and check your work by printing the list.


audio_tour_number = list(range(1,8))
print(audio_tour_number)


# Task 7
# We're finally read to create our master list. Zip the audio_tour_number list to the paintings list and save it as master_list.

# Hint: Make sure to convert the zipped object into a list using the list() function.

master_list = list(zip(audio_tour_number, paintings))

# Task 8
# Print the master_list to the terminal.

print('This is a numbered list of the paintings that are currently held in the museum: ' + str(master_list))