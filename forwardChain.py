from parser import extract_symbols

# parses the knowledge base to separate rules from facts
def parse_forward_chain_rules(knowledge_base):
    list_of_rules = []   
    list_of_facts = set() 
    
    # iterate over each clause in the knowledge base
    for clause in knowledge_base:
        # if the clause contains an implication, process it as a rule
        if "=>" in clause:
            premise_part, conclusion_part = clause.split("=>")
            # split premises if there are multiple conditions
            premises = [premise.strip() for premise in premise_part.split("&") if premise.strip()]
            conclusion = conclusion_part.strip()  # clean up the conclusion string
            list_of_rules.append((premises, conclusion))
        else:
            # if there is no implication, then it is fact
            list_of_facts.add(clause.strip())
    
    # return the separated rules and facts
    return list_of_rules, list_of_facts

# starts with known facts and then uses the rules to deduce new facts until the query is found
def forward_chain_method(knowledge_base, query):
    rules, facts = parse_forward_chain_rules(knowledge_base)
    
    # init a set to keep track of all deduced facts and a list to record the order of deduction
    deduced_facts = set()
    agenda_queue = []      # this list will act as our processing queue 
    deduction_order = []   # this list will record the order of deduced facts
    
    for fact in facts:
        if fact not in deduced_facts:
            deduced_facts.add(fact)
            agenda_queue.append(fact)
            deduction_order.append(fact)
    
    # create a dictionary to keep track of how many premises in each rule are not yet satisfied
    remaining_premises = {}
    for premises, conclusion in rules:
        remaining_premises[(tuple(premises), conclusion)] = len(premises)
    
    # processes the agenda until there are no more facts to check
    while agenda_queue:
        current_fact = agenda_queue.pop(0)
        
        # if the current fact is the query, we can output our result immediately
        if current_fact == query:
            print("YES: " + ", ".join(deduction_order))
            return
        
        # check each rule to see if the current fact is one of its premises
        for premises, conclusion in rules:
            if current_fact in premises:
                # decrement the count for this rule
                remaining_premises[(tuple(premises), conclusion)] -= 1
                # if all premises for this rule are satisfied and the conclusion hasn't been deduced yet
                if remaining_premises[(tuple(premises), conclusion)] == 0 and conclusion not in deduced_facts:
                    deduced_facts.add(conclusion)
                    agenda_queue.append(conclusion)
                    deduction_order.append(conclusion)
    
    # after processing, if the query has been deduced, output the order; otherwise, output NO
    if query in deduced_facts:
        print("YES: " + ", ".join(deduction_order))
    else:
        print("NO")
