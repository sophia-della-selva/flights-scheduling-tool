# Flight Information Program

This Python program allows users to interact with flight data stored in a CSV file. It provides multiple features for searching, analyzing, and exporting flight information.

## Files Included

- `flights.csv` – CSV file containing flight details including airline, flight number, departure time, arrival time, and price.  
- `flight_program.py` – Python program that implements all functionality.

## How to Run

1. Ensure both `flight_program.py` and `flights.csv` are in the same directory.  
2. Run the program using Python 3:

```bash
python flight_program.py
```

3. Follow the on-screen menu to select your desired option. The program will guide you through entering airline names, flight numbers, or times as needed.

## Features

- Search Flights: Find specific flights by airline and flight number.

- Filter by Duration: Find flights shorter than a maximum duration.

- Cheapest Flight: Identify the lowest-priced flight for a specific airline.

- Flights Departing After Time: Display flights departing after a user-specified time.

- Average Price: Calculate and display the average price of all flights.

- Sort Flights: Write a new CSV file with flights sorted by departure time.
  

## Output

The program may create an output file named `time-sorted-flights.csv` when exporting sorted flight data.


## Notes

Time inputs must be in HH:MM format (24-hour clock).

Prices in the CSV file should include a $ symbol, e.g., $350.

The program uses input validation to ensure users enter correct values for menu choices, times, and airline/flight numbers.
