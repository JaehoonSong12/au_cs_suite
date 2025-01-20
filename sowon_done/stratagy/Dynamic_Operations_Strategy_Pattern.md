
# Dynamic Operations with the Strategy Pattern in Java

## 1. Strategy Interface
Define a `Strategy` interface with a method accepting two numbers and returning the result:
```java
interface Strategy {
    int performOperation(int a, int b);
}
```

---

## 2. Concrete Strategy Implementations
Create classes for specific operations, implementing the `Strategy` interface:
```java
class Addition implements Strategy {
    @Override
    public int performOperation(int a, int b) {
        return a + b;
    }
}

class Subtraction implements Strategy {
    @Override
    public int performOperation(int a, int b) {
        return a - b;
    }
}
```

---

## 3. Dynamic Class Loader
A utility method dynamically loads a class by name, verifies it implements `Strategy`, and returns an instance:
```java
public class StrategyLoader {
    public static Strategy loadStrategy(String className) {
        try {
            Class<?> clazz = Class.forName(className);
            if (Strategy.class.isAssignableFrom(clazz)) {
                return (Strategy) clazz.getDeclaredConstructor().newInstance();
            } else {
                System.out.println("Error: Class does not implement the Strategy interface.");
            }
        } catch (ClassNotFoundException e) {
            System.out.println("Error: Operation class not found.");
        } catch (Exception e) {
            System.out.println("Error: Failed to load the operation. " + e.getMessage());
        }
        return null;
    }
}
```

---

## 4. Main Method
Handle user input, load the strategy, and perform the operation:
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter operation name (e.g., Addition, Subtraction): ");
        String operationName = scanner.nextLine();

        Strategy strategy = StrategyLoader.loadStrategy(operationName);
        if (strategy != null) {
            System.out.print("Enter the first number: ");
            int a = scanner.nextInt();

            System.out.print("Enter the second number: ");
            int b = scanner.nextInt();

            int result = strategy.performOperation(a, b);
            System.out.println("Result: " + result);
        } else {
            System.out.println("Error: Could not execute the operation.");
        }

        scanner.close();
    }
}
```

---

## Key Features
- **Clean Separation**: `loadStrategy` encapsulates dynamic loading logic.
- **Dynamic Handling**: Classes are loaded dynamically based on user input.
- **Meaningful Operations**: Each operation accepts inputs and returns a result.

This design is extensible, clean, and reusable. You can add new operations (like multiplication) by creating additional `Strategy` implementations without changing existing code.
