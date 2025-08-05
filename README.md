# Simple C Projects

This repository contains a growing collection of simple C projects created as I learn and practice C programming. Each project is focused on one specific concept or use-case, such as file handling, arrays, conditionals, and menu-driven logic.

License: Free to use, modify, and share with credit.


---

##  Projects Included

### ✅ 1. Student Record Manager
- Menu-driven program to add and view student records.
- Uses file handling to save data (`student.txt`).
- Covers: Loops, Conditionals, `fopen`, `fprintf`, `fscanf`, `fclose`.

### ✅ 2. Student Record Manager (Better Version)
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

More projects will be added as I explore new topics in C.

---

## 🛠️ How to Compile & Run

Use a C compiler like GCC:

```bash
gcc filename.c -o output
./output
