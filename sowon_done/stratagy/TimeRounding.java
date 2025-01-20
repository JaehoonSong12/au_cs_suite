
package ydjs.sowon;


import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.Arrays;
import java.util.List;

public class TimeRounding {
    public static void main(String[] args) {
        // Example input string
        String inputTimeString = "6:36 p.m.";

        // Parse and round the time, with exception handling in each method
        LocalTime parsedTime = parseTime(inputTimeString);

        if (parsedTime != null) {
            LocalTime roundedNearest = roundToNearestHalfHour(parsedTime);
            LocalTime roundedDown = roundDownToHalfHour(parsedTime);
            LocalTime roundedUp = roundUpToHalfHour(parsedTime);

            // Output results
            System.out.println("Original time: " + parsedTime);
            System.out.println("Rounded to nearest: " + roundedNearest);
            System.out.println("Rounded down: " + roundedDown);
            System.out.println("Rounded up: " + roundedUp);
        }
    }

    // Parse time from a string with flexible formats
    public static LocalTime parseTime(String timeString) {
        List<String> formats = Arrays.asList(
            "h:mm a", "hh:mm a", "h:mm:ss a", "hh:mm:ss a", // Standard 12-hour formats
            "H:mm", "HH:mm", "H:mm:ss", "HH:mm:ss"          // 24-hour formats
        );

        timeString = timeString.toUpperCase().replace(".", "").trim();

        for (String format : formats) {
            try {
                DateTimeFormatter formatter = DateTimeFormatter.ofPattern(format);
                return LocalTime.parse(timeString, formatter);
            } catch (DateTimeParseException ignored) {
                // Try the next format
            }
        }

        System.err.println("Invalid time format: " + timeString);
        return null;
    }

    // Round the time to the nearest half hour
    public static LocalTime roundToNearestHalfHour(LocalTime time) {
        try {
            int totalMinutes = time.getHour() * 60 + time.getMinute();
            int roundedMinutes = ((totalMinutes + 15) / 30) * 30;
            return LocalTime.of((roundedMinutes / 60) % 24, roundedMinutes % 60);
        } catch (Exception e) {
            System.err.println("Error rounding to nearest half hour: " + e.getMessage());
            return null;
        }
    }

    // Round the time down to the nearest half hour
    public static LocalTime roundDownToHalfHour(LocalTime time) {
        try {
            int totalMinutes = time.getHour() * 60 + time.getMinute();
            int roundedMinutes = (totalMinutes / 30) * 30;
            return LocalTime.of((roundedMinutes / 60) % 24, roundedMinutes % 60);
        } catch (Exception e) {
            System.err.println("Error rounding down to half hour: " + e.getMessage());
            return null;
        }
    }

    // Round the time up to the nearest half hour
    public static LocalTime roundUpToHalfHour(LocalTime time) {
        try {
            int totalMinutes = time.getHour() * 60 + time.getMinute();
            int roundedMinutes = ((totalMinutes + 29) / 30) * 30;
            return LocalTime.of((roundedMinutes / 60) % 24, roundedMinutes % 60);
        } catch (Exception e) {
            System.err.println("Error rounding up to half hour: " + e.getMessage());
            return null;
        }
    }
}
