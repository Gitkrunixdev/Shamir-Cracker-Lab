from shamir_mnemonic import shamir
from binascii import hexlife

def analyze_share(words): 
data = shamir.decode_mnemonic(words) 
print(""🧠 SHARE ANALYSIS"") 
print(f""ID: {data.identifier.hex()}"") 
print(f""Iterations: {data.iteration_exponent}"") 
print(f""Group: {data.group_index}/{data.group_threshold}"") 
print(f""Member: {data.member_index}/{data.member_threshold}"") 
print(f""HEX value: {hexlify(data.value).decode()}"")
