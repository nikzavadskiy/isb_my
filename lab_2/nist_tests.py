import math
import scipy.special as sp

def frequency_test(sequence):
    n = len(sequence)
    ones = sequence.count('1')
    zeros = n - ones
    s_obs = abs(ones - zeros) / math.sqrt(n)
    p_value = sp.erfc(s_obs / math.sqrt(2))
    return p_value

def runs_test(sequence):
    n = len(sequence)
    ones = sequence.count('1')
    zeros = n - ones
    pi = ones / n
    tau = 2 / math.sqrt(n)
    if abs(pi - 0.5) >= tau:
        return 0.0
    vobs = 1
    for i in range(n - 1):
        if sequence[i] != sequence[i + 1]:
            vobs += 1
    p = 2 * pi * (1 - pi)
    mu = 1 + (n - 1) * p
    sigma = math.sqrt(2 * (n - 1) * p * (1 - p))
    z = (vobs - mu) / sigma
    p_value = sp.erfc(abs(z) / math.sqrt(2))
    return p_value

def compute_chi_square(sequence, block_size):
    n = len(sequence)
    num_blocks = n // block_size
    counts = [0] * (block_size + 1)
    for i in range(num_blocks):
        block = sequence[i * block_size:(i + 1) * block_size]
        max_run = 0
        current_run = 0
        for bit in block:
            if bit == '1':
                current_run += 1
                max_run = max(max_run, current_run)
            else:
                current_run = 0
        counts[max_run] += 1
    chi_square = 0
    for i in range(block_size + 1):
        expected = num_blocks * (1 - math.exp(-(i + 1) / 2))
        chi_square += (counts[i] - expected) ** 2 / expected
    return chi_square

def longest_run_ones_in_block(sequence, block_size=8):
    n = len(sequence)
    num_blocks = n // block_size
    
    theoretical_probs = {
        0: 0.2148,
        1: 0.3672,
        2: 0.2305,
        3: 0.1875
    }
    
    counts = {0: 0, 1: 0, 2: 0, 3: 0}
    
    for i in range(num_blocks):
        block = sequence[i * block_size:(i + 1) * block_size]
        max_run = 0
        current_run = 0
        
        for bit in block:
            if bit == '1':
                current_run += 1
                max_run = max(max_run, current_run)
            else:
                current_run = 0
        
        if max_run <= 1:
            counts[0] += 1
        elif max_run == 2:
            counts[1] += 1
        elif max_run == 3:
            counts[2] += 1
        else:
            counts[3] += 1
    
    chi_square = 0
    for i in range(4):
        expected = num_blocks * theoretical_probs[i]
        chi_square += (counts[i] - expected) ** 2 / expected
    
    p_value = sp.gammaincc(3/2, chi_square/2)
    
    return p_value 