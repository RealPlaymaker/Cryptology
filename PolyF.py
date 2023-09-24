def multiply_polynomials(polynomial1, polynomial2, reducible_polynomial):
    max_degree = len(reducible_polynomial) - 1
    result = [0] * (max_degree * 2 + 1)

    # Perform polynomial multiplication
    for i in range(len(polynomial1)):
        for j in range(len(polynomial2)):
            result[i + j] ^= polynomial1[i] & polynomial2[j]

    # Reduce the result modulo the reducible polynomial
    while True:
        leading_term = next((i for i, coeff in enumerate(result) if coeff == 1), None)

        if leading_term is None or leading_term < max_degree:
            break  # No more terms to reduce

        # Perform polynomial division by XORing the result and the reducible polynomial shifted to the left
        for i in range(len(reducible_polynomial)):
            result[leading_term - max_degree + i] ^= reducible_polynomial[i]

    # Print the result
    print("Result:", result[:max_degree + 1])
    
# Input the coefficients of polynomial1 as a space-separated string
input_polynomial1 = input("Enter the coefficients of polynomial1 (e.g., 1 0 1 for x^2 + 1): ").split()
polynomial1 = [int(coeff) for coeff in input_polynomial1]

# Input the coefficients of polynomial2 as a space-separated string
input_polynomial2 = input("Enter the coefficients of polynomial2 (e.g., 1 0 1 for x^2 + 1): ").split()
polynomial2 = [int(coeff) for coeff in input_polynomial2]

# Input the coefficients of the reducible polynomial as a space-separated string
input_reducible_polynomial = input("Enter the coefficients of the reducible polynomial: ").split()
reducible_polynomial = [int(coeff) for coeff in input_reducible_polynomial]

# Multiply the two polynomials modulo the reducible polynomial
result = multiply_polynomials(polynomial1, polynomial2, reducible_polynomial)