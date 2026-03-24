# City-number-mapper-V2
A Python program that maps numbers to city names with JSON-based persistent storage.
# city_number_mapper_V2

## 📌 Overview
city_number_mapper_V2 is a simple Python program that maps numbers to city names.  
Users can retrieve a city by entering its assigned number or register a new city if it does not exist.

---

## ⚙️ Features
- Retrieve city names using assigned numbers  
- Register new cities dynamically  
- Automatically assigns a unique number to each new city  
- Persistent storage using a JSON file  
- Data remains saved even after the program is closed  

---

## 🧠 How It Works
- The program stores city-number mappings in a dictionary  
- Data is saved in a file named `cities_mapping.json`  
- On startup, the program loads existing data from the file  
- If the file does not exist or is empty, it is created automatically  
- Any new data is saved when the program exits  

---

## ▶️ How to Run

1. Make sure Python is installed  
2. Download or clone this repository  
3. Run the script:

```bash
python city_number_mapper_V2.py

