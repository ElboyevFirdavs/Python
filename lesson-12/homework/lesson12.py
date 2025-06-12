1.
Threaded Prime Number Checker

import threading

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    primes = [num for num in range(start, end) if is_prime(num)]
    result.extend(primes)

def threaded_prime_checker(start, end, num_threads=4):
    threads = []
    result = []
    result_lock = threading.Lock()
    chunk_size = (end - start) // num_threads

    for i in range(num_threads):
        chunk_start = start + i * chunk_size
        chunk_end = start + (i + 1) * chunk_size if i != num_threads - 1 else end

        def worker(s=chunk_start, e=chunk_end):
            local_primes = []
            check_primes(s, e, local_primes)
            with result_lock:
                result.extend(local_primes)

        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return sorted(result)

# Test
if __name__ == "__main__":
    primes = threaded_prime_checker(1, 100, num_threads=4)
    print("Primes between 1 and 100:", primes)


2.
Threaded File Word Count

import threading
from collections import Counter

def process_lines(lines, word_counts, lock):
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(word.lower().strip(",.?!") for word in words)

    with lock:
        word_counts.update(local_counter)

def threaded_word_count(file_path, num_threads=4):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    chunk_size = len(lines) // num_threads
    threads = []
    word_counts = Counter()
    lock = threading.Lock()

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else len(lines)
        thread_lines = lines[start:end]
        t = threading.Thread(target=process_lines, args=(thread_lines, word_counts, lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return word_counts

# Test
if __name__ == "__main__":
    file_path = "sample.txt"  # Faylni oldindan yaratgan bo‘ling
    counts = threaded_word_count(file_path)
    for word, count in counts.most_common(10):
        print(f"{word}: {count}")
