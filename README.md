# 3D Noise: A New Approach to Anonymous File Encryption and Sharing

## Overview
3D Noise is an innovative encryption method designed for anonymous file sharing and secure data distribution. The core concept involves splitting a file into three distinct layers (S_R, S_G, S_B), which are individually encrypted using XOR logic, hashing, and weights. Each layer alone is meaningless, appearing as random noise, but when combined, they reveal the original file.

![3DNoise](![DALL·E 2025-01-18 19.51.11 - A detailed block diagram showing the encryption and decryption process for a file split into three layers (S_R, S_G, S_B). The diagram includes the fo.webp](https://github.com/josephsvk/3D-Noise/blob/main/DALL%C2%B7E%202025-01-18%2019.51.11%20-%20A%20detailed%20block%20diagram%20showing%20the%20encryption%20and%20decryption%20process%20for%20a%20file%20split%20into%20three%20layers%20(S_R%2C%20S_G%2C%20S_B).%20The%20diagram%20includes%20the%20fo.webp))

## Features
- **Layered Encryption:** Files are divided into three layers representing different "colors."
- **Secure Sharing:** Only the combination of all three layers can decrypt the original file.
- **Anonymous Players:** Users, called "players," choose a layer (color) to share with others.
- **Hash-Based Security:** Uses global and stabilized hashes to ensure unique encryption for each layer.

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
- **Anonymous File Sharing:** Share data securely without revealing content unless all layers are combined.
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

