# shamir_lab
Experimental cryptography lab for analyzing and reconstructing Shamir Secret Sharing shares, deriving BIP-39 seeds, and testing Bitcoin addresses


```markdown
# 🔐 Shamir Cracker Lab

## 🧠 Functions

- Shamir Share Metadata Analysis
- Generating Test Shares from a Secret
- Reconstructing the Seed and Deriving a BTC Address
- Brute-Force with a Limited Dictionary
- Share Guessing Heuristics
- Tkinter Graphical User Interface (GUI)

## 🗂️ Project Structure

```
shamir_lab/
├── core/
│   ├── analyzer.py         # share analysis
│   ├── brute_force.py      # brute-force engine + heuristics
│   ├── generator.py        # generating test shares
│   └── utils.py            # auxiliary functions (e.g. dictionaries)
├── gui/
│   └── app.py              # graphical interface (tkinter)
├── wordlists/
│   ├── bip39_english.txt   # BIP-39 word list
│   └── custom.txt          # your own dictionary
├── examples/
│   └── sample_share.txt    # sample share
├── main.py                 # CLI entry point
└── README.md               # instruction
```



