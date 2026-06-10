#!/usr/bin/env python3
"""Build the 6x9 Autonomy Gate field manual and reference cards."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from xml.sax.saxutils import escape

DEPS = Path("/private/tmp/autonomy-gate-print-deps")
sys.path.insert(0, str(DEPS))

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import inch
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    Frame,
    HRFlowable,
    KeepTogether,
    ListFlowable,
    ListItem,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = Path(__file__).resolve().parent / "output"
PROOFS = Path(__file__).resolve().parent / "proofs"
OUT.mkdir(parents=True, exist_ok=True)
PROOFS.mkdir(parents=True, exist_ok=True)

PAGE = (6 * inch, 9 * inch)
CARD_QUICK = (5 * inch, 7 * inch)
CARD_VERDICT = (4 * inch, 6 * inch)

BLACK = HexColor("#0A0A0A")
OFFWHITE = HexColor("#F5F2E8")
AMBER = HexColor("#E8C547")
GRAPHITE = HexColor("#3A3A3A")
MID = HexColor("#77736A")
LIGHT = HexColor("#DED9CC")
RED = HexColor("#C4483A")
BLUE = HexColor("#607F9F")
WHITE = colors.white


def register_fonts() -> tuple[str, str, str]:
    """Use stable local fonts when available, otherwise PDF core fonts."""
    helv = "/System/Library/Fonts/Helvetica.ttc"
    mono_candidates = [
        "/System/Library/Fonts/SFNSMono.ttf",
        "/System/Library/Fonts/SFMono-Regular.otf",
        "/System/Library/Fonts/Menlo.ttc",
    ]
    body, bold, mono = "Helvetica", "Helvetica-Bold", "Courier"
    # TTC registration is inconsistent across ReportLab versions; use core
    # Helvetica for maximum portability and only register a standalone mono.
    for candidate in mono_candidates:
        if Path(candidate).exists() and candidate.endswith((".ttf", ".otf")):
            try:
                pdfmetrics.registerFont(TTFont("GateMono", candidate))
                mono = "GateMono"
                break
            except Exception:
                pass
    return body, bold, mono


BODY_FONT, BOLD_FONT, MONO_FONT = register_fonts()


def styles():
    s = getSampleStyleSheet()
    return {
        "body": ParagraphStyle(
            "Body", fontName=BODY_FONT, fontSize=9.3, leading=13.5,
            textColor=BLACK, spaceAfter=7, splitLongWords=True,
            allowWidows=0, allowOrphans=0,
        ),
        "lead": ParagraphStyle(
            "Lead", fontName=BODY_FONT, fontSize=12, leading=17,
            textColor=GRAPHITE, spaceAfter=14,
        ),
        "h1": ParagraphStyle(
            "H1", fontName=BOLD_FONT, fontSize=23, leading=25,
            textColor=BLACK, spaceBefore=8, spaceAfter=15, keepWithNext=True,
        ),
        "h2": ParagraphStyle(
            "H2", fontName=BOLD_FONT, fontSize=15, leading=18,
            textColor=BLACK, spaceBefore=15, spaceAfter=7, keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "H3", fontName=MONO_FONT, fontSize=9.5, leading=12,
            textColor=GRAPHITE, spaceBefore=12, spaceAfter=5,
            uppercase=True, keepWithNext=True,
        ),
        "h4": ParagraphStyle(
            "H4", fontName=BOLD_FONT, fontSize=10, leading=13,
            textColor=BLACK, spaceBefore=9, spaceAfter=4, keepWithNext=True,
        ),
        "small": ParagraphStyle(
            "Small", fontName=BODY_FONT, fontSize=7.6, leading=10.5,
            textColor=GRAPHITE, spaceAfter=4,
        ),
        "mono": ParagraphStyle(
            "Mono", fontName=MONO_FONT, fontSize=7.4, leading=10,
            textColor=BLACK, backColor=HexColor("#EEEAE0"),
            borderColor=LIGHT, borderWidth=.5, borderPadding=6, spaceAfter=8,
        ),
        "quote": ParagraphStyle(
            "Quote", fontName=BODY_FONT, fontSize=10.2, leading=15,
            textColor=GRAPHITE, leftIndent=13, borderColor=AMBER,
            borderWidth=0, borderLeft=2, borderPadding=8, spaceAfter=9,
        ),
        "callout": ParagraphStyle(
            "Callout", fontName=BOLD_FONT, fontSize=10.5, leading=14,
            textColor=BLACK, backColor=HexColor("#F2EBC9"),
            borderColor=AMBER, borderWidth=1, borderPadding=9, spaceAfter=10,
        ),
        "card_title": ParagraphStyle(
            "CardTitle", fontName=BOLD_FONT, fontSize=23, leading=25,
            textColor=BLACK, spaceAfter=12,
        ),
    }


S = styles()


def inline_markup(text: str) -> str:
    text = escape(text.strip())
    text = re.sub(r"`([^`]+)`", r'<font name="%s" color="#3A3A3A">\1</font>' % MONO_FONT, text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<u>\1</u>', text)
    return text


class Rule(Flowable):
    def __init__(self, color=AMBER, width=52, thickness=2, space=10):
        super().__init__()
        self.color, self.rule_width, self.thickness, self.height = color, width, thickness, space

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, self.height / 2, self.rule_width, self.height / 2)


class Diagram(Flowable):
    """Exact vector diagrams using authoritative product terminology."""

    def __init__(self, kind: str, title: str, height: float = 250):
        super().__init__()
        self.kind, self.title, self.height = kind, title, height
        self.width = 4.75 * inch

    def wrap(self, availWidth, availHeight):
        self.width = min(availWidth, 4.75 * inch)
        return self.width, self.height

    def label(self, c, x, y, text, size=7.5, color=BLACK, font=None, align="left"):
        c.setFont(font or MONO_FONT, size)
        c.setFillColor(color)
        if align == "center":
            c.drawCentredString(x, y, text)
        elif align == "right":
            c.drawRightString(x, y, text)
        else:
            c.drawString(x, y, text)

    def box(self, c, x, y, w, h, text="", fill=WHITE, stroke=GRAPHITE, text_color=BLACK, radius=3):
        c.setFillColor(fill)
        c.setStrokeColor(stroke)
        c.setLineWidth(.8)
        c.roundRect(x, y, w, h, radius, fill=1, stroke=1)
        if text:
            self.label(c, x + w / 2, y + h / 2 - 2.5, text, 7, text_color, MONO_FONT, "center")

    def arrow(self, c, x1, y1, x2, y2, color=GRAPHITE, width=1):
        c.setStrokeColor(color)
        c.setFillColor(color)
        c.setLineWidth(width)
        c.line(x1, y1, x2, y2)
        angle = 4
        if abs(x2 - x1) >= abs(y2 - y1):
            sign = 1 if x2 > x1 else -1
            c.line(x2, y2, x2 - sign * angle, y2 + angle / 2)
            c.line(x2, y2, x2 - sign * angle, y2 - angle / 2)
        else:
            sign = 1 if y2 > y1 else -1
            c.line(x2, y2, x2 + angle / 2, y2 - sign * angle)
            c.line(x2, y2, x2 - angle / 2, y2 - sign * angle)

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        c.setFillColor(OFFWHITE)
        c.roundRect(0, 0, w, h, 7, fill=1, stroke=0)
        self.label(c, 14, h - 20, self.title.upper(), 8.5, GRAPHITE, MONO_FONT)
        c.setStrokeColor(AMBER)
        c.setLineWidth(2)
        c.line(14, h - 27, 66, h - 27)
        getattr(self, f"draw_{self.kind}")(c, w, h - 36)

    def draw_pipeline(self, c, w, h):
        items = [("WORKFLOW", 56), ("SNAPSHOT", 58), ("PACKET", 54), ("ARTIFACT", 58), ("IMPLEMENT", 59)]
        x, y = 12, h / 2 - 12
        for i, (label, bw) in enumerate(items):
            fill = AMBER if label == "PACKET" else WHITE
            self.box(c, x, y, bw, 30, label, fill=fill)
            if i < len(items) - 1:
                self.arrow(c, x + bw + 3, y + 15, x + bw + 15, y + 15)
            x += bw + 17
        self.label(c, w / 2, y - 25, "THE GATE DECIDES. EXECUTION HAPPENS AFTER THE HANDOFF.", 6.7, MID, MONO_FONT, "center")

    def draw_boundary(self, c, w, h):
        split = w * .49
        c.setStrokeColor(GRAPHITE)
        c.setDash(3, 3)
        c.line(split, 25, split, h - 12)
        c.setDash()
        self.label(c, split - 10, h - 10, "DECISION LAYER", 7.2, GRAPHITE, MONO_FONT, "right")
        self.label(c, split + 10, h - 10, "EXECUTION LAYER", 7.2, GRAPHITE, MONO_FONT)
        self.box(c, 25, h / 2 - 10, 110, 42, "AUTONOMY GATE", fill=AMBER)
        self.box(c, 25, h / 2 - 65, 110, 30, "DECISION PACKET")
        self.arrow(c, 80, h / 2 - 13, 80, h / 2 - 32)
        ys = [h - 50, h / 2 - 8, 28]
        labels = ["PROJECT", "COWORK", "CODE_AGENT"]
        for y, label in zip(ys, labels):
            self.box(c, split + 35, y, 95, 30, label)
            self.arrow(c, split + 2, h / 2 - 50, split + 31, y + 15, AMBER)

    def draw_terminal(self, c, w, h):
        for row, (end, verdict, gate) in enumerate([
            ("RECOMMEND REFUND", "AUTONOMOUS", "NO MONEY MOVES"),
            ("ISSUE REFUND", "SUPERVISED", "GATE-1"),
        ]):
            y = h - 70 - row * 82
            x = 12
            for label, bw in [("REQUEST", 53), ("CHECK POLICY", 70), (end, 96)]:
                fill = AMBER if label == end else WHITE
                self.box(c, x, y, bw, 29, label, fill=fill)
                if label != end:
                    self.arrow(c, x + bw + 2, y + 14, x + bw + 13, y + 14)
                x += bw + 15
            self.box(c, x + 3, y, 77, 29, verdict, fill=BLACK, stroke=BLACK, text_color=WHITE)
            self.label(c, 12, y - 15, gate, 6.8, RED if gate.startswith("GATE") else MID, MONO_FONT)

    def draw_ladder(self, c, w, h):
        levels = [
            ("AUTONOMOUS", "NO PER-RUN APPROVAL", AMBER),
            ("SUPERVISED", "HUMAN APPROVES", WHITE),
            ("SOP_FIRST", "DOCUMENT FIRST", HexColor("#E6E1D5")),
            ("HUMAN_ONLY", "TERMINAL ACTION STAYS HUMAN", BLACK),
        ]
        y = h - 48
        for idx, (name, meaning, fill) in enumerate(levels):
            tc = WHITE if fill == BLACK else BLACK
            self.box(c, 40 + idx * 10, y - idx * 43, w - 80 - idx * 20, 31, "", fill=fill, stroke=GRAPHITE)
            self.label(c, 54 + idx * 10, y + 10 - idx * 43, name, 8, tc, MONO_FONT)
            self.label(c, w - 54 - idx * 10, y + 10 - idx * 43, meaning, 6.2, tc if fill == BLACK else GRAPHITE, MONO_FONT, "right")

    def draw_surfaces(self, c, w, h):
        data = [
            ("PROJECT", "HUMAN STARTS", "ANALYSIS + ARTIFACTS"),
            ("COWORK", "SCHEDULE / FILES", "WHEN CAPABILITIES EXIST"),
            ("CODE_AGENT", "CODE + APIS", "TESTS + ENFORCEMENT"),
            ("NO_AI", "NO AI EXECUTION", "HUMAN PROCESS"),
        ]
        y = h - 46
        for name, trigger, use in data:
            self.box(c, 15, y, 74, 28, name, fill=AMBER if name == "PROJECT" else WHITE)
            self.box(c, 100, y, 87, 28, trigger, fill=WHITE)
            self.box(c, 198, y, w - 213, 28, use, fill=WHITE)
            y -= 39

    def draw_matrix(self, c, w, h):
        left, bottom = 72, 38
        cw, ch = (w - 92) / 4, (h - 65) / 4
        cols = ["PROJECT", "COWORK", "CODE_AGENT", "NO_AI"]
        rows = ["AUTONOMOUS", "SUPERVISED", "SOP_FIRST", "HUMAN_ONLY"]
        valid = {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 3), (3, 3)}
        for j, col in enumerate(cols):
            self.label(c, left + j * cw + cw / 2, h - 18, col, 5.7, GRAPHITE, MONO_FONT, "center")
        for i, row in enumerate(rows):
            self.label(c, left - 8, bottom + (3 - i) * ch + ch / 2 - 2, row, 5.7, GRAPHITE, MONO_FONT, "right")
            for j in range(4):
                x, y = left + j * cw, bottom + (3 - i) * ch
                ok = (i, j) in valid
                c.setFillColor(AMBER if ok else HexColor("#E3DED2"))
                c.setStrokeColor(WHITE)
                c.rect(x, y, cw - 1, ch - 1, fill=1, stroke=1)
                if ok:
                    self.label(c, x + cw / 2, y + ch / 2 - 2, "VALID", 5.5, BLACK, MONO_FONT, "center")

    def draw_gates(self, c, w, h):
        gates = [
            ("GATE-1", "MOVES MONEY", "SUPERVISED", AMBER),
            ("GATE-2", "IRREVERSIBLE COMMITMENT", "HUMAN_ONLY", RED),
            ("GATE-3", "CHANGES ACCESS", "HUMAN_ONLY", RED),
            ("GATE-4", "SENSITIVE PUBLICATION", "SUPERVISED", AMBER),
            ("GATE-5", "NO LOG / ROLLBACK", "SUPERVISED", AMBER),
        ]
        y = h - 42
        for gid, condition, result, accent in gates:
            c.setFillColor(accent)
            c.rect(15, y, 7, 26, fill=1, stroke=0)
            self.box(c, 22, y, w - 37, 26, "", fill=WHITE, stroke=LIGHT)
            self.label(c, 32, y + 9, gid, 7.2, accent, MONO_FONT)
            self.label(c, 87, y + 9, condition, 6.4, GRAPHITE, MONO_FONT)
            self.label(c, w - 24, y + 9, result, 6.4, BLACK, MONO_FONT, "right")
            y -= 34

    def draw_packet(self, c, w, h):
        px, py, pw, ph = 55, 25, w - 110, h - 42
        c.setFillColor(WHITE)
        c.setStrokeColor(GRAPHITE)
        c.rect(px, py, pw, ph, fill=1, stroke=1)
        fields = [
            ("1", "TERMINAL ACTION", AMBER), ("2", "VERDICT + SURFACE", AMBER),
            ("3", "CONFIDENCE", GRAPHITE), ("4", "RULE / GATE IDS", BLUE),
            ("5", "CONTROLS", GRAPHITE), ("6", "EVIDENCE GAPS", GRAPHITE),
            ("7", "ARTIFACT REQUIRED", AMBER),
        ]
        y = py + ph - 28
        for num, label, accent in fields:
            c.setFillColor(accent)
            c.circle(px + 18, y + 4, 8, fill=1, stroke=0)
            self.label(c, px + 18, y + 1.5, num, 6.5, WHITE if accent != AMBER else BLACK, MONO_FONT, "center")
            self.label(c, px + 36, y, label, 6.8, BLACK, MONO_FONT)
            c.setStrokeColor(LIGHT)
            c.line(px + 36, y - 5, px + pw - 16, y - 5)
            y -= 23

    def draw_checkpoint(self, c, w, h):
        self.label(c, w * .25, h - 18, "NOTIFICATION THEATER", 7.2, RED, MONO_FONT, "center")
        self.label(c, w * .75, h - 18, "BLOCKING APPROVAL", 7.2, GRAPHITE, MONO_FONT, "center")
        for side in [0, 1]:
            x = 15 + side * (w / 2)
            y = h / 2
            self.box(c, x, y, 64, 29, "AI OUTPUT")
            self.arrow(c, x + 67, y + 14, x + 91, y + 14, RED if side == 0 else AMBER)
            if side == 0:
                self.box(c, x + 94, y, 59, 29, "EXECUTE", fill=RED, stroke=RED, text_color=WHITE)
                self.box(c, x + 43, y - 52, 72, 25, "REVIEWER NOTIFIED")
                c.setDash(2, 2)
                c.line(x + 79, y - 27, x + 79, y - 2)
                c.setDash()
            else:
                self.box(c, x + 94, y, 59, 29, "HOLD", fill=AMBER)
                self.box(c, x + 43, y - 52, 72, 25, "NAMED APPROVER")
                self.arrow(c, x + 79, y - 27, x + 117, y - 2, AMBER)
        c.setStrokeColor(LIGHT)
        c.line(w / 2, 20, w / 2, h - 26)

    def draw_lifecycle(self, c, w, h):
        labels = ["ASSESS", "REGISTER", "IMPLEMENT", "MONITOR", "REASSESS"]
        coords = [(w/2, h-42), (w-65, h/2+15), (w-92, 34), (92, 34), (65, h/2+15)]
        for i, ((x, y), label) in enumerate(zip(coords, labels)):
            self.box(c, x-34, y-12, 68, 24, label, fill=AMBER if label == "ASSESS" else WHITE)
            nx, ny = coords[(i+1) % len(coords)]
            self.arrow(c, x, y-15 if ny < y else y+15, nx, ny+15 if ny < y else ny-15, GRAPHITE)
        self.label(c, w/2, h/2-2, "INCIDENT / CHANGE", 7, RED, MONO_FONT, "center")

    def draw_handoff(self, c, w, h):
        self.box(c, w/2-52, h-53, 104, 34, "DECISION PACKET", fill=AMBER)
        lanes = [
            ("CLAUDE PROJECT", "COWORK", "CLAUDE CODE"),
            ("CHATGPT PROJECT", "", "CODEX"),
        ]
        y = h - 112
        for lane in lanes:
            x = 13
            active = [v for v in lane if v]
            bw = (w - 52) / len(active)
            for i, label in enumerate(active):
                self.box(c, x, y, bw - 10, 30, label)
                if i < len(active)-1:
                    self.arrow(c, x + bw - 7, y + 15, x + bw + 2, y + 15, AMBER)
                x += bw
            self.arrow(c, w/2, h-57, w/2, y+34, AMBER)
            y -= 61
        self.label(c, w/2, 10, "CONTROLS TRAVEL WITH THE PACKET", 6.8, GRAPHITE, MONO_FONT, "center")


class ChapterPage(Flowable):
    def __init__(self, number: str, title: str, subtitle: str):
        super().__init__()
        self.number, self.title, self.subtitle = number, title, subtitle
        self.height = 6.75 * inch

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        return availWidth, min(self.height, availHeight)

    def draw(self):
        c, w, h = self.canv, self.width, self.height
        c.setFillColor(BLACK)
        c.rect(-.55*inch, -.8*inch, w+1.1*inch, h+1.5*inch, fill=1, stroke=0)
        c.setFillColor(AMBER)
        c.setFont(MONO_FONT, 12)
        c.drawString(0, h-80, self.number)
        c.setFillColor(WHITE)
        c.setFont(BOLD_FONT, 31)
        y = h-130
        for line in self.title.upper().split("\n"):
            c.drawString(0, y, line)
            y -= 37
        c.setFillColor(AMBER)
        c.rect(0, y-5, 70, 3, fill=1, stroke=0)
        c.setFillColor(HexColor("#B7B3AA"))
        c.setFont(BODY_FONT, 11)
        text = c.beginText(0, y-38)
        text.setLeading(16)
        for line in self.subtitle.split("\n"):
            text.textLine(line)
        c.drawText(text)


def parse_markdown(path: Path, skip_first_h1=True):
    """Small, deterministic Markdown reader for the project's docs."""
    lines = path.read_text(encoding="utf-8").splitlines()
    out = []
    i = 0
    first_h1_skipped = False
    while i < len(lines):
        raw = lines[i]
        line = raw.rstrip()
        if not line.strip() or line.strip() == "---":
            i += 1
            continue
        if line.startswith("```"):
            lang = line[3:].strip()
            code = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            out.append(Preformatted("\n".join(code), S["mono"], maxLineLength=78))
            continue
        if re.match(r"^#{1,4}\s", line):
            m = re.match(r"^(#{1,4})\s+(.*)$", line)
            level, text = len(m.group(1)), m.group(2)
            if level == 1 and skip_first_h1 and not first_h1_skipped:
                first_h1_skipped = True
                i += 1
                continue
            out.append(Paragraph(inline_markup(text), S[f"h{level}"]))
            i += 1
            continue
        if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-+", lines[i+1]):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [x.strip() for x in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c.replace(" ", "")) for c in cells):
                    rows.append([Paragraph(inline_markup(c), S["small"]) for c in cells])
                i += 1
            if rows:
                cols = max(len(r) for r in rows)
                for r in rows:
                    r.extend([""] * (cols-len(r)))
                table = Table(rows, colWidths=[4.65*inch/cols]*cols, repeatRows=1, hAlign="LEFT")
                table.setStyle(TableStyle([
                    ("FONTNAME", (0,0), (-1,0), BOLD_FONT),
                    ("BACKGROUND", (0,0), (-1,0), BLACK),
                    ("TEXTCOLOR", (0,0), (-1,0), WHITE),
                    ("VALIGN", (0,0), (-1,-1), "TOP"),
                    ("GRID", (0,0), (-1,-1), .35, LIGHT),
                    ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, HexColor("#F4F1E8")]),
                    ("LEFTPADDING", (0,0), (-1,-1), 5),
                    ("RIGHTPADDING", (0,0), (-1,-1), 5),
                    ("TOPPADDING", (0,0), (-1,-1), 4),
                    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
                ]))
                out.extend([table, Spacer(1, 7)])
            continue
        if re.match(r"^\s*[-*]\s+", line) or re.match(r"^\s*\d+\.\s+", line):
            ordered = bool(re.match(r"^\s*\d+\.\s+", line))
            items = []
            pattern = r"^\s*\d+\.\s+" if ordered else r"^\s*[-*]\s+"
            while i < len(lines) and re.match(pattern, lines[i]):
                txt = re.sub(pattern, "", lines[i]).strip()
                items.append(ListItem(Paragraph(inline_markup(txt), S["body"]), leftIndent=12))
                i += 1
            out.append(ListFlowable(items, bulletType="1" if ordered else "bullet", leftIndent=18, bulletFontName=MONO_FONT, bulletFontSize=7, spaceAfter=5))
            continue
        if line.startswith(">"):
            text = line.lstrip("> ")
            out.append(Paragraph(inline_markup(text), S["quote"]))
            i += 1
            continue
        para = [line.strip()]
        i += 1
        while i < len(lines):
            nxt = lines[i].rstrip()
            if (not nxt.strip() or nxt.strip() == "---" or nxt.startswith("#") or nxt.startswith("```")
                or nxt.startswith("|") or nxt.startswith(">") or re.match(r"^\s*[-*]\s+", nxt)
                or re.match(r"^\s*\d+\.\s+", nxt)):
                break
            para.append(nxt.strip())
            i += 1
        out.append(Paragraph(inline_markup(" ".join(para)), S["body"]))
    return out


