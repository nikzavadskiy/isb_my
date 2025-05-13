from test_sequence import test_sequence

def main():
    # Test C++ generated sequence
    cpp_results = test_sequence("cpp_sequence.txt")
    print("C++ Sequence Results:")
    print(cpp_results)
    
    # Test Java generated sequence
    java_results = test_sequence("java_sequence.txt")
    print("\nJava Sequence Results:")
    print(java_results)

if __name__ == "__main__":
    main() 