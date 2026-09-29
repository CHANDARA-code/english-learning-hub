#!/usr/bin/env python3
"""
Generate reading_skills/examples/ielts_01_education.md (Topics 1-10)
Generate reading_skills/examples/ielts_02_technology.md (Topics 11-20)
Generate reading_skills/examples/ielts_03_environment.md (Topics 21-30)
"""

import os

OUT_DIR = "/Users/chandara-dgc/Documents/learn-english/reading_skills/examples"

# ==============================================================================
# THEME 1: EDUCATION (Topics 1–10)
# ==============================================================================
THEME_1_TOPICS = [
    {
        "num": 1,
        "title": "Digital Classrooms and Virtual Learning Environments",
        "title_kh": "ថ្នាក់រៀនឌីជីថល និងបរិស្ថានសិក្សាតាមប្រព័ន្ធនិម្មិត",
        "focus": "True / False / Not Given & Vocabulary in Context",
        "vocab": [
            ("pedagogy", "noun", "C1", "the method and practice of teaching", "គរុកោសល្យ, វិធីសាស្ត្របង្រៀន"),
            ("synchronous", "adj", "C1", "occurring at the same time", "ស្របពេលគ្នា, ដំណាលគ្នា"),
            ("retention", "noun", "B2", "the ability to remember knowledge", "ការចងចាំបានយូរ, ការរក្សាទុក"),
            ("autonomous", "adj", "B2/C1", "acting independently with self-direction", "ឯករាជ្យ, ម្ចាស់ការលើខ្លួនឯង"),
            ("distraction", "noun", "B1", "something that prevents concentration", "ការរំខានអារម្មណ៍"),
            ("facilitate", "verb", "B2", "to make an action or process easier", "សម្រួល, ជួយឱ្យកាន់តែងាយស្រួល")
        ],
        "b1_text": """In recent years, computers and the internet have fundamentally altered how students learn in schools and colleges. Many institutions now use virtual classrooms where teachers deliver lessons through live video and assign digital homework. This system offers several clear benefits. For example, learners can pause and replay recorded lectures at home whenever they wish, which helps them review difficult grammar rules or complex math equations at their own speed.

However, studying exclusively in front of a computer screen also introduces serious challenges for younger learners. When students sit alone in their bedrooms, it is very easy to lose focus and browse social media websites instead of completing assignments. In addition, online classes lack spontaneous face-to-face conversations with peers and teachers. While digital technology provides remarkable convenience, students still require strong personal self-discipline and active teacher support to achieve academic success.""",
        "b2_text": """The rapid proliferation of digital learning platforms has transformed contemporary educational methodologies. Modern institutions increasingly implement blended learning models that combine traditional classroom lectures with interactive digital modules. Proponents emphasize that this approach fosters autonomous learning, enabling students to navigate instructional materials at their individualized pace and reinforce conceptual understanding through automated quizzes and recorded repositories.

Nevertheless, pedagogical researchers express reservations regarding entirely virtual instruction. While asynchronous coursework grants scheduling flexibility, it frequently diminishes the collaborative dynamics and spontaneous analytical debates that occur naturally in physical seminars. Furthermore, empirical studies indicate that prolonged screen exposure contributes to cognitive fatigue and shortened attention spans. Consequently, maximizing academic retention requires educational planners to maintain a balanced synthesis between digital autonomy and structured in-person teacher mentorship.""",
        "c1_text": """Over the past decade, educational frameworks have experienced a profound paradigm shift from physical confinement to decentralized virtual spaces. The adoption of sophisticated learning management systems and algorithmically tailored content was initially hailed as an unprecedented democratization of knowledge, dismantling logistical constraints and accommodating diverse cognitive dispositions. Through synchronous seminars and asynchronous research repositories, tertiary institutions have largely decoupled academic acquisition from geographical immobility.

Crucially, contemporary pedagogical assessments increasingly challenge this uncritical techno-optimism. Rather than universally equalizing academic performance, unmediated virtual instruction frequently magnifies existing disparities in student agency. Highly self-directed individuals effectively harness digital flexibility to accelerate intellectual growth; conversely, less autonomous cohorts frequently succumb to cognitive fragmentation amidst persistent digital distractions. Moreover, the organic intellectual camaraderie cultivated through spontaneous academic discourse in a physical room remains exceptionally difficult to replicate across algorithmic interfaces. Digital pedagogy must therefore be treated not merely as an administrative efficiency, but as an educational medium necessitating rigorous institutional scaffolding.""",
        "c2_text": """The systemic migration of tertiary instruction toward virtual ecosystems represents far more than an operational expedient; it inaugurates an ontological redefinition of the pedagogical encounter. Evangelists of educational technology have long prophesied the obsolescence of brick-and-mortar academies, positing that frictionless digital dissemination inherently democratizes intellectual enlightenment. By commodifying instructional curricula into ubiquitous, algorithmically trackable data modules, the virtual academy purports to liberate scholarship from antiquated temporal and spatial strictures.

Yet this technocratic triumphalism obscures an irreplaceable dimension of intellectual formation: the visceral friction of embodied dialectic. True scholarly discernment is seldom synthesized in solitary cognitive silos mediated by high-resolution screens; it germinates through immediate intersubjective debate, reciprocal accountability, and the serendipitous collisions of inquiring minds. To conflate algorithmic data transmission with pedagogical cultivation is to confuse informational consumption with epistemic transformation. The cardinal dilemma confronting modern academia is whether it can exploit digital connectivity without dismantling the communal crucible wherein critical thought is irrevocably forged.""",
        "questions": [
            ("1", "Digital learning platforms require learners to exhibit greater individual self-discipline to counter digital distractions.", "TRUE"),
            ("2", "Modern tertiary institutions have completely eliminated physical classrooms in favor of online portals.", "FALSE"),
            ("3", "Students lacking metacognitive autonomy often struggle with cognitive fragmentation in virtual environments.", "TRUE"),
            ("4", "Synchronous web forums have proved completely identical in pedagogical value to physical seminar discussions.", "FALSE")
        ],
        "answers": [
            ("1", "TRUE", "Both B1 and C1 explicitly confirm that learners must maintain disciplined focus because screen-based studying introduces significant distractions and requires self-regulation.", "ពិត (TRUE) — អត្ថបទបញ្ជាក់ច្បាស់ថាសិស្សត្រូវការវិន័យផ្ទាល់ខ្លួនខ្ពស់ដើម្បីទប់ទល់នឹងការរំខានអារម្មណ៍ពីប្រព័ន្ធឌីជីថល។"),
            ("2", "FALSE", "B2 states that institutions adopt 'blended learning models' that integrate physical lectures with digital modules, directly contradicting total elimination.", "មិនពិត (FALSE) — អត្ថបទបញ្ជាក់ថាគ្រឹះស្ថានអប់រំអនុវត្តវិធីសាស្ត្រចម្រុះ (Blended learning) ដោយរួមបញ្ចូលទាំងការរៀនផ្ទាល់ និងអនឡាញ មិនមែនលុបចោលថ្នាក់រៀនផ្ទាល់ទាំងស្រុងនោះទេ។"),
            ("3", "TRUE", "C1 explicitly states that less autonomous cohorts frequently succumb to cognitive fragmentation amidst persistent distractions.", "ពិត (TRUE) — ក្នុងកម្រិត C1 បានបង្ហាញថាសិស្សដែលខ្វះភាពម្ចាស់ការលើខ្លួនឯង តែងតែជួបបញ្ហាបែកអារម្មណ៍ក្នុងការសិក្សា។"),
            ("4", "FALSE", "C1 and C2 emphasize that organic intellectual camaraderie and dialectic are exceptionally difficult to replicate across digital interfaces.", "មិនពិត (FALSE) — អត្ថបទបង្ហាញថាវេទិកាឌីជីថលពុំអាចជំនួសការជជែកដេញដោលស៊ីជម្រៅដោយផ្ទាល់ក្នុងថ្នាក់រៀនបានដូចគ្នាទាំងស្រុងនោះឡើយ។")
        ]
    },
    {
        "num": 2,
        "title": "Early Childhood Bilingualism and Cognitive Development",
        "title_kh": "ទ្វេភាសាក្នុងវ័យកុមារ និងការអភិវឌ្ឍការយល់ដឹង",
        "focus": "Matching Headings & True / False / Not Given",
        "vocab": [
            ("bilingualism", "noun", "B2", "the ability to speak two languages fluently", "ភាពចេះពីរភាសា"),
            ("cognitive", "adj", "B2", "relating to mental processes of understanding", "ដែលទាក់ទងនឹងការយល់ដឹង"),
            ("proficiency", "noun", "C1", "high degree of competence or skill", "កម្រិតជំនាញច្បាស់លាស់"),
            ("executive function", "noun", "C1", "cognitive processes managing goals and focus", "មុខងារប្រតិបត្តិខួរក្បាល"),
            ("linguistic", "adj", "B2", "relating to language or linguistics", "ដែលទាក់ទងនឹងភាសា"),
            ("inhibition", "noun", "C1/C2", "the mental ability to suppress irrelevant stimuli", "ការទប់ស្កាត់ការរំខានក្នុងខួរក្បាល")
        ],
        "b1_text": """Raising children to speak two languages from an early age has become very popular around the world. In the past, some educators believed that learning two languages at the same time would confuse a young child's brain and delay speech development. However, modern scientific studies prove that this belief was incorrect. Children who grow up in bilingual households are fully capable of learning vocabulary in both languages without lasting confusion.

Furthermore, being bilingual provides young children with important mental advantages. Research shows that bilingual children often solve puzzles faster and switch between different tasks more easily than monolingual children. Because their brains must regularly choose which language to use, their concentration improves significantly. In the long run, bilingualism opens up better international employment opportunities and creates deep respect for different cultural traditions.""",
        "b2_text": """The neurological and cognitive ramifications of early childhood bilingualism have received widespread empirical support in contemporary developmental psychology. Historical misconceptions posited that simultaneous dual-language acquisition overburdened young children's cognitive architecture, resulting in delayed linguistic milestones. Contemporary neuroimaging studies, however, convincingly demonstrate that the juvenile brain possesses extraordinary neuroplasticity, allowing effortless categorization and semantic processing of multiple linguistic codes.

Beyond basic communicative utility, bilingualism markedly enhances executive function—the cognitive control mechanism governing attention, working memory, and cognitive flexibility. Because bilingual children constantly suppress one linguistic system while activating another, their brains continuously practice inhibitory control. This lifelong cognitive workout enhances their problem-solving capabilities and shields the brain against age-related cognitive decline in later adulthood.""",
        "c1_text": """The neurodevelopmental trajectories of bilingual individuals have provided profound insights into the plasticity of human cognition. The mid-twentieth-century dogma that simultaneous language acquisition induced cognitive dissonance and expressive retardation has been decisively refuted by longitudinal linguistic research. Rather than straining cognitive bandwidth, early dual-language immersion stimulates neural circuitry associated with cognitive agility and structural linguistic awareness.

At the epicenter of this cognitive advantage lies the enhancement of executive functioning. Bilingual children continuously orchestrate complex linguistic operations, selectively inhibiting intrusive lexical items from the non-target language while deploying context-appropriate phonology and syntax. This sustained neurological exertion translates into superior attentional switching, enhanced working memory capacity, and pronounced cognitive adaptability. Furthermore, epidemiological data suggest that the structural cognitive reserve fostered through sustained multilingualism delays the clinical onset of neurodegenerative symptoms in senescence.""",
        "c2_text": """The epistemic shift regarding early childhood bilingualism illustrates the triumph of empirical neuroscience over persistent pedagogical folklorism. The erstwhile anxiety that dual linguistic encoding precipitated conceptual muddling has given way to an appreciation of the bilingual brain as an exemplar of dynamic neurological equilibrium. Far from encumbering cognitive processing, simultaneous bilingual exposure catalyzes sophisticated neural reconfigurations that optimize computational efficiency across disparate domains.

This cognitive resilience is mediated primarily through the relentless calibration of executive control networks. The imperative to navigate competing semantic universes necessitates continuous inhibitory gating, wherein the brain dynamically suppresses non-salient linguistic matrices without conscious deliberations. The resulting cognitive dividend extends well beyond linguistic facility: it bolsters divergent reasoning, refines abstract meta-linguistic discernment, and fortifies neural reserves against cerebrovascular pathology. To acquire multiple tongues in infancy is not merely to amass parallel lexical inventories, but to reforge the very architecture of consciousness.""",
        "questions": [
            ("1", "Mid-twentieth-century theories widely promoted the idea that bilingualism improved young children's IQ.", "FALSE"),
            ("2", "Inhibitory control is developed because bilingual brains routinely suppress one language system during communication.", "TRUE"),
            ("3", "Bilingual children inevitably take twice as long to achieve basic speech milestones compared to monolinguals.", "FALSE"),
            ("4", "Lifelong bilingual cognitive reserve has been linked to delaying clinical symptoms of dementia.", "TRUE")
        ],
        "answers": [
            ("1", "FALSE", "B1, B2, and C1 clarify that historical misconceptions claimed dual language learning caused confusion and delays, not superior IQ.", "មិនពិត (FALSE) — ទស្សនៈកាលពីអតីតកាលយល់ច្រឡំថាការរៀនពីរភាសាធ្វើឱ្យកុមារច្របូកច្របល់ និងពន្យឺតការនិយាយ មិនមែនបង្កើន IQ ឡើយ។"),
            ("2", "TRUE", "B2 and C1 explain that bilinguals constantly practice inhibitory control by suppressing the non-target language while speaking.", "ពិត (TRUE) — ខួរក្បាលអ្នកចេះពីរភាសាធ្វើការទប់ស្កាត់ភាសាមួយដោយស្វ័យប្រវត្តិកំឡុងពេលប្រើប្រាស់ភាសាមួយទៀត ដែលបង្កើតបានជាសមត្ថភាពគ្រប់គ្រងចិត្តយ៉ាងរឹងមាំ។"),
            ("3", "FALSE", "B1 and B2 state that modern science shows children learn both vocabularies without lasting speech retardation.", "មិនពិត (FALSE) — ការសិក្សាទំនើបបញ្ជាក់ថាកុមារមានសមត្ថភាពអភិវឌ្ឍភាសាទាំងពីរដោយគ្មានការពន្យារពេលនិយាយយូរអង្វែងឡើយ។"),
            ("4", "TRUE", "B2 and C1 explicitly observe that cognitive reserve shields the brain and delays the clinical onset of neurodegenerative symptoms in later life.", "ពិត (TRUE) — ការស្រាវជ្រាវវេជ្ជសាស្ត្របញ្ជាក់ថាការចេះពីរភាសាជួយពន្យារពេលរោគសញ្ញានៃជំងឺវង្វេងវង្វាន់ពេលចាស់ជរា។")
        ]
    }
]