class GateDocTemplate(BaseDocTemplate):
    def __init__(self, filename, **kw):
        super().__init__(filename, pagesize=PAGE, leftMargin=.62*inch, rightMargin=.62*inch,
                         topMargin=.68*inch, bottomMargin=.62*inch, **kw)
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="body")
        self.addPageTemplates(PageTemplate(id="main", frames=frame, onPage=self.draw_page))

    def draw_page(self, canv, doc):
        page = canv.getPageNumber()
        if page == 1:
            return
        canv.saveState()
        canv.setStrokeColor(LIGHT)
        canv.setLineWidth(.5)
        canv.line(self.leftMargin, PAGE[1]-.38*inch, PAGE[0]-self.rightMargin, PAGE[1]-.38*inch)
        canv.setFont(MONO_FONT, 6.7)
        canv.setFillColor(MID)
        canv.drawString(self.leftMargin, PAGE[1]-.30*inch, "THE AUTONOMY GATE — OPERATOR FIELD MANUAL")
        canv.drawRightString(PAGE[0]-self.rightMargin, .31*inch, f"{page:03d}")
        canv.restoreState()

    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            style = flowable.style.name
            if style in ("H1", "H2", "OutlineOnly"):
                level = 0 if style in ("H1", "OutlineOnly") else 1
                text = flowable.getPlainText()
                key = "h%d-%s" % (level, abs(hash(text)))
                self.canv.bookmarkPage(key)
                self.canv.addOutlineEntry(text, key, level=level, closed=False)
                if style != "OutlineOnly":
                    self.notify("TOCEntry", (level, text, self.page, key))


