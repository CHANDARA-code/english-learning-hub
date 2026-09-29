#!/usr/bin/env python3
import os
import re

OUTPUT_FILE = "/Users/chandara-dgc/Documents/learn-english/english_vocabulary.md"

PARTS = [
    ("a1_part1.md", 1, 250),
    ("a1_part2.md", 251, 500),
    ("a1_part3.md", 501, 750),
    ("a1_part4.md", 751, 1000),
    ("a2_part1.md", 1001, 1250),
    ("a2_part2.md", 1251, 1500),
    ("a2_part3.md", 1501, 1750),
    ("a2_part4.md", 1751, 2000),
    ("b1_part1.md", 2001, 2250),
    ("b1_part2.md", 2251, 2500),
    ("b1_part3.md", 2501, 2750),
    ("b1_part4.md", 2751, 3000),
    ("b1_part5.md", 3001, 3250),
    ("b1_part6.md", 3251, 3500),
    ("b2_part1.md", 3501, 3750),
    ("b2_part2.md", 3751, 4000),
    ("b2_part3.md", 4001, 4250),
    ("b2_part4.md", 4251, 4500),
    ("b2_part5.md", 4501, 4750),
    ("b2_part6.md", 4751, 5000),
]

def check_status():
    base_dir = "/Users/chandara-dgc/Documents/learn-english"
    total_found = 0
    missing = []
    for fname, start_exp, end_exp in PARTS:
        fpath = os.path.join(base_dir, fname)
        if not os.path.exists(fpath):
            missing.append(fname)
            print(f"[-] {fname}: MISSING")
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        entries = re.findall(r'^###\s+(\d+)\.\s+(.*?)$', content, re.MULTILINE)
        count = len(entries)
        total_found += count
        first = entries[0][0] if entries else "N/A"
        last = entries[-1][0] if entries else "N/A"
        print(f"[+] {fname}: {count} words (range {first}-{last})")
    print(f"\nTotal words ready: {total_found} / 5000")
    return missing

