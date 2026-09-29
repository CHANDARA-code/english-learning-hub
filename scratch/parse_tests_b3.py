import os
import re

RAW_DIR = "/Users/chandara-dgc/Documents/learn-english/scratch/ielts_raw"

def parse_test(test_num):
    raw_path = os.path.join(RAW_DIR, f"test_{test_num:02d}.txt")
    if not os.path.exists(raw_path):
        print(f"File not found: {raw_path}")
        return
    with open(raw_path, "r", encoding="utf-8") as f:
        text = f.read()

    ans_match = re.search(r"Answer\s+Listening\s+Practice\s+Test\s+\d+", text, re.IGNORECASE)
    ans_text = ""
    content_text = text
    if ans_match:
        content_text = text[:ans_match.start()]
        ans_text = text[ans_match.start():]

    print(f"=== TEST {test_num:02d} ===")
    print(f"Content length: {len(content_text)}, Answer text length: {len(ans_text)}")
    
    ans_sections = {}
    cur_sec = None
    for line in ans_text.splitlines():
        line = line.strip()
        m_sec = re.match(r"Section\s+([1-4])(.*)", line, re.IGNORECASE)
        if m_sec:
            cur_sec = int(m_sec.group(1))
            ans_sections[cur_sec] = []
            rem = m_sec.group(2).strip()
            if rem:
                ans_sections[cur_sec].append(rem)
            continue
        if cur_sec:
            if line and not any(line.startswith(x) for x in ["Answer", "Listening Test", "Advertisements"]):
                ans_sections[cur_sec].append(line)
                
    for s in range(1, 5):
        items = ans_sections.get(s, [])
        print(f"  Sec {s} answers ({len(items)} items): {items[:3]} ... {items[-2:] if len(items) > 2 else ''}")

if __name__ == "__main__":
    for i in range(22, 29):
        parse_test(i)
