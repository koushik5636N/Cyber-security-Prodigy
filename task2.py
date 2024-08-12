from PIL import Image
import numpy as np

def xor_encrypt_decrypt(image_array, key):
    """
    Encrypts or decrypts an image array using XOR with the given key.
    
    :param image_array: A numpy array of the image.
    :param key: The key to XOR with. Should be a number between 0 and 255.
    :return: The modified numpy array.
    """
    # Ensure the key is within the valid range
    if not (0 <= key <= 255):
        raise ValueError("Key must be an integer between 0 and 255.")

    # Apply XOR operation on each pixel
    encrypted_array = np.bitwise_xor(image_array, key)
    
    return encrypted_array

def process_image(input_file, output_file, key, encrypt=True):
    """
    Process an image by encrypting or decrypting it.
    
    :param input_file: Path to the input image file.
    :param output_file: Path to save the processed image.
    :param key: The key for encryption or decryption.
    :param encrypt: Boolean flag indicating whether to encrypt or decrypt.
    """
    # Open the image file
    image = Image.open(input_file)
    image_array = np.array(image)

    # Encrypt or decrypt the image array
    if encrypt:
        processed_array = xor_encrypt_decrypt(image_array, key)
    else:
        processed_array = xor_encrypt_decrypt(image_array, key)
    
    # Convert the processed array back to an image
    processed_image = Image.fromarray(processed_array.astype(np.uint8))
    
    # Save the processed image
    processed_image.save(output_file)

    print(f"Image {'encrypted' if encrypt else 'decrypted'} and saved to {output_file}")

if __name__ == "__main__":
    import argparse
    
    # Command line argument parsing
    parser = argparse.ArgumentParser(description='Encrypt or decrypt an image using XOR operation.')
    parser.add_argument('input', type=str, help='Input image file path')
    parser.add_argument('output', type=str, help='Output image file path')
    parser.add_argument('key', type=int, help='Encryption/Decryption key (0-255)')
    parser.add_argument('--decrypt', action='store_true', help='Decrypt the image (default is encrypt)')
    
    args = parser.parse_args()
    
    process_image(args.input, args.output, args.key, not args.decrypt)
