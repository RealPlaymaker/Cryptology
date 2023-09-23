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

# Define the two polynomials and the reducible polynomial as lists of coefficients
polynomial1 = [0, 1, 0, 0, 1, 0, 0, 0]  # x^5 + x^2 + x
polynomial2 = [0, 1, 1, 1, 0, 1, 0, 0]  # x^4 + x^3 + x^2 + x
reducible_polynomial = [1, 0, 0, 0, 1, 1, 0, 1, 1]  # x^8 + x^4 + x^3 + x + 1

# Multiply the two polynomials modulo the reducible polynomial
multiply_polynomials(polynomial1, polynomial2, reducible_polynomial)
