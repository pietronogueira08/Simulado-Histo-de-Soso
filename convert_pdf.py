"""
Converte todas as páginas do PDF em imagens PNG para uso no app timer.
Gera arquivos slide_001.png a slide_069.png na pasta ./slides/
"""
import fitz  # pymupdf
import os
import sys

PDF_PATH = "ED BIOTECIDUAL P2.pdf"
OUTPUT_DIR = "slides"
DPI = 150  # 150 DPI = boa qualidade com tamanho razoável (~800KB/pág)

def convert_pdf_to_images():
    if not os.path.exists(PDF_PATH):
        print(f"ERRO: Arquivo '{PDF_PATH}' não encontrado!")
        sys.exit(1)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"Abrindo '{PDF_PATH}'...")
    doc = fitz.open(PDF_PATH)
    total = len(doc)
    print(f"Total de páginas: {total}")

    mat = fitz.Matrix(DPI / 72, DPI / 72)  # fator de escala

    for i, page in enumerate(doc):
        out_path = os.path.join(OUTPUT_DIR, f"slide_{i+1:03d}.png")

        if os.path.exists(out_path):
            print(f"  [{i+1:02d}/{total}] já existe, pulando...")
            continue

        pix = page.get_pixmap(matrix=mat, alpha=False)
        pix.save(out_path)

        size_kb = os.path.getsize(out_path) // 1024
        print(f"  [{i+1:02d}/{total}] {os.path.basename(out_path)} ({size_kb} KB)")

    doc.close()
    print(f"\n✅ Conversão concluída! {total} slides salvos em './{OUTPUT_DIR}/'")

if __name__ == "__main__":
    convert_pdf_to_images()
