
# Function design:
# ---------------

# Function to open the data file and read data from the file
# Parameters: none
# Return dataFile
def openFile():

    # Track if a valid file has been opened
    goodFile = False

    # Loop until valid input is provided by user
    while goodFile == False:

        # Prompt the user to enter a file name
        fname = input("Please enter a file name: ")

        # Open the file with exception handling
        try:
            
            # Open the file and read it
            dataFile = open(fname, 'r')

            # GoodFile will be True if the file opens
            goodFile = True
            
        except IOError:
            # Inform user of invalid file and prompt user to try entering a valid input again
            print("Invalid file name try again ...")
            
        # Return the dataFile
    return dataFile

        
# Function to retrieve data from file and create separate lists
# Parameters: none
# Return airline_list, flight_num_list, departure_list, arrival_list, price_list
def getData():

    # Initialize empty lists to store data from file
    airline_list = []
    flight_num_list = []
    departure_list = []
    arrival_list = []
    price_list = []

    # Open the file
    dataFile = openFile()

    # Read each line of file
    for line in dataFile:
        
        # Skip the headers
        line = line.strip()

        # Split data
        airline, flightNum, departure, arrival, price = line.split(',')

        # Append data to empty lists
        airline_list.append(airline)
        flight_num_list.append(flightNum)
        departure_list.append(departure)
        arrival_list.append(arrival)

        # Convert the price to an integer
        intprice = int(price.strip('$'))
        
        # Append price to price list
        price_list.append(intprice)

        # Close the dataFile
    dataFile.close()

    # Return the lists
    return airline_list, flight_num_list, departure_list, arrival_list, price_list
        

# Function to display the menu and get user's choice
# Parameters: none
# Return userChoice
def getChoice():

    # Display the menu options
    print("\nPlease choose one of the following options: ")
    print("1 -- Find flight information by airline and flight number")
    print("2 -- Find flights shorter than a specified duration")
    print("3 -- Find the cheapest flight by a given airline")
    print("4 -- Find flight departing after a specified time")
    print("5 -- Find the average price of all flights")
    print("6 -- Write a file with flights sorted by departure time")
    print("7 -- Quit")

    # Prompt user for input while checking its validity
    userChoice = valid_input("Choice ==> ",1, 7)

    # Return the userChoice
    return userChoice
    

# Function to search for specific flights by airline and flight number
# Parameters: airline_list, flight_num_list, departure_list, arrival_list, price_list)
# Return i -- which is the index of the found flight. If not found, return -1
def flight_search(airline_list, flight_num_list, departure_list, arrival_list, price_list):

    # Print a blank line
    print("")
    
    # Get airline name from user
    airline_name = input("Enter airline name: ")

    # Validate user input
    while airline_name not in airline_list:

        # Display statement for invalid input
        print("Invalid input -- try again")

        # Allow user a retry 
        airline_name = input("Enter airline name: ")  

    # Get flight number from user
    flight_num = input("Enter flight number: ")

    # Validate user input
    while flight_num not in flight_num_list:

        # Display statement for invalid input
        print("Invalid input -- try again")

        # Allow user a retry
        flight_num = input("Enter flight number: ")
    
    # Loop through the airline_list for specific data
    for i in range(len(airline_list)):

        # Check if the flight index matches the airline and flight number
        if airline_list[i] == airline_name and flight_num_list[i] == flight_num:

            # if the index matches, return the index if found
            return i  
    
    # If no matches are found, inform user
    print("No flights meet your criteria")

     # Return -1 to indicate failure
    return -1 


# Function to convert time string to total minutes in "HH:MM" format
# Parameters: string
# Return int(total number of minutes)
def convert(string):

    # Create the ":" in the time statement
    hour, minute = string.split(':')

    # return the total time
    return int(minute) + 60 * int(hour)


# Function to calculate the duration of a flight in minutes (use arrival and departure time)
# Parameters: arrival and depart
# Return: flight duration calculation
def durations(arrival, depart):

    # return the flight duration calculation
    return convert(arrival) - convert(depart)


