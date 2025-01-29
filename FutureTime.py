# FutureTime.py
# Name: Mason Rodgers
# Date: 1/29/25
# Assignment: Future Time

# datetime will allow us to access the system date and time.
import datetime

def main():
  print("Future Time Calculator")

  # Getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 24
  currentMinute = (now.minute)  

  # Ask user for input
  moreHours = int(input("Enter hours to add: "))  
  moreMins = int(input("Enter minutes to add: ")) 

  # Calculate new time
  futureMinutes = (currentMinute + moreMins) % 60
  extraHours = (currentMinute + moreMins) // 60
  futureHours = (currentHour + moreHours + extraHours) % 24

  # Print results
  print(extraHours)  
  print(futureMinutes)  
  print("Future Time: " + str(futureHours) + ":" + str(futureMinutes))

# Call the main function
if __name__ == '__main__':
  main()
