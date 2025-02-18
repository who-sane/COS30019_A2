# Inference Engine for Propositional Logic

## Overview

This project implements an inference engine for propositional logic that supports three distinct inference methods:

- **Truth Table (TT) Method**
- **Forward Chaining (FC) Method**
- **Backward Chaining (BC) Method**

The engine processes a knowledge base written in Horn clause form along with a query, and it determines whether the query is entailed by the knowledge base.

## Project Structure

- **parser.py**: Functions to read and parse input files.
- **truthTable.py**: Implementation of the Truth Table method.
- **forwardChain.py**: Implementation of the Forward Chaining method.
- **backwardChain.py**: Implementation of the Backward Chaining method.
- **main.py**: Main script to process command-line arguments and dispatch to the appropriate inference method.
- **test.py**: A test suite to evaluate performance and correctness by running various test cases.


## User Guide

This section provides a concise guide to using the inference engine.

1. **Prepare Your Input File**  
   - Create a text file following the specified format:
     - Begin with the keyword `TELL` on a new line.
     - List all knowledge base clauses separated by semicolons (`;`).
     - After the knowledge base, add the keyword `ASK` on a new line.
     - On the following line, specify the query.
   - **Example:**
     ```
     TELL
     a=>b; b&c=>d; a;
     ASK
     d
     ```

2. **Running the Engine**  
   - Open a terminal or command prompt.
   - Navigate to the project directory.
   - Run the engine using:
     ```
     python main.py <METHOD> <FILENAME>
     ```
     - `<METHOD>`: Choose one of `TT`, `FC`, or `BC`.
     - `<FILENAME>`: Provide the path to your input file.
   - **Example:**
     ```
     python main.py FC test_HornKB.txt
     ```

3. **Interpreting the Output**  
   - For the TT method, the output will be in the form:
     ```
     YES: <number of models>
     ```
     if the query is entailed, or `NO` if it is not.
   - For the FC and BC methods, the output will list the sequence of inferred symbols if the query is derived, or `NO` if the query cannot be inferred.
   
4. **Troubleshooting**  
   - Ensure your input file adheres to the required format.
   - Confirm that every rule in the knowledge base ends with a semicolon.
   - Verify that there are no extra spaces or missing keywords (`TELL`, `ASK`).
   - Check the terminal for any error messages that indicate parsing or runtime issues.
   
  ---

This project was developed as part of the COS30019 Intro to Artificial Intelligence assignment. We would like to acknowledge the following resources for their invaluable contributions:

