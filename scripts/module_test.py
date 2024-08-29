import os
from expensive_statements_module import execute_expensive_statements

if __name__ == "__main__":
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'uploads/')
    execute_expensive_statements(path)