# Equation-Solver
The Equation Solver is a Python class designed to solve various types of mathematical equations, including quadratic, simultaneous linear, cubic, exponential, logarithmic, and trigonometric equations.

  ## Features

<span style="color:blue">quadratic(a, b, c):</span> Solves the quadratic equation ax^2 + bx + c = 0.

<span style="color:red">two_le_2_var(a1, b1, c1, a2, b2, c2):</span> Solves a system of two linear equations with two variables.

<span style="color:green">three_le_3_var(a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):</span> Solves a system of three linear equations with three variables.

<span style="color:purple">solve_cubic_equation(a, b, c, d):</span> Solves the cubic equation ax^3 + bx^2 + cx + d = 0.

<span style="color:orange">solve_exponential_equation(a, b):</span> Solves the exponential equation a^x = b.

<span style="color:navy">solve_logarithmic_equation(a, b):</span> Solves the logarithmic equation x = log_a(b).

<span style="color:darkorchid">solve_trig_equation(equation, variable):</span> Solves a trigonometric equation for the given variable.


## Installation
No installation is required. Simply clone or download the EquationSolver.py file and import it into your Python project.

## Usage
1. Import the EquationSolver class:
   ```python
   from EquationSolver import EquationSolver

2. Create an instance of the EquationSolver class:
   ```python
   solver = EquationSolver()
3. Use the desired method to solve the equation. The available methods are:
   *  quadratic(a, b, c): Solves the quadratic equation ax^2 + bx + c = 0.
   *  two_le_2_var(a1, b1, c1, a2, b2, c2): Solves a system of two linear equations with two variables.
   *  three_le_3_var(a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3): Solves a system of three linear equations with three variables.
   *  solve_cubic_equation(a, b, c, d): Solves the cubic equation ax^3 + bx^2 + cx + d = 0.
   *  solve_exponential_equation(a, b): Solves the exponential equation a^x = b.
   *  solve_logarithmic_equation(a, b): Solves the logarithmic equation x = log_a(b).
   *  solve_trig_equation(equation, variable): Solves a trigonometric equation for the given variable.
  
  For example, to solve the quadratic equation 2x^2 - 3x + 1 = 0, you can use the quadratic method:
  ```python
a, b, c = 2, -3, 1
roots = solver.quadratic(a, b, c)
print(f"Roots of the quadratic equation: {roots}")



```diff
- quadratic(a, b, c):
