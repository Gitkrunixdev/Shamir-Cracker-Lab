from shamir_mnemonic import shamir

def generate_shares(secret=""correct horse battery staple"", threshold=2, count=3): 
mnemonics = shamir.generate_mnemonics( 
threshold=threshold, 
count=count, 
master_secret=secret.encode() 
) 
for i, share in enumerate(mnemonics): 
print(f""Share {i+1}: {' '.join(share)}"") 
return mnemonics

