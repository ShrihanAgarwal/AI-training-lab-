import os

# Define the folder structure
folders = [
    "dataset/0_red",
    "dataset/1_blue"
]

# Create the folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created: {folder}")

print("✅ Folder setup complete! You can now drop your red and blue images into their respective folders.")