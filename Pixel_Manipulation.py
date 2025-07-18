from PIL import Image
import numpy as np
import os

def apply_xor(image_array, key):
    """Apply XOR operation to each pixel with the key"""
    key_length = len(key)
    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            for k in range(3):  # For each channel (RGB)
                char_index = (i + j + k) % key_length
                image_array[i][j][k] ^= ord(key[char_index])
    return image_array

def process_image(file_path, key, encrypt=True):
    """Core image processing function"""
    if not os.path.isfile(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    try:
        with Image.open(file_path) as img:
            img_array = np.array(img)
            processed_array = apply_xor(img_array.copy(), key)
            processed_img = Image.fromarray(processed_array)

            save_path = input("Enter the path to save the processed image (e.g., output.png): ")
            processed_img.save(save_path)
            action = "encrypted" if encrypt else "decrypted"
            print(f"Image {action} successfully! Saved to {save_path}.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    action = input("Do you want to (e)ncrypt or (d)ecrypt an image? ").strip().lower()
    if action not in ['e', 'd']:
        print("Invalid option. Please enter 'e' for encrypt or 'd' for decrypt.")
        return

    file_path = input("Enter the path of the image file: ")
    key = input("Enter an encryption key (any text): ")
    
    if action == 'e':
        process_image(file_path, key, encrypt=True)
    else:
        process_image(file_path, key, encrypt=False)

if __name__ == "__main__":
    main()

