# parses the knowledge base similarly to forward chaining,
def parse_backward_chain_rules(knowledge_base):
    list_of_rules = []   # list to store rules (premises and conclusion)
    list_of_facts = set()  # set to store facts
    # separating the rules (implications) from the facts.
    for clause in knowledge_base:
        if "=>" in clause:
            premise_part, conclusion_part = clause.split("=>")
            premises = [premise.strip() for premise in premise_part.split("&") if premise.strip()]
            conclusion = conclusion_part.strip()
            list_of_rules.append((premises, conclusion))
        else:
            list_of_facts.add(clause.strip())
    return list_of_rules, list_of_facts

# rec helper function for backward chaining.
# prove query by checking known facts and recursively proving premises.
def bc_or(query, rules, facts, visited_set, proof_chain):
    # in the base base case: if the query is a known fact, add it to the proof chain and return True
    if query in facts:
        if query not in proof_chain:
            proof_chain.append(query)
        return True
    
    # if the query has already been visited in this recursive path, return False (avoids infinite loop)
    if query in visited_set:
        return False
    visited_set.add(query)
    
    # check  rules where the conclusion matches the query
    for premises, conclusion in rules:
        if conclusion == query:
            all_premises_valid = True
            temporary_proof_chain = []  # holds chain for the current rule if successful
            # try to prove each premise in the rule recursively
            for premise in premises:
                if not bc_or(premise, rules, facts, visited_set.copy(), temporary_proof_chain):
                    all_premises_valid = False
                    break
            # if all premises for the rule have been successfully proven, update the proof chain and return True
            if all_premises_valid:
                for symbol in temporary_proof_chain:
                    if symbol not in proof_chain:
                        proof_chain.append(symbol)
                if query not in proof_chain:
                    proof_chain.append(query)
                return True
    # if no rule can prove the query, return False
    return False

# implements the backward chaining algorithm.
# atte,pt to prove the query and prints the proof chain if successful.
def backward_chain_method(knowledge_base, query):
    # first, parse the knowledge base into rules and facts
    rules, facts = parse_backward_chain_rules(knowledge_base)
    
    # init an empty proof chain and a set for tracking visited symbols in the recursion
    overall_proof_chain = []
    visited_symbols = set()
    
    # attempt to prove the query using backward chaining
    if bc_or(query, rules, facts, visited_symbols, overall_proof_chain):
        print("YES: " + ", ".join(overall_proof_chain))
    else:
        print("NO")
