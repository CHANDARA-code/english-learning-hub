#!/usr/bin/env python3
"""
Generate Master Index for Reading Skills Bank:
reading_skills/examples/ielts_00_index.md
"""

THEMES = [
    {
        "file": "ielts_01_education.md",
        "num": "01",
        "title": "Education & Learning",
        "title_kh": "ការអប់រំ និងការសិក្សា",
        "range": "1–10",
        "topics": [
            (1, "The Evolution of Virtual Classrooms and Online Higher Education"),
            (2, "Bilingual Education and Childhood Cognitive Plasticity"),
            (3, "Standardized Testing versus Holistic Evaluation"),
            (4, "STEM Education and Modern Workforce Demands"),
            (5, "Lifelong Learning and Adult Re-skilling in the Automated Age"),
            (6, "Early Childhood Education and Socioeconomic Equity"),
            (7, "The Role of Arts and Humanities in Modern Technical Curricula"),
            (8, "Open Educational Resources and the Democratization of Knowledge"),
            (9, "Critical Thinking Pedagogies in the Information Age"),
            (10, "Inclusive Education for Students with Special Needs")
        ]
    },
    {
        "file": "ielts_02_technology.md",
        "num": "02",
        "title": "Technology, AI & Digital Life",
        "title_kh": "បច្ចេកវិទ្យា បញ្ញាសិប្បនិម្មិត និងជីវិតឌីជីថល",
        "range": "11–20",
        "topics": [
            (11, "Generative Artificial Intelligence and Creative Labor"),
            (12, "Algorithmic Bias and Discrimination in Machine Learning"),
            (13, "Data Privacy and Surveillance Capitalism"),
            (14, "The Digital Divide and Global Technological Inequality"),
            (15, "Autonomous Vehicles and Urban Mobility Systems"),
            (16, "Social Media Algorithms and Psychological Well-being"),
            (17, "Blockchain Technology and Decentralized Governance"),
            (18, "Cybersecurity Infrastructures in an Hyperconnected World"),
            (19, "Smart Home Automation and the Internet of Things"),
            (20, "Virtual and Augmented Reality in Professional Training")
        ]
    },
    {
        "file": "ielts_03_environment.md",
        "num": "03",
        "title": "Environment, Climate & Ecology",
        "title_kh": "បរិស្ថាន បម្រែបម្រួលអាកាសធាតុ និងអេកូឡូស៊ី",
        "range": "21–30",
        "topics": [
            (21, "Ocean Acidification and Marine Ecosystem Collapse"),
            (22, "Renewable Energy Transition and Grid Modernization"),
            (23, "Deforestation and the Loss of Biodiversity Hotspots"),
            (24, "Urban Microclimates and the Heat Island Effect"),
            (25, "Plastic Pollution and Microplastic Bioaccumulation"),
            (26, "Carbon Capture and Sequestration Technologies"),
            (27, "Freshwater Scarcity and Transboundary Water Politics"),
            (28, "Rewilding and Ecological Restoration Strategies"),
            (29, "Sustainable Agriculture and Soil Health Regeneration"),
            (30, "The Impact of Fast Fashion on Global Ecosystems")
        ]
    },
    {
        "file": "ielts_04_health.md",
        "num": "04",
        "title": "Health, Medicine & Well-being",
        "title_kh": "សុខភាព វេជ្ជសាស្ត្រ និងសុខុមាលភាព",
        "range": "31–40",
        "topics": [
            (31, "Antimicrobial Resistance and the Superbug Crisis"),
            (32, "Telemedicine and Rural Healthcare Accessibility"),
            (33, "Ultra-Processed Foods and the Chronic Disease Epidemic"),
            (34, "Mental Health De-stigmatization and Workplace Well-being"),
            (35, "Sleep Deprivation and Modern Circadian Disruption"),
            (36, "Sedentary Lifestyles and Cardiovascular Health"),
            (37, "Preventive Medicine versus Reactive Healthcare"),
            (38, "Pandemic Preparedness and Global Health Governance"),
            (39, "The Gut Microbiome and Human Immunity"),
            (40, "Health Disparities and the Social Determinants of Health")
        ]
    },
    {
        "file": "ielts_05_work_economy.md",
        "num": "05",
        "title": "Work, Economy & Globalization",
        "title_kh": "ការងារ សេដ្ឋកិច្ច និងសកលភាវូបនីយកម្ម",
        "range": "41–50",
        "topics": [
            (41, "The Gig Economy and Precarious Labor"),
            (42, "Remote Work and the Transformation of Corporate Geography"),
            (43, "Automation, Robotics, and the Future of Employment"),
            (44, "The Gender Pay Gap and Corporate Glass Ceilings"),
            (45, "Universal Basic Income as an Economic Safety Net"),
            (46, "Circular Economy and Industrial Waste Elimination"),
            (47, "Global Supply Chain Disruptions and Reshoring Strategies"),
            (48, "The Rise of E-Commerce and Brick-and-Mortar Retail Decline"),
            (49, "Wealth Inequality and Socioeconomic Stratification"),
            (50, "Microfinance and Poverty Alleviation in Emerging Markets")
        ]
    },
    {
        "file": "ielts_06_society_family.md",
        "num": "06",
        "title": "Society, Demographics & Modern Culture",
        "title_kh": "សង្គម ប្រជាសាស្ត្រ និងវប្បធម៌សម័យទំនើប",
        "range": "51–60",
        "topics": [
            (51, "Aging Populations and the Silver Economy"),
            (52, "Youth Activism and Global Climate Movements"),
            (53, "Urban-to-Rural Migration and Regional Revitalization"),
            (54, "Social Isolation and the Loneliness Epidemic"),
            (55, "Changing Family Structures and Single-Parent Households"),
            (56, "The Influence of Celebrity Culture on Adolescent Identity"),
            (57, "Suburban Sprawl and the Loss of Social Cohesion"),
            (58, "Consumerism and the Psychology of Compulsive Shopping"),
            (59, "Gender Norm Evolution and Domestic Division of Labor"),
            (60, "The Digital Nomad Lifestyle and Cross-Border Living")
        ]
    },
    {
        "file": "ielts_07_crime_law_government.md",
        "num": "07",
        "title": "Law, Crime & Governance",
        "title_kh": "ច្បាប់ ឧក្រិដ្ឋកម្ម និងអភិបាលកិច្ច",
        "range": "61–70",
        "topics": [
            (61, "Restorative Justice versus Retributive Punishment"),
            (62, "White-Collar Crime and Corporate Embezzlement"),
            (63, "Facial Recognition Surveillance in Public Spaces"),
            (64, "Decriminalization of Minor Offenses and Prison Overcrowding"),
            (65, "Hate Speech versus Freedom of Expression in Digital Media"),
            (66, "Juvenile Justice and Rehabilitation Programs"),
            (67, "Environmental Law and Corporate Ecocide Accountability"),
            (68, "Whistleblower Protection and Investigative Journalism"),
            (69, "Police Demilitarization and Community Policing"),
            (70, "Electoral Integrity and Combating Digital Disinformation")
        ]
    },
    {
        "file": "ielts_08_cities_transport.md",
        "num": "08",
        "title": "Cities, Architecture & Infrastructure",
        "title_kh": "ទីក្រុង ស្ថាបត្យកម្ម និងហេដ្ឋារចនាសម្ព័ន្ធ",
        "range": "71–80",
        "topics": [
            (71, "The 15-Minute City Concept and Urban Proximity"),
            (72, "High-Speed Rail Networks and Regional Connectivity"),
            (73, "Affordable Housing Deficits and Urban Rent Control"),
            (74, "Biophilic Architecture and Green Building Standards"),
            (75, "Coastal Flood Barriers and Resilient Urban Engineering"),
            (76, "Pedestrianization and the Reclaiming of Public Squares"),
            (77, "Smart City Sensors and Municipal Resource Efficiency"),
            (78, "Adaptive Reuse of Industrial Heritage Buildings"),
            (79, "Electric Bus Fleets and Zero-Emission Public Transit"),
            (80, "Zero-Waste Municipal Frameworks and Landfill Diversion")
        ]
    },
    {
        "file": "ielts_09_culture_globalisation.md",
        "num": "09",
        "title": "Culture, Heritage & Global Tourism",
        "title_kh": "វប្បធម៌ បេតិកភណ្ឌ និងទេសចរណ៍សកល",
        "range": "81–90",
        "topics": [
            (81, "Overtourism and the Fragility of Historic Cities"),
            (82, "Indigenous Language Endangerment and Revitalization"),
            (83, "Museum Ethics and the Repatriation of Cultural Artifacts"),
            (84, "Cultural Appropriation versus Appreciation in Globalized Art"),
            (85, "Ecotourism and Community-Based Conservation"),
            (86, "The Preservation of Intangible Cultural Heritage"),
            (87, "Globalization and the Homogenization of Food Cultures"),
            (88, "Public Broadcasting and National Cultural Identity"),
            (89, "Adaptive Conservation of Archaeological Sites"),
            (90, "Dark Tourism and the Ethics of Commemoration")
        ]
    },
    {
        "file": "ielts_10_science_nature.md",
        "num": "10",
        "title": "Science, Nature & Space Exploration",
        "title_kh": "វិទ្យាសាស្ត្រ ធម្មជាតិ និងការរុករកអវកាស",
        "range": "91–100",
        "topics": [
            (91, "CRISPR-Cas9 Gene Editing and the Future of Medicine"),
            (92, "Exoplanet Biosignatures and the Search for Extraterrestrial Life"),
            (93, "Deep-Sea Mining and Ocean Ecosystem Fragility"),
            (94, "Early Earthquake Warning Systems and Seismology"),
            (95, "Quantum Computing and Cryptographic Security"),
            (96, "Biomimicry and Nature-Inspired Engineering"),
            (97, "Solar Storms, Geomagnetic Flares and Space Weather"),
            (98, "Mycelial Networks and Forest Communication"),
            (99, "Nuclear Fusion Energy: Harnessing the Power of the Sun"),
            (100, "Paleogenomics and the Resurrecting of Ancient DNA")
        ]
    }
]

