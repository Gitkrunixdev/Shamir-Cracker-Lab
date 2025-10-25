import itertools
from core.utils import load_wordlist
from core.analyzer import test_seed

def brute_force(known_share, wordlist_path, target_address, max_attempts=100000): 
wordlist = load_wordlist(wordlist_path) 
attempts = 0 

for combo in itertools.product(wordlist, repeat=20): 
guessed_share = list(combo) 
attempts += 1 

if test_seed([known_share, guessed_share], target_address): 
print(f""[✓] Found after {attempts} attempts!"") 
break 

if attempts % 1000 == 0: 
print(f""[{attempts}] attempts..."") 

if attempts >= max_attempts: 
print(""⏹️ Retry limit reached."") 
break
