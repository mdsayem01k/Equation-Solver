# Equation-Solver
The Equation Solver is a Python class designed to solve various types of mathematical equations, including quadratic, simultaneous linear, cubic, exponential, logarithmic, and trigonometric equations.

Features
Solves quadratic equations of the form 
�
�
2
+
�
�
+
�
=
0
ax 
2
 +bx+c=0.
Solves systems of two simultaneous linear equations with two variables.
Solves systems of three simultaneous linear equations with three variables.
Solves cubic polynomial equations of the form 
�
�
3
+
�
�
2
+
�
�
+
�
=
0
ax 
3
 +bx 
2
 +cx+d=0.
Solves exponential equations of the form 
�
�
=
�
a 
x
 =b.
Solves logarithmic equations of the form 
log
⁡
�
(
�
)
=
�
log 
a
​
 (x)=b.
Solves trigonometric equations of the form 
sin
⁡
(
�
)
=
value
sin(x)=value, 
cos
⁡
(
�
)
=
value
cos(x)=value, and 
tan
⁡
(
�
)
=
value
tan(x)=value.
Installation
No installation is required. Simply clone or download the EquationSolver.py file and import it into your Python project.

Usage
Import the EquationSolver class into your Python script:
python
Copy code
from EquationSolver import EquationSolver
Create an instance of the EquationSolver class:
python
Copy code
solver = EquationSolver()
Use the various methods of the EquationSolver class to solve equations. For example:
python
Copy code
# Solve a quadratic equation
solution = solver.quadratic(1, -3, 2)
print("Quadratic equation solution:", solution)

# Solve a system of two simultaneous linear equations
solution = solver.two_le_2_var(2, -1, 1, 1, 1, 3)
print("System of two simultaneous linear equations solution:", solution)

# Solve a system of three simultaneous linear equations
solution = solver.three_le_3_var(2, -1, 1, 1, 1, 3, 3, 2, 2, -1, 5, 5)
print("System of three simultaneous linear equations solution:", solution)

# Solve a cubic polynomial equation
solution = solver.solve_cubic_equation(1, -6, 11, -6)
print("Cubic polynomial equation solution:", solution)

# Solve an exponential equation
solution = solver.solve_exponential_equation(2, 8)
print("Exponential equation solution:", solution)

# Solve a logarithmic equation
solution = solver.solve_logarithmic_equation(2, 3)
print("Logarithmic equation solution:", solution)

# Solve a trigonometric equation
solution = solver.solve_trig_equation("sin(x) - 0.5", "x")
print("Trigonometric equation solution:", solution)
