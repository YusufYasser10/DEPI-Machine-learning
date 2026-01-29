import numpy as np
from PIL import Image

class ImageEditor:
    def __init__(self, filename):
        self.filename = filename
        try:
            # Load and convert to grayscale ('L')
            img = Image.open(filename).convert('L')
            img = img.resize((256, 256))
            self.image_matrix = np.array(img)
            print(f"✅ Success: Loaded {filename}")
        except FileNotFoundError:
            print("❌ Error: File not found.")
            self.image_matrix = None

    def save(self, new_filename):
        if self.image_matrix is None:
            return
        result_img = Image.fromarray(self.image_matrix.astype('uint8'))
        result_img.save(new_filename)
        print(f"💾 Saved to: {new_filename}")

    # --- FILTER 1: Black & White ---
    def apply_black_and_white(self):
        avg = np.mean(self.image_matrix)
        self.image_matrix = np.where(self.image_matrix > avg, 255, 0)
        print("Done: Applied Black & White Filter.")

    # --- FILTER 2: Invert (This was missing!) ---
    def apply_invert(self):
        # 255 - pixel value gives the negative
        self.image_matrix = 255 - self.image_matrix
        print("Done: Applied Invert Filter.")

    # --- FILTER 4: Flip ---
    def apply_flip(self, direction):
        if direction == 'h':
            self.image_matrix = np.fliplr(self.image_matrix)
        elif direction == 'v':
            self.image_matrix = np.flipud(self.image_matrix)
        print(f"Done: Flipped image ({direction}).")

# --- Main Execution Block ---
if __name__ == "__main__":
    # Change 'cameraman.bmp' to the actual name of an image you have uploaded
    filename = input("Enter image name (e.g. cameraman.bmp): ")
    
    processor = ImageEditor(filename)
    
    if processor.image_matrix is not None:
        while True:
            print("\nSelect a Filter:")
            print("1. Black & White")
            print("2. Invert")
            print("4. Flip Image")
            print("S. Save & Exit")
            
            choice = input("Choice: ").upper()
            
            if choice == '1':
                processor.apply_black_and_white()
            elif choice == '2':
                # This line caused the error because the method didn't exist before
                processor.apply_invert()
            elif choice == '4':
                direction = input("Flip (h)orizontal or (v)ertical? ")
                processor.apply_flip(direction)
            elif choice == 'S':
                save_name = input("Enter output name (e.g. result.bmp): ")
                processor.save(save_name)
                break
            else:
                print("Invalid choice.")