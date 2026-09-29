#!/usr/bin/env python3
"""
Generate Volume 4: Health, Medicine & Human Well-being (Topics 31–40)
reading_skills/examples/ielts_04_health.md
"""

from reading_generator_engine import write_theme_file

TOPICS = [
    {
        "num": 31,
        "title": "The Global Obesity Epidemic and Ultra-Processed Foods",
        "title_kh": "ការរាតត្បាតនៃភាពធាត់ជ្រុលជាសកល និងអាហារកែច្នៃកម្រិតខ្ពស់",
        "theme_name": "Health & Nutritional Science",
        "qtype": "True / False / Not Given",
        "vocab": [
            ("epidemic", "noun", "B2", "a widespread occurrence of an infectious disease or health crisis", "ការរាតត្បាត"),
            ("ultra-processed", "adj", "B2/C1", "foods industrially formulated with additives and minimal whole food", "កែច្នៃកម្រិតខ្ពស់"),
            ("satiety", "noun", "C2", "the feeling or state of being sated or full", "អារម្មណ៍ឆ្អែត"),
            ("hyper-palatable", "adj", "C1/C2", "foods deliberately engineered to induce overconsumption", "ដែលឆ្ងាញ់ខ្លាំងទប់ចិត្តមិនបាន"),
            ("cardiovascular", "adj", "B2/C1", "relating to the heart and blood vessels", "នៃបេះដូង និងសរសៃឈាម"),
            ("metabolic", "adj", "B2/C1", "relating to the body's chemical processes of converting food to energy", "នៃការរំលាយអាហារក្នុងរាងកាយ")
        ],
        "b1": """In almost every country in the world, the percentage of adults and children suffering from obesity has doubled over the past three decades. Being severely overweight increases the risk of developing serious long-term illnesses, such as type 2 diabetes, high blood pressure, and heart disease. While doctors originally blamed obesity on lack of exercise and individual laziness, modern nutritionists point to a much bigger culprit: ultra-processed foods.

Supermarket shelves are now packed with factory-made snacks, sugary sodas, packaged instant noodles, and frozen ready-meals. These foods are packed with artificial flavorings, high amounts of refined sugar, unhealthy saturated fats, and synthetic chemicals. Because they are soft, easy to chew, and digested very quickly, they trick the human brain into feeling hungry again soon after eating. Public health experts urge governments to tax junk food and ban misleading advertisements aimed at young children.""",
        "b2": """The escalation of global obesity rates constitutes one of the most critical public health crises of the twenty-first century. Epidemiological data demonstrate that the proliferation of obesity correlates directly with the industrial penetration of ultra-processed foods (UPFs) into national diets. Formulated through industrial deconstruction of whole foods into chemically isolated fats, starches, and sugars, UPFs are engineered to achieve an optimal 'bliss point' that overrides natural neurochemical satiety mechanisms.

The physiological consequences of chronic UPF consumption extend beyond excess caloric intake. These foods induce systemic low-grade inflammation, alter gut microbiome compositions, and precipitate insulin resistance, driving the global surge in non-communicable diseases such as non-alcoholic fatty liver disease and cardiovascular pathologies. Consequently, public health advocates argue that resolving the obesity epidemic requires structural regulatory interventions—including front-of-package nutritional warning labels, mandatory marketing restrictions, and agricultural subsidy reforms—rather than individual moral admonition.""",
        "c1": """The contemporary obesity pandemic represents an acute biocultural mismatch between human evolutionary metabolic physiology and an industrial food landscape engineered for profit. For millennia of hominid evolution, human energy regulation was calibrated to survive nutritional scarcity, prioritizing high-energy caloric intake and developing complex neuroendocrine satiety feedback loops mediated by leptin and ghrelin. Industrial food conglomerates have weaponized this evolutionary vulnerability by engineering hyper-palatable formulations characterized by unprecedented combinations of refined carbohydrates and industrial seed oils.

Controlled metabolic feeding trials demonstrate that ultra-processed diets promote passive overconsumption through elevated caloric density, rapid chewing speed, and delayed postprandial satiety signals. Furthermore, synthetic emulsifiers, artificial sweeteners, and advanced glycation end-products degrade the intestinal epithelial barrier, enabling endotoxin translocation that fuels chronic systemic metabolic endotoxemia. By framing obesity as a failure of individual willpower, corporate entities deflect regulatory scrutiny from an obesogenic food architecture that systematically undermines human biological self-regulation.""",
        "c2": """The worldwide proliferation of obesity is not a crisis of personal virtue; it is the physical manifestation of industrial dietary colonization. In transforming food from an organic source of communal nourishment into an ultra-processed commodity optimized for corporate shelf-life and shareholder returns, global food monopolies have engineered a metabolic catastrophe. The human body, perfected over geological epochs to thrive on the bounty of living ecosystems, has been subordinated to factory-engineered matrices of synthetic flavorings, industrial starches, and hyper-palatable neuro-toxins.

The moral obscenity of this dietary regime lies in its predatory exploitation of vulnerable populations. Cheap ultra-processed calories are relentlessly targeted at low-income communities, creating food deserts where nutrient-dense whole foods are economically unattainable, while chronic metabolic illness is mathematically guaranteed. To reduce this systemic violence to an admonition that citizens simply 'exercise more and eat less' is an act of grotesque gaslighting. Humanity must reclaim dietary sovereignty: deconstructing corporate food architectures, subsidizing agroecological farming, and restoring the sacred biological relationship between human health and the living soil.""",
        "questions": [
            ("1", "Ultra-processed foods are engineered with combinations of sugar and fat that can bypass natural brain satiety signals."),
            ("2", "Global obesity rates have declined by fifty percent over the past three decades due to mandatory school sports programs."),
            ("3", "Synthetic emulsifiers and food additives have been shown to degrade the intestinal epithelial barrier in metabolic trials."),
            ("4", "Public health experts argue that solving the obesity epidemic requires structural regulations on junk food advertising.")
        ],
        "answers": [
            ("1", "TRUE", "B2 and C1 explain that foods engineered to achieve a 'bliss point' override natural neurochemical satiety feedback loops.", "ពិត (TRUE) — អាហារកែច្នៃកម្រិតខ្ពស់ត្រូវបានផលិតឡើងដើម្បីបំភាន់ខួរក្បាល និងរំលងសញ្ញាប្រាប់ថាឆ្អែតពីធម្មជាតិ។"),
            ("2", "FALSE", "B1 states obesity rates have doubled over the past three decades, directly contradicting a decline.", "មិនពិត (FALSE) — អត្រាធាត់ជ្រុលបានកើនឡើងទ្វេដងក្នុងរយៈពេលបីទសវត្សរ៍ចុងក្រោយនេះ មិនមែនថយចុះ ៥០% នោះឡើយ។"),
            ("3", "TRUE", "C1 explicitly states synthetic emulsifiers and additives degrade the intestinal epithelial barrier, causing inflammation.", "ពិត (TRUE) — សារធាតុបន្ថែម និងសារធាតុផ្សំក្នុងអាហារកែច្នៃបំផ្លាញស្រទាប់កោសិកាការពារក្នុងពោះវៀន។"),
            ("4", "TRUE", "B1 and B2 state experts urge governments to tax junk foods and implement advertising restrictions.", "ពិត (TRUE) — អ្នកជំនាញសុខភាពសាធារណៈទាមទារឱ្យមានវិធានការច្បាប់តឹងរ៉ឹងលើការផ្សាយពាណិជ្ជកម្មអាហារមិនល្អដល់សុខភាព។")
        ]
    },
    {
        "num": 32,
        "title": "Antimicrobial Resistance in Modern Medicine",
        "title_kh": "ភាពស៊ាំនឹងថ្នាំអង់ទីប៊ីយោទិចក្នុងវេជ្ជសាស្ត្រទំនើប",
        "theme_name": "Health & Pharmacology",
        "qtype": "True / False / Not Given",
        "vocab": [
            ("antimicrobial", "adj", "B2/C1", "active against microbes, especially bacteria and viruses", "ដែលប្រឆាំងនឹងមេរោគ"),
            ("resistance", "noun", "B2", "the ability of microorganisms to withstand antibiotics", "ភាពស៊ាំ"),
            ("pathogen", "noun", "C1", "a bacterium, virus, or other microorganism causing disease", "ភ្នាក់ងារបង្ករោគ"),
            ("prophylactic", "adj", "C2", "intended to prevent disease or infection", "ដែលការពារទុកជាមុន"),
            ("horizontal gene transfer", "noun", "C2", "the movement of genetic material between unicellular organisms", "ការផ្ទេរហ្សែនរវាងបាក់តេរី"),
            ("post-antibiotic", "adj", "C1", "an era where antibiotics are no longer effective", "យុគសម័យក្រោយអង់ទីប៊ីយោទិច")
        ],
        "b1": """When Scottish scientist Alexander Fleming discovered penicillin in 1928, it revolutionized modern healthcare. Doctors were suddenly able to cure deadly bacterial infections like pneumonia and tuberculosis that had killed millions of people. For nearly a century, antibiotics made complex surgeries, organ transplants, and cancer therapies safe and routine.

However, the miracle of antibiotics is now under severe threat from antimicrobial resistance. Because doctors overprescribe antibiotics for simple colds and farmers feed massive amounts of antibiotics to healthy farm animals to make them grow faster, bacteria have mutated and learned to survive medicine. Today, dangerous 'superbugs' exist in hospitals that cannot be killed by any existing antibiotic. Health organizations warn that if new drugs are not developed quickly, minor cuts could once again become deadly.""",
        "b2": """Antimicrobial resistance (AMR) constitutes one of the most urgent existential threats confronting modern clinical medicine. The pervasive misuse and overprescription of antimicrobial agents in human healthcare, coupled with the routine prophylactic administration of antibiotics in industrial livestock production, has exerted intense selective pressure on bacterial populations. Microorganisms rapidly acquire and disseminate resistance genes through horizontal gene transfer mechanisms such as plasmid conjugation and transduction.

The emergence of multidrug-resistant pathogens—frequently termed 'superbugs,' including methicillin-resistant Staphylococcus aureus (MRSA) and carbapenem-resistant Enterobacteriaceae—jeopardizes foundational medical procedures. Routine clinical interventions, such as elective orthopedic surgeries, chemotherapy-induced immunosuppression, and neonatal intensive care, depend entirely on effective antibiotic prophylaxis. Without international coordination to implement antimicrobial stewardship programs and incentivize novel pharmaceutical pipelines, projections indicate AMR could claim ten million lives annually by 2050.""",
        "c1": """The escalating crisis of antimicrobial resistance marks the impending arrival of a post-antibiotic era, threatening to dismantle the cornerstone of twentieth-century clinical medicine. Bacterial evolutionary adaptability, honed over billions of years of competitive coexistence in soil biomes, enables rapid phenotypic adaptation against synthetic pharmacological agents. Pathogens deploy multifaceted biochemical resistance mechanisms, including enzymatic drug inactivation, membrane porin alteration that impedes drug entry, and active multi-drug efflux pumps that expel intracellular antibiotics.

Compounding this microbiological evolution is a systemic market failure within the pharmaceutical industry. The commercial development of novel antimicrobial classes has virtually ceased over recent decades; because antibiotics are prescribed for short curative durations, pharmaceutical conglomerates prioritize lucrative chronic maintenance drugs for oncology and cardiovascular disease. Addressing this therapeutic vacuum necessitates transformative global public-private funding models—such as market entry rewards and patent buyout incentives—alongside rigorous global bans on agricultural antibiotic growth promoters.""",
        "c2": """The crisis of antimicrobial resistance confronts industrial civilization with the biological limits of chemical warfare against the natural world. When medicine discovered penicillin, it adopted a militaristic paradigm: disease was conceptualized as an external enemy to be carpet-bombed and annihilated through industrial chemistry. In our hubris, we forgot that bacteria are the ancient, ubiquitous architects of the biosphere, possessing evolutionary memory and genetic flexibility that dwarfs human technological vanity.

By inundating the planet with hundreds of thousands of tons of antibiotics—sprayed on orchards, fed to feedlot cattle, and consumed for viral coughs—humanity accelerated bacterial evolution at a planetary scale. The superbug is not an alien invader; it is our own ecological reflection, an evolutionary organism forged in the crucible of pharmaceutical overconsumption. To avert the nightmare of a post-antibiotic dark age, medicine must abandon its conquest mentality and cultivate evolutionary stewardship: treating antibiotics as rare, sacred collective assets while restoring ecological balance to human and environmental biomes.""",
        "questions": [
            ("1", "Penicillin was discovered by Alexander Fleming in 1928, dramatically reducing deaths from bacterial infections."),
            ("2", "Feeding antibiotics prophylactically to livestock animals has zero impact on the development of antibiotic-resistant bacteria."),
            ("3", "Horizontal gene transfer enables bacteria to share resistance traits through plasmids and genetic material exchange."),
            ("4", "Pharmaceutical companies aggressively prioritize antibiotic discovery over chronic cardiovascular medications due to higher profits.")
        ],
        "answers": [
            ("1", "TRUE", "B1 states Alexander Fleming discovered penicillin in 1928, revolutionizing modern healthcare.", "ពិត (TRUE) — លោក Alexander Fleming បានរកឃើញថ្នាំប៉េនីស៊ីលីនក្នុងឆ្នាំ ១៩២៨ ដែលបានជួយសង្គ្រោះជីវិតមនុស្សរាប់លាននាក់ពីការបង្ករោគ។"),
            ("2", "FALSE", "B1 and B2 state feeding antibiotics to farm animals exerts selective pressure and accelerates superbug emergence.", "មិនពិត (FALSE) — ការប្រើប្រាស់ថ្នាំអង់ទីប៊ីយោទិចលើសត្វចិញ្ចឹមជាកត្តាចម្បងមួយដែលជំរុញឱ្យបាក់តេរីកាន់តែស៊ាំនឹងថ្នាំ។"),
            ("3", "TRUE", "B2 explicitly explains that bacteria disseminate resistance genes through horizontal gene transfer.", "ពិត (TRUE) — បាក់តេរីអាចបញ្ជូនហ្សែនស៊ាំថ្នាំទៅគ្នាទៅវិញទៅមកតាមរយៈដំណើរការផ្ទេរហ្សែនផ្ដេក (Horizontal gene transfer)។"),
            ("4", "FALSE", "C1 states the opposite: commercial drug companies abandon antibiotics because chronic maintenance drugs are much more lucrative.", "មិនពិត (FALSE) — ក្រុមហ៊ុនឱសថបោះបង់ការស្រាវជ្រាវថ្នាំអង់ទីប៊ីយោទិច ព្រោះថ្នាំព្យាបាលជំងឺរ៉ាំរ៉ៃ (ដូចជាបេះដូង និងមហារីក) រកប្រាក់ចំណេញបានច្រើនជាង។")
        ]
    }
]

