from PIL import Image

# Chemin de l'image PNG
png_file = "pageGarde.png"
pdf_file = "pageGarde.pdf"


# Taille de la page en pouces
page_width_inch = 7.8
page_height_inch = 11
dpi = 300

# Convertir la taille de la page en pixels
page_width_px = int(page_width_inch * dpi)
page_height_px = int(page_height_inch * dpi)

# --- 1. Ouvrir et redimensionner l'image pour couvrir toute la page ---
img = Image.open(png_file)

# Calcul des ratios pour couvrir la page
ratio_w = page_width_px / img.width
ratio_h = page_height_px / img.height
scale = max(ratio_w, ratio_h)

# Redimensionner
new_width = int(img.width * scale)
new_height = int(img.height * scale)
img_resized = img.resize((new_width, new_height), Image.LANCZOS)

# Recadrer pour correspondre à la page
left = (new_width - page_width_px) // 2
top = (new_height - page_height_px) // 2
right = left + page_width_px
bottom = top + page_height_px
img_cropped = img_resized.crop((left, top, right, bottom))

# --- 2. Créer une page blanche ---
white_page = Image.new("RGB", (page_width_px, page_height_px), "white")

# --- 3. Sauvegarder les deux pages dans un PDF ---
img_cropped.save(pdf_file, "PDF", resolution=dpi, save_all=True, append_images=[white_page])

print(f"PDF créé avec 2 pages : {pdf_file}")