from PIL import Image

print("Generating images...")

# Make 20 red images
for i in range(20):
    img = Image.new('RGB', (64, 64), color='red')
    img.save(f'dataset/0_red/red_{i}.jpg')

# Make 20 blue images
for i in range(20):
    img = Image.new('RGB', (64, 64), color='blue')
    img.save(f'dataset/1_blue/blue_{i}.jpg')

print("✅ Added 20 red and 20 blue images to your dataset folders!")