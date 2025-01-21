package ydjs.sowon;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.time.format.TextStyle;
import java.util.Arrays;
import java.util.List;
import java.util.Locale;

public class DateManager {
    public static void main(String[] args) {
        // Example input date strings
        String[] dateInputs = {
            "1/6/2025",
            "1/9/2025",
            "1/11/2025",

            "01/18/25",  // MM/dd/yy
            "18-01-2025", // dd-MM-yyyy
            "01-07-2025",
            "2025/01/18",  // yyyy/MM/dd
            "2025-01-18",  // yyyy-MM-dd
            "18/01/2025",  // dd/MM/yyyy
            "01-18-2025",  // MM-dd-yyyy
            "01.18.2025",  // MM.dd.yyyy (uncommon format)
            "18.01.25"     // dd.MM.yy (uncommon format)
        };

        dateInputs = new String[] {
            "01.21.2025",
            "01.23.2025",
            "01.24.2025",
            "01.26.2025"
        };
        
        // Loop through each date input and attempt parsing
        for (String dateStr : dateInputs) {
            System.out.println("Input: " + dateStr);
            String dayOfWeek = getDayOfWeek(dateStr);
            if (dayOfWeek != null) {
                System.out.println("Day of the week: " + dayOfWeek);
            } else {
                System.out.println("Invalid date format.");
            }
        }
    }
    
    public static String getDayOfWeek(String dateStr) {
        // Preprocess the date string to normalize it
        String normalizedDateStr = normalizeDate(dateStr);
        // List of possible date formats
        List<String> patterns = Arrays.asList(
            "MM/dd/yy",    // MM/dd/yy (e.g., 01/18/25)
            "dd-MM-yyyy",  // dd-MM-yyyy (e.g., 18-01-2025)
            "yyyy/MM/dd",  // yyyy/MM/dd (e.g., 2025/01/18)
            "MM/dd/yyyy",  // MM/dd/yyyy (e.g., 01/18/2025)
            "yyyy-MM-dd",  // yyyy-MM-dd (e.g., 2025-01-18)
            "dd/MM/yyyy",  // dd/MM/yyyy (e.g., 18/01/2025)
            "MM-dd-yyyy",  // MM-dd-yyyy (e.g., 01-18-2025)
            "MM.dd.yyyy",  // MM.dd.yyyy (e.g., 01.18.2025)
            "dd.MM.yy"     // dd.MM.yy (e.g., 18.01.25)
        );
        
        for (String pattern : patterns) {
            try {
                DateTimeFormatter formatter = DateTimeFormatter.ofPattern(pattern);
                LocalDate date = LocalDate.parse(normalizedDateStr, formatter);
                // Return the day of the week in a user-friendly format
                return date.getDayOfWeek().getDisplayName(TextStyle.FULL, Locale.ENGLISH);
            } catch (DateTimeParseException e) {
                // Continue checking with the next pattern
            }
        }
        
        // If none of the formats matched, return null
        return null;
    }

    // Normalize the date string by adding leading zeroes to month and day if needed
    public static String normalizeDate(String dateStr) {
        String[] parts = dateStr.split("[/\\-.]"); // Split by common date separators
        if (parts.length >= 3) {
            // Ensure month and day are two digits
            parts[0] = parts[0].length() == 1 ? "0" + parts[0] : parts[0];
            parts[1] = parts[1].length() == 1 ? "0" + parts[1] : parts[1];
            // Rebuild the normalized date string
            return String.join(dateStr.contains("-") ? "-" : dateStr.contains(".") ? "." : "/", parts);
        }
        return dateStr; // Return as is if not enough parts
    }
}
