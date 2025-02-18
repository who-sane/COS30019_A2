import itertools
from parser import extract_symbols

# eval a single clause given a truth assignment 
# maps each symbol to a boolean value (True or False)
def evaluate_clause(clause, model):
    # check if the clause contains an implication operator '=>'
    if "=>" in clause:
        # split the clause into the left-hand side (premises) and the right-hand side (conclusion)
        premise_string, conclusion_string = clause.split("=>")
        conclusion_symbol = conclusion_string.strip()  # remove whitespace
        
        # handle multiple premises by splitting them into a list
        premise_list = [premise.strip() for premise in premise_string.split("&")]
        
        # determine if all the premises are true under the current model
        all_premises_true = all(model[premise] for premise in premise_list)
        
        # an implication is true if either not all premises are true, or the conclusion is true
        # therefore, return true if either condition holds
        return (not all_premises_true) or model[conclusion_symbol]
    else:
        # return the truth value for that fact from the current model
        return model[clause.strip()]

# checks all possible truth assignments (models) for the given symbols
def truth_table_check(knowledge_base, query, symbols):
    total_models_where_kb_true = 0  # count models that satisfy the knowledge base
    total_models_where_query_true = 0  # count models that satisfy both the knowledge base and the query

    # iterate over every possible combination of truth values for the given symbols
    for truth_assignment in itertools.product([False, True], repeat=len(symbols)):
        # create a dictionary mapping each symbol to its truth value in the current assignment
        current_model = dict(zip(symbols, truth_assignment))
        
        knowledge_base_holds = all(evaluate_clause(clause, current_model) for clause in knowledge_base)
        
        # if the knowledge base is true in this model, update our counters
        if knowledge_base_holds:
            total_models_where_kb_true += 1
            # check if the query is also true under this model
            if current_model[query]:
                total_models_where_query_true += 1

    # query must be true in every model where the knowledge base is true
    query_entailed = (total_models_where_kb_true == total_models_where_query_true) and (total_models_where_kb_true > 0)
    return query_entailed, total_models_where_kb_true

# implements the truth table method for propositional logic inference
# extracts the symbols, checks all possible models, and then prints the result
def truth_table_method(knowledge_base, query):
    symbol_list = extract_symbols(knowledge_base, query)
    
    # perform the truth table check to see if the knowledge base entails the query
    query_is_entailed, model_count = truth_table_check(knowledge_base, query, symbol_list)
    
    # if the query is entailed, print YES followed by the number of models that satisfy the knowledge base
    if query_is_entailed:
        print("YES: " + str(model_count))
    else:
        print("NO")
