from datetime import datetime, timedelta

class TimeRounder:
    """
    Base class for time rounding strategies.
    Implements parsing and defines a method that subclasses should implement to round datetime objects.
    """
    def process(self, time_string: str) -> datetime:
        """
        Parse the input time string and round it based on specific criteria.
        Parameters:
            time_string (str): The time string to parse and round.
        Returns:
            datetime: The parsed and rounded time.
        """
        parsed_time = self.parse_time(time_string)
        if parsed_time:
            return self.round(parsed_time)
        else:
            raise ValueError("Failed to parse time")

    def parse_time(self, time_string: str) -> datetime:
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


class NearestHourRounder(TimeRounder):
    """
    Strategy for rounding time to the nearest hour.
    """
    def round(self, time: datetime) -> datetime:
        """
        Round the given time to the nearest hour.
        Parameters:
            time (datetime): The time to be rounded.
        Returns:
            datetime: Time rounded to the nearest hour.
        """
        if time.minute >= 30:
            return time + timedelta(minutes=(60 - time.minute)) - timedelta(seconds=time.second, microseconds=time.microsecond)
        else:
            return time - timedelta(minutes=time.minute, seconds=time.second, microseconds=time.microsecond)

class DownHourRounder(TimeRounder):
    """
    Strategy for rounding time down to the nearest hour.
    """
    def round(self, time: datetime) -> datetime:
        """
        Round the given time down to the nearest hour.
        Parameters:
            time (datetime): The time to be rounded.
        Returns:
            datetime: Time rounded down to the nearest hour.
        """
        return time.replace(minute=0, second=0, microsecond=0)

class UpHourRounder(TimeRounder):
    """
    Strategy for rounding time up to the nearest hour.
    """
    def round(self, time: datetime) -> datetime:
        """
        Round the given time up to the nearest hour.
        Parameters:
            time (datetime): The time to be rounded.
        Returns:
            datetime: Time rounded up to the nearest hour.
        """
        return time.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)

def main():
    """
    Main function to demonstrate time rounding strategies with hardcoded examples.
    """
    # Hardcoded time examples
    time_examples = ["6:36 PM", "11:52 AM", "3:17 AM", "12:45 PM"]

    # Instances of each rounding strategy
    down_half_hour_rounder = DownHalfHourRounder()
    up_half_hour_rounder = UpHalfHourRounder()
    nearest_hour_rounder = NearestHourRounder()
    down_hour_rounder = DownHourRounder()
    up_hour_rounder = UpHourRounder()

    # Displaying results
    for time_string in time_examples:
        print(f"\nInput Time: {time_string}")
        try:
            nearest_half_hour_rounder = NearestHalfHourRounder()
            rounded_nearest_half_hour = nearest_half_hour_rounder.process(time_string)
            
            rounded_down_half_hour = down_half_hour_rounder.process(time_string)
            rounded_up_half_hour = up_half_hour_rounder.process(time_string)
            rounded_nearest_hour = nearest_hour_rounder.process(time_string)
            rounded_down_hour = down_hour_rounder.process(time_string)
            rounded_up_hour = up_hour_rounder.process(time_string)

            print(f"Rounded to Nearest Half Hour: {rounded_nearest_half_hour.time()}")
            print(f"Rounded Down to Half Hour: {rounded_down_half_hour.time()}")
            print(f"Rounded Up to Half Hour: {rounded_up_half_hour.time()}")
            print(f"Rounded to Nearest Hour: {rounded_nearest_hour.time()}")
            print(f"Rounded Down to Hour: {rounded_down_hour.time()}")
            print(f"Rounded Up to Hour: {rounded_up_hour.time()}")
        except ValueError as e:
            print(str(e))

if __name__ == "__main__":
    main()
