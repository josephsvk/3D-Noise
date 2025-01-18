# 3D Noise: A New Approach to Anonymous File Encryption and Sharing

## Overview
3D Noise is an innovative encryption method designed for anonymous file sharing and secure data distribution. The core concept involves splitting a file into three distinct layers (S_R, S_G, S_B), which are individually encrypted using XOR logic, hashing, and weights. Each layer alone is meaningless, appearing as random noise, but when combined, they reveal the original file.

## Features
- **Layered Encryption:** Files are divided into three layers representing different "colors."
- **Secure Sharing:** Only the combination of all three layers can decrypt the original file.
- **Anonymous Players:** Users, called "players," choose a layer (color) to share with others.
- **Hash-Based Security:** Uses global and stabilized hashes to ensure unique encryption for each layer.

```
                        +-------------------------+
                        |        Input File       |
                        +-------------------------+
                                    |
                                    v
                        +-------------------------+
                        | Split file into layers  |
                        | S_R, S_G, S_B           |
                        | (e.g., RGB layers)      |
                        +-------------------------+

                        +-------------------------+
                        | Generate Global Hash H  |
                        | (Randomly generated,    |
                        | consistent size as      |
                        | the layers)             |
                        +-------------------------+
                                    |
                                    v
                        +-------------------------+
                        | Stabilize Hash for S_B  |
                        | (H + flipped H) mod 256 |
                        +-------------------------+

      +-------------------------+         +-------------------------+
      | Encrypt Layer S_R       |         | Encrypt Layer S_G       |
      | E_R = XOR(S_R, H, S_G)  |         | E_G = XOR(S_G, H, S_B)  |
      +-------------------------+         +-------------------------+
                           \              /
                              \            /
                              \          /
                         +-------------------------+
                         | Encrypt Layer S_B       |
                         | E_B = XOR(S_B, Stable H,|
                         | S_R)                    |
                         +-------------------------+

                         +-------------------------+
                         | Output Encrypted Layers |
                         | E_R, E_G, E_B           |
                         +-------------------------+


      +-------------------------+         +-------------------------+
      | Decrypt Layer S_R       |         | Decrypt Layer S_G       |
      | S_R = XOR(E_R, H, E_G)  |         | S_G = XOR(E_G, H, E_B)  |
      +-------------------------+         +-------------------------+
                           \              /
                              \            /
                              \          /
                         +-------------------------+
                         | Decrypt Layer S_B       |
                         | S_B = XOR(E_B, Stable H,|
                         | E_R)                    |
                         +-------------------------+

                         +-------------------------+
                         | Reconstruct Original    |
                         | File from Layers S_R,   |
                         | S_G, S_B                |
                         +-------------------------+
```
## Defining Security in the 3D Noise Project
### Basic Definition of Security
#### Security in the 3D Noise project is defined as follows:
Inaccessibility of information from individual layers: Each layer 
(𝑆𝑅,𝑆𝐺,𝑆𝐵) is meaningless on its own and appears as random noise.

Dependency on combination: The original file can only be reconstructed by combining all three layers (𝐸𝑅,𝐸𝐺,𝐸𝐵).

Reliance on global hash: Without the correct global hash (𝐻) and stabilized hash (𝐻𝑠), decryption is impossible.

### Specific Security Properties
#### Layer Confidentiality:
Individual layers do not reveal any meaningful information without the others.
XOR logic and hashing ensure that each layer is obfuscated and secure.
#### Resistance to Brute-Force Attacks:
The hashing mechanism provides a large keyspace, making brute-forcing impractical.
#### Independence of Layers:
Combining only two layers (e.g.,𝑆𝑅SR and 𝑆𝐺SG) does not provide any useful information about the original file.

### Protection Against Specific Attacks
#### Partial Layer Exposure:
An attacker cannot reconstruct the file without all three layers and the corresponding hashes.
#### Statistical Analysis:
The layers are designed to appear as random noise, complicating any frequency or pattern analysis.
#### Layer Manipulation:
Modifying a single layer without updating the others renders the file completely unreadable.