# Function to ensure input is a valid integer for a specific range
# Parameters: prompt, minVal, & maxVal
# Return userInput
def valid_input(prompt, minVal, maxVal):

    # Track if valid input has been received
    goodInput = False

    # Loop until valid input is provided by user
    while goodInput == False:
        try:
            
            # Prompt the user and try to convert input to int using exception handling
            userInput = int(input(prompt))

            # Check if input is in the specified range
            if userInput >= minVal and userInput <= maxVal:

                # If valid, end the loop 
                goodInput = True

            # Inform user that the input is out of range
            else:
                print("Entry must be between", minVal, "and", maxVal)

        # Handles if the input cannot be converted to an integer
        except ValueError:

            # Informs user that entry must be a number value
            print("Entry must be a number")

    # return userInput
    return userInput
    

# Function to find flights with duration shorter than the maximum specified
# Parameters: departure_list, arrival_list, airline_list, flight_num_list, price_list
# Return list of indices matching flights with durations shorter than specified maximum
def shorter_flights(departure_list, arrival_list, airline_list, flight_num_list, price_list):

    # Print New line
    print("")

    # Asks user for max duration in minutes, checking its within the range
    max_duration = valid_input("Enter maximum duration (in minutes): ", 0, 1000)

    # Initialize empty list for storing indices for matching flights
    matching_flights = []

    # Loop through all flights to calculate the durations
    for i in range(len(departure_list)):

        # Calcuate duration of current flight using the departure and arrival times
        duration = durations(arrival_list[i], departure_list[i])
        
        # If duration is less than or equal to specified max, store index
        if duration < max_duration:

            # Append the indices to the matching_flights list
            matching_flights.append(i)

    # Return list of indices of flights that meet the duration
    return matching_flights
    

# Function to find the cheapest flight for a specific airline based on its index
# Parameters: airline_list, flight_num_list, departure_list, arrival_list, price_list
# Return cheapest_index
def cheapest_flight(airline_list, flight_num_list, departure_list, arrival_list, price_list):

    # Asks the user to enter an airline name
    airline_name = input("\nEnter airline name: ")

    # Check if entered airline name is in the list by seeing if its not in it
    if airline_name not in airline_list:

        # If airline name is invalid, inform the user
        print("Invalid input -- try again")

        # Ask user to re-enter a name
        airline_name = input("\nEnter airline name: ")
        
    # Initialize cheapest price to first price in list
    cheapest_price = price_list[0]

    # Initialize the index of cheapest flight to 0 as a starting point
    cheapest_index = 0

    # Loop through all flights to get cheapest flight for specified airline
    for i in range(len(airline_list)):

        # Check if current flight's airline matches specified airline from user
        if airline_list[i] == airline_name:

            # If current flight price at index i is less than cheapest price found 
            if price_list[i] < cheapest_price:

                # Update cheapest price to match current flight's price
                cheapest_price = price_list[i]

                # Update the index of cheapest flight to current flight
                cheapest_index = i

    # Return index of cheapest flight for given airline
    return cheapest_index


# Function to convert user_time string in "HH:MM" to total minutes time format
# Parameters: user_time
# Return user_total_minutes
def convert_time(user_time):
    
    # Split input string to hours and minutes with a colon in between 
    user_hour,user_minute = user_time.split(':')

    # Convert hours to minutes and add minutes to find the total
    user_total_minutes = int(user_hour) * 60 + int(user_minute)

    # Return total minutes
    return user_total_minutes


# Function to ensure input is valid for "HH:MM" format
# Parameters: user_time
# Return user_time -- valid time string format
def valid_time(user_time):

    # Track if valid input was received
    goodInput = False

    # Loop until valid time input is given by user
    while goodInput == False:

        # Check if input is 5 characters long and has a colon
        if len(user_time) == 5 and (":") in user_time:
            
            try:
                # Split input into hours and minutes with colon in between
                hour, minute = user_time.split(':')

                # Check if hour is less than 24 and minute is less than 60
                if int(hour) < 24 and int(minute) < 60:

                    # Mark it as valid
                    goodInput = True

            # Handles the invalid input that cannot be split or converted to integer
            except ValueError:
                goodInput = False

        # If input is valid, ask user to try again
        if goodInput == False:
            user_time = input("Invalid time - Try again ")

    # Return the valid time string
    return user_time


