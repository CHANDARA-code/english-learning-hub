#!/usr/bin/env python3
"""
Generate Volume 2: Technology, Artificial Intelligence & Digital Life (Topics 11–20)
reading_skills/examples/ielts_02_technology.md
"""

from reading_generator_engine import write_theme_file

TOPICS = [
    {
        "num": 11,
        "title": "Generative AI and Academic Integrity",
        "title_kh": "បញ្ញាសិប្បនិម្មិតបង្កើតមាតិកា និងសុចរិតភាពក្នុងការសិក្សា",
        "theme_name": "Technology & Artificial Intelligence",
        "qtype": "True / False / Not Given",
        "vocab": [
            ("integrity", "noun", "B2/C1", "honesty and adherence to ethical principles", "សុចរិតភាព, ភាពស្មោះត្រង់"),
            ("plagiarism", "noun", "B2", "using someone else's work without attribution", "ការលួចចម្លងស្នាដៃ"),
            ("hallucination", "noun", "C1", "generation of plausible but false data by AI", "ការបង្កើតព័ត៌មានមិនពិតដោយ AI"),
            ("authenticate", "verb", "C1", "to prove that something is genuine", "ផ្ទៀងផ្ទាត់ភាពត្រឹមត្រូវ"),
            ("transformative", "adj", "B2/C1", "causing a major change or conversion", "ដែលធ្វើឱ្យមានការផ្លាស់ប្តូរជាវិជ្ជមាន"),
            ("diligence", "noun", "C1", "careful and persistent effort", "ការឧស្សាហ៍ព្យាយាម, ភាពហ្មត់ចត់")
        ],
        "b1": """In recent years, artificial intelligence computer programs have become capable of writing complete essays, solving mathematical problems, and generating computer code in seconds. For university students, these generative AI tools provide fast help with difficult homework and research projects. A student can type a topic into an AI software program and receive an organized summary immediately.

However, university professors and school leaders are very worried about academic honesty. If students submit essays written by AI tools instead of writing their own thoughts, they do not practice critical thinking or develop real research skills. Furthermore, AI tools frequently make factual mistakes and invent fake citations. To solve this problem, schools are introducing new guidelines that require students to declare when they use AI and to verify all facts carefully.""",
        "b2": """The sudden emergence of generative artificial intelligence has introduced unprecedented complexities into academic integrity frameworks. Large language models can synthesize extensive academic literature, construct coherent discursive essays, and debug intricate software algorithms with remarkable speed. While proponents highlight AI's potential as an individualized cognitive tutor that democratizes tutoring access, university administrators face widespread challenges concerning algorithmic plagiarism.

Traditional plagiarism detection algorithms, which scan for verbatim textual matching, are fundamentally incapable of identifying synthetically generated prose. Furthermore, large language models are prone to hallucinating citations and asserting erroneous assertions with syntactic confidence. Consequently, universities are moving away from punitive surveillance software toward process-oriented assessment methodologies, requiring oral defenses, real-time handwritten examinations, and mandatory transparency declarations regarding AI utilization.""",
        "c1": """The rapid diffusion of generative artificial intelligence across higher education has precipitated an ontological crisis regarding authorship, authenticity, and academic integrity. Generative models do not merely regurgitate existing texts; they synthesize probabilistic semantic combinations, simulating human reasoning and rhetorical nuance. This capability fundamentally destabilizes traditional mechanisms of scholastic accreditation, where written discourse long served as the primary proxy for intellectual cognition and critical comprehension.

Crucially, attempts to police generative AI through automated detection algorithms have proved epistemically flawed, often generating false positives that disproportionately penalize non-native English scholars. Concurrently, the uncritical deployment of synthetic text introduces systemic intellectual degradation, as students outsource deep semantic synthesis to predictive algorithms, thereby impairing their own neural consolidation of knowledge. Forward-looking pedagogical paradigms must therefore abandon the illusion of total prohibition, instead cultivating meta-cognitive AI literacy where learners critically interrogate algorithmic outputs rather than passively accepting automated scholarship.""",
        "c2": """The proliferation of generative artificial intelligence represents not merely a technical disruption to academic administration, but a profound philosophical confrontation with the essence of intellectual labor. For centuries, the arduous composition of analytical prose was conceived as the crucible within which thought itself was distilled, refined, and authenticated. In mechanizing textual generation, generative algorithms decouple communicative articulation from interior cognitive struggle, presenting the polished artifact of scholarship stripped of the intellectual journey that constitutes genuine understanding.

The academic panic surrounding algorithmic dishonesty exposes the fragility of contemporary credentialism. When tertiary institutions reduce scholarship to the transactional production of standardized essays, they inevitably invite automated substitution. To restore pedagogical legitimacy, academia must transcend superficial anxieties over plagiarism detection and confront the deeper existential challenge: fostering epistemological discernment that cannot be simulated by probabilistic token prediction. Education must cease to evaluate students as information assemblers and instead cultivate them as ethical, self-aware dialecticians capable of interrogating the automated intelligences they now command.""",
        "questions": [
            ("1", "Traditional plagiarism software detects generative AI text with near-perfect reliability through direct phrase matching."),
            ("2", "Generative AI models occasionally generate completely fabricated citations that sound linguistically authentic."),
            ("3", "Automated AI detection tools have been documented to produce false positives against non-native English writers."),
            ("4", "All world universities have strictly prohibited the ownership of computers to prevent AI misuse.")
        ],
        "answers": [
            ("1", "FALSE", "B2 and C1 state traditional detection tools scanning for verbatim matching are fundamentally incapable of reliably identifying synthetic prose.", "មិនពិត (FALSE) — កម្មវិធីពិនិត្យការលួចចម្លងបែបប្រពៃណីពុំអាចចាប់អត្ថបទដែលបង្កើតដោយ AI បានត្រឹមត្រូវឡើយ ដោយសារ AI សរសេរពាក្យថ្មីៗមិនមែនចម្លងផ្ទាល់។"),
            ("2", "TRUE", "B1 and B2 note AI frequently hallucinates fake citations with syntactic confidence.", "ពិត (TRUE) — ប្រព័ន្ធ AI តែងតែបង្កើតប្រភពឯកសារយោងក្លែងក្លាយដែលមើលទៅដូចពិត។"),
            ("3", "TRUE", "C1 explicitly states automated detectors generate false positives that disproportionately penalize non-native English scholars.", "ពិត (TRUE) — ឧបករណ៍ចាប់ AI ដោយស្វ័យប្រវត្តិតែងតែចាប់ខុសលើសំណេររបស់សិស្សមិនមែនជនជាតិដើមដែលប្រើភាសាអង់គ្លេស។"),
            ("4", "FALSE", "There is no mention that universities have banned computers; they are adapting guidelines and assessment methods.", "មិនពិត (FALSE) — គ្មានសាកលវិទ្យាល័យណាទៅហាមឃាត់ការប្រើកុំព្យូទ័រនោះឡើយ ផ្ទុយទៅវិញគេកែសម្រួលគោលការណ៍វាយតម្លៃ។")
        ]
    },
    {
        "num": 12,
        "title": "Algorithmic Bias in Recruitment and Hiring",
        "title_kh": "ភាពលម្អៀងនៃក្បួនដោះស្រាយក្នុងការជ្រើសរើសបុគ្គលិក",
        "theme_name": "Technology & Workplace Algorithms",
        "qtype": "True / False / Not Given",
        "vocab": [
            ("algorithmic", "adj", "B2", "relating to step-by-step computational rules", "នៃក្បួនដោះស្រាយកុំព្យូទ័រ"),
            ("recruitment", "noun", "B2", "the action of finding and hiring employees", "ការជ្រើសរើសបុគ្គលិក"),
            ("discriminatory", "adj", "B2/C1", "making an unjust distinction in treatment", "ដែលរើសអើង"),
            ("perpetuate", "verb", "C1", "to cause an undesirable situation to continue", "ធ្វើឱ្យបន្តកើតមាន"),
            ("transparency", "noun", "B2/C1", "operating in an open and accountable way", "តម្លាភាព"),
            ("proxy", "noun", "C1/C2", "a metric used to represent the value of something else", "តំណាង, រង្វាស់ជំនួស")
        ],
        "b1": """In the corporate world today, large companies receive thousands of job applications every week. To save time and human resources, human resource managers use automated computer algorithms to review resumes. These computer tools can scan a resume in a fraction of a second, checking for relevant university degrees, job titles, and specific technical keywords.

However, computer scientists have discovered that recruitment algorithms often contain unfair biases. Because these computer programs are trained on past hiring data from the company, they learn historical human prejudices. For example, if a software company hired mostly male engineers for twenty years, the computer algorithm might automatically give lower scores to female applicants. Companies must regularly inspect their hiring software to ensure every candidate is treated fairly and equally.""",
        "b2": """The deployment of artificial intelligence and machine learning algorithms in corporate talent recruitment has escalated rapidly. Corporations justify automated resume screening by emphasizing operational efficiency, reduction of administrative overhead, and the ostensible elimination of conscious human hiring biases. Natural language processing models evaluate candidate profiles against historical performance indicators, identifying optimal candidates within seconds.

Nevertheless, empirical audits reveal that automated recruitment systems frequently perpetuate and amplify systemic discrimination. Machine learning models trained on historical employment datasets inherit historical societal inequities. When trained on homogeneous corporate demographics, algorithms identify proxy variables—such as candidate sports activities, postal codes, or women's college affiliations—as negative predictors of workplace success. Consequently, algorithmic neutrality is often an illusion, necessitating regulatory oversight and independent algorithmic bias auditing.""",
        "c1": """The institutionalization of algorithmic hiring systems represents a technocratic attempt to rationalize employment selection through statistical modeling. Proponents claim that replacing subjective human intuition with quantifiable predictive metrics sanitizes recruitment from nepotism and cognitive bias. In operational reality, automated hiring software functions as an algorithmic mirror of structural labor inequalities, laundering historical discrimination through the veneer of mathematical objectivity.

Because neural networks identify statistical correlations rather than causal attributes, they latch onto subtle linguistic and demographic proxies that correlate with historical demographic dominance. An algorithm optimized to maximize similarity to a company's historical high performers will systematically undervalue candidates from marginalized backgrounds. Moreover, the proprietary nature of commercial recruitment algorithms creates an accountability vacuum—a 'black box' phenomenon where rejected candidates are systematically denied transparent explanations for their automated disqualification.""",
        "c2": """The ascendancy of algorithmic gatekeeping in employment recruitment exemplifies the insidious ideology of technological solutionism: the belief that complex socio-ethical dilemmas can be resolved through computational optimization. By reconfiguring the evaluation of human potential into an algorithmic screening process, corporations reduce the multifaceted nuances of human character, resilience, and lived experience to sterile vector embeddings and semantic proximity scores.

The profound danger of this algorithmic regime lies in its unassailable aesthetic of impartiality. While human prejudice is contingent, visible, and contestable, algorithmic bias is systemic, automated, and veiled in the sacred authority of mathematics. When software penalizes an applicant based on statistical proxies of class, race, or gender, it codifies historical oppression as an immutable law of technological probability. To surrender the sovereign discernment of human merit to opaque algorithmic black boxes is to abdicate moral responsibility, converting the labor market into a self-fulfilling prophecy of exclusion.""",
        "questions": [
            ("1", "Automated resume screeners identify ideal candidates in seconds by evaluating profiles against historical data."),
            ("2", "Recruitment algorithms are mathematically guaranteed to eliminate all forms of human prejudice completely."),
            ("3", "Algorithms trained on historically male-dominated datasets have been documented to downgrade female applicants."),
            ("4", "Most corporate recruitment algorithms provide open-source, fully transparent code for applicants to inspect.")
        ],
        "answers": [
            ("1", "TRUE", "B1 and B2 explain that automated algorithms scan thousands of resumes in seconds using keywords and past indicators.", "ពិត (TRUE) — ក្បួនដោះស្រាយស្វ័យប្រវត្តិអាចពិនិត្យប្រវត្តិរូបសង្ខេបរាប់ពាន់ក្នុងពេលតែប៉ុន្មានវិនាទីដោយផ្អែកលើទិន្នន័យអតីតកាល។"),
            ("2", "FALSE", "B1, B2, and C1 highlight that algorithms actually perpetuate and amplify historical discrimination rather than eliminating it.", "មិនពិត (FALSE) — អត្ថបទបញ្ជាក់ថាប្រព័ន្ធស្វ័យប្រវត្តិតែងតែចម្លង និងពង្រីកភាពលម្អៀងពីអតីតកាល មិនមែនលុបបំបាត់ការរើសអើងនោះទេ។"),
            ("3", "TRUE", "B1 and B2 give explicit examples of algorithms trained on past male demographics penalizing women's applications.", "ពិត (TRUE) — កម្មវិធីដែលរៀនពីទិន្នន័យចាស់ដែលមានបុគ្គលិកភាគច្រើនជាបុរស តែងតែទម្លាក់ពិន្ទុបេក្ខនារីដោយស្វ័យប្រវត្តិ។"),
            ("4", "FALSE", "C1 states commercial algorithms are proprietary 'black boxes' where rejected candidates are denied transparent explanations.", "មិនពិត (FALSE) — កម្មវិធីជ្រើសរើសបុគ្គលិកភាគច្រើនជាកម្មសិទ្ធិឯកជន និងជាប្រព័ន្ធបិទជិត (Black box) មិនមែនជាកូដចំហឱ្យពិនិត្យនោះឡើយ។")
        ]
    },
    {
        "num": 13,
        "title": "Social Media Algorithms and Attention Spans",
        "title_kh": "ក្បួនដោះស្រាយបណ្តាញសង្គម និងកម្រិតនៃការផ្ដោតអារម្មណ៍",
        "theme_name": "Technology & Cognitive Psychology",
        "qtype": "True / False / Not Given",
        "vocab": [
            ("algorithm", "noun", "B1/B2", "a computational process or set of rules", "ក្បួនដោះស្រាយ"),
            ("dopamine", "noun", "B2", "a brain chemical involved in reward and focus", "សារធាតុដូប៉ាមីន"),
            ("fragmentation", "noun", "C1", "the process of breaking into small pieces", "ការបែកខ្ញែក"),
            ("retention", "noun", "B2", "the capacity to maintain focus or keep facts", "ការរក្សាទុក, ការផ្ដោតជាប់"),
            ("monetization", "noun", "B2/C1", "the process of converting something into money", "ការរកប្រាក់ពីអ្វីមួយ"),
            ("hyper-stimulation", "noun", "C2", "excessive sensory arousal and stimulation", "ការភ្ញោចខ្លាំងហួសហេតុ")
        ],
        "b1": """Smartphones and social media apps have become an essential part of daily life for billions of people. Platforms like TikTok, Instagram, and YouTube use powerful computer algorithms to study what each user watches. Within seconds of opening an app, the software delivers short videos customized to capture the viewer's attention. This keeps users scrolling on their phones for hours without noticing the time pass.

However, medical doctors and psychologists warn that constant scrolling has severe consequences for human attention spans. When people become accustomed to watching ten-second videos, their brains find it difficult to concentrate on long books, detailed lectures, or demanding office work. Many teenagers report feeling restless and bored whenever they cannot check their smartphone notifications. Limiting daily screen time is becoming essential to protect mental health.""",
        "b2": """The profound impact of recommendation algorithms on human neuro-cognition has emerged as a major public health concern. Social media networks deploy variable ratio reward schedules—mechanisms identical to those utilized in casino slot machines—to maximize user retention and engagement metrics. By algorithmically serving ultra-concise, hyper-stimulating video content tailored to subconscious micro-preferences, platforms induce continuous dopamine spikes that reinforce habitual digital consumption.

This relentless sensory stimulation precipitates cognitive fragmentation. Psychological research demonstrates an inverse relationship between heavy short-form video consumption and sustained attentional capacity. As the brain adapts to rapid digital stimulation, its neural threshold for boredom drops dramatically, compromising working memory retention and deep analytical reading capabilities. Consequently, educational institutions report widespread difficulties in maintaining student focus during complex analytical tasks.""",
        "c1": """The commodification of human attention through algorithmic behavioral optimization constitutes an unprecedented cognitive transformation. Social media business models, fundamentally dependent upon advertising monetization, treat human consciousness as a finite extractive resource. Advanced machine learning models continuously map biological vulnerabilities, serving individualized content loops that exploit affective triggers, outrage, and novelty to preempt voluntary attentional disengagement.

The neurobiological consequences of this continuous partial attention are profound. Prolonged exposure to algorithmic hyper-stimulation attenuates the prefrontal cortex's capacity for top-down executive control, subordinating deliberate focus to bottom-up sensory capture. Cognitive faculties requiring contemplative depth—such as philosophical synthesis, extended narrative immersion, and dialectical problem-solving—are systematically atrophied. The resulting societal condition is not merely digital distraction, but an epistemic crisis characterized by systemic attentional impoverishment.""",
        "c2": """The algorithmic colonisation of the human attentional apparatus represents the apex of surveillance capitalism. In subjugating human consciousness to recursive neural optimization, social platforms have successfully engineered what philosophers term the prosthetic will: a state wherein human desire and attentional orientation are imperceptibly outsourced to predictive silicon engines. The sacred inner citadel of voluntary contemplation is dismantled and auctioned off to advertising consortia in microsecond intervals.

This systematic dismantling of contemplative stillness exacts an existential toll. A consciousness conditioned by ceaseless algorithmic feeding loses the capacity for sustained solitude—the very soil from which profound artistic creation, spiritual discernment, and philosophical rebellion germinate. When human attention is fractured into ephemeral dopamine-driven shards, the capacity for sustained political mobilization and collective deliberation evaporates. To reclaim one's attention from the algorithmic machine is thus no longer a matter of personal digital hygiene; it is an act of sovereign ontological resistance.""",
        "questions": [
            ("1", "Recommendation algorithms utilize reward mechanisms similar to those found in casino gambling machines."),
            ("2", "Watching short-form video clips has been proven to expand long-term working memory capacity in adolescents."),
            ("3", "Social media business models rely heavily on monetizing captured human attention through targeted advertisements."),
            ("4", "All major smartphone operating systems have permanently disabled all notification systems by federal law.")
        ],
        "answers": [
            ("1", "TRUE", "B2 explicitly compares social media reward schedules to mechanisms utilized in casino slot machines.", "ពិត (TRUE) — ក្បួនដោះស្រាយបណ្តាញសង្គមប្រើប្រាស់ទម្រង់រង្វាន់ភ្ញោចខួរក្បាលស្រដៀងនឹងម៉ាស៊ីនស្លុតក្នុងកាស៊ីណូ។"),
            ("2", "FALSE", "B2 states short-form video consumption compromises working memory retention and attentional capacity, the exact opposite of expanding it.", "មិនពិត (FALSE) — ការមើលវីដេអូខ្លីៗច្រើនហួសហេតុធ្វើឱ្យធ្លាក់ចុះការចងចាំ និងសមត្ថភាពផ្ដោតអារម្មណ៍ មិនមែនពង្រីកវាឡើយ។"),
            ("3", "TRUE", "C1 explicitly states social media business models depend upon advertising monetization, treating attention as an extractive resource.", "ពិត (TRUE) — គំរូអាជីវកម្មបណ្តាញសង្គមពឹងផ្អែកលើការទាញប្រាក់ពីការផ្សាយពាណិជ្ជកម្មតាមរយៈការទាក់ទាញចំណាប់អារម្មណ៍អ្នកប្រើ។"),
            ("4", "FALSE", "There is no mention of federal laws permanently disabling smartphone notifications.", "មិនពិត (FALSE) — គ្មានព័ត៌មានដែលបញ្ជាក់ថាច្បាប់បានហាមឃាត់ការលោតដំណឹង (Notification) លើទូរសព្ទនោះឡើយ។")
        ]
    },
    {
        "num": 14,
        "title": "The Evolution of Renewable Battery Technologies",
        "title_kh": "ការវិវត្តនៃបច្ចេកវិទ្យាអាគុយថាមពលកកើតឡើងវិញ",
        "theme_name": "Technology & Clean Energy",
        "qtype": "True / False / Not Given",
        "vocab": [
            ("renewable", "adj", "B1/B2", "energy from a source not depleted when used", "កកើតឡើងវិញ"),
            ("intermittency", "noun", "C1", "the state of stopping and starting at intervals", "ភាពមិនទៀងទាត់"),
            ("degradation", "noun", "B2/C1", "the process of deteriorating in condition", "ការទ្រុឌទ្រោម, ការធ្លាក់ចុះគុណភាព"),
            ("density", "noun", "B2", "compactness; storage capacity per unit volume", "ដង់ស៊ីតេ, បរិមាណផ្ទុកក្នុងមាឌ"),
            ("electrolyte", "noun", "C1", "a liquid or gel containing ions conducting electricity", "អេឡិចត្រូលីត, ជាតិគីមីចម្លងអគ្គិសនី"),
            ("scalability", "noun", "B2/C1", "the capacity to be changed in size or scale", "សមត្ថភាពពង្រីកមាត្រដ្ឋាន")
        ],
        "b1": """Solar panels and wind turbines produce clean electricity without burning coal or oil. However, wind does not blow all the time, and solar panels cannot generate power during the night. For this reason, modern clean energy systems require advanced rechargeable batteries to store excess electricity for cloudy days and quiet nights.

Currently, lithium-ion batteries are the most common type used in electric cars and home energy storage. While lithium batteries store a large amount of power in a lightweight package, they have serious drawbacks. Mining lithium and cobalt damages local environments, and batteries lose storage capacity after several years of daily charging. Scientists around the world are working hard to invent safer, cheaper batteries made from common materials like sodium and salt.""",
        "b2": """The widespread transition toward a decarbonized energy grid is fundamentally reliant on breakthroughs in stationary electrochemical storage. Renewable energy sources like photovoltaic solar and offshore wind inherently suffer from intermittency—the inability to align peak generation with temporal consumer demand. Scalable utility-scale batteries provide the critical grid-stabilization mechanism required to store peak renewable overproduction and dispatch it during periods of high demand.

While traditional lithium-ion chemistries dominate the electric mobility sector due to their high volumetric energy density, their suitability for stationary grid-scale storage is increasingly questioned. Lithium and cobalt extraction entails severe geopolitical vulnerability, supply chain volatility, and acute ecological devastation. In response, materials scientists are accelerating the commercialization of alternative chemistries, notably sodium-ion batteries and iron-flow systems, which offer superior thermal stability and abundant raw materials at reduced capital cost.""",
        "c1": """The decarbonization of terrestrial energy systems has exposed electrochemical energy storage as the vital technological bottleneck of the clean energy transition. The deployment of variable renewable energy introduces profound instability into electrical transmission grids, demanding storage architectures capable of frequency regulation, peak shaving, and multi-day dispatchability. While market momentum has propelled lithium-nickel-manganese-cobalt (NMC) chemistries to manufacturing supremacy, their thermodynamic limitations and material supply constraints demand diversification.

Solid-state electrolyte architectures represent a quantum leap in electrochemical performance, theoretically eliminating flammable liquid electrolytes while enabling lithium-metal anodes that drastically elevate energy densities. Concurrently, for non-mobile stationary applications where spatial compactness is secondary to levelized cost of storage, redox-flow batteries and zinc-air systems demonstrate immense promise. These flow architectures decouple power capacity from energy capacity, permitting near-infinite cycling lifespans without the catastrophic thermal runaway vulnerabilities endemic to legacy chemistries.""",
        "c2": """The quest for high-density electrochemical storage encapsulates the central physical paradox of modern technological civilization: the imperative to capture and domesticate thermodynamic entropy. The green energy transition was long heralded as a liberation from the material extraction of fossilized hydrocarbons; yet the contemporary battery economy reveals itself as an equally intensive regime of geophysical plunder, requiring vast quantities of rare earths, lithium brines, and transition metals extracted through devastating ecological exploitation.

True technological maturation in energy storage requires transcending the lithium paradigm altogether. The frontier of electrochemical engineering lies in closed-loop, earth-abundant material systems that mimic biological metabolic cycles. By harnessing sodium, iron, and aqueous electrolytes, researchers are pioneering storage media that dissolve the Faustian bargain between clean grid stability and environmental degradation. The triumph of renewable civilization will ultimately be determined not by the sheer quantity of electricity we generate, but by the material wisdom embedded within the vessels built to contain it.""",
        "questions": [
            ("1", "Renewable energy from wind and solar is intermittent because generation does not always coincide with peak usage."),
            ("2", "Lithium-ion batteries maintain 100% of their storage capacity perpetually without chemical degradation."),
            ("3", "Alternative battery chemistries such as sodium-ion utilize more abundant materials and provide enhanced thermal stability."),
            ("4", "Redox-flow battery systems couple energy capacity rigidly to power capacity, preventing separate scaling.")
        ],
        "answers": [
            ("1", "TRUE", "B1 and B2 state that solar and wind suffer from intermittency because weather fluctuates and does not match consumer demand.", "ពិត (TRUE) — ថាមពលខ្យល់ និងពន្លឺព្រះអាទិត្យមានភាពមិនទៀងទាត់ ព្រោះការផលិតមិនត្រូវគ្នានឹងតម្រូវការប្រើប្រាស់គ្រប់ពេលនោះទេ។"),
            ("2", "FALSE", "B1 explicitly states batteries lose storage capacity after several years, and C1 mentions thermodynamic degradation.", "មិនពិត (FALSE) — អាគុយលីចូមតែងតែធ្លាក់ចុះគុណភាព និងបាត់បង់សមត្ថភាពស្តុកថាមពលបន្ទាប់ពីការប្រើប្រាស់ច្រើនឆ្នាំ។"),
            ("3", "TRUE", "B2 states sodium-ion batteries offer superior thermal stability and use abundant materials at lower costs.", "ពិត (TRUE) — បច្ចេកវិទ្យាអាគុយសូដ្យូមប្រើប្រាស់វត្ថុធាតុដើមសម្បូរបែបក្នុងធម្មជាតិ និងមានស្ថេរភាពកម្ដៅល្អប្រសើរជាង។"),
            ("4", "FALSE", "C1 explicitly states flow architectures decouple power capacity from energy capacity, directly contradicting the statement.", "មិនពិត (FALSE) — អត្ថបទបញ្ជាក់ថាអាគុយប្រភេទ Redox-flow ញែកដាច់រវាងកម្លាំងថាមពល និងបរិមាណផ្ទុក ដែលអនុញ្ញាតឱ្យពង្រីកបានដោយឯករាជ្យ។")
        ]
    },
    {
        "num": 15,
        "title": "Automation and the Displacement of White-Collar Jobs",
        "title_kh": "ស្វ័យប្រវត្តិកម្ម និងការជំនួសការងារការិយាល័យ",
        "theme_name": "Technology & Labor Economics",
        "qtype": "True / False / Not Given",
        "vocab": [
            ("automation", "noun", "B2", "the use of automatic equipment and software in work", "ស្វ័យប្រវត្តិកម្ម"),
            ("displacement", "noun", "B2/C1", "the removal of someone or something from a role", "ការផ្លាស់ចេញ, ការជំនួស"),
            ("white-collar", "adj", "B2", "relating to professional or office work", "ការងារការិយាល័យ, បញ្ញវន្ត"),
            ("redundant", "adj", "C1", "no longer needed or useful; superfluous", "ដែលលែងត្រូវការ"),
            ("cognitive", "adj", "B2/C1", "relating to intellectual mental tasks", "ខាងបញ្ញា"),
            ("reskilling", "noun", "B2/C1", "training employees in new skills for new roles", "ការបណ្តុះបណ្តាលជំនាញថ្មី")
        ],
        "b1": """In the past, automated machines replaced mostly blue-collar workers in factories, such as assembly line builders and packaging operators. Today, however, artificial intelligence software is beginning to affect white-collar office jobs. Computer algorithms can now review legal contracts, analyze financial accounting data, and write marketing articles much faster than human workers.

This rapid automation causes deep worry among university students and office workers. Many people fear that administrative jobs, basic journalism, and routine legal research will disappear completely. However, economists point out that technology also creates new opportunities. While machines handle repetitive data tasks, humans can focus on creative strategy, leadership, and emotional counseling. To remain employed, workers must commit to lifelong learning and upgrade their skills regularly.""",
        "b2": """The current wave of cognitive automation powered by advanced machine learning models marks a paradigm shift in the history of labor economics. Unlike twentieth-century industrial mechanization, which predominantly displaced routine manual labor, generative algorithms and automated analytical tools are directly invading knowledge-intensive domains. Fields once considered impregnable to automation—including paralegal discovery, radiological image diagnosis, software debugging, and equity research—are undergoing rapid labor substitution.

This structural transformation generates substantial economic disruption. Middle-tier office roles face acute contraction, exacerbating wealth polarization between elite algorithmic architects and an expanding precariat of low-wage service workers. While optimistic economists argue that artificial intelligence will create complementary positions through task re-composition, the velocity of technological displacement severely outpaces the capacity of institutional reskilling programs, resulting in technological unemployment for specialized professionals.""",
        "c1": """The automation of cognitive labor marks the unraveling of the historic social contract governing knowledge workers. For generations, the acquisition of specialized academic credentials insulated white-collar professionals from the precarious winds of technological disruption. Today, generative neural architectures commodify complex cognitive operations, executing semantic synthesis, statistical modeling, and programmatic coding at near-zero marginal cost. This erosion of cognitive exceptionalism is destabilizing professional middle classes worldwide.

The dynamics of this displacement are characterized by a profound bifurcation of the labor market. While high-level conceptual ideation, ethical oversight, and intersubjective negotiations retain human preeminence, intermediate analytical execution is systematically automated. Consequently, corporate hierarchies are flattening, eliminating traditional entry-level apprenticeship roles through which junior professionals historically accumulated domain mastery. Without structural interventions such as tax reform on algorithmic capital or state-funded transitional stipends, the unconstrained automation of intellectual labor threatens to precipitate widespread socioeconomic alienation.""",
        "c2": """The automated liquidation of white-collar employment marks the final commodification of the intellect under advanced digital capitalism. In stripping the knowledge worker of the illusion of cognitive immunity, artificial intelligence lays bare the relentless logic of industrial efficiency: any labor that can be formalized into computational syntax will inevitably be outsourced to synthetic processors. The paralegal, the financial analyst, and the copywriter find themselves standing where the loom operator and autoworker stood a century prior—disposable flesh in the path of mechanical inevitability.

The tragedy of this transition lies not merely in the loss of economic livelihood, but in the existential eviction of human beings from the sphere of creative and intellectual purpose. When algorithms author our arguments, compose our symphonies, and arbitrate our disputes, they do not emancipate humanity; they alienate us from our defining faculties. A civilization that automates its intellectual consciousness in pursuit of corporate margin is a civilization asleep at the wheel of its own obsolescence. The urgent task is not to accommodate the machine, but to subordinate technological power to humanistic dignity.""",
        "questions": [
            ("1", "Nineteenth-century industrial automation predominantly targeted white-collar accounting and legal positions."),
            ("2", "AI models can now review legal documents and diagnose radiological imagery with high computational speed."),
            ("3", "The speed of algorithmic workplace displacement currently exceeds the capacity of many worker retraining programs."),
            ("4", "All world governments have voted unanimously to ban artificial intelligence in corporate environments.")
        ],
        "answers": [
            ("1", "FALSE", "B1 and B2 state that earlier industrial mechanization displaced routine manual factory labor, not white-collar legal jobs.", "មិនពិត (FALSE) — បដិវត្តន៍ឧស្សាហកម្មកាលពីអតីតកាលជំនួសកម្លាំងពលកម្មរោងចក្រ មិនមែនការងារការិយាល័យ និងច្បាប់នោះទេ។"),
            ("2", "TRUE", "B1 and B2 confirm algorithms review legal contracts and assist in radiological diagnostic imaging.", "ពិត (TRUE) — ក្បួនដោះស្រាយបច្ចុប្បន្នអាចពិនិត្យកិច្ចសន្យាច្បាប់ និងវិភាគរូបភាពវេជ្ជសាស្ត្របានយ៉ាងលឿន។"),
            ("3", "TRUE", "B2 states that the velocity of displacement severely outpaces the capacity of institutional reskilling programs.", "ពិត (TRUE) — ល្បឿននៃការផ្លាស់ប្តូរការងារដោយសារ AI កំពុងដើរលឿនជាងសមត្ថភាពនៃការបណ្តុះបណ្តាលបុគ្គលិកឡើងវិញ។"),
            ("4", "FALSE", "There is no claim of any worldwide unanimous ban on corporate artificial intelligence.", "មិនពិត (FALSE) — គ្មានរដ្ឋាភិបាលណាបានបោះឆ្នោតជាឯកច្ឆន្ទហាមឃាត់ AI ក្នុងវិស័យសាជីវកម្មនោះឡើយ។")
        ]
    },
    {
        "num": 16,
        "title": "Quantum Computing and Modern Cryptography",
        "title_kh": "កុំព្យូទ័រខ្វាន់ទិច និងគ្រីបតូក្រាហ្វីទំនើប",
        "theme_name": "Technology & Cyber Defense",
        "qtype": "True / False / Not Given",
        "vocab": [
            ("quantum", "adj", "C1", "relating to the smallest discrete values of physics", "ខាងខ្វាន់ទិច"),
            ("cryptography", "noun", "C1", "the practice of securing communications using codes", "គ្រីបតូក្រាហ្វី, ការអ៊ិនគ្រីប"),
            ("qubit", "noun", "C2", "a basic unit of quantum information", "ឃ្យូប៊ីត (ឯកតាព័ត៌មានខ្វាន់ទិច)"),
            ("vulnerability", "noun", "B2", "the state of being exposed to attack or harm", "ភាពងាយរងគ្រោះ"),
            ("superposition", "noun", "C2", "the ability of quantum systems to be in multiple states simultaneously", "ការស្ថិតក្នុងស្ថានភាពច្រើនដំណាលគ្នា"),
            ("infrastructure", "noun", "B2", "basic physical and organizational structures", "ហេដ្ឋារចនាសម្ព័ន្ធ")
        ],
        "b1": """Every time you purchase something online or log into your bank account, your personal information is protected by digital encryption. Standard computers protect this data using complex mathematical problems that would take a normal computer thousands of years to crack. This encryption system keeps credit card numbers and passwords safe from cyber criminals.

However, the rapid development of quantum computers threatens this digital security. Unlike regular computers that process information in simple ones and zeros, quantum computers use the rules of physics to perform calculations at unbelievable speeds. Scientists estimate that a powerful quantum computer could break current banking encryption in a matter of minutes. Governments and technology companies are now racing to build new 'post-quantum' security systems before these supermachines become fully operational.""",
        "b2": """The advent of scalable quantum computing poses an existential challenge to global cybersecurity and cryptographic infrastructure. Contemporary public-key cryptography—predominantly asymmetric algorithms like RSA and Elliptic Curve Cryptography—relies on the computational intractability of prime factorization and discrete logarithms. Classic supercomputers would require millennia to brute-force these cryptographic keys, ensuring secure transmission of financial transactions and state secrets.

Quantum computing fundamentally alters this computational paradigm through the principles of superposition and entanglement. Leveraging Shor's algorithm, a sufficiently fault-tolerant quantum computer utilizing thousands of error-corrected qubits could solve prime factorization equations in polynomial time, rendering existing public-key encryption obsolete. Consequently, international standards organizations are expediting the ratification and deployment of post-quantum cryptography (PQC) based on lattice-based mathematics to safeguard critical infrastructure against retroactive decryption.""",
        "c1": """The intersection of quantum information theory and algorithmic cryptography represents a profound inflection point in digital statecraft and data sovereignty. The security architecture of the global digital economy is predicated upon a fragile mathematical asymmetry: encrypting information is computationally trivial, whereas deciphering it without the private key is computationally insurmountable for classical Turing architectures. The realization of fault-tolerant quantum hardware collapses this foundational asymmetry.

The strategic gravity of this vulnerability has triggered a clandestine phenomenon termed 'harvest now, decrypt later,' wherein hostile state actors systematically intercept and archive encrypted diplomatic and military communications, anticipating future quantum decryption capabilities. To avert systemic cryptographic collapse, cryptographers are developing lattice-based and multivariate polynomial algorithms that remain computationally intractable even for quantum architectures. However, transitioning global legacy hardware, telecommunications protocols, and industrial control systems to post-quantum standards presents a colossal logistical endeavor fraught with systemic vulnerabilities.""",
        "c2": """The impending quantum transcendence of classical cryptography exposes the ephemeral nature of all human security paradigms. For decades, modern civilization constructed its digital empires upon the serene mathematical assumption that certain mathematical barriers were impenetrable. Yet nature operates not on the rigid binaries of classical arithmetic, but on the shimmering, probabilistic canvas of quantum mechanics, where qubits traverse simultaneous realities in defiance of classical computational limits.

This technological revolution carries profound geopolitical stakes. The nation or entity that achieves sovereign quantum supremacy will hold the master key to global financial networks, satellite telecommunications, and intelligence archives, collapsing the cryptographic armor of adversaries overnight. To imagine that post-quantum mathematical algorithms will permanently insulate society against quantum penetration is an exercise in hubris. We are crossing into an era of permanent computational fluidity, where the illusion of absolute cryptographic permanence dissolves before the infinite computational majesty of the cosmos.""",
        "questions": [
            ("1", "Modern online banking encryption relies on mathematical problems that take classical computers thousands of years to break."),
            ("2", "Quantum computers process data strictly using ordinary binary bits restricted to zero or one."),
            ("3", "'Harvest now, decrypt later' refers to actors intercepting encrypted data to decrypt with future quantum hardware."),
            ("4", "Post-quantum cryptographic algorithms have already been completely installed on all devices worldwide.")
        ],
        "answers": [
            ("1", "TRUE", "B1 and B2 state that current encryption relies on math problems like prime factorization that take classical computers millennia to break.", "ពិត (TRUE) — ការអ៊ិនគ្រីបធនាគារបច្ចុប្បន្នពឹងផ្អែកលើលំហាត់គណិតវិទ្យាដែលកុំព្យូទ័រធម្មតាត្រូវចំណាយពេលរាប់ពាន់ឆ្នាំដើម្បីបំបែក។"),
            ("2", "FALSE", "B1 and B2 state quantum computers utilize quantum principles such as qubits, superposition, and entanglement, not simple binary bits.", "មិនពិត (FALSE) — កុំព្យូទ័រខ្វាន់ទិចប្រើប្រាស់ Qubits និងគោលការណ៍ Superposition មិនមែនប្រព័ន្ធទ្វេភាគ ០ និង ១ ធម្មតានោះឡើយ។"),
            ("3", "TRUE", "C1 explicitly defines 'harvest now, decrypt later' as intercepting and archiving data for future quantum decryption.", "ពិត (TRUE) — យុទ្ធសាស្ត្រនេះសំដៅលើការលួចរក្សាទុកទិន្នន័យអ៊ិនគ្រីបទុកជាមុន ដើម្បីចាំបំបែកកូដនៅពេលកុំព្យូទ័រខ្វាន់ទិចលេចរូបរាងឡើង។"),
            ("4", "FALSE", "C1 states transitioning legacy systems to post-quantum standards presents a colossal and ongoing logistical endeavor.", "មិនពិត (FALSE) — ការផ្លាស់ប្តូរទៅប្រព័ន្ធគ្រីបតូក្រាហ្វីជំនាន់ថ្មីកំពុងស្ថិតក្នុងការអភិវឌ្ឍ និងដំឡើងជាបន្តបន្ទាប់ មិនទាន់បញ្ចប់ទូទាំងពិភពលោកឡើយ។")
        ]
    },
    {
        "num": 17,
        "title": "Surveillance Capitalism and Personal Data Privacy",
        "title_kh": "មូលធននិយមឃ្លាំមើល និងឯកជនភាពទិន្នន័យផ្ទាល់ខ្លួន",
        "theme_name": "Technology & Digital Ethics",
        "qtype": "True / False / Not Given",
        "vocab": [
            ("surveillance", "noun", "B2", "close observation or monitoring", "ការឃ្លាំមើល"),
            ("capitalism", "noun", "B2", "an economic system based on private ownership", "មូលធននិយម"),
            ("monetize", "verb", "B2/C1", "to convert an asset or data into money", "ទាញយកប្រាក់"),
            ("commodification", "noun", "C2", "treating something as a mere commercial product", "ការធ្វើឱ្យទៅជាទំនិញ"),
            ("behavioral", "adj", "B2", "relating to actions and conduct", "ខាងអាកប្បកិរិយា"),
            ("sovereignty", "noun", "C1", "supreme power or personal autonomy", "អធិបតេយ្យភាព, ភាពជាម្ចាស់")
        ],
        "b1": """Most popular online smartphone apps and search engines are completely free to download and use. However, these internet companies earn billions of dollars every month. They make money by tracking what users do online—including search history, geographic location, messages, and shopping habits. This practice of gathering personal information to sell targeted advertisements is called the data economy.

Many privacy advocates believe that this data collection has gone too far. Users often click 'Agree' on terms of service without understanding that their private messages and daily habits are recorded and shared with corporate advertisers. In some cases, data brokers even sell sensitive medical and financial details without clear permission. Citizens must demand stricter legal protections to keep their digital lives private.""",
        "b2": """The socioeconomic paradigm known as 'surveillance capitalism' has redefined the architecture of the modern internet. Pioneered by tech conglomerates, this business model extracts behavioral data from digital interactions not merely to enhance service quality, but to fabricate predictive behavioral profiles. These computational profiles are subsequently auctioned to advertisers seeking to manipulate consumer decisions and voting preferences with psychological precision.

This pervasive data extraction compromises the foundational right to personal privacy. The opacity of algorithmic tracking frameworks, coupled with consumer resignation toward convoluted terms-of-service agreements, renders genuine informed consent a legal fiction. Furthermore, the aggregation of intimate biometric, financial, and relational data by monopolistic corporations creates profound societal vulnerabilities, enabling unprecedented corporate surveillance and the subtle erosion of democratic self-determination.""",
        "c1": """Surveillance capitalism represents a unilateral colonization of human experience as raw material for behavioral data extraction. In her seminal critique, Shoshana Zuboff delineates how tech oligarchies claim human cognitive activity as a free resource, converting behavioral surplus into predictive algorithmic products that are bought and sold on behavioral futures markets. In this asymmetrical economic regime, users are neither customers nor products; they are the dispossessed source of algorithmic rents.

The existential danger of this paradigm transcends conventional notions of privacy infringement. By deploying nudging algorithms, dynamic psychographic profiling, and micro-targeted behavioral feedback loops, surveillance platforms do not merely predict human behavior—they actively modify and condition it. This digital behaviorism degrades autonomous human volition, creating an epistemic environment wherein individual choices are imperceptibly directed toward corporate profitability and political polarization, undermining the deliberative autonomy essential for democratic citizenship.""",
        "c2": """The architecture of surveillance capitalism embodies an unprecedented totalitarian mutation of economic power. Unlike historic autocracies that enforced compliance through physical violence and state terror, the surveillance digital apparatus governs through omnipresent algorithmic seduction, behavioral preemption, and cognitive enclosure. Every keystroke, physiological tremor, and subconscious gaze is captured, quantified, and transmuted into behavioral capital by corporate panopticons that operate entirely beyond democratic accountability.

To characterize this systematic dispossession merely as a regulatory privacy dispute is to fundamentally misunderstand its historical magnitude. Surveillance capitalism represents an ontological assault on the sanctuary of the human interior—the sacred realm of unmonitored contemplation, self-invention, and moral agency. When the deepest precincts of the human psyche are strip-mined for speculative behavioral extraction, humanity is reduced to algorithmic livestock grazing within corporate walled gardens. The reclamation of data sovereignty is therefore the preeminent human rights struggle of the twenty-first century.""",
        "questions": [
            ("1", "Digital tech companies collect consumer behavioral data solely to improve server response times."),
            ("2", "Shoshana Zuboff's critique describes behavioral data being commodified into predictive market products."),
            ("3", "Complex terms-of-service agreements frequently make genuine informed consent unrealistic for average users."),
            ("4", "All social media platforms are legally prohibited from selling targeted advertisements in democratic countries.")
        ],
        "answers": [
            ("1", "FALSE", "B1 and B2 state data is extracted to fabricate predictive profiles and sell hyper-targeted advertisements for profit.", "មិនពិត (FALSE) — ក្រុមហ៊ុនបច្ចេកវិទ្យាប្រមូលទិន្នន័យដើម្បីបង្កើតប្រវត្តិរូបទស្សន៍ទាយ និងលក់ការផ្សាយពាណិជ្ជកម្មចំគោលដៅ មិនមែនគ្រាន់តែពន្លឿនម៉ាស៊ីនបម្រើការនោះទេ។"),
            ("2", "TRUE", "C1 explicitly cites Zuboff's theory of behavioral surplus being sold on behavioral futures markets.", "ពិត (TRUE) — ទស្សនៈរបស់ Shoshana Zuboff បញ្ជាក់ថាទិន្នន័យអាកប្បកិរិយារបស់មនុស្សត្រូវបានកែច្នៃជាទំនិញទីផ្សារទស្សន៍ទាយនាពេលអនាគត។"),
            ("3", "TRUE", "B2 states that convoluted terms-of-service agreements render genuine informed consent a legal fiction.", "ពិត (TRUE) — កិច្ចព្រមព្រៀងលក្ខខណ្ឌប្រើប្រាស់វែងអន្លាយ និងស្មុគស្មាញ ធ្វើឱ្យការយល់ព្រមពិតប្រាកដរបស់អ្នកប្រើប្រាស់ក្លាយជារឿងពិបាកកើតឡើង។"),
            ("4", "FALSE", "The text explains targeted advertising is the core business model of tech giants, not legally banned.", "មិនពិត (FALSE) — គ្មានការហាមឃាត់ការលក់ពាណិជ្ជកម្មចំគោលដៅនៅក្នុងប្រទេសប្រជាធិបតេយ្យទាំងស្រុងនោះឡើយ។")
        ]
    },
    {
        "num": 18,
        "title": "Telemedicine and Remote Healthcare Delivery",
        "title_kh": "វេជ្ជសាស្ត្រពីចម្ងាយ និងការផ្តល់សេវាថែទាំសុខភាពតាមប្រព័ន្ធឌីជីថល",
        "theme_name": "Technology & Digital Health",
        "qtype": "True / False / Not Given",
        "vocab": [
            ("telemedicine", "noun", "B2", "the remote diagnosis and treatment of patients via telecommunications", "វេជ្ជសាស្ត្រពីចម្ងាយ"),
            ("consultation", "noun", "B2", "a meeting with a medical expert for advice", "ការពិគ្រោះជំងឺ"),
            ("accessibility", "noun", "B2", "the quality of being easy to reach or obtain", "ភាពងាយស្រួលក្នុងការទទួលបាន"),
            ("diagnostic", "adj", "B2/C1", "concerned with the diagnosis of illness", "ខាងរោគវិនិច្ឆ័យ"),
            ("disparity", "noun", "C1", "a great difference or inequality", "វិសមភាព, គម្លាត"),
            ("palpation", "noun", "C2", "the physical examination of medical tissues using hands", "ការស្ទាបពិនិត្យដោយដៃ")
        ],
        "b1": """Telemedicine allows patients to consult with certified doctors and medical specialists using video calls, telephone appointments, and mobile health apps. During the COVID-19 pandemic, this digital healthcare service expanded rapidly because people could not visit clinics safely. For individuals living in remote countryside villages, telemedicine eliminates the expensive travel costs and long travel times required to visit big city hospitals.

However, telemedicine cannot completely replace traditional in-person medical care. Doctors cannot physically touch a patient's body to check for swollen organs, listen closely to lung sounds, or perform immediate emergency blood tests through a video screen. In addition, elderly patients and low-income families often lack reliable high-speed internet connections or smartphones. A blended medical system combining online check-ups with physical clinic visits offers the most practical solution.""",
        "b2": """The institutional integration of telemedicine has revolutionized contemporary healthcare delivery frameworks. By leveraging high-speed broadband, secure biometric video conferencing, and wearable health monitoring devices, digital healthcare expands clinical access to historically underserved rural populations. Telemedicine dramatically reduces patient travel expenses, optimizes clinical appointment scheduling, and mitigates the transmission of hospital-acquired communicable pathogens in outpatient waiting rooms.

Nevertheless, significant clinical limitations accompany remote healthcare paradigms. The absence of physical palpation and hands-on diagnostic examination introduces risks of clinical misdiagnosis, particularly regarding acute abdominal pathologies or complex dermatological conditions. Furthermore, the 'digital health divide'—characterized by unequal access to broadband infrastructure and varying levels of digital health literacy among socioeconomically disadvantaged and geriatric demographics—threatens to exacerbate existing health inequities.""",
        "c1": """The digital reconfiguration of clinical medicine through telehealth platforms represents a transformative paradigm shift in healthcare economics and patient-physician relational dynamics. By decoupling diagnostic consultations from physical clinical infrastructure, telemedicine operationalizes asynchronous triage, chronic disease remote telemonitoring, and cross-border clinical consultations. This infrastructural decentralization enhances hospital capacity management and optimizes medical specialist allocation across disparate geographical territories.

However, this technological convenience introduces profound epistemological and bioethical dilemmas. The clinical encounter has historically constituted an embodied ritual where somatic tactile feedback, unspoken postural cues, and emotional presence inform diagnostic intuition. Virtual consultations risk reducing clinical diagnosis to algorithmic symptom-matching, increasing the likelihood of defensive over-prescribing of pharmaceuticals. Moreover, concerns regarding healthcare data breaches and the commercialization of confidential biometric tele-monitoring data underscore the urgent need for stringent regulatory safeguards.""",
        "c2": """The wholesale digitization of the clinical encounter under the rubric of telemedicine threatens to dismantle the ancient ontological foundation of medical practice: the sacred communion of embodied healing. Since the dawn of the Hippocratic tradition, healing has required physical presence—the diagnostic touch, the unmediated gaze, and the empathetic resonance between clinician and sufferer. In reducing the therapeutic relationship to an audiovisual pixel stream, digital medicine risks converting the profound human drama of illness into a transactional technocratic commodity.

While telehealth undoubtedly solves logistical friction across geographical peripheries, it must not be mistaken for the ultimate evolution of medical care. A disembodied clinician cannot feel the fever beneath the skin, detect the subtle cadence of labored breath, or convey the non-verbal solidarity that comforts a dying patient. To celebrate virtual care as an unmitigated advance without interrogating its spiritual and diagnostic losses is a symptom of technological myopia. True medicine must remain anchored in somatic reality; to abandon the flesh in favor of the screen is to forfeit the soul of healing.""",
        "questions": [
            ("1", "Telemedicine allows rural populations to access specialized medical consultations without expensive travel."),
            ("2", "Remote video consultations permit doctors to conduct hands-on physical palpation of internal organs."),
            ("3", "The 'digital health divide' describes disparities in broadband access and digital literacy affecting marginalized groups."),
            ("4", "All surgical procedures are now performed exclusively over Zoom calls without hospital operating rooms.")
        ],
        "answers": [
            ("1", "TRUE", "B1 and B2 state telemedicine eliminates travel expenses and expands access to underserved rural populations.", "ពិត (TRUE) — វេជ្ជសាស្ត្រពីចម្ងាយជួយអ្នករស់នៅតំបន់ជនបទទទួលបានការពិគ្រោះយោបល់ជាមួយគ្រូពេទ្យជំនាញដោយមិនបាច់ចំណាយពេលធ្វើដំណើរ។"),
            ("2", "FALSE", "B1, B2, and C2 emphasize that doctors cannot physically touch or palpate a patient's body through video screens.", "មិនពិត (FALSE) — អត្ថបទបញ្ជាក់ច្បាស់ថាគ្រូពេទ្យមិនអាចស្ទាបពិនិត្យសរីរាង្គកាយ ឬស្តាប់ចង្វាក់សួតតាមអេក្រង់វីដេអូនោះឡើយ។"),
            ("3", "TRUE", "B2 explicitly defines the digital health divide as unequal access to broadband and digital literacy among disadvantaged demographics.", "ពិត (TRUE) — គម្លាតសុខភាពឌីជីថលសំដៅលើវិសមភាពនៃការទទួលបានអ៊ីនធឺណិត និងចំណេះដឹងបច្ចេកវិទ្យាក្នុងចំណោមក្រុមងាយរងគ្រោះ។"),
            ("4", "FALSE", "There is no claim that all surgeries are performed over video calls; this is an absurd and unfounded exaggeration.", "មិនពិត (FALSE) — គ្មានការលើកឡើងថាការវះកាត់ទាំងអស់ត្រូវធ្វើឡើងតាម Zoom នោះឡើយ។")
        ]
    },
    {
        "num": 19,
        "title": "Autonomous Vehicles and Ethical Dilemmas",
        "title_kh": "យានយន្តស្វ័យប្រវត្ត និងបញ្ហាក្រមសីលធម៌",
        "theme_name": "Technology & Ethical Engineering",
        "qtype": "True / False / Not Given",
        "vocab": [
            ("autonomous", "adj", "B2/C1", "acting independently without direct human intervention", "ស្វ័យប្រវត្ត, ម្ចាស់ការ"),
            ("utilitarianism", "noun", "C2", "ethical doctrine prioritizing the greatest good for the greatest number", "ទ្រឹស្ដីប្រយោជន៍និយម"),
            ("liability", "noun", "B2/C1", "legal responsibility for consequences", "ការទទួលខុសត្រូវតាមផ្លូវច្បាប់"),
            ("dilemma", "noun", "B2", "a difficult situation where a tough choice has to be made", "ស្ថានភាពលំបាកសម្រេចចិត្ត"),
            ("algorithm", "noun", "B1/B2", "computational logic controlling vehicle decisions", "ក្បួនដោះស្រាយ"),
            ("unimpaired", "adj", "C1", "not damaged, weakened, or intoxicated", "ដែលមិនខូចខាត, មិនស្រវឹង")
        ],
        "b1": """Self-driving cars, also called autonomous vehicles, are being tested on public streets in several major countries. These advanced automobiles use cameras, laser sensors, and artificial intelligence computers to navigate traffic without a human driver touching the steering wheel. Engineers claim that autonomous cars will make roads much safer because computers never fall asleep, get distracted by text messages, or drive drunk.

However, self-driving vehicles introduce difficult ethical and moral dilemmas. In an unavoidable accident, how should an autonomous car's computer choose between hitting a group of pedestrians or crashing into a wall and harming the vehicle's passengers? Furthermore, if a self-driving car crashes into another vehicle, it is not clear who is legally responsible—the car owner, the software programmer, or the car manufacturing company. Governments must create clear laws before driverless cars are allowed everywhere.""",
        "b2": """The commercial development of autonomous vehicles promises to revolutionize municipal transportation and traffic safety. Human driver error accounts for over ninety percent of vehicular fatalities globally, primarily attributable to intoxication, fatigue, and mobile phone distraction. Proponents emphasize that autonomous navigation systems—utilizing LiDAR telemetry, computer vision, and predictive trajectory algorithms—can virtually eliminate avoidable traffic collisions, while simultaneously optimizing urban traffic flow and reducing carbon emissions.

Nevertheless, autonomous vehicles confront profound ethical and legal quandaries, most famously exemplified by programmatic variations of the classic 'Trolley Problem.' In catastrophic, non-zero-sum crash scenarios, automated algorithms must execute instantaneous life-and-death trade-offs. Should computational systems prioritize utilitarian outcomes by minimizing aggregate casualties, or should they prioritize the fiduciary protection of the vehicle's occupants? Compounding this ethical dilemma is the unresolved issue of tort liability: determining whether civil and criminal culpability rests with the vehicle operator, software developers, or original equipment manufacturers.""",
        "c1": """The imminent advent of autonomous vehicular fleets exposes the acute friction between algorithmic utilitarianism and deontological ethics. In delegating critical spatial navigation to machine learning models, society is forced to operationalize moral philosophy into algorithmic code. Crash optimization algorithms cannot remain ethically agnostic; an autonomous vehicle programmed to execute evasive maneuvers in unavoidable accident scenarios must inherently value certain lives over others, converting abstract ethical debates into deterministic execution protocols.

International surveys, such as the global Moral Machine experiment, illustrate that cultural consensus regarding algorithmic ethics is deeply fractured. While Western cohorts lean toward utilitarian frameworks that sacrifice vehicular occupants to save greater numbers of pedestrian lives, other cultures emphasize individual passenger protection and the respect for seniority. Furthermore, the commercial deployment of self-driving fleets creates acute product liability conundrums. If insurance algorithms and vehicle manufacturers absorb liability for autonomous accidents, the legal concept of personal driver agency dissolves, necessitating an overhaul of motor insurance and tort jurisprudence.""",
        "c2": """The imperative to encode moral decision-making into autonomous vehicular algorithms forces modern civilization to confront a profound hubris: the delusion that ethical tragedy can be resolved through mathematical optimization. For millennia, tragic motor accidents were understood as unpredictable, chaotic events governed by imperfect human reflexes and tragic misfortune. In pre-programming collision trajectories into machine code, we transform chaotic human tragedy into premeditated algorithmic execution.

To delegate life-and-death selection to a silicon processor is to commit an act of moral cowardice. An algorithm has no soul to grieve, no conscience to interrogate, and no capacity to bear existential guilt; it merely executes probabilistic arithmetic. When a vehicle's software calculates whether an elderly pedestrian or a young passenger possesses higher statistical social utility, it inaugurates a technocratic regime of algorithmic eugenics. The true challenge of autonomous engineering is not merely building a car that can steer without a driver, but recognizing the tragic boundaries of computational logic when confronted with the sanctity of human life.""",
        "questions": [
            ("1", "Human driving errors, including intoxication and distraction, account for over ninety percent of global vehicular deaths."),
            ("2", "The classic 'Trolley Problem' in autonomous vehicle ethics explores moral choices during unavoidable collision scenarios."),
            ("3", "International studies reveal that all global cultures share an identical, unanimous ethical consensus on crash priorities."),
            ("4", "The widespread adoption of autonomous cars creates legal uncertainties regarding manufacturer and programmer liability.")
        ],
        "answers": [
            ("1", "TRUE", "B2 explicitly confirms human driver error accounts for over ninety percent of vehicular fatalities worldwide.", "ពិត (TRUE) — កំហុសរបស់អ្នកបើកបរមនុស្ស ដូចជាការស្រវឹង និងការបាត់បង់ការផ្ដោតអារម្មណ៍ បង្កឱ្យមានគ្រោះថ្នាក់ចរាចរណ៍ជាង ៩០% នៅទូទាំងពិភពលោក។"),
            ("2", "TRUE", "B2 and C1 cite the Trolley Problem as a framework for analyzing life-and-death algorithmic trade-offs during collisions.", "ពិត (TRUE) — បញ្ហាក្រមសីលធម៌ 'Trolley Problem' ត្រូវបានយកមកវិភាគជម្រើសរវាងការបុកអ្នកថ្មើរជើង ឬអ្នកជិះក្នុងឡានពេលមានគ្រោះថ្នាក់។"),
            ("3", "FALSE", "C1 explicitly states the Moral Machine experiment demonstrates cultural consensus on algorithmic ethics is deeply fractured.", "មិនពិត (FALSE) — ការស្រាវជ្រាវអន្តរជាតិបង្ហាញថាវប្បធម៌នីមួយៗមានទស្សនៈខុសៗគ្នាលើការសម្រេចចិត្តខាងក្រមសីលធម៌របស់រថយន្ត។"),
            ("4", "TRUE", "B1, B2, and C1 affirm unresolved questions of tort liability regarding whether software developers or manufacturers are responsible.", "ពិត (TRUE) — យានយន្តស្វ័យប្រវត្តបង្កជាភាពមិនច្បាស់លាស់ខាងផ្លូវច្បាប់ថា តើក្រុមហ៊ុនផលិត ឬអ្នកសរសេរកម្មវិធីត្រូវទទួលខុសត្រូវពេលមានគ្រោះថ្នាក់។")
        ]
    },
    {
        "num": 20,
        "title": "Space Exploration: Commercialization vs. Scientific Discovery",
        "title_kh": "ការរុករកអវកាស៖ ពាណិជ្ជូបនីយកម្មធៀបនឹងការស្រាវជ្រាវវិទ្យាសាស្ត្រ",
        "theme_name": "Technology & Space Exploration",
        "qtype": "True / False / Not Given",
        "vocab": [
            ("commercialization", "noun", "B2/C1", "managing something primarily for financial profit", "ពាណិជ្ជូបនីយកម្ម"),
            ("extraterrestrial", "adj", "B2/C1", "originating or existing outside the earth", "ក្រៅភពផែនដី"),
            ("astrophysics", "noun", "C1", "branch of astronomy dealing with physics of the universe", "រូបវិទ្យាតារាសាស្ត្រ"),
            ("privatization", "noun", "B2", "transfer of an industry from public to private ownership", "ឯកជនភាវូបនីយកម្ម"),
            ("orbital", "adj", "B2", "relating to an orbit around a planet or star", "នៃគន្លងតារាវិថី"),
            ("hegemony", "noun", "C2", "leadership or dominance by one country or group", "អនុត្តរភាព, ឥទ្ធិពលត្រួតត្រា")
        ],
        "b1": """During the twentieth century, space exploration was conducted exclusively by wealthy national governments, such as the United States and the Soviet Union. Government agencies like NASA built giant rockets to send astronauts to the Moon and launch satellites to study weather and astronomy. These historic missions were paid for entirely by taxpayers to advance scientific knowledge and national pride.

Today, private aerospace corporations founded by billionaire entrepreneurs have fundamentally changed the space industry. Companies like SpaceX build reusable rockets that drastically lower the cost of launching satellites into orbit. While private investment accelerates space technology, some astronomers worry that commercial satellite constellations will ruin night sky observations. Furthermore, commercial space tourism remains an expensive luxury that only the ultra-wealthy can enjoy.""",
        "b2": """The structural privatization and commercialization of space exploration marks a radical departure from the state-dominated geopolitical space race of the twentieth century. Private aerospace enterprises have achieved historic efficiencies through rapid prototyping and reusable booster stages, reducing launch costs per kilogram into low Earth orbit by nearly ninety percent. This dramatic cost reduction facilitates unprecedented satellite deployment for global broadband connectivity and earth observation telemetry.

Conversely, the unchecked commercial exploitation of the orbital commons generates severe scientific and regulatory challenges. Astronomers increasingly report that massive mega-constellations of low-orbit telecommunication satellites produce optical interference that degrades ground-based astrophysical observations and telescope imaging. Furthermore, the accumulation of space debris in low Earth orbit elevates the threat of the Kessler syndrome—a catastrophic cascade of orbital collisions that could render orbital transit hazardous for future scientific missions.""",
        "c1": """The transition from public astropolitical exploration to private space commercialization reflects the imperial expansion of capital into extraterrestrial space. Historically, outer space was codified under the 1967 Outer Space Treaty as a global commons—the 'province of all mankind'—insulated from sovereign appropriation and dedicated to collaborative scientific inquiry. Today, venture capital and commercial corporations are actively dismantling this egalitarian paradigm, aggressively pursuing private asteroid mining claims, lunar resource extraction, and orbital real estate.

This neoliberal enclosure of the cosmos threatens the fundamental ethos of scientific astronomy. Ground-based astronomical infrastructure is compromised by light pollution generated by thousands of commercial satellites, obstructing deep-space spectroscopic analysis and planetary defense monitoring. Furthermore, as private corporations outpace sovereign states in orbital launch capability, global space governance fractures, allowing billionaire oligarchs to unilaterally dictate the terms of human interplanetary exploration without democratic oversight or international consensus.""",
        "c2": """The privatization of outer space represents the final, tragic frontier of commodification: the reduction of the sublime infinite into speculative corporate capital. The cosmos, which for millennia served as the transcendent mirror of human wonder and philosophical humility, is rapidly being transformed into an orbital billboard and industrial strip mine for private billionaires. Under the cynical guise of promoting human multi-planetary survival, private aerospace conglomerates are merely extending terrestrial inequality and environmental exploitation beyond the atmosphere.

The true peril of this extraterrestrial gold rush is the destruction of the cosmic commons. By crowding low Earth orbit with tens of thousands of commercial satellites, capital threatens to blind human civilization to the wonders of deep space, severing the sacred optical cord that connects humanity to the stars. To allow private corporate interests to colonize the celestial firmament without international democratic stewardship is an act of species-wide vandalism. Space must remain what it has always been: a shared realm of scientific wonder, philosophical transcendence, and collective human destiny.""",
        "questions": [
            ("1", "Twentieth-century space exploration was financed almost entirely through private venture capital corporations."),
            ("2", "Reusable rocket boosters have reduced the cost of launching payloads into low Earth orbit by nearly ninety percent."),
            ("3", "Astronomers report that large satellite constellations interfere with ground-based optical and deep-space telescope observations."),
            ("4", "The Kessler syndrome describes a cascade of collisions caused by accumulating orbital space debris.")
        ],
        "answers": [
            ("1", "FALSE", "B1 and B2 explain that twentieth-century space programs were funded exclusively by national governments and taxpayers.", "មិនពិត (FALSE) — ការរុករកអវកាសក្នុងសតវត្សរ៍ទី២០ ត្រូវបានផ្តល់ថវិកាដោយរដ្ឋាភិបាល និងប្រជាពលរដ្ឋបង់ពន្ធ មិនមែនក្រុមហ៊ុនឯកជនឡើយ។"),
            ("2", "TRUE", "B2 states reusable boosters have reduced launch costs per kilogram into low Earth orbit by nearly ninety percent.", "ពិត (TRUE) — បច្ចេកវិទ្យារ៉ុក្កែតប្រើឡើងវិញបានកាត់បន្ថយថ្លៃដើមនៃការបាញ់បង្ហោះចូលគន្លងផែនដីរហូតដល់ប្រមាណ ៩០%។"),
            ("3", "TRUE", "B2, C1, and C2 highlight that mega-constellations produce light pollution and optical interference for astronomical observatories.", "ពិត (TRUE) — ក្រុមតារាវិទូព្រមានថាផ្កាយរណបពាណិជ្ជកម្មច្រើនសន្ធឹកសន្ធាប់រំខានដល់ការសង្កេតផ្ទៃមេឃ និងតេឡេស្កុប។"),
            ("4", "TRUE", "B2 explicitly defines the Kessler syndrome as a catastrophic cascade of orbital collisions caused by accumulated space debris.", "ពិត (TRUE) — បាតុភូត Kessler syndrome សំដៅលើការប៉ះទង្គិចបន្តកន្ទុយគ្នានៃកម្ទេចកម្ទីក្នុងគន្លងតារាវិថី។")
        ]
    }
]

if __name__ == "__main__":
    write_theme_file(
        filename="ielts_02_technology.md",
        theme_title="Technology, Artificial Intelligence & Digital Life (Topics 11–20)",
        theme_kh="បច្ចេកវិទ្យា បញ្ញាសិប្បនិម្មិត និងជីវិតឌីជីថល (ប្រធានបទ ១១ ដល់ ២០)",
        theme_desc="This volume presents 10 comprehensive academic reading topics on Artificial Intelligence, Digital Privacy, Robotics, Quantum Computing, and Clean Energy Technology. Each topic contains an authentic IELTS/CEFR reading passage adapted across four CEFR levels (B1, B2, C1, C2), key academic vocabulary with Khmer translations, 4 mock exam questions, and full explanatory walkthroughs.",
        topics=TOPICS
    )