def cover_story():
    toc_title = ParagraphStyle("OutlineOnly", parent=S["h1"])
    return [
        ChapterPage("FIELD MANUAL 01", "THE AUTONOMY\nGATE", "Minimum justified autonomy for every workflow.\nOwner manual · public edition · version 1.0"),
        PageBreak(),
        Paragraph("Capability is not authority.", ParagraphStyle("Statement", parent=S["h1"], fontSize=27, leading=31, textColor=BLACK, spaceAfter=18)),
        Rule(),
        Paragraph("The Autonomy Gate receives a business workflow, decides how much authority AI should have, assigns the right execution surface, and produces the document required before anyone acts.", S["lead"]),
        Spacer(1, 25),
        Diagram("pipeline", "The Gate In One Page", 170),
        Spacer(1, 14),
        Paragraph("The Gate decides. It does not execute the workflow.", S["callout"]),
        PageBreak(),
        Paragraph("Contents", toc_title),
        Rule(),
        TableOfContents(),
        PageBreak(),
    ]


def part(number, title, subtitle, diagrams=()):
    story = [ChapterPage(number, title, subtitle), PageBreak()]
    for kind, name, height in diagrams:
        story.extend([Diagram(kind, name, height), Spacer(1, 14)])
    return story


def build_manual():
    story = cover_story()
    story += part("PART I", "START", "Install the Gate. Run the first workflow.\nUnderstand what happens next.", [
        ("boundary", "Decision, Not Execution", 220),
    ])
    story += parse_markdown(DOCS / "START_HERE.md")

    story += [PageBreak()]
    story += part("PART II", "UNDERSTAND", "Terminal action, consequence, autonomy,\nsurface, confidence, and hard gates.", [
        ("terminal", "Terminal Action Changes The Verdict", 225),
        ("ladder", "Four Autonomy Levels", 235),
        ("surfaces", "Four Execution Surfaces", 220),
        ("matrix", "The Two-Axis Verdict Matrix", 235),
        ("gates", "The Five Hard Gates", 240),
    ])
    story += parse_markdown(DOCS / "OWNER_MANUAL.md")

    story += [PageBreak()]
    story += part("PART III", "ACT", "Read the packet. Use the artifact.\nImplement the required controls.", [
        ("packet", "Anatomy Of A Decision Packet", 240),
        ("checkpoint", "A Real Approval Checkpoint Blocks Execution", 220),
    ])
    story += parse_markdown(DOCS / "VERDICT_PLAYBOOK.md")
    story += [PageBreak()]
    story += parse_markdown(DOCS / "ARTIFACT_GUIDE.md")

    story += [PageBreak()]
    story += part("PART IV", "APPLY", "Build calibration through representative workflows.\nDiagnose surprises without weakening the Gate.")
    story += parse_markdown(DOCS / "USE_CASE_COOKBOOK.md")
    story += [PageBreak()]
    story += parse_markdown(DOCS / "TROUBLESHOOTING.md")

    story += [PageBreak()]
    story += part("PART V", "SCALE", "Turn individual verdicts into an operating system.\nCarry governance across execution surfaces.", [
        ("lifecycle", "Governance Registry Lifecycle", 225),
        ("handoff", "The Packet Travels Across Surfaces", 230),
    ])
    story += parse_markdown(DOCS / "GOVERNANCE_REGISTRY_TEMPLATE.md")
    story += [PageBreak()]
    story += parse_markdown(DOCS / "POWER_USER_GUIDE.md")

    story += [PageBreak()]
    story += part("APPENDIX", "REFERENCE", "Terms, platform assumptions, and source notes.")
    story += parse_markdown(DOCS / "GLOSSARY.md")
    story += [PageBreak()]
    story += parse_markdown(DOCS / "reference" / "SOURCES.md")
    story += [
        Paragraph("Official Links", S["h2"]),
        Paragraph("Claude Projects", S["h3"]),
        Paragraph("https://support.claude.com/en/articles/9517075-what-are-projects", S["small"]),
        Paragraph("Claude Code Memory", S["h3"]),
        Paragraph("https://code.claude.com/docs/en/memory", S["small"]),
        Paragraph("ChatGPT Projects", S["h3"]),
        Paragraph("https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt", S["small"]),
        Paragraph("OpenAI Codex Documentation", S["h3"]),
        Paragraph("https://developers.openai.com/codex", S["small"]),
    ]

    story += [PageBreak(), Paragraph("Workflow Intake Worksheet", S["h1"]), Rule()]
    fields = ["Workflow name", "Who starts it", "Trigger", "Inputs", "Steps", "Systems touched", "Terminal action", "Who uses the output", "Worst realistic failure", "Reversibility", "Known exceptions", "Desired automation"]
    data = []
    for f in fields:
        data.append([Paragraph(f"<b>{f}</b>", S["small"]), ""])
    worksheet = Table(data, colWidths=[1.35*inch, 3.3*inch], rowHeights=[.42*inch]*len(data))
    worksheet.setStyle(TableStyle([("GRID",(0,0),(-1,-1),.45,LIGHT), ("VALIGN",(0,0),(-1,-1),"TOP"), ("BACKGROUND",(0,0),(0,-1),HexColor("#F0ECE2")), ("LEFTPADDING",(0,0),(-1,-1),6), ("TOPPADDING",(0,0),(-1,-1),6)]))
    story.append(worksheet)

    output = OUT / "AUTONOMY_GATE_FIELD_MANUAL_6x9.pdf"
    doc = GateDocTemplate(str(output), title="The Autonomy Gate — Operator Field Manual", author="Ariel Ortiz")
    doc.multiBuild(story)
    return output