# Function to get flights departing after time specified by user
# Parameters: departure_list, airline_list, flight_num_list, arrival_list, price_list
# Return List of indices for flights departing after the specified time
def departing_after_flights(departure_list, airline_list, flight_num_list, arrival_list, price_list):

    # Ask the user for earliest departure time (in hours and minutes)
    user_time = input("\nEnter earliest departure time: ")

    # Validate the user's time entered by calling the valid_time function created earlier
    user_time = valid_time(user_time)

    # Convert the validated time to total minutes 
    user_total_minutes = convert_time(user_time)

    # Initialize a list to store indices of matching flights
    matching_flights = []

    # Loop through the list of departure times
    for i in range(len(departure_list)):

        # Convert the flight's departure time to total minutes
        dep_total_minutes = convert_time(departure_list[i])

        # Check if flight's departure time is after or the same as specified time
        if dep_total_minutes >= user_total_minutes:

            # Append the flight's index to the matching_flights list if the previous condition occurs
            matching_flights.append(i)

    # Return list of indices of matching flights
    return matching_flights


# Function to calculate the average price of flights
# Parameters: price_list
# Return none
def average_price(price_list):

    # Initialize a variable to store the total price of all flights
    total_price = 0

    # Loop through the price_list to gather the total price
    for i in range(len(price_list)):

        # Add the price of all flights to the total_price
        total_price += price_list[i]

    # Calculate the average price by dividing the total_price by the number of flights
    average_price = total_price / len(price_list)

    # Display the average price with two decimal places
    print("\nThe average price is $ {:.2f}".format(average_price))


# Function to sort the indices of the departure times (selection sort)
# Parameters: departure_list
# Return convert_index
def selectionSort(departure_list):

    # Initialize emply list to store converted times
    theList = []

    # Loop through the departure_list and convert time into minutes
    for i in (range(len(departure_list))):
        n = convert(departure_list[i])

        # Append the converted time to theList
        theList.append(n)

    # Initialize an empty list to store the original indices from the converted times
    convert_index = []

    # Loop through theList
    for i in range(len(theList)):

        # Append the indicies to the convert_index
        convert_index.append(i)

    # Use the selection sort on theList to keep track of the indices    
    for i in range(0, len(theList)):            

        # Consider the current position has the smallest value
        minute = i

        # Loop through the rest of the unsorted list starting at the next position
        for j in range(i + 1, len(theList)):

            # Compare current element with smallest one found so far
            if theList[j] < theList[minute]:

                # Keep updating minute so it becomes the index of new smallest amount 
                minute = j
                
        # Switch the values in theList to sort from smallest to largest
        theList[i], theList[minute] = theList[minute], theList[i]

        # Switch the indicies in convert_index to keep the matching indices
        convert_index[i], convert_index[minute] = convert_index[minute], convert_index[i]
        
    # Return the list of indices that match the sorted times
    return convert_index


# Function to write the sorted flight data to a file
# Parameters: index_list, airline_list, flight_num_list, departure_list, arrival_list, price_list
# Return none but will be creating a file
def sorting_flights(index_list, airline_list, flight_num_list, departure_list, arrival_list, price_list):
    
    # Create the name of the output file
    outfname = "time-sorted-flights.csv"

    # Open output file in write mode
    outfile = open(outfname, 'w')

    # Loop through the list of flights in departure_list
    for i in range(len(departure_list)):

        # Write the flight details for each flight to the data file using the sorted index_list
        outfile.write(airline_list[index_list[i]] + ',' + flight_num_list[index_list[i]] + ',' + departure_list[index_list[i]] + ',' + arrival_list[index_list[i]] + ', $' + str(price_list[index_list[i]]) + '\n') 

    # Close the file 
    outfile.close()

    # Inform user that the sorted data has been written to the file
    print("\nSorted data has been written to file: ", outfname)