### Algorithm-Driven Security
#### Dependency on Hash:
The global hash (𝐻) is randomly generated, ensuring unique encryption for each file.
The stabilized hash (𝐻𝑠) for SB adds another layer of protection.
#### XOR Logic:
XOR operations ensure that input data combinations are unique and reversible only with precise inputs.

### Security Limitations
#### Vulnerability to Coordinated Attacks:
If an attacker obtains all three layers and the hash, they can reconstruct the original file.
#### Randomness of Hashing:
The system relies on the quality of randomness when generating 𝐻.

### Potential Extensions to Improve Security
**Multi-Hash Dependency**: Introduce multiple layers of hashing for added complexity.
**Dynamic Weights**: Dynamically generate weights for layers (𝑅,𝐺,𝐵) based on additional inputs.
**Integration of KDF**: Use Key Derivation Functions (e.g., PBKDF2, Argon2) to enhance resistance to brute-force attacks.

### Summary of Security Definition:
“The security of the 3D Noise system lies in the impossibility of reconstructing the original file without all three layers and the hash keys. The combination of layers is designed to ensure anonymity and prevent data analysis unless all layers and keys are available.”


## How It Works
### 1. Splitting the File
The input file is divided into three layers:
- **S_R:** Red layer
- **S_G:** Green layer
- **S_B:** Blue layer
   
### 2. Generating Hashes
- A global hash (H) is generated for encryption.
- A stabilized hash (H_s) for S_B is derived from H:  
 ```
  \[
  H_s[i, j] = \left(H[i, j] + H[n-i-1, j]\right) \mod 256
  \]
 ```

### 3. Encrypting Layers
Each layer is encrypted using XOR logic:
```markdown
\[
E_R[i, j] = S_R[i, j] \oplus H[i, j] \oplus S_G[i, j]
\]
\[
E_G[i, j] = S_G[i, j] \oplus H[i, j] \oplus S_B[i, j]
\]
\[
E_B[i, j] = S_B[i, j] \oplus H_s[i, j] \oplus S_R[i, j]
\]

```
### 4. Decrypting Layers
The original layers are reconstructed by reversing the encryption process:
```markdown
\[
S_R[i, j] = E_R[i, j] \oplus H[i, j] \oplus E_G[i, j]
\]
\[
S_G[i, j] = E_G[i, j] \oplus H[i, j] \oplus E_B[i, j]
\]
\[
S_B[i, j] = E_B[i, j] \oplus H_s[i, j] \oplus E_R[i, j]
\]
```

### 5. Reconstructing the File
All layers are combined to restore the original file.

## Use Cases
- **Anonymous File Sharing:** Share data securely without revealing content unless all layers are combined.python
- **Decentralized Storage:** Distribute encrypted layers across multiple participants.
- **Secure Collaboration:** Enable teams to share partial data securely.

# No tested only generate 

## Getting Started
### Prerequisites
- Python 3.x
- NumPy library

### Installation
Clone the repository:
```bash
git clone https://github.com/josephsvk/3d-noise.git
cd 3d-noise
```

Install dependencies:
```bash
pip install numpy
```

### Usage
#### Encrypt a File
1. Divide the file into layers (S_R, S_G, S_B).
2. Run the encryption script:
   ```bash
   python encrypt.py
   ```

#### Decrypt a File
1. Combine encrypted layers (E_R, E_G, E_B).
2. Run the decryption script:
   ```bash
   python decrypt.py
   ```

## Contributing
We welcome contributions! If you have ideas for improving 3D Noise or new use cases, feel free to:
- Fork the repository.
- Create a branch for your feature.
- Submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer
This project is an experimental approach to encryption and data sharing. Use at your own risk. The author is not responsible for any misuse or issues arising from the use of this system.

## Acknowledgments
This project is inspired by concepts in cryptography and discussions with the community. Special thanks to resources like ChatGPT and open-source projects that helped shape this idea.