def draw_gate_symbol(c, x, y, scale=1.0):
    c.setStrokeColor(AMBER)
    c.setLineWidth(2.4 * scale)
    c.line(x, y, x + 30*scale, y)
    c.rect(x + 30*scale, y - 17*scale, 24*scale, 34*scale, fill=0, stroke=1)
    c.line(x + 54*scale, y, x + 88*scale, y)


def card_base(c, size, dark=False):
    w, h = size
    c.setFillColor(BLACK if dark else OFFWHITE)
    c.rect(0, 0, w, h, fill=1, stroke=0)
    c.setStrokeColor(AMBER)
    c.setLineWidth(2)
    c.line(.35*inch, h-.38*inch, w-.35*inch, h-.38*inch)


def build_quick_card():
    p = OUT / "AUTONOMY_GATE_QUICK_START_CARD_5x7.pdf"
    c = canvas.Canvas(str(p), pagesize=CARD_QUICK)
    c.setTitle("The Autonomy Gate — Quick-Start Card")
    c.setAuthor("Ariel Ortiz")
    w, h = CARD_QUICK
    card_base(c, CARD_QUICK)
    c.setFillColor(BLACK); c.setFont(BOLD_FONT, 21); c.drawString(.38*inch, h-.78*inch, "RUN YOUR FIRST GATE")
    c.setFont(MONO_FONT, 7); c.setFillColor(GRAPHITE); c.drawString(.38*inch, h-1.02*inch, "QUICK-START CARD · VERSION 1.0")
    steps = [
        ("01", "CREATE A PROJECT", "Claude Project or ChatGPT Project"),
        ("02", "LOAD THE OPERATOR", "Add the operator files listed in the manual"),
        ("03", "PASTE A WORKFLOW", "Describe what it does and what can go wrong"),
        ("04", "CHECK TERMINAL ACTION", "Then read verdict, surface, and artifact"),
    ]
    y = h-1.52*inch
    for num, title, detail in steps:
        c.setFillColor(AMBER); c.roundRect(.38*inch,y-.03*inch,.34*inch,.34*inch,3,fill=1,stroke=0)
        c.setFillColor(BLACK); c.setFont(MONO_FONT,8); c.drawCentredString(.55*inch,y+.075*inch,num)
        c.setFont(BOLD_FONT,9.5); c.drawString(.84*inch,y+.10*inch,title)
        c.setFont(BODY_FONT,7.6); c.setFillColor(GRAPHITE); c.drawString(.84*inch,y-.08*inch,detail)
        y -= .69*inch
    c.setFillColor(BLACK); c.roundRect(.38*inch,.45*inch,w-.76*inch,1.34*inch,5,fill=1,stroke=0)
    c.setFillColor(AMBER); c.setFont(MONO_FONT,7); c.drawString(.55*inch,1.52*inch,"FIRST TEST")
    c.setFillColor(WHITE); c.setFont(BODY_FONT,7.7)
    text = c.beginText(.55*inch,1.27*inch); text.setLeading(10)
    for line in ["We generate a weekly KPI report every Monday.", "A human provides stable exports. Produce a", "Slack-ready narrative summary. Errors are", "correctable by posting a revised report."]:
        text.textLine(line)
    c.drawText(text)
    c.showPage()
    card_base(c, CARD_QUICK, dark=True)
    c.setFillColor(WHITE); c.setFont(BOLD_FONT,18); c.drawString(.38*inch,h-.78*inch,"READ THE OUTPUT")
    y=h-1.45*inch
    for num,title,detail in [
        ("1","SNAPSHOT","Confirm the Gate understood the workflow."),
        ("2","DECISION PACKET","Read verdict, surface, confidence, and controls."),
        ("3","ARTIFACT","Use the document to implement the decision."),
    ]:
        c.setFillColor(AMBER); c.circle(.58*inch,y+.05*inch,.17*inch,fill=1,stroke=0)
        c.setFillColor(BLACK); c.setFont(MONO_FONT,8); c.drawCentredString(.58*inch,y+.015*inch,num)
        c.setFillColor(WHITE); c.setFont(BOLD_FONT,10); c.drawString(.88*inch,y+.09*inch,title)
        c.setFillColor(HexColor("#C7C4BC")); c.setFont(BODY_FONT,7.7); c.drawString(.88*inch,y-.10*inch,detail)
        y-=.9*inch
    draw_gate_symbol(c,.55*inch,1.62*inch,1.15)
    c.setFillColor(WHITE); c.setFont(BOLD_FONT,12); c.drawString(.55*inch,1.10*inch,"THE GATE DECIDES.")
    c.setFillColor(AMBER); c.drawString(.55*inch,.83*inch,"IT DOES NOT EXECUTE.")
    c.setFillColor(HexColor("#AAA79F")); c.setFont(MONO_FONT,6.8); c.drawString(.55*inch,.42*inch,"CHECK THE TERMINAL ACTION BEFORE ACTING.")
    c.save()
    return p