# Function to display flight details that match user's input
# Parameters: index, airline_list, flight_num_list, departure_list, arrival_list, price_list
# Return none
def printResults(index, airline_list, flight_num_list, departure_list, arrival_list, price_list):

    # Check if the index provided is valid
    if index != -1:

        # Print a blank line
        print("")

        # Inform user and dispaly the flight that matched their criteria
        print("The flight that meets your criteria is:")

        # Print a blank line
        print("")

        # Print section headers with proper spacing
        print("AIRLINE ".ljust(8), "FLT#".ljust(6), "DEPART".rjust(7), "ARRIVE".rjust(7), "PRICE".ljust(5))

        # Print the flight details in alignment with the headers
        print(airline_list[index].ljust(8), flight_num_list[index].ljust(6), 
              departure_list[index].rjust(7), arrival_list[index].rjust(7), 
              "$", str(price_list[index]).rjust(3))

    # Handles if no matching flights were found 
    else:
        # Print a blank line
        print("")

        # Informs user when input is invalid and to try again
        print("Invalid input -- try again.")


# Function to display multiple flights that match the criteria given
# Parameters: matching_flights, airline_list, flight_num_list, departure_list, arrival_list, price_list
# Return: none
def printResults_list(matching_flights, airline_list, flight_num_list, departure_list, arrival_list, price_list):

    # If no matching flights are found, inform the user 
    if len(matching_flights) == 0:
        print("\nNo flights meet your criteria")

    # If matching flights are found, inform the user and display the corresponding info
    else:

        # Print a blank line
        print("")

        # Print statement for flights meeting the criteria provided
        print("The flights that meet your criteria are:")

        # Print a blank line
        print("")

        # Print the flights' details in alignment with the headers
        print("AIRLINE ".ljust(8), "FLT#".ljust(6), "DEPART".rjust(7), "ARRIVE".rjust(7), "PRICE".ljust(5))

    # Loop through the matching flights to print details
    for i in matching_flights:

        # Print statement to display flights' details
        print(airline_list[i].ljust(8), flight_num_list[i].ljust(6), 
              departure_list[i].rjust(7), arrival_list[i].rjust(7), 
              "$", str(price_list[i]).rjust(3))


# Function that controls how the program behaves based on interactions
# Parameters: none
# Return none
def main():

    # Call the getData funtion to collect the flight data
    airline_list, flight_num_list, departure_list, arrival_list, price_list = getData()

    # Initialize user's choice at 0 to start looping
    userChoice = 0  

    # Run the loop until the user chooses to quit (option 7)
    while userChoice != 7:
        
        # Get user's choice by calling getChoice function
        userChoice = getChoice()  

        # Flight search by airline and flight number (option 1)
        if userChoice == 1:

            # Call the flight_search function & print the results
            index = flight_search(airline_list, flight_num_list, departure_list, arrival_list, price_list)
            printResults(index, airline_list, flight_num_list, departure_list, arrival_list, price_list)

        # Flights shorter than a specified duration (option 2)
        elif userChoice == 2:

            # Call the shorter_flights function & print the results
            matching_flights = shorter_flights(departure_list, arrival_list, airline_list, flight_num_list, price_list)
            printResults_list(matching_flights, airline_list, flight_num_list, departure_list, arrival_list, price_list)

        # Cheapest flight by an airline (option 3)
        elif userChoice == 3:

            # Call the cheapest_flight function & print the results
            cheapest_index = cheapest_flight(airline_list, flight_num_list, departure_list, arrival_list, price_list)
            printResults(cheapest_index, airline_list, flight_num_list, departure_list, arrival_list, price_list)

        # Flights departing after a specified time (option 4)
        elif userChoice == 4:

            # Call the departing_after_flights & print the results
            matching_flights = departing_after_flights(departure_list, airline_list, flight_num_list, arrival_list, price_list)
            printResults_list(matching_flights, airline_list, flight_num_list, departure_list, arrival_list, price_list)

        # Average price of all flights (option 5)
        elif userChoice == 5:

            # Call the average_price function
            average_price(price_list)
            
        # Flights sorted by departure time (option 6)
        elif userChoice == 6:

            # Call the selectionSort function and sorting_flights function
            index_list = selectionSort(departure_list)
            sorting_flights(index_list, airline_list, flight_num_list, departure_list, arrival_list, price_list)
            
         # Quit the program (option 7)
        elif userChoice == 7:

            # Print statement for when the program ends
            print("\nThank you for flying with us")

        # If the user's input is invalid, inform the user and prompt for them to try again
        else:
            print("Invalid choice. Please try again.")