# Write helper to format a single topic markdown section
def format_topic_section(t):
    md = []
    num = t["num"]
    title = t["title"]
    title_kh = t["title_kh"]
    focus = t["focus"]

    md.append(f"## {num}. {title}")
    md.append(f"### {title_kh}\n")
    md.append(f"**Target Alignment:** IELTS Academic & General Reading · CEFR B1–C2  ")
    md.append(f"**Question Type Focus:** {focus}  \n")
    
    md.append("### 📚 Key Academic Vocabulary & Khmer Glossary\n")
    md.append("| Term | Part of Speech | CEFR | Academic Definition | អត្ថន័យជាភាសាខ្មែរ |")
    md.append("| :--- | :--- | :--- | :--- | :--- |")
    for word, pos, cefr, definition, kh in t["vocab"]:
        md.append(f"| **{word}** | {pos} | {cefr} | {definition} | {kh} |")
    md.append("\n---\n")

    md.append("### 📖 Adaptive Reading Passages (អត្ថបទអានសម្របតាមកម្រិតទាំង ៤: B1 · B2 · C1 · C2)\n")

    # B1
    md.append("#### 🟡 B1 Level — Intermediate (IELTS 4.5–5.0 · ~150 words)")
    for p in t["b1_text"].strip().split("\n\n"):
        md.append(f"> {p.strip()}\n>")
    md.append("\n")

    # B2
    md.append("#### 🔴 B2 Level — Upper-Intermediate (IELTS 5.5–6.5 · ~200 words)")
    for p in t["b2_text"].strip().split("\n\n"):
        md.append(f"> {p.strip()}\n>")
    md.append("\n")

    # C1
    md.append("#### 🟣 C1 Level — Advanced (IELTS 7.0–8.0 · ~250 words)")
    for p in t["c1_text"].strip().split("\n\n"):
        md.append(f"> {p.strip()}\n>")
    md.append("\n")

    # C2
    md.append("#### ⚫ C2 Level — Proficiency (IELTS 8.5–9.0 · ~250 words)")
    for p in t["c2_text"].strip().split("\n\n"):
        md.append(f"> {p.strip()}\n>")
    md.append("\n")

    md.append("---\n")
    md.append("### 📝 Mock Exam Questions (IELTS Reading Style)\n")
    md.append("**Questions 1–4: Do the following statements agree with the information given in the passages above?**\n")
    md.append("*Write:*\n- **TRUE** if the statement agrees with the information\n- **FALSE** if the statement contradicts the information\n- **NOT GIVEN** if there is no information on this\n")
    for q_num, text, _ in t["questions"]:
        md.append(f"{q_num}. {text}")
    md.append("\n---\n")

    md.append("### 🔑 Answer Key & Explanatory Walkthrough (ចម្លើយ និងការពន្យល់លម្អិតជាភាសាខ្មែរ)\n")
    for q_num, ans, eng_exp, kh_exp in t["answers"]:
        md.append(f"- **Question {q_num}: {ans}**")
        md.append(f"  - *Evidence & Logic:* {eng_exp}")
        md.append(f"  - *Khmer Analysis:* {kh_exp}")
    md.append("\n---\n")

    return "\n".join(md)

print("Template builder script ready.")
