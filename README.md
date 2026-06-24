# brood-29

### Status: Active Cryptanalysis Toolkit for Cicada 3301's Liber Primus

brood-29 is a Python-based cryptographic framework designed specifically to analyze and attack the remaining unsolved pages of Cicada 3301’s infamous runic book, the Liber Primus.

Most traditional automated cryptanalysis tools and natural language processing libraries fail when applied to this puzzle because they are hardcoded for the standard 26-letter English alphabet. This repository rebuilds classical cipher mechanics from the ground up to operate entirely within a non-standard, 29-character runic architecture.

### 🧠 The Architecture Problem

The Liber Primus is written in Anglo-Saxon Futhorc runes. To decrypt it, characters must be mapped to specific numeric values and primes using Cicada's custom lookup table, the Gematria Primus.Because of this, standard polyalphabetic analysis does not work. This engine processes text streams using localized arithmetic wrapped entirely around a base-29 system:$$C_i \equiv (P_i + K_i) \pmod{29}$$Where $C$ is the ciphertext index, $P$ is the plaintext index, and $K$ is the key-stream index derived from the Gematria.

### 🛠️ Key Features
- Bidirectional Gematria Mapping: A strict, type-validated matrix that maps raw Futhorc runes to their historical transliterations, 0-28 indices, and assigned prime numbers.

- Modulo-29 Cipher Engine: A specialized polyalphabetic decryption and encryption engine built to handle looping key-streams in base-29 arithmetic.

- Base-29 Index of Coincidence (IoC): A statistical analysis tool calibrated to measure the entropy of the unsolved pages, identifying whether targeted text blocks are monoalphabetic, polyalphabetic, or completely random (where a random distribution sits at $\approx 0.034$).

-  Automated Key Stream Harvester: An ingestion pipeline designed to scrape, parse, and clean heavy philosophical, mathematical, or occult texts (such as those heavily referenced by Cicada), converting them into potential multi-word key streams for brute-force execution.

### 🚀 Getting Started
#### Prerequisites 
- Python 3.10+

- pytest (for running the validation suites)

- Installation
```bash
git clone https://github.com/KLERIZGWEN/brood-29.git
cd brood-29
pip install -r requirements.txt
```

### Running Tests
To verify the core engine against historically solved pages (e.g., verifying Page 1 using the known key FIRFENG):
```bash
pytest tests/
```

### 📜 Disclaimer
This project is dedicated to the open-source preservation and collaborative analysis of the Cicada 3301 mysteries. It is built for educational and cryptographic research purposes. The truth is a rabbit hole.