#!/usr/bin/env python3
"""
Common Engine for generating IELTS & CEFR Reading Mock Exam Markdown Files.
"""

import os

OUT_DIR = "/Users/chandara-dgc/Documents/learn-english/reading_skills/examples"

def build_topic_markdown(t):
    md = []
    num = t["num"]
    title = t["title"]
    title_kh = t["title_kh"]
    qtype = t.get("qtype", "True / False / Not Given & Reading Comprehension")
    
    md.append(f"## {num}. {title}")
    md.append(f"### {title_kh}\n")
    md.append(f"**Theme:** {t['theme_name']} · **Exam Focus:** IELTS Academic & General / CEFR Reading")
    md.append(f"**Target Question Format:** {qtype}\n")
    
    md.append("### 📚 Key Academic Vocabulary & Khmer Glossary (វាក្យសព្ទគន្លឹះ)\n")
    md.append("| Term | PoS | Level | Academic Definition | អត្ថន័យជាភាសាខ្មែរ |")
    md.append("| :--- | :--- | :--- | :--- | :--- |")
    for row in t["vocab"]:
        word, pos, cefr, defn, kh = row
        md.append(f"| **{word}** | {pos} | {cefr} | {defn} | {kh} |")
    md.append("\n---\n")
    
    md.append("### 📖 Adaptive Reading Passages (អត្ថបទអានសម្របតាមកម្រិតទាំង ៤: B1 · B2 · C1 · C2)\n")
    
    # B1
    md.append("#### 🟡 B1 Level — Intermediate (IELTS 4.5–5.0 · ~150 words)")
    for p in t["b1"].strip().split("\n\n"):
        md.append(f"> {p.strip()}\n>")
    md.append("\n")
    
    # B2
    md.append("#### 🔴 B2 Level — Upper-Intermediate (IELTS 5.5–6.5 · ~200 words)")
    for p in t["b2"].strip().split("\n\n"):
        md.append(f"> {p.strip()}\n>")
    md.append("\n")
    
    # C1
    md.append("#### 🟣 C1 Level — Advanced (IELTS 7.0–8.0 · ~250 words)")
    for p in t["c1"].strip().split("\n\n"):
        md.append(f"> {p.strip()}\n>")
    md.append("\n")
    
    # C2
    md.append("#### ⚫ C2 Level — Proficiency (IELTS 8.5–9.0 · ~250 words)")
    for p in t["c2"].strip().split("\n\n"):
        md.append(f"> {p.strip()}\n>")
    md.append("\n")
    
    md.append("---\n")
    md.append("### 📝 Mock Exam Questions (IELTS Reading Style)\n")
    q_instr = t.get("q_instruction", "Do the following statements agree with the information given in the reading passages above?\n*Write:*\n- **TRUE** if the statement agrees with the information\n- **FALSE** if the statement contradicts the information\n- **NOT GIVEN** if there is no information on this")
    md.append(f"**{q_instr}**\n")
    for q_num, q_text in t["questions"]:
        md.append(f"{q_num}. {q_text}")
    md.append("\n---\n")
    
    md.append("### 🔑 Answer Key & Explanatory Walkthrough (ចម្លើយ និងការពន្យល់លម្អិតជាភាសាខ្មែរ)\n")
    for q_num, ans, evidence, kh_exp in t["answers"]:
        md.append(f"- **Question {q_num}: {ans}**")
        md.append(f"  - *Evidence in Text:* {evidence}")
        md.append(f"  - *Khmer Analysis:* {kh_exp}")
    md.append("\n---\n")
    
    return "\n".join(md)

def write_theme_file(filename, theme_title, theme_kh, theme_desc, topics):
    filepath = os.path.join(OUT_DIR, filename)
    os.makedirs(OUT_DIR, exist_ok=True)
    
    lines = []
    lines.append(f"# 📖 IELTS & CEFR Reading Mock Exams — {theme_title}")
    lines.append(f"## {theme_kh}\n")
    lines.append(f"> Part of the **[100 Real IELTS & CEFR Reading Mock Topics (B1–C2)](ielts_00_index.md)** library.")
    lines.append(f"> {theme_desc}\n")
    lines.append("## 📑 Table of Topics in this Volume\n")
    lines.append("| # | Topic Title | Reading Question Type Focus | Target Levels |")
    lines.append("| :- | :--- | :--- | :--- |")
    for t in topics:
        lines.append(f"| {t['num']} | [{t['title']}](#{t['num']}-{t['title'].lower().replace(' ', '-').replace(',', '').replace('&', '').replace(':', '').replace('.', '').replace('/', '')}) | {t.get('qtype', 'True/False/Not Given')} | B1 · B2 · C1 · C2 |")
    lines.append("\n---\n")
    
    for t in topics:
        lines.append(build_topic_markdown(t))
        
    content = "\n".join(lines)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[+] Successfully generated: {filepath} ({len(topics)} topics, {len(content)} bytes)")
