import numpy as np

def encrypt(S_R, S_G, S_B, global_hash):
    """
    Encrypts layers using XOR logic and a global hash.
    
    Args:
        S_R, S_G, S_B: Layers representing the split file.
        global_hash: Global hash used for encryption.
    
    Returns:
        E_R, E_G, E_B: Encrypted Noise layers.
    """
    weight = 1  # Simplified weights
    stabilized_hash_B = (global_hash + np.flip(global_hash, axis=0)) % 256

    E_R = np.bitwise_xor((S_R * weight) % 256, np.bitwise_xor(global_hash, (S_G * weight) % 256))
    E_G = np.bitwise_xor((S_G * weight) % 256, np.bitwise_xor(global_hash, (S_B * weight) % 256))
    E_B = np.bitwise_xor((S_B * weight) % 256, np.bitwise_xor(stabilized_hash_B, (S_R * weight) % 256))

    return E_R, E_G, E_B

def decrypt(E_R, E_G, E_B, global_hash):
    """
    Decrypts layers using XOR logic and a global hash.
    
    Args:
        E_R, E_G, E_B: Encrypted Noise layers.
        global_hash: Global hash used for decryption.
    
    Returns:
        S_R, S_G, S_B: Original file layers.
    """
    weight = 1  # Simplified weights
    stabilized_hash_B = (global_hash + np.flip(global_hash, axis=0)) % 256

    S_R_dec = (np.bitwise_xor(E_R, np.bitwise_xor(global_hash, (E_G * weight) % 256)) // weight) % 256
    S_G_dec = (np.bitwise_xor(E_G, np.bitwise_xor(global_hash, (E_B * weight) % 256)) // weight) % 256
    S_B_dec = (np.bitwise_xor(E_B, np.bitwise_xor(stabilized_hash_B, (E_R * weight) % 256)) // weight) % 256

    return S_R_dec, S_G_dec, S_B_dec

# Example Usage
def run_demo(matrix_R, matrix_G, matrix_B):
    global_hash = np.random.randint(0, 256, size=matrix_R.shape, dtype=np.uint8)

    # Encrypt layers
    E_R, E_G, E_B = encrypt(matrix_R, matrix_G, matrix_B, global_hash)

    # Decrypt layers
    S_R_dec, S_G_dec, S_B_dec = decrypt(E_R, E_G, E_B, global_hash)

    # Check success
    errors_R = np.sum(matrix_R != S_R_dec)
    errors_G = np.sum(matrix_G != S_G_dec)
    errors_B = np.sum(matrix_B != S_B_dec)

    return {
        "Global_Hash": global_hash,
        "Encrypted_Layers": {"E_R": E_R, "E_G": E_G, "E_B": E_B},
        "Decrypted_Layers": {"S_R": S_R_dec, "S_G": S_G_dec, "S_B": S_B_dec},
        "Errors": {"R": errors_R, "G": errors_G, "B": errors_B},
        "Success": errors_R == 0 and errors_G == 0 and errors_B == 0
    }
