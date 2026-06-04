"""
Converte todos os slides PNG para JPEG (menor tamanho para deploy no Vercel)
e atualiza as referências no index.html
"""
import os
from PIL import Image

SLIDES_DIR = "slides"
QUALITY = 85  # boa qualidade com tamanho reduzido

def convert_to_jpeg():
    pngs = sorted([f for f in os.listdir(SLIDES_DIR) if f.endswith('.png')])
    print(f"Convertendo {len(pngs)} PNGs para JPEG (qualidade {QUALITY})...")
    
    total_before = 0
    total_after = 0
    
    for fname in pngs:
        png_path = os.path.join(SLIDES_DIR, fname)
        jpg_name = fname.replace('.png', '.jpg')
        jpg_path = os.path.join(SLIDES_DIR, jpg_name)
        
        size_before = os.path.getsize(png_path) // 1024
        total_before += os.path.getsize(png_path)
        
        img = Image.open(png_path).convert('RGB')
        img.save(jpg_path, 'JPEG', quality=QUALITY, optimize=True)
        
        size_after = os.path.getsize(jpg_path) // 1024
        total_after += os.path.getsize(jpg_path)
        
        print(f"  {fname} -> {jpg_name}: {size_before}KB -> {size_after}KB")
        os.remove(png_path)  # remove PNG original
    
    print(f"\nTotal antes: {total_before//1024//1024} MB")
    print(f"Total depois: {total_after//1024//1024} MB")
    print(f"Reducao: {round((1 - total_after/total_before)*100)}%")
    print("Concluido!")

if __name__ == "__main__":
    convert_to_jpeg()
