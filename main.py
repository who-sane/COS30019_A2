import sys
from parser import parse_file
from truthTable import truth_table_method
from forwardChain import forward_chain_method
from backwardChain import backward_chain_method

#processes the arguments and dispatches to the appropriate inference method
def main():
    # verify that the user has provided exactly two command-line arguments:
    # the method to use (TT, FC, or BC) and the input filename
    if len(sys.argv) != 3:
        print("usage: inference engine method filename")
        sys.exit(1)
    
    # retrieve the method and filename from the command-line arguments
    selected_method = sys.argv[1].upper()  # case conversion (upper) to simplify comparison
    input_filename = sys.argv[2]
    
    # parse the input file to extract the knowledge base and query
    knowledge_base, query = parse_file(input_filename)
    
    # depending on the selected method, call the corresponding function
    if selected_method == "TT":
        truth_table_method(knowledge_base, query)
    elif selected_method == "FC":
        forward_chain_method(knowledge_base, query)
    elif selected_method == "BC":
        backward_chain_method(knowledge_base, query)
    else:
        # if the method specified does not match any of the expected ones, print an error message
        print("error: unknown method. please use 'TT' for truth table, 'FC' for forward chaining, or 'BC' for backward chaining.")
        sys.exit(1)

# if this module is run as the main program, execute the main function
if __name__ == "__main__":
    main()
