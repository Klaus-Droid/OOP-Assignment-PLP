📱 OOP Smartphones & Polymorphism
📖 Overview

This project demonstrates Object-Oriented Programming (OOP) concepts in Python by designing a class hierarchy for smartphones.
It covers:

✅ Classes & Constructors

✅ Encapsulation (private attributes with getters/setters)

✅ Inheritance (specialized smartphone models)

✅ Polymorphism (same method behaves differently in each subclass)

🏗️ Features

Smartphone (Base Class):
Stores brand, model, and battery life.
Allows charging and checking battery status.
Default action() → making a call.
SmartphonePro (Subclass):
Inherits from Smartphone.
Adds a stylus feature.
Overrides action() → taking a high-resolution photo.

GamingPhone (Subclass):

Inherits from Smartphone.
Adds a cooling system attribute.
Overrides action() → playing a game.

🎭 Polymorphism in Action

All smartphones share the same method action(), but each executes it differently:
Smartphone.action() → "Making a call 📞"
SmartphonePro.action() → "Taking a high-res photo 📸"
GamingPhone.action() → "Playing a game 🎮"

🚀 How to Run

Clone this repository or copy the code.
Save it in a file named smartphones.py.

Run with:

python smartphones.py

🖥️ Example Output
Galaxy S22 is making a call 📞
iPhone 15 Pro is taking a high-res photo 📸
Infinix Hot 50 is playing a game 🎮
80% battery remaining
Using stylus 🖊️
Charged! Now at 90% 🔋

📚 Concepts Covered

Encapsulation: _Smartphone__battery is private.

Inheritance: SmartphonePro and GamingPhone extend Smartphone.

Polymorphism: action() behaves differently depending on the object.