def merge():
    base_dir = "/Users/chandara-dgc/Documents/learn-english"
    header = """# 📚 Complete English Vocabulary Guide (A1 · A2 · B1 · B2)
## វចនានុក្រមភាសាអង់គ្លេសពេញលេញកម្រិត A1 ដល់ B2 ជាមួយការបកប្រែជាភាសាខ្មែរ

> **Total Words:** 5,000 words  
> **Levels:** A1 (Beginner: 1–1,000) · A2 (Elementary: 1,001–2,000) · B1 (Intermediate: 2,001–3,500) · B2 (Upper Intermediate: 3,501–5,000)  
> **Content per word:** English word · Part of Speech · Accurate Khmer Translation · 3 CEFR-leveled Example Sentences  

---

## 📑 Table of Contents (មាតិកា)

- [🟢 Level A1 — Beginner (Words 1–1000)](#-level-a1--beginner-words-11000)
  - [Part 1: Basic Objects & Everyday Nouns (1–250)](#a1-part-1-basic-objects--everyday-nouns-1250)
  - [Part 2: Home, School & Common Places (251–500)](#a1-part-2-home-school--common-places-251500)
  - [Part 3: Actions, Time & Daily Life (501–750)](#a1-part-3-actions-time--daily-life-501750)
  - [Part 4: Nature, Body & Simple Descriptions (751–1000)](#a1-part-4-nature-body--simple-descriptions-7511000)
- [🔵 Level A2 — Elementary (Words 1001–2000)](#-level-a2--elementary-words-10012000)
  - [Part 1: Travel, Transport & Places (1001–1250)](#a2-part-1-travel-transport--places-10011250)
  - [Part 2: Shopping, Food & Services (1251–1500)](#a2-part-2-shopping-food--services-12511500)
  - [Part 3: People, Feelings & Relationships (1501–1750)](#a2-part-3-people-feelings--relationships-15011750)
  - [Part 4: Health, Hobbies & Free Time (1751–2000)](#a2-part-4-health-hobbies--free-time-17512000)
- [🟡 Level B1 — Intermediate (Words 2001–3500)](#-level-b1--intermediate-words-20013500)
  - [Part 1: Work & Career (2001–2250)](#b1-part-1-work--career-20012250)
  - [Part 2: Education & Learning (2251–2500)](#b1-part-2-education--learning-22512500)
  - [Part 3: Society & Community (2501–2750)](#b1-part-3-society--community-25012750)
  - [Part 4: Environment & Nature (2751–3000)](#b1-part-4-environment--nature-27513000)
  - [Part 5: Technology & Media (3001–3250)](#b1-part-5-technology--media-30013250)
  - [Part 6: Culture, Travel & Arts (3251–3500)](#b1-part-6-culture-travel--arts-32513500)
- [🔴 Level B2 — Upper Intermediate (Words 3501–5000)](#-level-b2--upper-intermediate-words-35015000)
  - [Part 1: Academic Language (3501–3750)](#b2-part-1-academic-language-35013750)
  - [Part 2: Economics & Business (3751–4000)](#b2-part-2-economics--business-37514000)
  - [Part 3: Politics & Law (4001–4250)](#b2-part-3-politics--law-40014250)
  - [Part 4: Science & Research (4251–4500)](#b2-part-4-science--research-42514500)
  - [Part 5: Psychology & Behavior (4501–4750)](#b2-part-5-psychology--behavior-45014750)
  - [Part 6: Philosophy & Abstract Ideas (4751–5000)](#b2-part-6-philosophy--abstract-ideas-47515000)

---

## 🟢 Level A1 — Beginner (Words 1–1000)

"""
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write(header)
        for fname, start_exp, end_exp in PARTS:
            fpath = os.path.join(base_dir, fname)
            with open(fpath, "r", encoding="utf-8") as inf:
                c = inf.read().strip()
            
            # Clean up duplicate headers if needed
            if fname == "a2_part1.md":
                out.write("\n\n---\n\n## 🔵 Level A2 — Elementary (Words 1001–2000)\n\n")
            elif fname == "b1_part1.md":
                out.write("\n\n---\n\n## 🟡 Level B1 — Intermediate (Words 2001–3500)\n\n")
            elif fname == "b2_part1.md":
                out.write("\n\n---\n\n## 🔴 Level B2 — Upper Intermediate (Words 3501–5000)\n\n")
            
            out.write("\n\n" + c + "\n")
        
        out.write("""
---

## 🎉 Congratulations! អបអរសាទរ!

អ្នកបានបញ្ចប់បញ្ជីពាក្យគន្លឹះភាសាអង់គ្លេសចំនួន **5,000 ពាក្យ** ចាប់ពីកម្រិត **A1 ដល់ B2** រួចរាល់ហើយ!

- **Level A1 (1–1,000):** ពាក្យមូលដ្ឋានប្រចាំថ្ងៃ វត្ថុជុំវិញខ្លួន គ្រួសារ សកម្មភាពសាមញ្ញ
- **Level A2 (1,001–2,000):** ការធ្វើដំណើរ ម្ហូបអាហារ អារម្មណ៍ សុខភាព ចំណង់ចំណូលចិត្ត
- **Level B1 (2,001–3,500):** ការងារ ការអប់រំ សង្គម បរិស្ថាន បច្ចេកវិទ្យា និងវប្បធម៌
- **Level B2 (3,501–5,000):** ការស្រាវជ្រាវសិក្សា សេដ្ឋកិច្ច នយោបាយ ច្បាប់ វិទ្យាសាស្ត្រ ចិត្តវិទ្យា ទស្សនវិជ្ជា

💡 **គន្លឹះរៀនឱ្យមានប្រសិទ្ធភាព:**
1. រៀនមួយថ្ងៃ ២០–៣០ ពាក្យ
2. អានប្រយោគគំរូទាំង ៣ ឱ្យឮៗ
3. សាកល្បងតែងប្រយោគផ្ទាល់ខ្លួនដោយប្រើពាក្យទាំងនោះ
""")

    print(f"\nMerged successfully into {OUTPUT_FILE}!")

if __name__ == "__main__":
    missing = check_status()
    if not missing:
        merge()
