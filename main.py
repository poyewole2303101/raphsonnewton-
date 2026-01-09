def newton_raphson(f, df, x0, tolerance=1e-6, max_iter=100):
    """
    Newton-Raphson method for finding roots of equations.
    """
    x = x0
    iterations = 0

    while iterations < max_iter:
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            raise ValueError("Derivative became zero. Method fails.")

        x_new = x - fx / dfx

        if abs(x_new - x) < tolerance:
            return x_new, iterations + 1

        x = x_new
        iterations += 1

    raise ValueError("Method did not converge within max iterations")


def main():
    print("Newton-Raphson Numerical Solver")
 
 print("--------------------------------")
    # User inputs equation
    equation = input("Enter f(x) (example: x**2 - 2): ")
    derivative = input("Enter f'(x) (example: 2*x): ")
    guess = float(input("Enter initial guess: "))

    # Convert string input to functions
    f = lambda x: eval(equation)
    df = lambda x: eval(derivative)

    try:
        root, steps = newton_raphson(f, df, guess)
        print(f"\nRoot found: {root}")
        print(f"Iterations: {steps}")
    except ValueError as e:
        print(f"\nError: {e}")


if _name_ == "_main_":
    main()
