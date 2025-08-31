# Simple C Projects

This repository contains a growing collection of simple C projects created as I learn and practice C programming. Each project is focused on one specific concept or use-case, such as file handling, arrays, conditionals, and menu-driven logic.

License: Free to use, modify, and share with credit.


---

##  Projects Included

### ✅ 1. Student Record Manager (C)
- Menu-driven program to add and view student records.
- Uses file handling to save data (`student.txt`).
- Covers: Loops, Conditionals, `fopen`, `fprintf`, `fscanf`, `fclose`.

### ✅ 2. Student Record Manager (Better Version) (C)
- Menu-driven program to add and view student details (name, class, percentage).
- Uses file handling to store data persistently in (`student.txt`).
- Covers: Loops, Conditionals, `fopen`, `fprintf`, `fscanf`, `fclose`.

####  What's Better in This Version
| Feature            | Advantage                           |
|--------------------|-------------------------------------|
| Data Storage       | Saves data permanently in a file    |
| Persistence        | Records remain after program exits  |
| Records Limit      | No limit (depends on file size)     |
| Extra Option       | Can view stored records anytime     |
| Practical Use      | Closer to real-world record systems |


### ✅ 3. Gambling Game (Python)
- Menu-driven program to bet on colors (red or black) with a starting balance.
- Uses the `random` module to generate a winning color each round.
- Covers: Loops, Functions, Conditionals, `random.choice`.

### ✅ 4. PC Components Store (Python)
- Interactive program to browse and purchase PC components.
- Features two pages of components with navigation and purchase options.
- Validates credit card and CVV input.
- Simulates payment processing with a loading effect.
- Covers: Loops, Functions, Input Validation, `time.sleep`.

####  Features
| Feature              | Advantage                              |
|----------------------|----------------------------------------|
| Multi-page Catalog   | View two pages of PC components        |
| Purchase Option      | Buy any component with validation      |
| Input Validation     | Ensures correct card details           |
| Payment Simulation   | Realistic loading effect               |
| Exit Anytime         | User-friendly navigation               |


### ✅ 5. Movie Database Manager (Python)
- menu-driven program to add, remove, view, and query movies in a mysql database.
- connects to a `movies` database and performs CRUD (create, read, update, delete) operations.
- covers: functions, loops, mysql connector, parameterized queries, database transactions.

#### key features
- add new movie records  
- remove movies by title  
- view all stored movies  
- run custom sql queries  
- secure database operations using parameterized queries


### ✅ 6. Gobta Multi-Tool Bot (Python)
- Menu-driven program that offers a timer, lottery game, and a student record saver.
- Combines file handling, countdown logic, and random number generation.
- Covers: Loops, Conditionals, `time.sleep`, `random.randint`, `open`, `input`.

more projects will be added as I explore new topics in C.

# ✅ 7. Student Database Program (Python)

A **menu-driven program** to create and manage a simple student database.  
The program allows storing student details in either a **text file** or a **binary file (using pickle)**.  
 Features
- Add student details:  
  - Name  
  - Class  
  - Subjects & Marks  
- Store data in:
  - **Text File (`txt.txt`)** → saves data in plain text format
  - **Binary File (`bin.bin`)** → saves data using Python's `pickle` module
- View all stored records after each entry
- Menu-driven loop to add multiple students until user exits


  
---

## 🛠️ How to Compile & Run

Use a C compiler like GCC:

```bash
gcc filename.c -o output
./output
