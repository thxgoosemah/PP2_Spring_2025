from datetime import datetime

# Get the current datetime
current_datetime = datetime.now()

# Drop the microseconds
current_datetime_without_microseconds = current_datetime.replace(microsecond=0)

# Print the result
print(f"Current datetime without microseconds: {current_datetime_without_microseconds}")
