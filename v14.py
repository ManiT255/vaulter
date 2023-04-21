#WIP
import itertools
import random
import string
import timeit

import numpy as np

allowed_chars = string.ascii_lowercase + " "

# read vault.o contents
with open('vault.o', 'rb') as f:
    vault_contents = f.read()

def check_password(guess):
    # test guess against the contents of vault.o
    return guess.encode('ascii') in vault_contents

def random_str(size):
    return ''.join(random.choices(allowed_chars, k=size))

def crack_length(max_len=32, verbose=False) -> int:
    trials = 2000
    times = np.empty(max_len)
    for i in range(max_len):
        i_time = timeit.repeat(stmt='check_password(x)',
                               setup=f'x=random_str({i!r})',
                               globals=globals(),
                               number=trials,
                               repeat=10)
        times[i] = min(i_time)

    if verbose:
        most_likely_n = np.argsort(times)[::-1][:5]
        print(most_likely_n, times[most_likely_n] / times[most_likely_n[0]])

    most_likely = int(np.argmax(times))
    return most_likely

def crack_password(length, verbose=False):
    guess = random_str(length)
    counter = itertools.count()
    trials = 1000
    while True:
        i = next(counter) % length
        for c in allowed_chars:
            alt = guess[:i] + c + guess[i + 1:]

            alt_time = timeit.repeat(stmt='check_password(x)',
                                     setup=f'x={alt!r}',
                                     globals=globals(),
                                     number=trials,
                                     repeat=10)
            guess_time = timeit.repeat(stmt='check_password(x)',
                                       setup=f'x={guess!r}',
                                       globals=globals(),
                                       number=trials,
                                       repeat=10)

            if check_password(alt):
                return alt

            if min(alt_time) > min(guess_time):
                guess = alt
                if verbose:
                    print(guess)


def main():
    length = crack_length(verbose=True)
    print(f"using most likely length {length}")
    input("hit enter to continue...")
    password = crack_password(length, verbose=True)
    print(f"password cracked:'{password}'")


if __name__ == '__main__':
    main()
