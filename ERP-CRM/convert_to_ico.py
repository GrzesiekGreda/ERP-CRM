from PIL import Image, ImageDraw, ImageFont

# Create a simple favicon with 'G' letter
ico_path = r'c:\Users\g.greda\GREDA\ERP-CRM\app\static\favicon.ico'

# Create a 32x32 image
img = Image.new('RGBA', (32, 32), (10, 10, 10, 255))
draw = ImageDraw.Draw(img)

# Draw red border
draw.rectangle([1, 1, 30, 30], outline=(255, 0, 0, 255), width=2)

# Draw 'G' in the center
try:
    font = ImageFont.truetype("arial.ttf", 20)
except:
    font = ImageFont.load_default()

# Draw text with red outline effect
text = "G"
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
x = (32 - text_width) // 2
y = (32 - text_height) // 2 - 2

# Red outline
for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
        if dx != 0 or dy != 0:
            draw.text((x + dx, y + dy), text, font=font, fill=(255, 0, 0, 255))

# Black fill
draw.text((x, y), text, font=font, fill=(0, 0, 0, 255))

# Save as ICO with multiple sizes
img.save(ico_path, format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])

print("✓ favicon.ico created successfully!")
