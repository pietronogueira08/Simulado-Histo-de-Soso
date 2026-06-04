# 🔬 Simulado Histo de Soso — Timer Interativo

Timer para o **Estudo Dirigido de Biologia Tecidual P2**, com slides das lâminas histológicas.

## ⚡ Como usar

1. Abra o arquivo **`index.html`** no navegador
2. Clique em **"Iniciar ▶"**
3. O timer começa automaticamente

## ⏱ Tempos

| Tipo de slide | Tempo |
|---|---|
| 🔴 **Pergunta** — imagem da lâmina | **60 segundos** |
| 🟢 **Resposta** — nome + características | **15 segundos** |

O timer avança automaticamente ao zerar.

## ⌨️ Controles

| Tecla | Ação |
|---|---|
| `→` / `Espaço` | Avançar slide |
| `←` | Voltar slide |
| `P` | Pausar / Retomar |
| `R` | Reiniciar timer |
| `F` | Fullscreen |

## 📁 Estrutura

```
├── index.html          # App principal
├── convert_pdf.py      # Script de conversão PDF → PNG
└── slides/             # 69 slides em PNG
    ├── slide_001.png
    └── ...
```

## 🛠 Gerar slides novamente

Caso precise regenerar os slides a partir do PDF:

```bash
pip install pymupdf
python convert_pdf.py
```

---

Feito com ❤️ pelos monitores: Maria Paula, Valter Kauã e Emilly
