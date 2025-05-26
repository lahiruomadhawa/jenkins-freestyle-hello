
import sys

# This is a sample .py file for testing pipeline
def print_hello(name):
    print("="*30)
    print("Hello from python,", name)
    print("="*30)


name = sys.argv[1] if len(sys.argv) > 1 else "World"
print_hello(name)