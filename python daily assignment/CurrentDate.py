from datetime import datetime
import pytz  # pytz module for time zone information

# Get the current date and time
current_datetime = datetime.now(pytz.timezone('Asia/Kolkata'))  # Adjust time zone based on your requirement

# Format the date and time as per the specified format
formatted_date = current_datetime.strftime("%a %b %d %H:%M:%S %Z %Y")

# Print the formatted date
print("Current Date:", formatted_date)