def generate_index():
    lines = []
    lines.append("# 📖 IELTS Academic & CEFR Reading — 100 Adaptive Mock Exam Topics (B1–C2)")
    lines.append("## បណ្តុំប្រធានបទប្រឡងអាន IELTS & CEFR ១០០ ប្រធានបទ សម្របតាមកម្រិត B1–C2\n")
    lines.append("> **100 Academic Topics × 4 Adaptive CEFR Levels = 400 Authentic Reading Passages**")
    lines.append("> **400 Mock Exam Questions + 600 Academic Vocabulary Terms (English + Khmer) + 400 Comprehensive Explanatory Walkthroughs.**")
    lines.append("> These original, meticulously crafted mock exams simulate authentic IELTS Academic Reading and CEFR standards from B1 (Preliminary) to C2 (Mastery).\n")
    lines.append("---\n")
    
    lines.append("## 📋 Contents\n")
    lines.append("1. [The Exam Task: IELTS Academic & CEFR Reading](#1-the-exam-task-ielts-academic--cefr-reading)")
    lines.append("2. [CEFR Levels and IELTS Band Alignment](#2-cefr-levels-and-ielts-band-alignment)")
    lines.append("3. [How Each Topic is Organised](#3-how-each-topic-is-organised)")
    lines.append("4. [Strategic Reading Methodology (Skim, Scan, Map)](#4-strategic-reading-methodology-skim-scan-map)")
    lines.append("5. [Question Types Covered in this Bank](#5-question-types-covered-in-this-bank)")
    lines.append("6. [The 10 Thematic Volumes](#6-the-10-thematic-volumes)")
    lines.append("7. [Complete Directory of All 100 Topics](#7-complete-directory-of-all-100-topics)\n")
    lines.append("---\n")

    lines.append("## 1. The Exam Task: IELTS Academic & CEFR Reading\n")
    lines.append("| Dimension | IELTS Academic Reading | CEFR Reading Assessment |")
    lines.append("| :--- | :--- | :--- |")
    lines.append("| **Format** | 3 long academic texts (approx. 2,150–2,750 words total) | Graded texts testing B1, B2, C1, and C2 reading competence |")
    lines.append("| **Time** | **60 minutes** strictly timed (including answer sheet transfer) | 45–90 minutes depending on candidate level tier |")
    lines.append("| **Questions** | **40 questions** (True/False/Not Given, Headings, Summary, MCQs) | Objective multiple-choice, matching, and text verification |")
    lines.append("| **Skills Tested** | Skimming for gist, scanning for specific detail, recognizing tone & author attitude, identifying logical arguments, lexical inference | Literal comprehension, inferential reasoning, pragmatic nuance, stylistic tone appreciation |\n")
    lines.append("---\n")

    lines.append("## 2. CEFR Levels and IELTS Band Alignment\n")
    lines.append("Every topic in this library presents the exact same conceptual subject matter rendered at four distinct CEFR tiers, allowing learners to witness how syntactic complexity, discourse markers, and lexical density evolve.\n")
    lines.append("| CEFR Level | IELTS Band | Cambridge Level | Linguistic Characteristics in this Bank |")
    lines.append("| :--- | :--- | :--- | :--- |")
    lines.append("| 🟡 **B1** (Threshold) | 4.0 – 5.0 | B1 Preliminary (PET) | ~150 words. Direct syntactic structures, active voice, everyday vocabulary, clear topic sentences, straightforward factual statements. |")
    lines.append("| 🔴 **B2** (Vantage) | 5.5 – 6.5 | B2 First (FCE) | ~200 words. Academic terminology, passive constructions, relative clauses, hedging markers (*tend to, indicate, suggest*), factual case studies and empirical examples. |")
    lines.append("| 🟣 **C1** (Effective) | 7.0 – 8.0 | C1 Advanced (CAE) | ~250 words. High lexical density, nominalization, complex subordination, epistemological arguments, systemic societal and socioeconomic analysis. |")
    lines.append("| ⚫ **C2** (Mastery) | 8.5 – 9.0 | C2 Proficiency (CPE) | ~250 words. Nuanced rhetoric, philosophical abstraction, poetic metaphors, complex irony, rhythmic sentence variety, deep cultural and civilizational contemplation. |\n")
    lines.append("---\n")

    lines.append("## 3. How Each Topic is Organised\n")
    lines.append("Every single one of the 100 reading topics follows a standardized pedagogical layout:\n")
    lines.append("| Section | Purpose & Pedagogical Benefit |")
    lines.append("| :--- | :--- |")
    lines.append("| **1. Metadata & Header** | Topic number, English title, Khmer translation, academic theme, and question format focus. |")
    lines.append("| **2. Academic Vocabulary Bank** | 6 high-utility academic words with part of speech, CEFR rating, English definition, and accurate Khmer translation. |")
    lines.append("| **3. Adaptive Passages (B1–C2)** | The core reading text adapted across four levels. Allows comparative reading to build advanced vocabulary and syntax. |")
    lines.append("| **4. Mock Exam Questions** | 4 IELTS-standard questions testing detail, inference, and global comprehension. |")
    lines.append("| **5. Comprehensive Walkthrough** | Complete answer keys with direct textual quotes, citation cross-references, and bilingual English-Khmer explanations. |\n")
    lines.append("---\n")

    lines.append("## 4. Strategic Reading Methodology (Skim, Scan, Map)\n")
    lines.append("To achieve Band 8.0+ or C1/C2 proficiency, apply this rigorous 4-step reading system:\n")
    lines.append("1. **Skim for Architecture (2 minutes):** Read the title, subheadings, and the first sentence of each paragraph to grasp the conceptual roadmap.")
    lines.append("2. **Deconstruct the Questions (2 minutes):** Underline essential keywords in the questions (names, dates, specialized terms, qualifying adverbs like *always, mainly, partially*).")
    lines.append("3. **Targeted Scanning:** Scan the text for synonyms and paraphrases of your keywords. Remember: IELTS rarely repeats the exact question words; it tests your recognition of lexical substitution.")
    lines.append("4. **Paraphrase Mapping & Verification:** Locate the specific sentence. Cross-verify whether the question statement matches the exact meaning (TRUE), contradicts the author (FALSE), or introduces unverifiable speculation (NOT GIVEN).\n")
    lines.append("---\n")

    lines.append("## 5. Question Types Covered in this Bank\n")
    lines.append("| Question Type | Key Challenge | Winning Strategy |")
    lines.append("| :--- | :--- | :--- |")
    lines.append("| **True / False / Not Given** | Differentiating between a direct factual contradiction (FALSE) and lack of evidence (NOT GIVEN). | If the text says the opposite, it is FALSE. If the author never took a stand or never gave evidence, it is NOT GIVEN. |")
    lines.append("| **Yes / No / Not Given** | Identifying the author's subjective opinion, perspective, and argumentative stance. | Trace modal verbs (*could, should, might*) and evaluative adjectives (*untenable, vital, hubristic*). |")
    lines.append("| **Matching Headings** | Identifying the primary macro-argument of a paragraph rather than isolated micro-details. | Read the first two sentences and the concluding sentence; formulate your own heading before checking options. |")
    lines.append("| **Multiple Choice Questions** | Eliminating tempting distractors that repeat keywords from the text out of context. | Treat each option as a True/False statement against the exact target sentence. |")
    lines.append("| **Summary / Note Completion** | Synthesizing information across multiple sentences with strict word-limit constraints. | Identify the required grammatical part of speech (noun, verb, adjective) before choosing the target word. |\n")
    lines.append("---\n")

    lines.append("## 6. The 10 Thematic Volumes\n")
    lines.append("| Vol | Theme Title | Khmer Translation | Topics | File Link |")
    lines.append("| :--- | :--- | :--- | :--- | :--- |")
    for t in THEMES:
        lines.append(f"| {t['num']} | {t['title']} | {t['title_kh']} | {t['range']} | [{t['file']}]({t['file']}) |")
    lines.append("\n---\n")

    lines.append("## 7. Complete Directory of All 100 Topics\n")
    for t in THEMES:
        lines.append(f"### Volume {t['num']} · {t['title']} ({t['range']})")
        lines.append(f"*{t['title_kh']}* — [`{t['file']}`]({t['file']})\n")
        lines.append("| # | Topic Title | Target File |")
        lines.append("| :--- | :--- | :--- |")
        for num, title in t["topics"]:
            # Anchor format: #<num>-<slug>
            slug = title.lower().replace(" ", "-").replace(":", "").replace("'", "").replace(",", "").replace("/", "").replace("(", "").replace(")", "")
            lines.append(f"| {num:03d} | [{title}]({t['file']}#{num}-{slug}) | [`{t['file']}`]({t['file']}) |")
        lines.append("\n")

    content = "\n".join(lines)
    with open("/Users/chandara-dgc/Documents/learn-english/reading_skills/examples/ielts_00_index.md", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[+] Master index successfully generated: {len(content)} bytes")

if __name__ == "__main__":
    generate_index()
