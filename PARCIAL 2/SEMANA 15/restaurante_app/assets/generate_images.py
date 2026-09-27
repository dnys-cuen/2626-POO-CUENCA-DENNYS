from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

out = Path(r'C:/Users/PC-ENV/UEA/2626-POO-CUENCA-DENNYS/PARCIAL 2/SEMANA 15/restaurante_app/assets')
out.mkdir(parents=True, exist_ok=True)

# Helper to load default font
try:
    font_large = ImageFont.truetype('arial.ttf', 36)
    font_med = ImageFont.truetype('arial.ttf', 18)
    font_small = ImageFont.truetype('arial.ttf', 12)
except Exception:
    from PIL import ImageFont
    font_large = ImageFont.load_default()
    font_med = ImageFont.load_default()
    font_small = ImageFont.load_default()

# Create logo (600x140)
logo = Image.new('RGBA', (600, 140), (250, 245, 240, 255))
d = ImageDraw.Draw(logo)
# left emblem circle
d.ellipse((20,20,140,140), fill=(200,60,40,255), outline=(160,40,30,255))
# simple fork/spoon lines
d.line((70,40,70,100), fill=(255,255,255,255), width=4)
d.line((85,45,105,85), fill=(255,255,255,255), width=4)
# Text
try:
    w,h = font_large.getsize('Restaurante App')
except Exception:
    w,h = d.textbbox((0,0),'Restaurante App', font=font_large)[2:]
d.text((160,35), 'Restaurante App', font=font_large, fill=(30,30,30,255))
try:
    w2,h2 = font_med.getsize('Semana 15 - Gestión de Ventas')
except Exception:
    w2,h2 = d.textbbox((0,0),'Semana 15 - Gestión de Ventas', font=font_med)[2:]
d.text((160,80), 'Semana 15 - Gestión de Ventas', font=font_med, fill=(80,80,80,255))
logo.save(out / 'logo.png')
logo.save(out / 'logo_small.png')

# Create banner (900x120)
banner = Image.new('RGBA', (900, 120), (40, 100, 80, 255))
d = ImageDraw.Draw(banner)
# decorative stripe
for i in range(0, 900, 40):
    d.rectangle((i, 70, i+20, 120), fill=(60,140,100,180))
# center text
try:
    w,h = font_large.getsize('Restaurante App')
except Exception:
    w,h = d.textbbox((0,0),'Restaurante App', font=font_large)[2:]
d.text(((900-w)/2,20), 'Restaurante App', font=font_large, fill=(255,255,255,255))
# subtitle
try:
    w2,h2 = font_med.getsize('Administración de Productos y Ventas')
except Exception:
    w2,h2 = d.textbbox((0,0),'Administración de Productos y Ventas', font=font_med)[2:]
d.text(((900-w2)/2,70), 'Administración de Productos y Ventas', font=font_med, fill=(230,230,230,200))
banner.save(out / 'banner.png')

# Create square icons 64x64 with simple pictograms
icons = {
    'icon_users.png': ('U', (70,130,180)),
    'icon_products.png': ('P', (180,90,60)),
    'icon_sales.png': ('S', (60,150,80)),
    'icon_logout.png': ('L', (160,60,100)),
    'icon.png': ('R', (40,120,160)),
}
for name, (char, color) in icons.items():
    img = Image.new('RGBA', (64,64), (255,255,255,0))
    d = ImageDraw.Draw(img)
    d.ellipse((4,4,60,60), fill=(color[0], color[1], color[2],255))
    try:
        fw, fh = font_large.getsize(char)
    except Exception:
        fw, fh = d.textbbox((0,0),char, font=font_large)[2:]
    d.text(((64-fw)/2, (64-fh)/2-4), char, font=font_large, fill=(255,255,255,255))
    img.save(out / name)

# Decorative small resources
decor = Image.new('RGBA', (200,60), (255,255,255,0))
d = ImageDraw.Draw(decor)
d.rounded_rectangle((0,0,200,60), radius=12, fill=(255,245,235,220), outline=(200,150,120,200))
d.text((16,18), 'Bienvenido', font=font_med, fill=(80,60,40,255))
decor.save(out / 'decor_welcome.png')

print('Generated assets in', out)
