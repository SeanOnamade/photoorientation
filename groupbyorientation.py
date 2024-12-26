import os
from PIL import Image

def group_photos_by_orientation(folder_path):
    # This function is to help making posting my photography to Instagram easier
    subfolders = {
        "landscape": os.path.join(folder_path, "Landscape"),
        "vertical": os.path.join(folder_path, "Vertical"),
        "square": os.path.join(folder_path, "Square"),
    }

    # If the subfolders don't exist
    for subfolder in subfolders.values():
        os.makedirs(subfolder, exist_ok=True)

    # Iterate through the files in the folder of this file
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories and non-images
        if os.path.isdir(file_path) or not filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tiff", ".webp")):
            continue

        try:
            # Open image and check dimensions
            with Image.open(file_path) as img:
                width, height = img.size

            # Determine its orientation
            aspect_ratio = width / height
            if 0.9 <= aspect_ratio <= 1.1:  # allow some flexibility for square photos
                orientation = "square"
            elif width > height:
                orientation = "landscape"
            else:
                orientation = "vertical"

            # move the file to the right subfolder
            new_path = os.path.join(subfolders[orientation], filename)
            os.rename(file_path, new_path)
            print(f"Moved {filename} to {orientation} folder.")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

# replace '[path]' with the path to the folder of photos; allow input maybe?
folder_path = r"[path]"
group_photos_by_orientation(folder_path)