if __name__ == "__main__":
    extra_health_topics = [
        {
            "num": 33,
            "title": "Mental Health Paradigms and Workplace Burnout",
            "title_kh": "ទស្សនវិស័យសុខភាពផ្លូវចិត្ត និងការស្រុតចុះកម្លាំងកាយចិត្តនៅកន្លែងធ្វើការ (Burnout)",
            "theme_name": "Health & Occupational Psychology",
            "qtype": "True / False / Not Given",
            "vocab": [
                ("burnout", "noun", "B2", "state of emotional, physical, and mental exhaustion caused by excessive stress", "ការអស់កម្លាំងចិត្ត និងកាយ, ការបាក់កម្លាំង"),
                ("occupational", "adj", "B2/C1", "relating to a job or profession", "នៃមុខរបរ, នៃកន្លែងធ្វើការ"),
                ("depersonalization", "noun", "C2", "state of feeling detached from one's body or mental processes", "ការបាត់បង់អារម្មណ៍ជាមនុស្ស"),
                ("cognitive", "adj", "B2", "relating to mental processes of perception and judgment", "ខាងការយល់ដឹង"),
                ("stigmatization", "noun", "C1", "the action of describing or regarding something as worthy of disgrace", "ការមាក់ងាយ, ការរើសអើង"),
                ("absenteeism", "noun", "B2/C1", "the practice of staying away from work without good reason", "ការអវត្តមានពីការងារ")
            ],
            "b1": """In the modern fast-paced corporate world, millions of employees suffer from chronic physical and emotional exhaustion known as workplace burnout. Constant overtime, demanding deadlines, and the expectation to answer work emails during evenings and weekends leave workers with little time to rest. People experiencing burnout feel continuously drained, lose interest in their daily duties, and suffer from frequent headaches, insomnia, and anxiety.

Workplace burnout is not just an individual problem; it causes major financial losses for companies worldwide. Burnt-out employees make more mistakes, take frequent sick days, and often resign unexpectedly. To protect mental health, progressive companies are introducing flexible work hours, enforcing rules against answering emails after six in the evening, and providing free mental health counseling to their staff.""",
            "b2": """Workplace burnout has transitioned from a subjective cultural catchphrase into an officially recognized occupational phenomenon classified by the World Health Organization (WHO). Characterized by three dimensional axes—feelings of energy depletion, increased mental distancing or cynicism toward one's occupation (depersonalization), and reduced professional efficacy—burnout is fundamentally rooted in organizational dysfunction rather than individual emotional weakness.

The physiological manifestations of prolonged occupational stress are profound. Sustained elevation of cortisol and inflammatory biomarkers impairs executive cognitive functioning, prefrontal cortex neuroplasticity, and memory consolidation. Economically, burnout precipitates massive corporate losses through presenteeism—working while cognitively impaired—and elevated turnover rates. Overcoming this workplace crisis requires systemic institutional restructuring, including balanced workload distribution, psychological safety, and realistic performance metrics.""",
            "c1": """The proliferation of workplace burnout in contemporary knowledge economies reflects the intensification and boundary erosion of modern corporate labor. In high-velocity professional ecosystems, digital connectivity has dissolved the temporal and spatial demarcation between labor and domestic life, subjecting employees to continuous cognitive availability. Under the rubric of 'agile productivity' and corporate commitment, organizations subtly externalize systemic operational pressures onto the individual psychic apparatus of workers.

Crucially, corporate wellness initiatives—such as mindfulness workshops and digital meditation applications—frequently function as ideological pacifiers that individualize and pathologize structural organizational failure. By framing burnout as a personal resilience deficit to be remediated through private self-care, management evades accountability for toxic corporate cultures, predatory billable-hour quotas, and chronic understaffing. Authentic occupational mental health paradigms demand structural workplace democracy, collective bargaining protections, and legally enforceable boundaries safeguarding human rest.""",
            "c2": """Workplace burnout is the inevitable psychic harvest of an economic system that views human life as an exhaustible fuel source for corporate capital. In reducing the multidimensional human soul to an instrument of continuous productivity and quantifiable output, late-stage corporate culture systematically cannibalizes the biological and emotional foundations of human existence. The burnt-out professional—depleted of vitality, cynicism-hardened, and spiritually hollowed—is the tragic icon of a civilization that has sacrificed human flourishing upon the altar of corporate margin.

To offer corporate yoga classes and wellness seminars to workers crushed beneath unreasonable workloads is an act of grotesque moral cowardice. It demands that the victim meditate away the pain of their own exploitation while leaving the predatory machinery entirely intact. We must recover the radical human dignity of limits: the profound recognition that human beings are not machines engineered for 24-hour algorithmic utilization. To reclaim our time, our rest, and our mental tranquility is an act of spiritual defiance—a declaration that human worth can never be measured by a corporate performance review.""",
            "questions": [
                ("1", "The World Health Organization officially recognizes workplace burnout as an occupational phenomenon."),
                ("2", "Prolonged occupational stress has been demonstrated to maintain normal cortisol levels with zero effect on memory."),
                ("3", "Presenteeism refers to the practice of employees being physically present at work while cognitively impaired."),
                ("4", "Critics argue corporate wellness apps often individualize structural workplace failures as personal resilience deficits.")
            ],
            "answers": [
                ("1", "TRUE", "B2 confirms workplace burnout is officially recognized by the WHO as an occupational phenomenon.", "ពិត (TRUE) — អង្គការសុខភាពពិភពលោក (WHO) បានទទួលស្គាល់ការបាក់កម្លាំងពីការងារ (Burnout) ជាបាតុភូតសុខភាពការងារជាផ្លូវការ។"),
                ("2", "FALSE", "B2 states sustained stress causes elevated cortisol and impairs cognitive functioning and memory consolidation.", "មិនពិត (FALSE) — សម្ពាធការងាររ៉ាំរ៉ៃធ្វើឱ្យអ័រម៉ូនស្ត្រេស (Cortisol) កើនឡើងខ្ពស់ និងប៉ះពាល់ដល់ការចងចាំ មិនមែនរក្សាកម្រិតធម្មតានោះទេ។"),
                ("3", "TRUE", "B2 defines presenteeism as working while cognitively impaired, leading to massive corporate productivity losses.", "ពិត (TRUE) — Presenteeism សំដៅលើស្ថានភាពដែលបុគ្គលិកទៅធ្វើការទាំងកាយវិការ ប៉ុន្តែខួរក្បាល និងស្មារតីអស់កម្លាំងខ្លាំងធ្វើការមិនកើត។"),
                ("4", "TRUE", "C1 states wellness apps frame burnout as a personal resilience deficit, deflecting blame from corporate understaffing.", "ពិត (TRUE) — អ្នករិះគន់លើកឡើងថាកម្មវិធីសុខភាពរបស់ក្រុមហ៊ុនតែងតែទម្លាក់កំហុសលើបុគ្គលិកថាខ្វះការអត់ធ្មត់ ជំនួសឱ្យការកែទម្រង់ប្រព័ន្ធការងារ។")
            ]
        },
        {
            "num": 34,
            "title": "Sleep Deprivation and Neurodegenerative Diseases",
            "title_kh": "ការគេងមិនគ្រប់គ្រាន់ និងជំងឺសរសៃប្រសាទខួរក្បាលទ្រុឌទ្រោម",
            "theme_name": "Health & Neuroscience",
            "qtype": "True / False / Not Given",
            "vocab": [
                ("deprivation", "noun", "B2", "the damaging lack of material or biological necessities", "ការខ្វះខាត, ការដកហូត"),
                ("neurodegenerative", "adj", "C1", "resulting in the progressive deterioration of nervous tissue", "នៃការខូចខាតសរសៃប្រសាទ"),
                ("glymphatic", "adj", "C2", "macroscopic waste clearance system utilizing cerebrospinal fluid", "នៃប្រព័ន្ធសម្អាតកាកសំណល់ខួរក្បាល"),
                ("tau", "noun", "C2", "a protein that stabilizes microtubules, implicated in Alzheimer's", "ប្រូតេអ៊ីន Tau"),
                ("plaque", "noun", "B2/C1", "abnormal accumulation of proteins in tissues", "កំទេចកំទីប្រូតេអ៊ីនកកស្ទះ"),
                ("cognitive", "adj", "B2", "relating to mental processes of perception and reasoning", "ខាងការយល់ដឹង")
            ],
            "b1": """In our modern world of glowing smartphone screens and late-night television, many adults sleep fewer than six hours per night. Many busy professionals proudly boast that they do not need sleep, believing that sleeping less allows them to work harder and earn more money. However, medical scientists have discovered that chronic lack of sleep causes severe, permanent damage to the human brain.

While you are sleeping peacefully, your brain is actually performing essential cleaning work. Specialized fluids wash through brain tissues, removing toxic chemical waste products that accumulate during waking hours. When people cut their sleep short night after night, these toxic proteins build up inside brain cells. Over several decades, this toxic accumulation dramatically increases the risk of developing memory loss and Alzheimer's disease in old age.""",
            "b2": """Recent neuroscientific breakthroughs have unveiled a critical mechanistic link between chronic sleep deprivation and the etiology of neurodegenerative disorders, particularly Alzheimer's disease. Historically, sleep was viewed as a passive state of physiological quiescence. Contemporary neuroimaging, however, reveals that slow-wave deep sleep activates the glymphatic system—a specialized waste clearance network that flushes cerebrospinal fluid through interstitial brain channels.

During deep non-REM sleep, the glymphatic flow accelerates significantly, purging toxic metabolic waste products including amyloid-beta plaques and hyperphosphorylated tau proteins. Chronic sleep restriction impedes this vital neurochemical filtration process. As toxic peptides aggregate within neocortical and hippocampal networks, they initiate neuroinflammatory cascades and synaptic degradation, accelerating the clinical onset of cognitive decline. Prioritizing seven to eight hours of restorative sleep is therefore a foundational prophylactic measure against neurodegeneration.""",
            "c1": """The discovery of the glymphatic clearance pathway has fundamentally reframed sleep from an evolutionary vulnerability into a vital neuro-protective biological imperative. Astrocytic water channels mediated by aquaporin-4 facilitate the convective influx of cerebrospinal fluid through the brain parenchyma during slow-wave sleep, contracting interstitial space and amplifying solute clearance rates by over sixty percent compared to waking baselines.

The relationship between sleep architecture disruption and neurodegenerative pathophysiology is bidirectionally pathogenic. Sleep fragmentation impairs the diurnal clearance of neurotoxic oligomers; concurrently, the progressive cortical deposition of amyloid-beta and neurofibrillary tau tangles damages the thalamocortical circuitry necessary to generate restorative slow-wave oscillations. This self-reinforcing pathological loop accelerates neurovascular uncoupling, chronic neuroinflammation, and progressive dementia. Consequently, clinical interventions must recognize sleep fragmentation not merely as a symptom of neurodegeneration, but as an active, modifiable driver of neuro-pathology.""",
            "c2": """The contemporary epidemic of chronic sleep deprivation is the physiological price of an industrialized culture that wages war against human biology. In exalting constant sleepless hustle as a badge of moral honor, modern society has turned its back on the ancient biological sanctuary of slumber. We treat the sleeping brain as an unproductive machine that can be cheated with caffeine and screen light, blind to the biological truth that during sleep, the brain performs the sacred, quiet alchemy of cellular repair and memory consolidation.

The scientific revelation of the glymphatic wash reveals the terrifying consequences of this hubris. To starve the brain of deep sleep is to turn off the janitorial filtration of the mind, allowing metabolic toxins to calcify into the devastating plaques and tangles of Alzheimer's disease. The professional who boasts of surviving on four hours of sleep is not a titan of industrial efficiency; they are unwittingly presiding over the slow neuro-chemical decay of their own intellect. Sleep is not a negotiable luxury; it is the non-negotiable biological foundation of human consciousness.""",
            "questions": [
                ("1", "The glymphatic system flushes cerebrospinal fluid to clear toxic metabolic waste during deep slow-wave sleep."),
                ("2", "Sleeping fewer than five hours nightly has been proven to permanently immunize the brain against Alzheimer's disease."),
                ("3", "Amyloid-beta and tau proteins are waste products cleared from the brain during restorative sleep."),
                ("4", "The relationship between sleep disruption and neurodegeneration is described as bidirectionally pathogenic.")
            ],
            "answers": [
                ("1", "TRUE", "B2 and C1 explicitly state the glymphatic system accelerates during deep sleep, flushing fluid to clear toxic waste.", "ពិត (TRUE) — ប្រព័ន្ធ Glymphatic បង្កើនល្បឿនសម្អាតកាកសំណល់គីមីពុលចេញពីខួរក្បាលអំឡុងពេលយើងគេងលក់ស្កប់ស្កល់។"),
                ("2", "FALSE", "B1, B2, and C1 highlight that chronic sleep loss dramatically increases the risk of Alzheimer's, not immunizes against it.", "មិនពិត (FALSE) — ការគេងមិនគ្រប់គ្រាន់បង្កើនហានិភ័យនៃជំងឺភ្លេចភ្លាំង (Alzheimer's) យ៉ាងខ្លាំង មិនមែនជួយការពារនោះឡើយ។"),
                ("3", "TRUE", "B2 and C1 identify amyloid-beta and tau proteins as toxic metabolic waste cleared during deep sleep.", "ពិត (TRUE) — ប្រូតេអ៊ីន Amyloid-beta និង Tau គឺជាកាកសំណល់ជាតិពុលដែលត្រូវសម្អាតចេញពីខួរក្បាលពេលគេង។"),
                ("4", "TRUE", "C1 states the relationship is bidirectionally pathogenic: sleep loss causes plaque accumulation, which in turn further disrupts sleep.", "ពិត (TRUE) — ទំនាក់ទំនងនេះមានលក្ខណៈបំផ្លាញទៅវិញទៅមក (ការគេងមិនលក់បង្កើតជាតិពុល ហើយជាតិពុលធ្វើឱ្យកាន់តែគេងមិនលក់)។")
            ]
        },
        {
            "num": 35,
            "title": "Personalized Genomics and Precision Medicine",
            "title_kh": "ពន្ធុវិទ្យាផ្ទាល់ខ្លួន និងវេជ្ជសាស្ត្រជាក់លាក់ (Precision Medicine)",
            "theme_name": "Health & Medical Genetics",
            "qtype": "True / False / Not Given",
            "vocab": [
                ("genomics", "noun", "B2/C1", "branch of molecular biology studying genomes", "ពន្ធុវិទ្យា"),
                ("precision medicine", "noun", "B2/C1", "medical care designed for a patient's individual genetics", "វេជ្ជសាស្ត្រជាក់លាក់"),
                ("oncology", "noun", "C1", "the study and treatment of cancer and tumors", "មហារីកវិទ្យា"),
                ("pharmacogenomics", "noun", "C2", "how genetic variations influence drug responses", "ឱសថពន្ធុវិទ្យា"),
                ("prophylactic", "adj", "C1/C2", "intended to prevent disease", "ដែលការពារជំងឺ"),
                ("disparity", "noun", "B2/C1", "a great difference; inequality", "វិសមភាព, គម្លាត")
            ],
            "b1": """For decades, doctors treated illnesses like cancer and high blood pressure using a standard 'one-size-fits-all' approach. Every patient diagnosed with the same disease was given the exact same pills or chemotherapy drugs. However, because every human body is genetically unique, a medication that cures one patient might cause severe allergic reactions or fail to work in another person.

Today, advanced DNA sequencing technologies make personalized genomics possible. By analyzing a patient's unique genetic code from a simple blood sample, doctors can select medications designed specifically for their biological profile. For cancer patients, precision medicine can target the specific genetic mutations inside a tumor without harming healthy cells. While personalized medicine saves lives, it remains extremely expensive and is not yet available to patients in poorer nations.""",
            "b2": """Precision medicine and personalized genomics represent an epochal transformation from reactive symptom management toward individualized predictive healthcare. By leveraging high-throughput next-generation DNA sequencing, clinicians can decipher a patient's complete genomic architecture, identifying single-nucleotide polymorphisms (SNPs) and pathogenic somatic mutations that dictate disease susceptibility and drug metabolism.

The clinical efficacy of precision oncology provides the most compelling paradigm. Rather than subjecting cancer patients to cytotoxic chemotherapy, oncologists deploy targeted molecular inhibitors that neutralize specific oncogenic driver mutations—such as EGFR inhibitors in non-small cell lung cancer or HER2-targeted monoclonal antibodies in breast oncology. Furthermore, pharmacogenomic profiling prevents adverse drug reactions by identifying metabolic enzyme variations, substantially optimizing drug efficacy and minimizing patient morbidity.""",
            "c1": """The integration of genomic sequencing, transcriptomics, and metabolomics into clinical practice marks the dawn of stratified systems medicine. Conventional medical taxonomy, which categorized diseases based on anatomical location and macroscopic pathology, is being dismantled in favor of molecular disease taxonomies. By mapping individual genetic variants, clinicians can execute predictive polygenic risk scoring, enabling targeted prophylactic interventions long before clinical phenotypes manifest.

However, the widespread realization of genomic medicine confronts formidable structural and bioethical hurdles. Genomic reference databases exhibit profound demographic bias; over eighty percent of sequenced cohorts are of European ancestry, generating substantial diagnostic disparities for populations of African, Asian, and Latin American descent. Furthermore, the handling of sensitive genetic data raises alarming privacy concerns regarding genetic discrimination in employment and health insurance markets, necessitating comprehensive legal protections such as the Genetic Information Nondiscrimination Act.""",
            "c2": """Personalized genomics stands as a crowning achievement of contemporary molecular biology: the deciphering of the unique biological scripture written into every human cell. In liberating medicine from the crude approximations of mass therapeutics, precision genomics promises to treat every patient with the reverence due to their genetic uniqueness. The dream of targeting disease at the molecular level without collateral harm to the living body is the fulfillment of medicine's most compassionate ideal.

Yet this scientific triumph is shadowed by a grave ethical peril: the emergence of genetic inequality. When breakthrough genomic therapies cost hundreds of thousands of dollars per patient, precision medicine risks becoming an exclusive luxury reserved for wealthy elites, while ordinary populations remain consigned to antiquated, generic treatments. A society that uses genetic sequencing to heal the wealthy while denying basic healthcare to the impoverished is a society constructing an biological aristocracy. The ultimate moral test of genomics is not merely whether it can cure a disease, but whether its life-saving power can be democratized for all humanity.""",
            "questions": [
                ("1", "Precision oncology utilizes targeted molecular inhibitors directed at specific genetic driver mutations."),
                ("2", "Over eighty percent of existing genomic sequencing databases are derived from cohorts of European ancestry."),
                ("3", "Next-generation genomic medicine has completely abolished all health insurance inequalities worldwide."),
                ("4", "Pharmacogenomic profiling analyzes individual genetic variations to predict adverse drug metabolic reactions.")
            ],
            "answers": [
                ("1", "TRUE", "B2 confirms precision oncology uses targeted inhibitors neutralizing specific oncogenic driver mutations.", "ពិត (TRUE) — ក្នុងការព្យាបាលជំងឺមហារីក វេជ្ជសាស្ត្រជាក់លាក់ប្រើប្រាស់ថ្នាំដែលវាយប្រហារចំគោលដៅលើការប្រែប្រួលហ្សែនបង្កជំងឺ។"),
                ("2", "TRUE", "C1 explicitly states that over eighty percent of sequenced cohorts in genomic databases are of European descent.", "ពិត (TRUE) — ជាង ៨០% នៃទិន្នន័យហ្សែនបច្ចុប្បន្នបានមកពីប្រជាជនដើមកំណើតអឺរ៉ុប ដែលបង្កជាគម្លាតវិនិច្ឆ័យសម្រាប់ជាតិសាសន៍ដទៃ។"),
                ("3", "FALSE", "C1 and C2 emphasize unresolved ethical and privacy issues regarding genetic discrimination in health insurance.", "មិនពិត (FALSE) — បញ្ហាវិសមភាពធានារ៉ាប់រង និងការរើសអើងហ្សែននៅតែជាបញ្ហាប្រឈមធ្ងន់ធ្ងរ មិនទាន់ត្រូវបានលុបបំបាត់ឡើយ។"),
                ("4", "TRUE", "B2 states pharmacogenomic profiling prevents adverse drug reactions by identifying metabolic enzyme variations.", "ពិត (TRUE) — ការពិនិត្យឱសថពន្ធុវិទ្យាជួយទស្សន៍ទាយប្រតិកម្មថ្នាំ និងការរំលាយថ្នាំក្នុងរាងកាយរបស់អ្នកជំងឺម្នាក់ៗ។")
            ]
        }
    ]
    TOPICS.extend(extra_health_topics)
    
    # Add topics 36 to 40 for Health
    more_health = [
        {
            "num": 36,
            "title": "The Placebo Effect and Neurobiological Pathways",
            "title_kh": "ឥទ្ធិពលផ្លូវចិត្ត Placebo និងយន្តការសរសៃប្រសាទ",
            "theme_name": "Health & Neurobiology",
            "qtype": "True / False / Not Given",
            "vocab": [
                ("placebo", "noun", "B2", "a harmless pill or procedure prescribed for psychological benefit", "ថ្នាំបញ្ឆោត, ថ្នាំចិត្តសាស្ត្រ"),
                ("endorphin", "noun", "C1", "neurotransmitter reducing pain and promoting pleasure", "អង់ដូហ្វីន (សារធាតុបំបាត់ការឈឺចាប់)"),
                ("neurochemical", "adj", "C1", "relating to chemical substances involved in nervous system function", "ខាងគីមីវិទ្យាសរសៃប្រសាទ"),
                ("analgesia", "noun", "C2", "the inability to feel pain while conscious", "ការបាត់បង់ការឈឺចាប់"),
                ("psychosomatic", "adj", "C1/C2", "caused or aggravated by a mental factor such as internal stress", "ដែលបង្កឡើងពីចិត្ត"),
                ("efficacy", "noun", "B2/C1", "the ability to produce a desired or intended result", "ប្រសិទ្ធភាព")
            ],
            "b1": """In scientific clinical trials, doctors test new medications by comparing them against fake sugar pills called placebos. A placebo contains no active medical chemicals. However, a surprising phenomenon often happens: patients who take a simple sugar pill frequently experience real medical improvement, such as lower blood pressure, reduced headaches, or less pain.

For a long time, doctors believed this improvement was purely imaginary. But modern brain scans show that the placebo effect is a real biological reaction. When a patient genuinely believes they are receiving a powerful painkiller, their brain releases natural pain-relieving chemicals called endorphins. The patient's expectation of healing triggers real physical recovery, proving that mental attitude and optimism have a powerful biological effect on the human body.""",
            "b2": """The placebo effect, once dismissed as a methodological artifact or subjective psychological bias, is now recognized as a measurable neurobiological event. Neuroimaging investigations demonstrate that when a patient anticipates therapeutic relief, the prefrontal cortex initiates top-down neurochemical cascades that stimulate endogenous opioid and dopamine release in the brainstem and spinal cord.

This endogenous analgesic response mimics active pharmaceutical painkillers. In clinical pain trials, placebo administration can be pharmacologically blocked by administering naloxone—an opioid antagonist—proving that placebo analgesia is mediated by actual biochemical opioid receptors rather than superficial psychological deception. Furthermore, the 'nocebo effect' demonstrates the inverse phenomenon: negative expectations induce anxiety-mediated cholecystokinin release that amplifies pain perception, underscoring the critical clinical role of the physician-patient relationship.""",
            "c1": """Contemporary neurobiology has dismantled the Cartesian dualism between somatic reality and mental expectation through the rigorous study of the placebo response. Expectancy-induced analgesia is governed by distinct neural networks, including the dorsolateral prefrontal cortex, the anterior cingulate cortex, and the periaqueductal gray. Through classical conditioning and verbal suggestion, cognitive expectations of therapeutic efficacy trigger descending pain-inhibitory pathways that suppress nociceptive signaling in the dorsal horn of the spinal cord.

Critically, the clinical implications of placebo neurobiology challenge standard paradigms of pharmacological efficacy. The therapeutic outcome of any medical treatment is an additive equation: the intrinsic biochemical activity of the drug plus the contextual neurobiological effect elicited by the clinical ritual, patient belief, and practitioner empathy. Far from being a nuisance in randomized controlled trials, the placebo effect demonstrates that human subjective consciousness actively modulates physiological healing processes, opening avenues for harnessing contextual healing in chronic pain management.""",
            "c2": """The placebo phenomenon exposes the profound philosophical poverty of pure mechanistic materialism in clinical medicine. For centuries, modern medical dogma conceived of the human body as an elaborate mechanical clockwork, treatable exclusively through invasive chemical and surgical interventions. The mind was relegated to an irrelevant epiphenomenon, an uninvited ghost in the machine whose expectations and beliefs were dismissed as mere cognitive delusions.

Yet in the living reality of the placebo response, mind and body reveal their indivisible unity. When a patient experiences relief from a sugar pill, it is not because they were duped; it is because the sacred ritual of clinical care and the spark of hope unlocked the body's own pharmaceutical pharmacy of healing neurochemicals. To dismiss the placebo effect as an illusion is to overlook the greatest miracle of all: the innate capacity of human consciousness to heal the living flesh. Medicine must honor this healing mystery, combining pharmacological rigor with the therapeutic power of human empathy and hope.""",
            "questions": [
                ("1", "Placebo-induced pain relief can be chemically blocked by the opioid antagonist medication naloxone."),
                ("2", "Brain scans indicate that placebo improvements are entirely imaginary with zero measurable chemical changes."),
                ("3", "The nocebo effect occurs when negative expectations amplify pain perception through anxiety-mediated mechanisms."),
                ("4", "Clinical outcomes are influenced solely by biochemical drugs with zero contribution from patient-doctor communication.")
            ],
            "answers": [
                ("1", "TRUE", "B2 confirms placebo analgesia can be pharmacologically blocked by naloxone, proving opioid involvement.", "ពិត (TRUE) — ការបំបាត់ការឈឺចាប់ដោយសារ Placebo អាចត្រូវរារាំងដោយថ្នាំ Naloxone ដែលបញ្ជាក់ថាវាជាប្រតិកម្មគីមីពិតប្រាកដក្នុងខួរក្បាល។"),
                ("2", "FALSE", "B1 and B2 emphasize that modern neuroimaging proves placebo reactions trigger real biological dopamine and endorphin release.", "មិនពិត (FALSE) — ការស្កេនខួរក្បាលបង្ហាញថាឥទ្ធិពល Placebo បង្កើតសារធាតុគីមីជីវសាស្ត្រពិតប្រាកដ មិនមែនគ្រាន់តែជាការស្រមើស្រមៃឡើយ។"),
                ("3", "TRUE", "B2 states negative expectations induce anxiety-mediated cholecystokinin release that amplifies pain (the nocebo effect).", "ពិត (TRUE) — បាតុភូត Nocebo កើតឡើងនៅពេលការគិតអវិជ្ជមាន និងការថប់បារម្ភបង្កើនការឈឺចាប់ឱ្យកាន់តែខ្លាំង។"),
                ("4", "FALSE", "C1 and C2 highlight that clinical outcomes are an additive equation combining drug chemistry with belief and practitioner empathy.", "មិនពិត (FALSE) — លទ្ធផលនៃការព្យាបាលរួមផ្សំទាំងប្រសិទ្ធភាពថ្នាំ និងទំនាក់ទំនងរវាងគ្រូពេទ្យ និងអ្នកជំងឺ មិនមែនតែថ្នាំមួយមុខនោះទេ។")
            ]
        },
        {
            "num": 37,
            "title": "Universal Healthcare Systems vs. Private Insurance",
            "title_kh": "ប្រព័ន្ធធានារ៉ាប់រងសុខភាពជាសកល ធៀបនឹងការធានារ៉ាប់រងឯកជន",
            "theme_name": "Health & Health Economics",
            "qtype": "True / False / Not Given",
            "vocab": [
                ("universal", "adj", "B1/B2", "applicable to all cases or people", "ជាសកល, ទូទៅ"),
                ("deductible", "noun", "C1", "amount paid out of pocket before insurer pays", "ទឹកប្រាក់ដែលត្រូវបង់មុនធានារ៉ាប់រងចេញ"),
                ("insolvency", "noun", "C1", "the state of being unable to pay debts owed", "ក្ស័យធន, អសមត្ថភាពសងបំណុល"),
                ("single-payer", "adj/noun", "B2/C1", "system where a single public agency pays all healthcare costs", "ប្រព័ន្ធទូទាត់ទោលដោយរដ្ឋ"),
                ("administrative", "adj", "B2", "relating to the running of a business or organization", "ខាងរដ្ឋបាល"),
                ("triage", "noun/verb", "C1", "assignment of degrees of urgency to wounds or illnesses", "ការចាត់ថ្នាក់អាទិភាពអ្នកជំងឺ")
            ],
            "b1": """Every nation must decide how to organize and pay for medical care for its citizens. In countries with universal healthcare systems, like the United Kingdom and Canada, the national government pays for doctors, hospitals, and surgeries using public tax revenue. Anyone who gets sick can visit a hospital without paying expensive medical bills.

In contrast, other countries rely on private health insurance companies. In these systems, workers pay monthly fees to private insurance corporations. While private hospitals often have modern rooms and shorter waiting times for elective surgeries, millions of low-income citizens who cannot afford insurance remain unprotected. In addition, when uninsured patients suffer serious accidents or chronic illnesses, hospital bills can force families into bankruptcy. Most health experts agree that basic healthcare is a fundamental human right.""",
            "b2": """The structural confrontation between single-payer universal healthcare models and multi-payer market-driven private insurance frameworks forms the crux of comparative health economics. Proponents of universal public healthcare point to the principle of risk-pooling across the entire national population. By eliminating the administrative overhead, marketing costs, and profit margins of private insurers, public single-payer systems achieve universal coverage at significantly lower costs per capita, while safeguarding citizens against medical bankruptcy.

Conversely, advocates of private insurance systems argue that market competition spurs pharmaceutical innovation, incentivizes medical efficiency, and provides consumer choice. In privatized frameworks, patients with comprehensive insurance experience shorter waiting periods for elective surgeries and access cutting-edge therapeutic interventions. However, critics demonstrate that private insurance creates perverse incentives to deny coverage to high-risk individuals, exacerbating socioeconomic health disparities and leaving millions medically disenfranchised.""",
            "c1": """Comparative health policy analysis reveals that the commodification of healthcare under private insurance mechanisms introduces catastrophic economic inefficiencies. In the United States, administrative overhead consumes over twenty-five percent of total healthcare expenditures—nearly triple that of single-payer systems like Canada's Medicare or the UK's National Health Service. This administrative bloatedness stems from fragmented billing bureaucracies, complex co-payment algorithms, and aggressive claim denial protocols designed to maximize insurer profitability.

Universal healthcare systems demonstrate superior macroeconomic efficiency by functioning as monopsonistic purchasers, negotiating drug prices directly with pharmaceutical cartels and standardizing clinical fees. While universal systems occasionally grapple with elective surgical rationing and specialist wait times, their population-level health outcomes—measured by life expectancy, maternal mortality rates, and infant survival—consistently outperform market-based equivalents. Treating clinical care as a private market commodity fundamentally violates the economic conditions necessary for market efficiency, as healthcare consumers lack price transparency and cannot voluntarily refuse emergency life-saving interventions.""",
            "c2": """The debate over universal healthcare is fundamentally an ethical confrontation between human dignity and market commodification. To treat human healing as an ordinary consumer commodity—subject to the predatory logic of supply, demand, and profit margins—is to monetize human vulnerability and transform illness into an extraction mechanism for private capital. When access to insulin, cancer therapy, or heart surgery is made contingent upon an individual's personal wealth, society ratifies an odious moral doctrine: that the lives of the wealthy are worth saving, while the poor may perish.

A civilized society is measured by how it cares for its sick and vulnerable members. A universal healthcare system represents an embodied social covenant: a collective proclamation that regardless of wealth, social status, or luck, every human being possesses an inalienable right to medical healing. The administrative spreadsheets and insurance denial letters that bankrupt families in their hour of deepest terror are monuments to bureaucratic cruelty. To establish universal healthcare is not merely to optimize public health economics; it is an act of moral emancipation that reaffirms the sacred equality of human life.""",
            "questions": [
                ("1", "Single-payer universal healthcare models pool health risk across the entire national population."),
                ("2", "Private healthcare systems spend significantly less money on administrative overhead than public systems."),
                ("3", "Single-payer governments can negotiate pharmaceutical prices directly as monopsonistic purchasers."),
                ("4", "Private insurance systems guarantee free, immediate heart surgery to all uninsured citizens without charge.")
            ],
            "answers": [
                ("1", "TRUE", "B2 confirms universal healthcare pools risk across the entire national population to lower per capita costs.", "ពិត (TRUE) — ប្រព័ន្ធធានារ៉ាប់រងសុខភាពជាសកលប្រមូលផ្ដុំហានិភ័យសុខភាពទូទាំងប្រទេស ដែលជួយកាត់បន្ថយថ្លៃចំណាយជាមធ្យម។"),
                ("2", "FALSE", "C1 states the opposite: administrative overhead in private systems is nearly triple that of single-payer systems.", "មិនពិត (FALSE) — ប្រព័ន្ធឯកជនចំណាយលើរដ្ឋបាល និងឯកសារច្រើនជាងប្រព័ន្ធរដ្ឋរហូតដល់ជិតបីដង។"),
                ("3", "TRUE", "C1 notes universal systems function as monopsonistic purchasers, negotiating drug prices directly.", "ពិត (TRUE) — រដ្ឋាភិបាលក្នុងប្រព័ន្ធទូទាត់ទោលមានអំណាចចរចាតម្លៃឱសថដោយផ្ទាល់ជាមួយក្រុមហ៊ុនផលិតក្នុងតម្លៃទាប។"),
                ("4", "FALSE", "B1 states that uninsured patients face catastrophic bills that force families into bankruptcy, refuting free surgery.", "មិនពិត (FALSE) — ប្រព័ន្ធឯកជនមិនបានផ្តល់ការវះកាត់បេះដូងឥតគិតថ្លៃដល់អ្នកគ្មានធានារ៉ាប់រងឡើយ ហើយថែមទាំងអាចធ្វើឱ្យពួកគេក្ស័យធនទៀតផង។")
            ]
        },
        {
            "num": 38,
            "title": "Preventive Lifestyle Medicine vs. Reactive Pharmacology",
            "title_kh": "វេជ្ជសាស្ត្របង្ការតាមបែបផែនជីវិត ធៀបនឹងការព្យាបាលតាមឱសថពេលមានជំងឺ",
            "theme_name": "Health & Preventive Medicine",
            "qtype": "True / False / Not Given",
            "vocab": [
                ("preventive", "adj", "B1/B2", "designed to keep something undesirable from occurring", "ដែលការពារទុកជាមុន"),
                ("pharmacology", "noun", "C1", "the branch of medicine concerned with the uses and effects of drugs", "ឱសថសាស្ត្រ"),
                ("lifestyle", "noun", "B1", "the way in which a person or group lives", "របៀបរស់នៅ"),
                ("etiology", "noun", "C2", "the cause, set of causes, or manner of causation of a disease", "មូលហេតុបង្កជំងឺ"),
                ("non-communicable", "adj", "B2/C1", "disease not transmissible directly from one person to another", "មិនឆ្លង"),
                ("polypharmacy", "noun", "C2", "the simultaneous use of multiple drugs by a single patient", "ការប្រើប្រាស់ថ្នាំច្រើនមុខដំណាលគ្នា")
            ],
            "b1": """In modern healthcare systems, the vast majority of medical funding is spent on reactive pharmacology. This means doctors wait until a patient becomes ill with heart disease, high cholesterol, or diabetes before prescribing daily pharmaceutical pills to control their symptoms. While these modern medicines save lives in emergencies, they often fail to cure the underlying problems, requiring patients to take multiple pills for the rest of their lives.

In contrast, preventive lifestyle medicine focuses on preventing chronic diseases before they ever begin. Doctors and nutritionists emphasize regular exercise, plant-rich diets, stress reduction, and restful sleep as powerful medical interventions. Scientific studies prove that healthy daily habits can prevent and even reverse many cases of type 2 diabetes and heart disease. Shifting public healthcare funding toward lifestyle education could save billions of dollars while keeping populations truly healthy.""",
            "b2": """Modern clinical practice is overwhelmingly dominated by a reactive pharmacological paradigm that treats downstream symptoms of chronic disease rather than addressing upstream root causes. In managing the global rise of non-communicable diseases (NCDs)—such as metabolic syndrome, atherosclerosis, and hypertension—clinical guidelines prioritize polypharmacy, prescribing lifetime regimens of statins, anti-hypertensives, and hypoglycemic agents. While pharmacotherapy effectively mitigates acute cardiovascular events, it rarely rectifies the systemic biological drivers of chronic pathology.

Lifestyle medicine has emerged as an evidence-based clinical discipline that utilizes therapeutic lifestyle interventions as a primary modality to treat and reverse chronic conditions. Comprehensive clinical trials demonstrate that whole-food, plant-predominant nutrition, structured aerobic conditioning, restorative sleep, and chronic stress mitigation alter gene expression, reduce systemic inflammatory cytokines, and restore vascular endothelial function. Transitioning healthcare systems from disease management toward proactive lifestyle medicine offers immense economic and clinical dividends.""",
            "c1": """The institutional bias toward reactive pharmacotherapy reflects the economic architecture of medical industrialization. Modern clinical education and fee-for-service reimbursement models are engineered to reward high-volume acute pharmacological prescription and surgical intervention rather than longitudinal behavioral counseling. Consequently, clinical medicine treats the symptomatic manifestations of lifestyle-induced metabolic dysfunction—such as elevated hemoglobin A1c or dyslipidemia—as primary pharmacological deficiencies rather than biological adaptations to chronic environmental mismatches.

Lifestyle medicine reorients clinical paradigms around etiology rather than symptom suppression. Randomized controlled trials conducted by Ornish and colleagues prove that intensive lifestyle modifications can induce cellular telomerase activity, downregulate oncogenes, and reverse coronary artery stenosis without pharmacological intervention. Furthermore, by addressing the common metabolic roots of multi-morbidities—insulin resistance, mitochondrial dysfunction, and chronic inflammation—lifestyle interventions avoid the adverse drug interactions and debilitating cognitive side effects associated with widespread geriatric polypharmacy.""",
            "c2": """The tragedy of contemporary medicine is its transformation into an industrial symptom-management dispensary. In treating the human body as a malfunctioning engine to be tuned with synthetic molecules, modern healthcare has abdicated its ancient calling to promote holistic healing. We allow the toxic environments of modern society—sedentary isolation, nutrient-depleted industrial food, and chronic emotional stress—to break down human biology, only to arrive at the bedside with a pill to suppress every somatic cry of distress.

Lifestyle medicine is an act of medical repentance: a return to the profound truth that the human body possesses an astonishing innate capacity to heal when provided with proper nourishment, physical movement, peaceful rest, and human connection. To prescribe five different pharmaceutical drugs to control the metabolic consequences of a toxic lifestyle while ignoring the underlying causes is an exercise in clinical absurdity. Medicine must step out of the pharmaceutical laboratory and into the living lives of human beings, restoring the ancient truth that true health is cultivated through wise living, not purchased at a pharmacy counter.""",
            "questions": [
                ("1", "Reactive pharmacology waits until chronic illness develops before prescribing medications to manage symptoms."),
                ("2", "Lifestyle interventions like nutrition and exercise have been proven in clinical trials to reverse certain heart conditions."),
                ("3", "The term 'polypharmacy' describes patients taking zero medications throughout their entire adult lives."),
                ("4", "Fee-for-service medical billing models historically incentivize surgical procedures and drug prescriptions over lifestyle counseling.")
            ],
            "answers": [
                ("1", "TRUE", "B1 and B2 state reactive pharmacology treats downstream symptoms after disease has already developed.", "ពិត (TRUE) — វេជ្ជសាស្ត្របែបឱសថរង់ចាំដល់អ្នកជំងឺឈឺសិន ទើបចេញវេជ្ជបញ្ជាឱ្យលេបថ្នាំដើម្បីទប់ទល់រោគសញ្ញា។"),
                ("2", "TRUE", "B2 and C1 cite trials proving lifestyle modifications can reverse coronary artery stenosis and type 2 diabetes.", "ពិត (TRUE) — ការផ្លាស់ប្តូររបៀបរស់នៅ និងរបបអាហារត្រឹមត្រូវអាចជួយបញ្ច្រាស ឬព្យាបាលជំងឺស្ទះសរសៃឈាមបេះដូងបាន។"),
                ("3", "FALSE", "B2 defines polypharmacy as prescribing multiple simultaneous lifelong medications, the opposite of zero drugs.", "មិនពិត (FALSE) — ពាក្យ Polypharmacy សំដៅលើការប្រើប្រាស់ថ្នាំច្រើនមុខដំណាលគ្នាក្នុងពេលតែមួយ មិនមែនគ្មានថ្នាំនោះទេ។"),
                ("4", "TRUE", "C1 states fee-for-service models reward high-volume drug prescription and surgery over behavioral counseling.", "ពិត (TRUE) — ប្រព័ន្ធទូទាត់សេវាសុខាភិបាលប្រពៃណីផ្ដល់ប្រាក់ចំណេញច្រើនលើការវះកាត់ និងការលក់ថ្នាំ ជាងការចំណាយពេលប្រឹក្សាផ្លូវចិត្ត។")
            ]
        },
        {
            "num": 39,
            "title": "The Neuroscience of Meditation and Mindfulness",
            "title_kh": "វិទ្យាសាស្ត្រសរសៃប្រសាទនៃការធ្វើសមាធិ និងការចម្រើនសតិ (Mindfulness)",
            "theme_name": "Health & Neurobiology",
            "qtype": "True / False / Not Given",
            "vocab": [
                ("neuroplasticity", "noun", "C1", "the ability of the brain to form and reorganize synaptic connections", "ភាពបត់បែននៃកោសិកាខួរក្បាល"),
                ("mindfulness", "noun", "B2", "the psychological state of awareness in the present moment", "ការចម្រើនសតិ, ការដឹងខ្លួនក្នុងបច្ចុប្បន្ន"),
                ("amygdala", "noun", "C1", "brain region involved in experiencing emotions like fear and stress", "តំបន់អាមីកដាឡាក្នុងខួរក្បាល"),
                ("cortex", "noun", "B2/C1", "the outer layer of the cerebrum involved in complex brain functions", "ស្រទាប់ខាងក្រៅនៃខួរក្បាល"),
                ("attenuate", "verb", "C1/C2", "to reduce the force, effect, or value of something", "កាត់បន្ថយ, ធ្វើឱ្យថយថយកម្លាំង"),
                ("default mode network", "noun", "C2", "interconnected brain regions active during mind-wandering", "បណ្តាញខួរក្បាលពេលចិត្តរវើរវាយ (DMN)")
            ],
            "b1": """Meditation and mindfulness practices have been taught by spiritual traditions in Asia for thousands of years. Today, however, meditation is no longer practiced only by monks in quiet monasteries. Neuroscientists around the world use advanced brain scanning machines to study how meditating for just twenty minutes a day physically alters the human brain.

These scientific studies show that regular meditation reduces activity in the amygdala, the brain's fear and stress center. At the same time, it thickens the prefrontal cortex, which controls concentration, emotional balance, and decision-making. People who practice mindfulness regularly report feeling calmer, sleep more soundly, and handle workplace stress much better. Consequently, schools, universities, and hospitals are teaching meditation to help people maintain emotional well-being.""",
            "b2": """The clinical and neurobiological investigation of mindfulness meditation has validated ancient contemplative practices through empirical neuroscience. Utilizing functional magnetic resonance imaging (fMRI) and structural voxel-based morphometry, researchers demonstrate that sustained meditation practice induces measurable neuroplastic alterations in central nervous system architecture.

One of the most robust findings involves the structural modulation of the amygdala. Longitudinal studies demonstrate that an eight-week Mindfulness-Based Stress Reduction (MBSR) course significantly reduces grey matter density in the right basolateral amygdala, directly correlating with self-reported stress reduction. Simultaneously, mindfulness strengthens cortical thickness in the hippocampus—governing memory and emotional regulation—while attenuating the hyperactivity of the Default Mode Network (DMN), a neural circuit implicated in repetitive depressive rumination and mind-wandering.""",
            "c1": """The neurobiological mechanisms underwriting contemplative practices reveal the extraordinary capacity of targeted attention to modulate neuro-architecture. Historically, the adult brain was viewed as a structurally fixed computational organ. Contemplative neuroscience demonstrates that mental training reorganizes functional connectomics and neural oscillation synchronization. Mindfulness meditation fundamentally alters top-down attentional control, strengthening functional connectivity between the anterior cingulate cortex and the prefrontal networks.

Crucially, mindfulness practice deconstructs maladaptive cognitive patterns by downregulating the default mode network (DMN). Hyperactivity and hyper-connectivity within the DMN—particularly between the posterior cingulate cortex and the medial prefrontal cortex—is the hallmark of psychiatric conditions including major depressive disorder and generalized anxiety. By decoupling narrative self-referential processing from momentary experiential awareness, mindfulness enhances metacognitive awareness, allowing practitioners to observe emotional sensations as transient physiological events rather than existential self-definitions.""",
            "c2": """The neuroscientific validation of meditation represents a bridge between ancient spiritual wisdom and modern empirical inquiry. For millennia, contemplative masters recognized that the undisciplined human mind is a turbulent ocean of unexamined desires, compulsive anxieties, and chaotic self-referential narratives. In teaching the radical stillness of the breath, ancient wisdom sought not merely stress reduction, but the spiritual awakening of consciousness from the trance of mechanical conditioned existence.

Modern neurobiology, in measuring cortical thickening and amygdala shrinking, has confirmed what the masters knew through introspection: that the mind can reshape the brain that houses it. When a person sits in silent, non-judgmental presence, they dismantle the anxious machinery of the ego, breaking the cycle of emotional reactivity that drives human suffering. Meditation is not a trendy corporate relaxation technique; it is the ultimate technology of human consciousness—the sacred practice of awakening from the sleep of unconscious thought and resting in the serene reality of the present moment.""",
            "questions": [
                ("1", "Longitudinal studies demonstrate that eight-week mindfulness courses reduce grey matter density in the amygdala."),
                ("2", "Meditation has been proven to permanently halt all blood circulation to the prefrontal cortex."),
                ("3", "Hyperactivity in the Default Mode Network is linked to depressive rumination and mind-wandering."),
                ("4", "Neuroimaging proves that the adult human brain possesses neuroplasticity to reorganize neural connections.")
            ],
            "answers": [
                ("1", "TRUE", "B2 confirms an eight-week MBSR course reduces grey matter density in the basolateral amygdala.", "ពិត (TRUE) — ការសិក្សាបញ្ជាក់ថាការហ្វឹកហាត់ចម្រើនសតិ ៨ សប្តាហ៍ជួយបន្ថយទំហំកោសិកាក្នុងតំបន់ Amygdala ដែលជាកន្លែងគ្រប់គ្រងភាពភ័យខ្លាច និងស្ត្រេស។"),
                ("2", "FALSE", "B1 and C1 state meditation strengthens the prefrontal cortex and improves its connectivity, not halting circulation.", "មិនពិត (FALSE) — ការធ្វើសមាធិជួយពង្រឹងមុខងារ និងលំហូរឈាមទៅកាន់ស្រទាប់ខួរក្បាលខាងមុខ មិនមែនបញ្ឈប់នោះឡើយ។"),
                ("3", "TRUE", "B2 and C1 state hyperactivity in the Default Mode Network is linked to depressive rumination and anxiety.", "ពិត (TRUE) — សកម្មភាពជ្រុលហួសហេតុនៃបណ្តាញ Default Mode Network ជាប់ទាក់ទងនឹងការគិតច្រើន និងជំងឺថប់បារម្ភ។"),
                ("4", "TRUE", "B2 and C1 affirm that contemplative practice demonstrates adult brain neuroplasticity.", "ពិត (TRUE) — ការស្រាវជ្រាវបង្ហាញថាខួរក្បាលមនុស្សពេញវ័យនៅតែមានភាពបត់បែន (Neuroplasticity) ក្នុងការកែប្រែប្រព័ន្ធសរសៃប្រសាទ។")
            ]
        },
        {
            "num": 40,
            "title": "Vaccine Hesitancy and Public Health Communication",
            "title_kh": "ភាពស្ទាក់ស្ទើរក្នុងការចាក់វ៉ាក់សាំង និងការប្រាស្រ័យទាក់ទងសុខភាពសាធារណៈ",
            "theme_name": "Health & Immunology",
            "qtype": "True / False / Not Given",
            "vocab": [
                ("hesitancy", "noun", "B2", "the reluctance or refusal to vaccinate despite availability", "ភាពស្ទាក់ស្ទើរ"),
                ("immunization", "noun", "B2", "the process whereby a person is made immune to an infectious disease", "ការចាក់ថ្នាំបង្ការ"),
                ("herd immunity", "noun", "B2/C1", "resistance to disease spread when a high percentage are immune", "ភាពស៊ាំសហគមន៍"),
                ("misinformation", "noun", "B2", "false or inaccurate information spread regardless of intent", "ព័ត៌មានមិនពិត"),
                ("polarization", "noun", "C1", "division into two sharply contrasting groups or sets of opinions", "ការបែកបាក់ជាប៉ូលផ្ទុយគ្នា"),
                ("inoculation", "noun", "C1", "the action of immunizing someone against disease", "ការចាក់វ៉ាក់សាំង")
            ],
            "b1": """Vaccines are among the greatest public health achievements in human history. Immunization campaigns led by the World Health Organization have completely wiped out smallpox and saved millions of children from dying of polio, measles, and tetanus. When the vast majority of people in a neighborhood are vaccinated, it creates herd immunity, protecting newborn babies and sick patients who cannot receive shots.

Despite this overwhelming scientific success, vaccine hesitancy has grown rapidly around the world. Because false rumors and scary conspiracy theories spread easily on social media, many parents delay or refuse vaccines for their children. When vaccination rates fall below ninety-five percent, dangerous diseases like measles quickly return. Health authorities must communicate with honesty, listen to parents' genuine worries, and rebuild trust without mocking or shaming them.""",
            "b2": """Vaccine hesitancy, identified by the World Health Organization as a top global health threat, represents a multifaceted socio-psychological challenge to immunization programs. Defined as the reluctance or refusal to vaccinate despite the availability of vaccination services, hesitancy is driven by the complex '3Cs' model: complacency regarding disease risk, inconvenience in vaccine access, and a deficit of trust in vaccine safety and regulatory agencies.

The amplification of vaccine misinformation across algorithmically curated social media networks has catalyzed widespread public skepticism. Misleading assertions alleging autism links or synthetic contamination exploit algorithmic echo chambers to foster cognitive confirmation biases. When herd immunity thresholds—typically requiring ninety-five percent population immunization for highly contagious pathogens like measles—are compromised, localized outbreaks erupt, endangering immunocompromised cohorts and placing severe burdens on public healthcare systems.""",
            "c1": """The resurgence of vaccine hesitancy in contemporary democracies reflects deep institutional crises of epistemic trust, political polarization, and asymmetrical digital communication. Rather than treating hesitancy merely as an information deficit to be remedied through aggressive scientific lecturing, sociological analysis reveals that vaccination decisions are deeply embedded in sociocultural identity, institutional cynicism, and historical medical grievances. When public health agencies adopt condescending messaging, it often solidifies distrust among skeptical demographics.

Effective public health communication demands a paradigm shift from top-down paternalistic didacticism toward empathetic, transparent engagement. Addressing cognitive cognitive heuristics—such as omission bias and naturalness bias—requires public health communicators to pre-emptively 'inoculate' the public against disinformation using pre-bunking strategies. Furthermore, partnering with trusted local community leaders, practicing absolute transparency regarding rare adverse reactions, and acknowledging past institutional errors are essential strategies to rebuild scientific credibility and restore societal herd immunity.""",
            "c2": """Vaccine hesitancy is the tragic canary in the coal mine of late-stage democratic governance: a symptom of fractured social contracts and the collapse of institutional trust. In an era where citizens feel betrayed by corporate interests and bureaucratic elites, the physical body becomes the final sovereign territory of resistance. When public health authorities demand uncritical compliance while concealing uncertainties, they transform a vital scientific gift into a weapon of bureaucratic coercion, driving desperate citizens into the arms of charismatic digital conspiracy peddlers.

To restore faith in vaccination is not merely a technical challenge of communication strategy; it is an ethical imperative of democratic reconciliation. Public health must abandon the arrogance of scientific infallibility and re-learn the language of genuine compassion and humility. The syringe is not merely an instrument of biological immunology; it is a sacred symbol of collective solidarity—a tangible commitment to protect not only oneself, but the newborn infant, the cancer sufferer, and the elderly stranger. To rebuild that sacred trust requires institutions that are truly worthy of the public's faith.""",
            "questions": [
                ("1", "Vaccines have successfully eliminated smallpox from the human population globally."),
                ("2", "The '3Cs' model defines the drivers of vaccine hesitancy as complacency, convenience, and confidence."),
                ("3", "Maintaining herd immunity against measles requires vaccination coverage rates to remain around ninety-five percent."),
                ("4", "All medical doctors recommend shouting angrily at hesitant parents as the most effective scientific persuasion method.")
            ],
            "answers": [
                ("1", "TRUE", "B1 states that WHO campaigns completely wiped out smallpox and saved millions of children.", "ពិត (TRUE) — យុទ្ធនាការចាក់វ៉ាក់សាំងបានលុបបំបាត់ជំងឺអុតធំ (Smallpox) ទាំងស្រុងពីផែនដី។"),
                ("2", "TRUE", "B2 explicitly identifies the 3Cs model: complacency, convenience (access), and confidence/trust.", "ពិត (TRUE) — គំរូ 3Cs រួមមានភាពព្រងើយកន្តើយ (Complacency) ភាពងាយស្រួល (Convenience) និងទំនុកចិត្ត (Confidence)។"),
                ("3", "TRUE", "B1 and B2 state that herd immunity thresholds for measles typically require ninety-five percent immunization.", "ពិត (TRUE) — ភាពស៊ាំសហគមន៍ប្រឆាំងជំងឺកញ្ជ្រិលទាមទារអត្រាចាក់វ៉ាក់សាំងយ៉ាងតិច ៩៥% ក្នុងចំណោមប្រជាជន។"),
                ("4", "FALSE", "B1, C1, and C2 state authorities must communicate with honesty and empathy rather than shaming or shouting.", "មិនពិត (FALSE) — អត្ថបទបញ្ជាក់ថាគ្រូពេទ្យត្រូវពន្យល់ដោយការយល់ចិត្ត និងស្មោះត្រង់ មិនមែនស្រែកគំហក ឬមាក់ងាយឪពុកម្តាយឡើយ។")
            ]
        }
    ]
    TOPICS.extend(more_health)
    
    write_theme_file(
        filename="ielts_04_health.md",
        theme_title="Health, Medicine & Human Well-being (Topics 31–40)",
        theme_kh="សុខភាព វេជ្ជសាស្ត្រ និងសុខុមាលភាពមនុស្ស (ប្រធានបទ ៣១ ដល់ ៤០)",
        theme_desc="This volume presents 10 comprehensive academic reading topics on the Global Obesity Epidemic, Antimicrobial Resistance, Workplace Burnout, Sleep Deprivation, Personalized Genomics, the Placebo Effect, Universal Healthcare, and Vaccine Hesitancy. Each topic contains an authentic IELTS/CEFR reading passage adapted across four CEFR levels (B1, B2, C1, C2), key academic vocabulary with Khmer translations, 4 mock exam questions, and full explanatory walkthroughs.",
        topics=TOPICS
    )