def build_verdict_card():
    p = OUT / "AUTONOMY_GATE_VERDICT_CARD_4x6.pdf"
    c = canvas.Canvas(str(p), pagesize=CARD_VERDICT)
    c.setTitle("The Autonomy Gate — Verdict Reference Card")
    c.setAuthor("Ariel Ortiz")
    w,h=CARD_VERDICT
    card_base(c,CARD_VERDICT,dark=True)
    c.setFillColor(WHITE); c.setFont(BOLD_FONT,17); c.drawString(.3*inch,h-.72*inch,"AUTONOMY")
    c.setFont(MONO_FONT,6.5); c.setFillColor(AMBER); c.drawString(.3*inch,h-.94*inch,"HOW MUCH AUTHORITY DOES AI GET?")
    rows=[
        ("AUTONOMOUS","NO PER-RUN APPROVAL",AMBER,BLACK),
        ("SUPERVISED","HUMAN APPROVES",WHITE,BLACK),
        ("SOP_FIRST","DOCUMENT THE PROCESS",HexColor("#B8B4AA"),BLACK),
        ("HUMAN_ONLY","TERMINAL ACTION STAYS HUMAN",RED,WHITE),
    ]
    y=h-1.45*inch
    for name,detail,fill,tc in rows:
        c.setFillColor(fill); c.roundRect(.3*inch,y-.1*inch,w-.6*inch,.58*inch,3,fill=1,stroke=0)
        c.setFillColor(tc); c.setFont(BOLD_FONT,8.5); c.drawString(.42*inch,y+.20*inch,name)
        c.setFont(MONO_FONT,5.7); c.drawRightString(w-.42*inch,y+.20*inch,detail)
        y-=.76*inch
    c.setFillColor(HexColor("#AAA79F")); c.setFont(MONO_FONT,6.1); c.drawString(.3*inch,.36*inch,"MINIMUM JUSTIFIED AUTONOMY — NOT MAXIMUM CAPABILITY")
    c.showPage()
    card_base(c,CARD_VERDICT)
    c.setFillColor(BLACK); c.setFont(BOLD_FONT,17); c.drawString(.3*inch,h-.72*inch,"SURFACES")
    c.setFont(MONO_FONT,6.5); c.setFillColor(GRAPHITE); c.drawString(.3*inch,h-.94*inch,"WHERE DOES THE GOVERNED WORK RUN?")
    rows=[
        ("PROJECT","HUMAN-INITIATED ANALYSIS"),
        ("COWORK","SCHEDULED / LOCAL FILE WORK"),
        ("CODE_AGENT","CODE, APIS, TESTS, ENFORCEMENT"),
        ("NO_AI","HUMAN PROCESS ONLY"),
    ]
    y=h-1.38*inch
    for name,detail in rows:
        c.setStrokeColor(LIGHT); c.line(.3*inch,y-.12*inch,w-.3*inch,y-.12*inch)
        c.setFillColor(AMBER); c.setFont(BOLD_FONT,8.7); c.drawString(.3*inch,y+.12*inch,name)
        c.setFillColor(GRAPHITE); c.setFont(MONO_FONT,5.8); c.drawRightString(w-.3*inch,y+.12*inch,detail)
        y-=.63*inch
    c.setFillColor(BLACK); c.roundRect(.3*inch,.45*inch,w-.6*inch,1.22*inch,4,fill=1,stroke=0)
    c.setFillColor(AMBER); c.setFont(MONO_FONT,6.5); c.drawString(.43*inch,1.42*inch,"HARD GATES")
    c.setFillColor(WHITE); c.setFont(MONO_FONT,5.8)
    for idx,line in enumerate(["1 MONEY   2 COMMITMENT   3 ACCESS", "4 SENSITIVE PUBLICATION   5 NO LOG/ROLLBACK"]):
        c.drawString(.43*inch,(1.14-idx*.24)*inch,line)
    c.setFillColor(RED); c.setFont(BOLD_FONT,7.5); c.drawString(.43*inch,.62*inch,"GATE-2 + GATE-3 → HUMAN_ONLY")
    c.save()
    return p


def main():
    manual = build_manual()
    quick = build_quick_card()
    verdict = build_verdict_card()
    print(manual)
    print(quick)
    print(verdict)


if __name__ == "__main__":
    main()
