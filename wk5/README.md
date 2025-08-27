# 🐍 OOP Assignments in Python

This repository contains two Python programs demonstrating **Object-Oriented Programming (OOP)** concepts such as **classes, inheritance, encapsulation, and polymorphism**.

---

## 📌 Assignment 1: Smartphone Class (`assignment1.py`)

### Overview

In this program, we design a `Smartphone` class and extend it into specific smartphone brands (`Samsung` and `Iphone`).  
It demonstrates:

- **Inheritance** (`Samsung` and `Iphone` inherit from `Smartphone`)
- **Encapsulation** (private attribute `__mobilebanking` in `Samsung`)
- **Polymorphism** (different implementations of `use_whatsapp()` across brands)
- **Constructors** to initialize unique values

### Example Features

- Make calls and send messages
- Use Samsung’s **M-PESA mobile banking**
- Use Apple’s **Apple Pay**
- Both brands implement WhatsApp differently

### Sample Output

Calling 123-456-7890 from Samsung Galaxy S21...
Sending message to 123-456-7890 from Samsung Galaxy S21: Hello from Samsung!
Calling 098-765-4321 from Apple iPhone 13 Pro...
Sending message to 098-765-4321 from Apple iPhone 13 Pro: Greetings from iPhone!
Using Apple Pay on Apple iPhone 13 Pro.
Using WhatsApp (iOS version) on Apple iPhone 13 Pro.
Using mobile banking MPESA on Samsung Galaxy S21.
Using WhatsApp (Android version) on Samsung Galaxy S21.

---

## 📌 Activity 2: Polymorphism with Animals (`activity2.py`)

### Overview

This program demonstrates **polymorphism** using an `Animal` base class and multiple subclasses (`Dog`, `Bird`, and `Fish`).  
Each subclass defines the same method (`move()`) differently.

### Example Features

- Dogs run on all fours 🐕
- Birds fly in the sky 🕊️
- Fish swim in the water 🐠

### Sample Output

Buddy is a Dog.
Buddy is running on all fours 🐕
Tweety is a Bird.
Tweety is flying in the sky 🕊️
Nemo is a Fish.
Nemo is swimming in the water 🐠

---

## 🚀 How to Run

1. Clone this repository or download the `.py` files.
2. Run the programs:
   ```bash
   python assignment1.py
   python activity2.py
   ```

🧑‍💻 Concepts Covered

Classes & Objects

Constructors (**init**)

Inheritance

Encapsulation (private attributes)

Polymorphism (method overriding)

String Representation (**str**)
