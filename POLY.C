#include <stdio.h>

// Define the maximum degree for the polynomials
#define MAX_DEGREE 8

// Function to multiply two polynomials modulo a reducible polynomial
void multiply_polynomials(int polynomial1[MAX_DEGREE + 1], int polynomial2[MAX_DEGREE + 1], int reducible_polynomial[MAX_DEGREE + 1]) {
    int result[MAX_DEGREE * 2 + 1] = {0};

    // Perform polynomial multiplication
    for (int i = 0; i <= MAX_DEGREE; i++) {
        for (int j = 0; j <= MAX_DEGREE; j++) {
            result[i + j] ^= polynomial1[i] & polynomial2[j];
        }
    }

    // Reduce the result modulo the reducible polynomial
    while (1) {
        int leading_term = -1;

        // Find the leading term
        for (int i = 0; i <= MAX_DEGREE * 2; i++) {
            if (result[i] == 1) {
                leading_term = i;
                break;
            }
        }

        if (leading_term == -1 || leading_term < MAX_DEGREE) {
            break;  // No more terms to reduce
        }

        // Perform polynomial division by XORing the result and the reducible polynomial shifted to the left
        for (int i = 0; i <= MAX_DEGREE; i++) {
            result[leading_term - MAX_DEGREE + i] ^= reducible_polynomial[i];
        }
    }

    // Print the result
    printf("Result: ");
    for (int i = MAX_DEGREE; i >= 0; i--) {
        printf("%d ", result[i]);
    }
    printf("\n");
}

int main() {
    // Define the two polynomials and the reducible polynomial as arrays of coefficients
    int polynomial1[MAX_DEGREE + 1] = {0, 1, 0, 0, 1, 0, 0, 0};  // x^5 + x^2 + x
    int polynomial2[MAX_DEGREE + 1] = {0, 1, 1, 1, 0, 1, 0, 0};  // x^4 + x^3 + x^2 + x
    int reducible_polynomial[MAX_DEGREE + 1] = {1, 0, 0, 0, 1, 1, 0, 1, 1};  // x^8 + x^4 + x^3 + x + 1

    // Multiply the two polynomials modulo the reducible polynomial
    multiply_polynomials(polynomial1, polynomial2, reducible_polynomial);

    return 0;
}
