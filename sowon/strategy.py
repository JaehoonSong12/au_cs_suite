from datetime import datetime, timedelta

class TimeRounder:
    """
    Base class for time rounding strategies.
    Defines a method that subclasses should implement to round datetime objects.
    """
    def round(self, time: datetime) -> datetime:
        """
        Round the given time to a specific criterion.
        
        Parameters:
            time (datetime): The time to be rounded.
        
        Returns:
            datetime: The rounded time.
        """
        raise NotImplementedError("Subclasses must implement this method")

class NearestHalfHourRounder(TimeRounder):
    """
    Strategy for rounding time to the nearest half hour.
    """
    def round(self, time: datetime) -> datetime:
        """
        Round the given time to the nearest half hour.
        
        Parameters:
            time (datetime): The time to be rounded.
        
        Returns:
            datetime: Time rounded to the nearest half hour.
        """
        nearest = round(time.minute / 30) * 30
        return time.replace(minute=0, second=0, microsecond=0) + timedelta(minutes=nearest)

class DownHalfHourRounder(TimeRounder):
    """
    Strategy for rounding time down to the nearest half hour.
    """
    def round(self, time: datetime) -> datetime:
        """
        Round the given time down to the nearest half hour.
        
        Parameters:
            time (datetime): The time to be rounded.
        
        Returns:
            datetime: Time rounded down to the nearest half hour.
        """
        down = (time.minute // 30) * 30
        return time.replace(minute=down, second=0, microsecond=0)

class UpHalfHourRounder(TimeRounder):
    """
    Strategy for rounding time up to the nearest half hour.
    """
    def round(self, time: datetime) -> datetime:
        """
        Round the given time up to the nearest half hour.
        
        Parameters:
            time (datetime): The time to be rounded.
        
        Returns:
            datetime: Time rounded up to the nearest half hour.
        """
        up = ((time.minute + 29) // 30) * 30
        return time.replace(minute=0, second=0, microsecond=0) + timedelta(minutes=up)

def parse_time(time_string: str) -> datetime:
    """
    Parse a string into a datetime object using multiple time formats.
    
    Parameters:
        time_string (str): The time string to parse.
        
    Returns:
        datetime: The parsed datetime object.
        
    Raises:
        ValueError: If the time_string does not match any supported formats.
    """
    formats = ["%I:%M %p", "%H:%M", "%I:%M:%S %p", "%H:%M:%S"]
    for fmt in formats:
        try:
            return datetime.strptime(time_string.strip(), fmt)
        except ValueError:
            continue
    raise ValueError("Invalid time format")

def main():
    """
    Main function to demonstrate time rounding strategies with hardcoded examples.
    """
    time_examples = ["6:36 p.m.", "11:52 a.m.", "3:17 a.m.", "12:45 p.m."]
    
    for input_time_string in time_examples:
        print(f"\nProcessing time: {input_time_string}")
        try:
            parsed_time = parse_time(input_time_string)

            # Create instances of each rounding strategy
            nearest_half_hour = NearestHalfHourRounder()
            down_half_hour = DownHalfHourRounder()
            up_half_hour = UpHalfHourRounder()

            # Apply each strategy
            rounded_nearest = nearest_half_hour.round(parsed_time)
            rounded_down = down_half_hour.round(parsed_time)
            rounded_up = up_half_hour.round(parsed_time)

            # Output results
            print(f"Original time: {parsed_time.time()}")
            print(f"Rounded to nearest half hour: {rounded_nearest.time()}")
            print(f"Rounded down to half hour: {rounded_down.time()}")
            print(f"Rounded up to half hour: {rounded_up.time()}")
        except ValueError as e:
            print(str(e))

if __name__ == "__main__":
    main()
