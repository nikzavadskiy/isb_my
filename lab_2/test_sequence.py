import argparse
import json
from nist_tests import frequency_test, runs_test, longest_run_ones_in_block

def test_sequence(filename):
    with open(filename, 'r') as f:
        sequence = f.read().strip()
    
    # Получаем p-значения
    freq_p = frequency_test(sequence)
    runs_p = runs_test(sequence)
    longest_p = longest_run_ones_in_block(sequence)
    
    # Форматируем результаты
    results = {
        "frequency_test_p_value": f"{freq_p:.6f}",
        "runs_test_p_value": f"{runs_p:.6f}",
        "longest_run_test_p_value": f"{longest_p:.6f}"
    }
    
    with open(f"{filename}_results.json", 'w') as f:
        json.dump(results, f, indent=4)
    
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Path to the file containing the bit sequence")
    args = parser.parse_args()
    test_sequence(args.filename) 