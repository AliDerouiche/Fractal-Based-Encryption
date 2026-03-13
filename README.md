# Fractal-Based-Encryption
This project implements a simple encryption algorithm based on fractal mathematics, specifically the Sierpiński triangle.

## Concept

Fractals are mathematical structures characterized by self-similarity and fractional dimensions.  
The Sierpiński triangle can be generated using Pascal's triangle modulo 2.

In this project, the fractal pattern is used as a binary mask to encrypt data using XOR operations.

## Encryption Process

1. Convert plaintext into binary bits.
2. Arrange the bits into a square matrix.
3. Generate a Sierpiński fractal matrix.
4. Apply XOR between the data matrix and the fractal matrix.

## Decryption Process

Since XOR is symmetric, applying the same fractal mask again restores the original data.
