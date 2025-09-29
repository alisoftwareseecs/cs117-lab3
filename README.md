# Project Reflections

## 1. Assembly Reflections
- **Registers and Instructions:**  
  We noticed that registers are very limited in number and size, so we constantly had to manage which values go into which register. Instructions are also very low-level, handling only basic operations step by step.  
- **Difference from Python:**  
  Coding in Assembly requires thinking about every small detail, like memory access and data movement, whereas Python lets us focus on logic and results. Assembly feels “manual,” while Python feels more “automated” and high-level.

## 2. Python Reflections
- **Ease and Speed:**  
  Python is easier and faster for building the same project because it abstracts away memory management and provides built-in operations instead of writing multiple low-level instructions.  
- **Helpful Features for Abstraction:**  
  - **Variables** let us store values without worrying about registers.  
  - **Functions** allow us to reuse code instead of repeating instructions.  
  - **Loops** make iteration much simpler compared to manually jumping in Assembly.  

| **Feature**        | **Assembly Example** | **Python Example** | **Notes** |
|---------------------|----------------------|--------------------|-----------|
| **Variable storage** | `MOV EAX, 5`        | `x = 5`            | Assembly uses registers; Python uses variables in memory. |
| **Printing output** | `INT 21h`            | `print()`          | Assembly relies on system interrupts; Python has built-in functions. |
| **Arithmetic**      | `ADD AX, BX`         | `x + y`            | Assembly is step-by-step; Python is more abstract and simple. |
