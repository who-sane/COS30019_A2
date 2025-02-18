import time
import subprocess
import os

# run the inference engine for a given method and test file then return output and runtime
def run_inference(method, test_file):
    start = time.time()
    # call the main program with the specified method and test file
    result = subprocess.run(["python", "main.py", method, test_file],
                            capture_output=True, text=True)
    runtime = time.time() - start
    return result.stdout.strip(), runtime

# create a test file with the given filename and content
def create_test_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)

# define a couple of test cases
test_cases = [
    ("simple_kb", 
     "TELL\n"
     "a; b; a=>c; c=>d;\n"
     "ASK\n"
     "d\n"),
    ("circular_kb", 
     "TELL\n"
     "a=>b; b=>c; c=>a; a;\n"
     "ASK\n"
     "c\n")
]

methods = ["TT", "FC", "BC"]

# run each test case using each inference method and print the results
for test_name, content in test_cases:
    filename = f"{test_name}.txt"
    create_test_file(filename, content)
    print(f"Test Case: {test_name}")
    for method in methods:
        output, runtime = run_inference(method, filename)
        print(f"  Method: {method} | Runtime: {runtime:.4f} sec | Output: {output}")
    print("-" * 40)
    os.remove(filename)
