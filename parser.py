import re
import sys

# reads the input file provided by the user and extracts the knowledge base and the query
# open the file in read mode and store in var
def parse_file(filename):
    try:
        with open(filename, 'r') as input_file:
            file_content = input_file.read()
    except IOError:
        print("error: could not open file " + filename)
        sys.exit(1)
    
    # split the file content into separate lines and remove any empty lines
    all_lines = [line.strip() for line in file_content.splitlines() if line.strip()]
    
    # locate the 'TELL' and 'ASK' sections in the file to delimit the knowledge base and query
    try:
        tell_section_index = all_lines.index("TELL")
        ask_section_index = all_lines.index("ASK")
    except ValueError:
        print("error: input file must contain both 'TELL' and 'ASK' markers")
        sys.exit(1)
    
    # the lines between 'TELL' and 'ASK' contain the knowledge base information
    knowledge_base_text = " ".join(all_lines[tell_section_index + 1 : ask_section_index])
    
    knowledge_base = [clause.strip() for clause in knowledge_base_text.split(';') if clause.strip()]
    
    if ask_section_index + 1 < len(all_lines):
        query = all_lines[ask_section_index + 1].strip()
    else:
        print("error: there is no query specified after 'ASK'")
        sys.exit(1)
    
    # return the parsed knowledge base and query as a tuple
    return knowledge_base, query

# extracts all unique proposition symbols from the knowledge base and the query
def extract_symbols(knowledge_base, query):
    symbol_set = set()
    # regular expression pattern to match symbols (alphanumeric words)
    symbol_pattern = re.compile(r'\b[A-Za-z0-9]+\b')
    
    # process each clause in the knowledge base
    for clause in knowledge_base:
        found_symbols = symbol_pattern.findall(clause)
        symbol_set.update(found_symbols)
    
    # make sure that the query is also included in the set of symbols
    symbol_set.add(query)
    
    # return a sorted list of symbols for consistency in further processing
    return sorted(symbol_set)
