# Factory Method Pattern Explained Simply

The **Factory Method Pattern** is a design approach used to create objects without specifying the exact class of the object that will be created. Instead of directly calling a class constructor, you call a special method—called a factory method—that returns an instance of a class.

This pattern is useful when your program needs to decide which specific class to instantiate during runtime. It makes the code more flexible, easier to maintain, and simpler to extend in the future.

## How It Works

- There is an **abstract product** which defines the interface or blueprint for objects.
- Multiple **concrete products** implement this interface in different ways.
- A **factory** contains a method that creates and returns objects based on given input or conditions.
- The client code calls the factory method to get an object but does not need to know the exact class being instantiated.

## Benefits

- **Flexibility:** The client code can work with any product created by the factory without changing itself.
- **Encapsulation:** Object creation logic is hidden inside the factory.
- **Extensibility:** New product types can be added easily by creating new classes and updating the factory.

## Important Terms

- **Instantiate:** To create an actual object from a class.
- **Abstract class:** A class that serves as a template and cannot be created directly. It usually has methods that subclasses must implement.
- **Factory method:** A method responsible for creating and returning objects of a particular type.

## Example Use Case

Imagine you are developing a notification system that sends different types of notifications, such as **Email** and **SMS**. 

- You create an abstract product interface called **Notification** that defines a method `send`.
- You implement concrete products like **EmailNotification** and **SMSNotification**, each with its own way of sending messages.
- You design a factory class with a factory method that decides which notification object to create based on user preference or configuration.
- The client uses the factory method to get the right notification object and calls `send` without worrying about the underlying implementation.

This use case demonstrates how the Factory Method Pattern allows easy addition of new notification types in the future, without changing client code.
