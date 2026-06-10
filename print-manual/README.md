# The Autonomy Gate Print Manual

This directory contains the print-ready owner documentation for The Autonomy Gate.

## Package Contents

- `output/AUTONOMY_GATE_FIELD_MANUAL_6x9.pdf` — 6 × 9 inch owner field manual
- `output/AUTONOMY_GATE_QUICK_START_CARD_5x7.pdf` — two-sided 5 × 7 inch onboarding card
- `output/AUTONOMY_GATE_VERDICT_CARD_4x6.pdf` — two-sided 4 × 6 inch verdict reference card
- `build_manual.py` — deterministic PDF generator
- `proofs/` — rasterized pages used for visual quality assurance

## Print Specifications

### Field Manual

- Trim: 6 × 9 inches
- Binding: perfect bound or wire bound
- Interior: full color, uncoated or matte stock
- Recommended stock: 70–80 lb text
- Cover: 100 lb matte cover stock
- Printing: actual size; do not fit to Letter or A4

### Quick-Start Card

- Trim: 5 × 7 inches
- Printing: duplex, flip on the short edge
- Recommended stock: 100–130 lb matte cover stock

### Verdict Reference Card

- Trim: 4 × 6 inches
- Printing: duplex, flip on the short edge
- Recommended stock: 100–130 lb matte cover stock

## Source Documents

The generator imports the forward-facing documentation in `../docs/`. The print build does not import internal assessments, production notes, or the older duplicate owner manual.

## Rebuild

The script expects ReportLab in `/private/tmp/autonomy-gate-print-deps`.

```bash
python3 print-manual/build_manual.py
```

After rebuilding, verify page sizes with `pdfinfo`, extract text with `pdftotext`, and rasterize representative pages with `pdftoppm` before release.

## Release Boundary

Ship the three PDFs and, when useful, this README. Do not publish the wider competition working folder by treating this directory as an automatic release manifest.
