import sympy as sym
import math
import numpy as np

class EquationSolver():


    def quadratic(self, a, b, c):
        discriminant = b**2 - 4*a*c

        if discriminant > 0:
            root1 = (-b + discriminant**0.5) / (2*a)
            root2 = (-b - discriminant**0.5) / (2*a)
            return root1, root2
        elif discriminant == 0:
            root = -b / (2*a)
            return root,
        else:
            real_part = -b / (2*a)
            imaginary_part = (-discriminant)**0.5 / (2*a)
            root1 = complex(real_part, imaginary_part)
            root2 = complex(real_part, -imaginary_part)
            return root1, root2

    def two_le_2_var(self, a1, b1, c1, a2, b2, c2):
        determinant = a1 * b2 - a2 * b1
        if determinant == 0:
            raise ValueError("The system of equations does not have a unique solution.")
    
        x = (c1 * b2 - c2 * b1) / determinant
        y = (a1 * c2 - a2 * c1) / determinant

        return x, y
    
    def three_le_3_var(self, a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):
        coeff_x1 = a1 * c2 - a2 * c1
        coeff_y1 = b1 * c2 - b2 * c1
        const1 = d1 * c2 - d2 * c1

        coeff_x2 = a3 * c1 - a1 * c3
        coeff_y2 = b3 * c1 - b1 * c3
        const2 = d3 * c1 - d1 * c3

        coeff_x = coeff_x1 * coeff_y2 - coeff_x2 * coeff_y1
        coeff_z = const1 * coeff_y2 - const2 * coeff_y1
        const = const2 * coeff_x1 - const1 * coeff_x2

        if coeff_x == 0 and coeff_z == 0:
            if const == 0:
                return (float('inf'), float('inf'), float('inf'))  # Infinite solutions
            else:
                return (None, None, None)  # No solution

        z = const / coeff_z
        y = (const1 - coeff_x1 * z) / coeff_y1
        x = (d1 - b1 * y - c1 * z) / a1

        return (x, y, z)
    
    def solve_cubic_equation(self, a, b, c, d):
        coefficients = [a, b, c, d]
        roots = np.roots(coefficients)
        return roots
    
    def solve_exponential_equation(self, a, b):
        if a <= 0 or a == 1:
            raise ValueError("Base 'a' must be a positive real number greater than 1.")
        if b <= 0:
            raise ValueError("Value 'b' must be a positive real number.")

        x = math.log(b, a)
        return x
    
    def solve_logarithmic_equation(self, a, b):
        if a <= 0 or a == 1:
            raise ValueError("Base 'a' must be a positive real number greater than 1.")

        x = a ** b
        return x
    
    def solve_trig_equation(self, equation, variable):
        x = sym.Symbol(variable)
        expr = sym.sympify(equation)
        solutions = sym.solveset(expr, x, domain=sym.Reals)
        solutions_list = list(solutions)
        return solutions_list
