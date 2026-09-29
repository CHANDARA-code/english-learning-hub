#!/usr/bin/env python3
"""
Generate Volume 9: Culture, Heritage & Global Tourism (Topics 81–90)
reading_skills/examples/ielts_09_culture_globalisation.md
"""

from reading_generator_engine import write_theme_file

TOPICS = [
    {
        "num": 81,
        "title": "Overtourism and the Fragility of Historic Cities",
        "title_kh": "ការទេសចរណ៍លើសកម្រិត និងភាពងាយរងគ្រោះនៃទីក្រុងប្រវត្តិសាស្ត្រ",
        "theme_name": "Culture & Heritage",
        "qtype": "True / False / Not Given",
        "vocab": [
            ("overtourism", "noun", "B2/C1", "excessive numbers of tourist visits to a popular destination causing damage", "ការទេសចរណ៍ហួសកម្រិត"),
            ("fragility", "noun", "C1", "the quality of being easily broken, damaged, or harmed", "ភាពផុយស្រួយ, ភាពងាយរងគ្រោះ"),
            ("displacement", "noun", "B2/C1", "the enforced departure of people from their homes or lands", "ការផ្លាស់ទីលំនៅដោយបង្ខំ"),
            ("congestion", "noun", "B2", "the state of being overcrowded or obstructed with traffic or visitors", "ការកកស្ទះ"),
            ("degradation", "noun", "C1", "the process of deteriorating or losing quality and character", "ការធ្លាក់ចុះគុណភាព"),
            ("carrying capacity", "noun", "C1/C2", "the maximum population or tourist count an ecosystem can sustainably support", "សមត្ថភាពផ្ទុកអតិបរមា")
        ],
        "b1": """Every year, millions of travelers fly across oceans to visit ancient cities like Venice, Dubrovnik, and Kyoto. These destinations offer breathtaking historic architecture, cobblestone alleys, and unforgettable cultural traditions. However, the explosive growth of low-cost budget flights and giant cruise ships has produced a serious crisis called overtourism. In popular destinations, the sheer volume of tourists has overwhelmed historic streets and damaged delicate stone buildings.

Local residents suffer greatly from this tourism boom. Longtime grocery markets, neighborhood bakeries, and craft shops have closed down, replaced by souvenir stores selling cheap plastic souvenirs. Even worse, landlords convert affordable rental apartments into short-term holiday vacation homes, forcing local families and teachers to leave their hometowns because rents are too expensive. To protect their cities, municipal governments are now charging entrance fees, restricting giant cruise ships, and setting daily tourist quotas.""",
        "b2": """Overtourism describes a threshold condition wherein visitor volumes exceed the physical, infrastructural, and ecological carrying capacity of a cultural destination, degrading both the visitors' experience and residents' living standards. Historic European capitals and UNESCO World Heritage sites have become acute epicenters of this crisis, driven by hyper-mobility, international discount airlines, and digital vacation-rental booking algorithms.

The consequences for urban host communities are devastating. The widespread conversion of residential housing stock into commercial short-term tourist accommodation causes severe residential displacement and skyrockets local rental prices. Municipal infrastructure—including waste disposal networks, public transit systems, and ancient pedestrian pathways—faces chronic strain. In response, cities are pioneering aggressive containment policies. Venice has instituted a daily day-tripper visitor tax and banned mega-cruise liners from its historic canal basins, while Dubrovnik has enacted real-time digital surveillance cameras to cap pedestrian density within its medieval fortress walls.""",
        "c1": """The phenomenon of overtourism embodies the predatory financialization of cultural heritage under late-stage neoliberal globalization. Historic urban fabrics, organically cultivated over centuries of vernacular civic habitation, have been transformed into commodified theme-park backdrops designed for ephemeral transnational consumption and algorithmic social-media broadcasting. This monocultural tourist economy cannibalizes the living urban social fabric that originally attracted visitors, triggering intense friction between transient tourist populations and marginalized permanent residents.

Mitigating overtourism demands structural policy interventions that dismantle speculative holiday rental platforms. Regulators must enforce strict municipal zoning caps that prioritize local residential tenure over speculative hospitality platforms, levy progressive tourist surcharges dedicated to historic preservation trust funds, and mandate enforceable seasonal visitor quotas. Without decisive regulatory containment, global heritage destinations risk terminal physical degradation, transforming into depopulated, sterile architectural museums emptied of genuine cultural vitality.""",
        "c2": """There is a tragic irony at the heart of modern tourism: in our desperate hunger to touch the authentic soul of ancient places, we trample them into oblivion. The ancient stone bridges of Venice and the sacred mountain temples of Kyoto were never built to withstand the relentless march of tens of millions of selfie-seeking travelers each year. When a historic city is overrun by surging tides of tourists, its quiet beauty is drowned out by the commerce of cheap trinkets and noisy tour buses.

A city is not a theme park; it is a sacred tapestry of living human souls, whispered memories, and daily neighborhood life. When local butchers, bookshops, and families are driven out by luxury boutique hotels and vacation rentals, the city loses its beating heart. We must rediscover the lost art of mindful, humble pilgrimage—visiting other cultures not as entitled consumers seeking sensory spectacle, but as respectful guests willing to step lightly upon the sacred stones of human history.""",
        "questions": [
            ("1", "Overtourism occurs when the volume of visitors exceeds the sustainable carrying capacity of an urban destination."),
            ("2", "The conversion of apartments into short-term holiday rentals generally lowers rental housing costs for local residents."),
            ("3", "Venice has introduced a day-tripper entrance fee and banned large cruise ships from its historic canal basins."),
            ("4", "Dubrovnik utilizes digital camera surveillance to monitor and cap tourist pedestrian density in its medieval core.")
        ],
        "answers": [
            ("1", "TRUE", "B1 and B2 define overtourism as visitor numbers exceeding the physical and ecological carrying capacity of destinations.", "ពិត (TRUE) — ការទេសចរណ៍លើសកម្រិតកើតឡើងនៅពេលចំនួនភ្ញៀវទេសចរហួសពីសមត្ថភាពផ្ទុកជាក់ស្តែង និងហេដ្ឋារចនាសម្ព័ន្ធនៃទីក្រុង។"),
            ("2", "FALSE", "B1, B2, and C1 state converting homes into holiday rentals forces local residents out and skyrockets rent prices.", "មិនពិត (FALSE) — ការកែប្រែផ្ទះជួលទៅជាកន្លែងស្នាក់នៅវិស្សមកាលទេសចរណ៍រយៈពេលខ្លី បានធ្វើឱ្យតម្លៃផ្ទះជួលឡើងថ្លៃខ្លាំង និងបណ្តេញអ្នកស្រុកដើមចេញ។"),
            ("3", "TRUE", "B2 states Venice instituted a daily visitor tax and banned mega-cruise liners from its historic canal basins.", "ពិត (TRUE) — ទីក្រុងវ៉េនីសបានដាក់ពន្ធលើអ្នកមកទស្សនាក្នុងមួយថ្ងៃ និងហាមឃាត់កប៉ាល់ទេសចរណ៍ខ្នាតធំមិនឱ្យចូលអាងព្រែកជីកប្រវត្តិសាស្ត្រ។"),
            ("4", "TRUE", "B2 mentions Dubrovnik uses real-time digital surveillance cameras to cap pedestrian density within medieval fortress walls.", "ពិត (TRUE) — ទីក្រុង Dubrovnik ប្រើកាមេរ៉ាឌីជីថលតាមដានទិន្នន័យជាក់ស្តែង ដើម្បីកម្រិតចំនួនអ្នកថ្មើរជើងនៅក្នុងបន្ទាយបុរាណ។")
        ]
    },
    {
        "num": 82,
        "title": "Indigenous Language Endangerment and Revitalization",
        "title_kh": "ការគំរាមកំហែងដល់ភាសាជនជាតិដើមភាគតិច និងការស្តារឡើងវិញ",
        "theme_name": "Language & Indigenous Rights",
        "qtype": "True / False / Not Given",
        "vocab": [
            ("endangerment", "noun", "B2/C1", "the state of being exposed to danger or at risk of extinction", "ការប្រឈមមុខនឹងគ្រោះថ្នាក់/ការផុតពូជ"),
            ("revitalization", "noun", "C1", "the act of imbuing something with new life, vigor, and active use", "ការធ្វើឱ្យរស់រវើកឡើងវិញ"),
            ("linguicide", "noun", "C2", "the deliberate destruction or death of a language", "ការបំផ្លាញភាសា, មរណភាពនៃភាសា"),
            ("indigenous", "adj", "B2", "originating or occurring naturally in a particular place; native", "ជនជាតិដើមភាគតិច"),
            ("assimilation", "noun", "C1", "the process of absorbing one cultural group into harmony with another", "ការធ្វើសមាហរណកម្មវប្បធម៌"),
            ("epistemology", "noun", "C2", "a theory or framework of knowledge and way of understanding reality", "ទស្សនវិជ្ជាស្តីពីចំណេះដឹង")
        ],
        "b1": """Language is much more than simply a tool for speaking and trading; it carries a community's unique songs, folklore, historical wisdom, and connection to the land. Sadly, linguists estimate that of the roughly 7,000 languages spoken worldwide today, more than half could disappear before the end of this century. Many indigenous languages around the globe are spoken only by a small handful of elderly grandparents.

Languages become endangered primarily because historical government policies forced indigenous children into boarding schools where speaking native tongues was strictly forbidden. Today, dominant global languages like English, Spanish, and Mandarin dominate television, internet media, and formal schools. Fortunately, passionate indigenous communities are fighting back through revitalization programs. In New Zealand and Hawaii, 'language nest' preschools immerse young toddlers in native Maori and Hawaiian speech, raising thousands of proud, fluent new speakers.""",
        "b2": """Linguistic diversity is experiencing an unprecedented planetary extinction event. Sociolinguists categorize over forty percent of the world's 7,000 spoken languages as critically endangered, with a language vanishing roughly every fortnight. This catastrophic loss of intangible cultural heritage stems from centuries of coercive colonial assimilation policies, including residential schooling systems designed to eradicate indigenous vernaculars, alongside the contemporary digital dominance of major linguistic superpowers.

The extinction of an indigenous language represents not merely a lexical loss, but the irreparable destruction of unique epistemological frameworks. Indigenous idioms contain sophisticated taxonomic classifications of regional flora, ecological medicinal remedies, and ancestral oral histories that exist nowhere in western scientific literature. Innovative revitalization strategies—exemplified by the Maori Kohanga Reo ('language nest') model and digital linguistic archiving using mobile applications—demonstrate that with community sovereignty and educational investment, critically endangered mother tongues can successfully reclaim intergenerational transmission.""",
        "c1": """Linguistic endangerment must be diagnosed as the structural consequence of colonial linguicide and communicative capitalism. Nation-states historically deployed institutional linguistic standardization as an instrument of political hegemony, systematically pathologizing indigenous dialects and violently suppressing minority speech through punitive educational assimilation regimes. In the twenty-first century, algorithmic media feeds and global software architectures perpetuate this linguistic enclosure by operating almost exclusively within dominant imperial idioms.

When a language dies, an entire irreplaceable cosmos of human thought, philosophy, and environmental wisdom is extinguished forever. Grammatical structures reflect unique cognitive mappings of time, space, and kinship relations, encoding ecological insights gathered over millenary coexistence with local ecosystems. Counteracting language death requires more than passive archival documentation; it necessitates linguistic decolonization. Governments must recognize indigenous language rights as fundamental human rights, finance immersion pedagogy, and restore indigenous land sovereignty, ensuring that ancestral languages remain living instruments of community self-determination.""",
        "c2": """Every language is a magnificent temple of the human spirit, built stone by stone through thousands of years of human love, struggle, poetry, and song. When an elder takes their final breath carrying the last words of an ancient tongue, an entire universe of human memory collapses into eternal silence. No dictionary, no audio recording can ever truly replace the living breath of a language spoken between mother and child under the stars.

To allow an indigenous language to die is to betray our ancestors and impoverish our descendants. In ancestral words lie the secret names of desert herbs, the forgotten songs of ancient rivers, and ways of understanding our place within nature that modern industrial culture has tragically forgotten. When we help a young child speak the words of their indigenous great-grandparents, we are not merely saving sounds; we are rekindling an ancient sacred flame that keeps humanity whole.""",
        "questions": [
            ("1", "More than half of the world's approximately 7,000 spoken languages are at risk of extinction this century."),
            ("2", "Colonial boarding schools historically encouraged and celebrated the daily use of indigenous languages."),
            ("3", "The New Zealand Maori 'Kohanga Reo' initiative immerses young children in their native language to ensure transmission."),
            ("4", "Indigenous vocabularies often preserve sophisticated ecological knowledge and botanical terms not found in Western literature.")
        ],
        "answers": [
            ("1", "TRUE", "B1 and B2 state more than half (over 40-50%) of the world's 7,000 languages are at severe risk of disappearance.", "ពិត (TRUE) — អ្នកភាសាវិទ្យាប៉ាន់ប្រមាណថាជាងពាក់កណ្តាលនៃភាសាសរុប ៧.០០០ លើពិភពលោកប្រឈមនឹងការបាត់បង់ក្នុងសតវត្សរ៍នេះ។"),
            ("2", "FALSE", "B1 and B2 state colonial boarding schools strictly forbade and eradicated native tongues.", "មិនពិត (FALSE) — សាលារៀនសម័យអាណានិគមបានហាមឃាត់ និងដាក់ទណ្ឌកម្មយ៉ាងតឹងរ៉ឹងចំពោះកុមារដែលនិយាយភាសាកំណើតរបស់ខ្លួន មិនមែនលើកទឹកចិត្តឡើយ។"),
            ("3", "TRUE", "B1 and B2 highlight the Maori Kohanga Reo ('language nest') model which immerses toddlers in native Maori.", "ពិត (TRUE) — គំរូ 'សំបុកភាសា' (Kohanga Reo) របស់ជនជាតិ Maori នៅនូវែលសេឡង់ ជួយបណ្តុះបណ្តាលកុមារតូចៗឱ្យចេះនិយាយភាសាកំណើតយ៉ាងស្ទាត់ជំនាញ។"),
            ("4", "TRUE", "B2 states indigenous idioms contain sophisticated taxonomic classifications of flora and medicinal remedies.", "ពិត (TRUE) — វាក្យសព្ទភាសាជនជាតិដើមភាគតិចផ្ទុកទៅដោយចំណេះដឹងអេកូឡូស៊ី រុក្ខឱសថ និងចំណាត់ថ្នាក់រុក្ខជាតិដែលគ្មាននៅក្នុងអក្សរសិល្ប៍វិទ្យាសាស្ត្របស្ចិមប្រទេសឡើយ។")
        ]
    },
    {
        "num": 83,
        "title": "Museum Ethics and the Repatriation of Cultural Artifacts",
        "title_kh": "សីលធម៌សារមន្ទីរ និងការប្រគល់វត្ថុបុរាណវប្បធម៌ត្រឡប់ទៅមាតុភូមិវិញ",
        "theme_name": "Museums & Ethics",
        "qtype": "True / False / Not Given",
        "vocab": [
            ("repatriation", "noun", "C1", "the return of cultural property or art to its country or community of origin", "ការប្រគល់ត្រឡប់ទៅមាតុភូមិវិញ"),
            ("plunder", "noun/verb", "B2/C1", "the violent theft or looting of goods during war or colonial occupation", "ការលួចប្លន់ទ្រព្យសម្បត្តិ"),
            ("provenance", "noun", "C1/C2", "the place of origin or earliest known history of something, especially art", "ប្រភពដើមនៃវត្ថុសិល្បៈ"),
            ("illicit", "adj", "C1", "forbidden by law, rules, or custom; illegal", "ខុសច្បាប់"),
            ("custodianship", "noun", "C1", "the protective care or guardianship of something valuable", "ការគ្រប់គ្រងថែរក្សា"),
            ("restitution", "noun", "C1", "the restoration of something lost or stolen to its proper owner", "ការសង/ប្រគល់សំណងឡើងវិញ")
        ],
        "b1": """Major world-famous museums in London, Paris, and Berlin attract millions of international visitors every year to admire ancient treasures. In these grand galleries, tourists can see the Rosetta Stone from Egypt, magnificent carved bronze statues from Nigeria, and stone sculptures from the Parthenon in Greece. For many decades, Western museum directors argued that keeping these treasures in big metropolitan cities allowed the entire world to view and study them safely.

Today, however, an intense global debate surrounds the legal and ethical ownership of these historic treasures. Many of these famous cultural artifacts were violently plundered or stolen by imperial soldiers during colonial wars. Countries across Africa, Asia, and the Mediterranean are now formally demanding the return, or repatriation, of their sacred heritage. They argue that these artifacts were stolen unlawfully and belong in the homeland where they were created to heal historical wounds.""",
        "b2": """The ethical foundations of Western encyclopedic museums are undergoing a historic transformation regarding the restitution of cultural patrimony. For centuries, prestigious European and North American institutions justified retaining plundered colonial antiquities—such as the Benin Bronzes looted by British troops in 1897 and the Parthenon Sculptures taken from Athens—under the doctrine of 'universal custodianship.' Museum curators asserted that major metropolitan centers provided superior conservation facilities and global accessibility.

In recent years, rigorous provenance research and post-colonial diplomatic pressure have thoroughly dismantled this paternalistic defense. Independent investigations have revealed that vast quantities of museum acquisitions were acquired through illicit military pillage, coercion, and archaeological smuggling. Groundbreaking initiatives, notably the 2018 Sarr-Savoy report commissioned by the French presidency, advocate the permanent restitution of sub-Saharan African cultural artifacts. Leading museums in Germany and France have begun officially transferring legal ownership of looted treasures back to their sovereign nations of origin.""",
        "c1": """The institutional refusal of Western encyclopedic museums to repatriate plundered cultural patrimony constitutes an ongoing perpetuation of colonial epistemic violence. By displaying sacred religious effigies, royal regalia, and ancestral funerary remains behind glass vitrines as aesthetic trophies of imperial conquest, museums strip these artifacts of their living spiritual, liturgical, and ceremonial functions. The invocation of 'universal heritage' serves as an ideological smokescreen designed to legitimize historical illicit extraction and reinforce global structural hierarchies.

Authentic decolonization demands the unconditional legal and physical restitution of all cultural treasures acquired under conditions of military subjugation and colonial asymmetry. Arguments alleging that originating Global South nations lack adequate conservation infrastructure represent unrepentant neocolonial condescension. Sovereign nations possess the inalienable moral and jurisdictional right to curate their own ancestral legacy. Restitution is not merely a transfer of property; it is an indispensable reparative act essential for psychological healing and post-colonial justice.""",
        "c2": """Inside the quiet, temperature-controlled glass cases of grand Western museums, ancient bronze kings and sacred stone deities gaze out at crowds of passing tourists. Yet beneath their silent beauty lies a painful history of blood, cannon fire, and imperial conquest. These sacred sculptures were never meant to be sterile art commodities hung on white museum walls; they were the sacred guardians of shrines, the spiritual heartbeat of kings, and the sacred living memory of sovereign civilizations.

To hold onto stolen treasure while claiming to be its 'guardian' is an act of profound moral hypocrisy. True honor lies in letting go. When a nation returns a sacred artifact stolen during the darkness of colonial war, it does not diminish itself; it redeems its soul. The return of the sacred Benin Bronzes to Nigeria and ancient carvings to their ancestral temples heals deep historic wounds and proves that justice, however long delayed, will always overcome imperial pride.""",
        "questions": [
            ("1", "The Benin Bronzes were taken by British forces during a military expedition in the late nineteenth century."),
            ("2", "The 2018 Sarr-Savoy report recommended that all colonial-era African artifacts should permanently remain in Paris."),
            ("3", "Opponents of repatriation historically argued that Western museums provided safer conservation facilities for global artifacts."),
            ("4", "Several major museums in Germany and France have initiated the legal transfer of looted antiquities back to their countries of origin.")
        ],
        "answers": [
            ("1", "TRUE", "B2 mentions the Benin Bronzes were looted by British troops in 1897 during colonial expeditions.", "ពិត (TRUE) — រូបចម្លាក់សំរឹទ្ធ Benin ត្រូវបានកងទ័ពអង់គ្លេសលួចប្លន់ក្នុងបេសកកម្មយោធាកាលពីឆ្នាំ ១៨៩៧។"),
            ("2", "FALSE", "B2 states the Sarr-Savoy report advocated the permanent restitution of sub-Saharan African artifacts, not retaining them.", "មិនពិត (FALSE) — របាយការណ៍ Sarr-Savoy ឆ្នាំ ២០១៨ គាំទ្រយ៉ាងពេញទំហឹងឱ្យប្រគល់វត្ថុបុរាណអាហ្វ្រិកត្រឡប់ទៅវិញ មិនមែនរក្សាទុកនៅប៉ារីសឡើយ។"),
            ("3", "TRUE", "B1 and B2 state museum directors argued metropolitan cities provided superior conservation facilities and accessibility.", "ពិត (TRUE) — ពីមុន សារមន្ទីរលោកខាងលិចបានអះអាងថាសារមន្ទីររបស់ពួកគេមានលក្ខខណ្ឌអភិរក្ស និងសុវត្ថិភាពល្អជាងសម្រាប់វត្ថុបុរាណ។"),
            ("4", "TRUE", "B2 confirms leading museums in Germany and France have begun transferring legal ownership of looted treasures back home.", "ពិត (TRUE) — សារមន្ទីរធំៗនៅអាល្លឺម៉ង់ និងបារាំងបានចាប់ផ្តើមផ្ទេរកម្មសិទ្ធិស្របច្បាប់នៃវត្ថុបុរាណដែលត្រូវបានប្លន់ត្រឡប់ទៅប្រទេសដើមវិញ។")
        ]
    },
    {
        "num": 84,
        "title": "Cultural Appropriation versus Appreciation in Globalized Art",
        "title_kh": "ការកេងចំណេញវប្បធម៌ ទល់នឹងការឲ្យតម្លៃវប្បធម៌ក្នុងសិល្បៈសកល",
        "theme_name": "Culture & Modern Society",
        "qtype": "True / False / Not Given",
        "vocab": [
            ("appropriation", "noun", "C1", "the unacknowledged or inappropriate adoption of customs or practices of another group", "ការកេងចំណេញវប្បធម៌"),
            ("appreciation", "noun", "B2", "recognition and enjoyment of the good qualities of someone or something", "ការឲ្យតម្លៃ, ការយល់ដឹងគុណតម្លៃ"),
            ("commodification", "noun", "C1", "the transformation of goods, services, or culture into commodities", "ទំនិញភាវូបនីយកម្ម"),
            ("disrespectful", "adj", "B1/B2", "showing a lack of respect or courtesy; insolent", "ដែលគ្មានការគោរព"),
            ("homogenization", "noun", "C1", "the process of making things uniform or similar across borders", "ការធ្វើឱ្យដូចគ្នា, ឯកសណ្ឋានភាព"),
            ("hegemony", "noun", "C2", "leadership or dominance, especially by one social group over others", "អនុត្តរភាព, អំណាចត្រួតត្រា")
        ],
        "b1": """In our modern, interconnected world, fashion designers, musicians, and artists can easily find creative inspiration from diverse cultures around the globe. Beautiful textile patterns from West Africa, traditional indigenous tattoos, and Asian festival clothing regularly appear on global fashion runways and in viral music videos. Many artists believe this cross-cultural borrowing is a wonderful celebration of human diversity that brings people closer together.

However, a serious problem arises when dominant commercial brands use sacred symbols from minority cultures without understanding or respect. This is called cultural appropriation. It happens when powerful businesses copy sacred traditional designs to make huge corporate profits, without giving credit, permission, or financial compensation to the original creators. In contrast, genuine cultural appreciation involves taking time to learn the deep spiritual meaning of traditions, honoring the original artisans, and asking for their consent.""",
        "b2": """The boundary between cultural appreciation and cultural appropriation represents one of the most contentious debates in contemporary creative industries. In an interconnected digital economy, artists and commercial enterprises continually draw inspiration from cross-cultural motifs. Genuine cultural appreciation is characterized by mutual respect, deep historical contextualization, explicit artistic attribution, and collaborative economic engagement with originating cultural communities.

Conversely, cultural appropriation occurs when members of a dominant socioeconomic group adopt, extract, or commodify cultural elements—especially sacred religious symbols, ceremonial garments, or vernacular musical traditions—from historically marginalized groups without authorization or contextual understanding. This extractive dynamic often trivializes profound spiritual traditions, reducing sacred heritage into superficial novelty accessories. Furthermore, corporate fast-fashion retailers frequently monetize traditional indigenous textile motifs while indigenous craft artisans remain trapped in economic poverty without legal intellectual property protections.""",
        "c1": """The discourse surrounding cultural appropriation must be analyzed through the lens of asymmetric power relations and structural imperial hegemony. In the contemporary cultural marketplace, the unilateral extraction of aesthetic forms from historically subaltern populations mirrors the economic resource extraction of classic colonialism. When corporate conglomerates monetize indigenous iconography without structural remuneration or consent, they enact an extractive epistemic violence that divorces cultural signifiers from their sacred ontological moorings.

Conversely, defensive cultural essentialism—which seeks to enforce rigid ethnic borders around artistic production—risks stifling the organic syncretism that has catalyzed creative evolution throughout human civilizational history. The imperative task is not to prohibit cross-cultural hybridity, but to dismantle asymmetric economic exploitation. Ethical creative exchange requires dismantling intellectual property monopolies, establishing collective copyright protections for indigenous communities, and ensuring equitable profit-sharing whenever ancestral cultural forms enter the global commercial sphere.""",
        "c2": """Culture is not a stagnant fortress built to keep the world away; it is a flowing river that has always nourished human creativity through exchange, storytelling, and wonder. Throughout history, the mingling of different cultures has given birth to our greatest treasures—from the silk roads that blended Eastern and Western arts to the birth of jazz from African rhythms and European melodies. Cross-cultural learning is the supreme testament to human kinship.

Yet there is a sacred line between loving another culture and exploiting it for cheap profit. When powerful corporations pluck sacred ceremonial feathers or prayer robes off their ancestral altars and turn them into cheap party costumes, they wound the dignity of ancient peoples. To truly appreciate a culture is to bow before its history, to learn its tears as well as its songs, and to treat its sacred symbols with the reverent gentleness that we would wish for our own.""",
        "questions": [
            ("1", "Cultural appreciation is characterized by mutual respect, historical contextualization, and proper attribution."),
            ("2", "Fast-fashion brands always allocate fifty percent of their profits directly to indigenous craftspeople."),
            ("3", "Cultural appropriation frequently reduces sacred ceremonial symbols into superficial fashion accessories."),
            ("4", "Some cultural theorists caution that rigid artistic boundaries could stifle creative syncretism and hybridity.")
        ],
        "answers": [
            ("1", "TRUE", "B1 and B2 state cultural appreciation involves mutual respect, deep historical understanding, and giving credit.", "ពិត (TRUE) — ការឲ្យតម្លៃវប្បធម៌ត្រូវបានសម្គាល់ដោយការគោរពគ្នាទៅវិញទៅមក ការយល់ដឹងពីប្រវត្តិសាស្ត្រ និងការទទួលស្គាល់ប្រភពដើម។"),
            ("2", "FALSE", "B2 states fast-fashion retailers monetize indigenous designs while indigenous craftspeople remain in poverty without compensation.", "មិនពិត (FALSE) — ក្រុមហ៊ុនសំលៀកបំពាក់ច្រើនតែរកប្រាក់ចំណេញរាប់លានពីក្បាច់រចនាបុរាណ ខណៈសិប្បករជនជាតិដើមមិនទទួលបានប្រាក់កម្រៃ ឬការការពារកម្មសិទ្ធិបញ្ញាឡើយ។"),
            ("3", "TRUE", "B2 and C2 confirm appropriation trivializes sacred spiritual traditions into superficial novelty accessories or party costumes.", "ពិត (TRUE) — ការកេងចំណេញវប្បធម៌បានប្រែក្លាយនិមិត្តសញ្ញាសាសនាដ៏ពិសិដ្ឋទៅជាគ្រឿងតុបតែងម៉ូដសាមញ្ញដោយខ្វះការគោរព។"),
            ("4", "TRUE", "C1 warns that defensive cultural essentialism with rigid ethnic borders risks stifling organic creative syncretism.", "ពិត (TRUE) — ទ្រឹស្តីវិទូខ្លះព្រមានថាការកំណត់ព្រំដែនតឹងរ៉ឹងពេកលើការច្នៃប្រឌិតវប្បធម៌ អាចរារាំងការលាយបញ្ចូលគ្នានៃសិល្បៈបែបច្នៃប្រឌិត។")
        ]
    },
    {
        "num": 85,
        "title": "Ecotourism and Community-Based Conservation",
        "title_kh": "អេកូទេសចរណ៍ និងការអភិរក្សផ្អែកលើសហគមន៍",
        "theme_name": "Tourism & Ecology",
        "qtype": "True / False / Not Given",
        "vocab": [
            ("ecotourism", "noun", "B2", "responsible travel to natural areas that conserves the environment and improves local lives", "អេកូទេសចរណ៍"),
            ("stewardship", "noun", "C1", "the responsible overseeing and protection of natural resources and land", "ការគ្រប់គ្រងថែរក្សាធនធាន"),
            ("encroachment", "noun", "C1", "intrusion on a person's territory or rights; gradual expansion into wild habitat", "ការទន្ទ្រាន"),
            ("concession", "noun", "B2/C1", "a preferential allowance or grant to operate a commercial venture in a protected zone", "សម្បទាន"),
            ("livelihood", "noun", "B2", "a means of securing the necessities of life and income", "ជីវភាពរស់នៅ, មុខរបរ"),
            ("greenwashing", "noun", "C1", "disinformation disseminated by an organization so as to present an environmentally responsible public image", "ការបន្លំធ្វើជាស្រឡាញ់បរិស្ថាន")
        ],
        "b1": """Traditional mass tourism often harms the environment through excessive plastic garbage, noisy jet skis, and giant high-rise hotels that destroy coastal wetlands. In contrast, ecotourism is an exciting travel model that focuses on visiting pristine wilderness areas responsibly. Ecotourists want to experience untouched nature—such as lush rainforests, wildlife reserves, and coral reefs—without leaving harmful footprints behind.

A vital branch of this industry is community-based ecotourism, where rural villagers and indigenous communities own and run the guest lodges, guided hiking tours, and nature excursions themselves. Instead of hunting endangered animals or cutting down ancient timber for quick cash, local residents earn stable salaries as wildlife guides, park rangers, and lodge cooks. In countries like Costa Rica, Kenya, and Cambodia, this model gives rural communities a powerful financial incentive to protect their wild ecosystems.""",
        "b2": """Community-based ecotourism (CBET) integrates biodiversity conservation with sustainable rural poverty alleviation. In conventional tourism paradigms, multinational hotel conglomerates capture up to eighty percent of total tourist expenditures—a phenomenon known as tourism leakage—leaving local communities with degraded ecosystems and low-wage menial employment. CBET disrupts this extractive model by vesting resource ownership, governance, and revenue distribution directly in resident agrarian and indigenous communities.

By creating alternative economic livelihoods tied to habitat preservation, CBET effectively disincentivizes environmentally destructive practices such as illegal logging, slash-and-burn agriculture, and wildlife poaching. In Namibia's communal conservancies and Costa Rica's Monteverde Cloud Forest, local wildlife tracking and hospitality cooperatives have catalyzed remarkable recoveries of endangered megafauna. However, ecotourism ventures must guard against greenwashing, wherein conventional mass-resort developers falsely advertise eco-friendly credentials while accelerating groundwater depletion and habitat fragmentation.""",
        "c1": """The political ecology of community-based ecotourism interrogates whether commodifying wilderness conservation can resolve structural contradictions between ecological preservation and rural economic survival. Proponents celebrate market-based conservation as a win-win neoliberal synergy that monetizes biodiversity through high-yield experiential tourism. By internalizing the financial value of intact ecosystems, rural populations are re-conceptualized as autonomous micro-entrepreneurial ecological stewards.

However, critical geographers contend that ecotourism risks establishing a paternalistic ecological dependency. Exposing vulnerable rural communities to volatile global travel shocks—demonstrated by the catastrophic revenue collapses during international pandemic border closures—jeopardizes both community livelihood stability and long-term conservation funding. Furthermore, ill-conceived ecotourism projects frequently replicate exclusionary fortress conservation, enclosing ancestral commons and restricting traditional subsistence foraging to manufacture pristine, depopulated landscapes tailored to affluent Western tourist expectations.""",
        "c2": """When we walk silently through a primordial rainforest, breathing the damp scent of moss and listening to the symphony of wild birds, our hearts fill with awe. Nature is not an industrial resource to be consumed, nor is it a pristine museum meant only for wealthy sightseers. The forests and rivers of the earth have been cared for by indigenous guardians for millennia, whose ancient songs taught that humanity is not the master of nature, but its humble child.

True ecotourism is a sacred partnership between traveler, local host, and the living earth. When travelers choose to stay in community-run village lodges, eat local vegetables, and listen to the stories of village elders, they help transform tourism into a healing force. Every dollar spent on community-guided conservation protects an ancient tree from the chainsaw and shields an endangered animal from the poacher's snare, proving that human prosperity and wild nature can thrive together in peace.""",
        "questions": [
            ("1", "Community-based ecotourism ensures that tourism revenues and governance remain directly with local communities."),
            ("2", "In conventional mass tourism, local communities consistently retain more than ninety percent of total tourist spending."),
            ("3", "Namibia's communal conservancies have successfully used ecotourism revenues to support endangered wildlife recovery."),
            ("4", "Ecotourism economies are completely immune to global crises, pandemics, and international border closures.")
        ],
        "answers": [
            ("1", "TRUE", "B1 and B2 explain CBET vests resource ownership, revenue, and governance directly in resident communities.", "ពិត (TRUE) — អេកូទេសចរណ៍ផ្អែកលើសហគមន៍ធានាថាប្រាក់ចំណូល និងការគ្រប់គ្រងស្ថិតនៅក្នុងដៃរបស់អ្នកស្រុកផ្ទាល់។"),
            ("2", "FALSE", "B2 states up to 80% of spending leaks out to multinational conglomerates, the opposite of keeping 90%.", "មិនពិត (FALSE) — ក្នុងទេសចរណ៍ធម្មតា ប្រាក់ចំណូលរហូតដល់ ៨០% ធ្លាយចេញទៅក្រុមហ៊ុនបរទេសធំៗ ដោយសហគមន៍មូលដ្ឋានទទួលបានតិចតួចប៉ុណ្ណោះ។"),
            ("3", "TRUE", "B2 highlights Namibia's communal conservancies where ecotourism catalyzed recoveries of endangered megafauna.", "ពិត (TRUE) — តំបន់អភិរក្សសហគមន៍នៅប្រទេសណាមីប៊ី បានប្រើប្រាស់ប្រាក់ចំណូលទេសចរណ៍ដើម្បីស្តារចំនួនសត្វព្រៃកម្រឱ្យកើនឡើងវិញ។"),
            ("4", "FALSE", "C1 states ecotourism exposes communities to volatile travel shocks such as catastrophic collapses during pandemics.", "មិនពិត (FALSE) — សេដ្ឋកិច្ចអេកូទេសចរណ៍ងាយរងគ្រោះខ្លាំងដោយសារវិបត្តិសកល និងការបិទព្រំដែនពេលមានជំងឺរាតត្បាត។")
        ]
    },
    {
        "num": 86,
        "title": "The Preservation of Intangible Cultural Heritage",
        "title_kh": "ការអភិរក្សបេតិកភណ្ឌវប្បធម៌អរូបី",
        "theme_name": "Heritage & Folklore",
        "qtype": "True / False / Not Given",
        "vocab": [
            ("intangible", "adj", "B2/C1", "unable to be touched; not having physical presence", "អរូបី, ដែលមិនអាចប៉ះបាន"),
            ("heritage", "noun", "B1/B2", "property, traditions, or values passed down from previous generations", "បេតិកភណ្ឌ"),
            ("oral history", "noun", "B2", "historical information obtained through interviews with living survivors", "ប្រវត្តិសាស្ត្រផ្ទាល់មាត់"),
            ("artisan", "noun", "B2", "a worker in a skilled trade, especially one that involves making things by hand", "សិប្បករ"),
            ("safeguarding", "noun", "C1", "the act of protecting something valuable from harm or loss", "ការការពារថែរក្សា"),
            ("transmission", "noun", "B2/C1", "the passing on from one person or generation to another", "ការផ្ទេរចំណេះដឹង/បន្តវេន")
        ],
        "b1": """When people think of world heritage, they usually picture famous physical monuments like the Pyramids of Giza, Angkor Wat, or the Roman Colosseum. However, human culture consists of much more than stone temples and brick towers. Just as important is our intangible cultural heritage—the living traditions, oral storytelling, classical dances, music, weaving techniques, and festive rituals that communities pass down from generation to generation.

In 2003, the United Nations organization UNESCO created a special international treaty to safeguard intangible cultural treasures. Examples include the Royal Ballet of Cambodia, flamenco guitar dancing in Spain, and traditional pizza-making in Naples, Italy. Because these traditions exist only inside the memory and hands of living practitioners, they are extremely vulnerable. As young people migrate away to modern cities, elderly master artisans struggle to find apprentices willing to learn these ancient arts.""",
        "b2": """While the 1972 UNESCO World Heritage Convention primarily focused on monumental built architecture and exceptional natural landscapes, the adoption of the 2003 Convention for the Safeguarding of the Intangible Cultural Heritage marked a profound paradigm shift. Intangible heritage encompasses non-material cultural expressions: oral traditions, performing arts, social rituals, festive events, ecological know-how, and traditional artisanal craftsmanship.

The preservation of intangible cultural patrimony presents unique conceptual and methodological challenges. Unlike stone castles or cathedrals, which can be chemically conserved and physically reinforced, intangible heritage exists solely through continuous human enactment and intergenerational transmission. Urbanization, globalization, and digital entertainment have ruptured traditional pedagogical apprenticeships, leaving ancient crafts and musical genres critically vulnerable to extinction. Effective safeguarding strategies must therefore prioritize supporting living cultural practitioners—such as declaring master artisans as 'Living National Treasures' and integrating traditional arts into national school curricula.""",
        "c1": """The safeguarding of intangible cultural heritage occupies a complex ontological tension between dynamic living folklore and static archival museumification. Cultural expressions are inherently malleable, constantly evolving in response to changing sociopolitical conditions and generational sensibilities. Institutional efforts to catalog, codify, and formalize intangible practices on international treaty registries often risk ossifying dynamic cultural traditions into tourist spectacles or state-sanctioned folklore commodities.

Authentic safeguarding must empower practitioners to maintain autonomous control over the evolution of their traditions. This requires establishing robust legal protections against commercial piracy, securing the economic viability of traditional craft professions, and protecting the ecological commons from which artisans harvest raw biological materials—such as specific timber, reeds, and natural mineral dyes. Safeguarding intangible heritage is fundamentally a project of cultural democracy that validates the dignity of vernacular working-class and indigenous knowledge systems.""",
        "c2": """A stone temple can stand for a thousand years in the jungle, but a song dies in an instant if there is no human voice left to sing it. A grand painting can be hung in a palace gallery, but the delicate dance of an ancient loom vanishes forever when the last weaver puts down her wooden shuttle. Intangible heritage is the breathing, pulsing soul of humanity: the jokes our ancestors told around campfires, the lullabies mothers sang to soothe crying babies, and the sacred prayers spoken to the rising sun.

To preserve an ancient dance or craft is not an exercise in nostalgic sentimentality; it is a sacred act of civilizational memory. We do not honor our ancestors by turning their rituals into frozen museum displays for foreign tourists. We honor them by dancing their steps, singing their verses, and placing the tools of creation into the eager hands of our children, ensuring that the living song of our people echoes down into the centuries to come.""",
        "questions": [
            ("1", "The 2003 UNESCO Convention was created specifically to safeguard intangible cultural heritage."),
            ("2", "Intangible cultural heritage consists entirely of physical monuments, stone castles, and natural parks."),
            ("3", "The Royal Ballet of Cambodia and traditional Neapolitan pizza-making are recognized intangible cultural practices."),
            ("4", "Experts note that intangible heritage exists solely through ongoing human practice and generational transmission.")
        ],
        "answers": [
            ("1", "TRUE", "B1 and B2 state UNESCO created a dedicated treaty in 2003 to safeguard intangible cultural heritage.", "ពិត (TRUE) — អនុសញ្ញាអង្គការយូណេស្កូឆ្នាំ ២០០៣ ត្រូវបានបង្កើតឡើងជាពិសេសដើម្បីការពារបេតិកភណ្ឌវប្បធម៌អរូបី។"),
            ("2", "FALSE", "B1 and B2 contrast intangible heritage with physical monuments, explaining it consists of oral traditions, dances, and crafts.", "មិនពិត (FALSE) — បេតិកភណ្ឌអរូបីមិនមែនជាប្រាសាទថ្ម ឬសំណង់រូបវន្តឡើយ ប៉ុន្តែជាប្រពៃណី ចម្រៀង របាំ និងចំណេះដឹងដែលផ្ទេរតាមរយៈមនុស្ស។"),
            ("3", "TRUE", "B1 cites the Royal Ballet of Cambodia and Neapolitan pizza-making as recognized intangible cultural examples.", "ពិត (TRUE) — របាំព្រះរាជទ្រព្យកម្ពុជា និងការធ្វើភីហ្សាប្រពៃណីនៅទីក្រុងណាបផល គឺជាបេតិកភណ្ឌវប្បធម៌អរូបីដ៏ល្បីល្បាញ។"),
            ("4", "TRUE", "B2 states intangible heritage exists solely through continuous human enactment and intergenerational transmission.", "ពិត (TRUE) — អ្នកជំនាញបញ្ជាក់ថាបេតិកភណ្ឌអរូបីអាចរស់នៅបានលុះត្រាតែមានការអនុវត្តផ្ទាល់ និងការផ្ទេរចំណេះដឹងពីជំនាន់មួយទៅជំនាន់មួយ។")
        ]
    },
    {
        "num": 87,
        "title": "Globalization and the Homogenization of Food Cultures",
        "title_kh": "សកលភាវូបនីយកម្ម និងការរួមបញ្ចូលគ្នានៃវប្បធម៌ម្ហូបអាហារ",
        "theme_name": "Culture & Food",
        "qtype": "True / False / Not Given",
        "vocab": [
            ("homogenization", "noun", "C1", "the process of making things uniform or similar, reducing diversity", "ការធ្វើឱ្យដូចគ្នា, ឯកសណ្ឋានភាព"),
            ("culinary", "adj", "B2", "of or for cooking or the kitchen", "ផ្នែកធ្វើម្ហូប, ផ្នែកម្ហូបអាហារ"),
            ("standardization", "noun", "B2/C1", "the process of making something conform to a standard", "ស្ដង់ដារភាវូបនីយកម្ម"),
            ("dietary", "adj", "B2", "relating to food or the diet", "ដែលទាក់ទងនឹងរបបអាហារ"),
            ("monoculture", "noun", "C1", "the agricultural practice of growing a single crop or uniform culture", "កសិកម្មដំណាំទោល, វប្បធម៌ទោល"),
            ("gastronomy", "noun", "C1/C2", "the practice or art of choosing, cooking, and eating good food", "សិល្បៈនៃការចម្អិន និងទទួលទានអាហារ")
        ],
        "b1": """For centuries, what people ate depended entirely on their regional geography, local climate, and inherited family traditions. In Mediterranean villages, people enjoyed fresh olive oil, tomatoes, and grilled fish, while in Southeast Asia, families prepared aromatic soups flavored with lemongrass, ginger, and wild herbs. Every valley, island, and town possessed its own distinct culinary identity rooted in local agriculture.

Today, however, the rapid rise of economic globalization and giant multinational fast-food corporations is transforming our plates. Bright corporate logos for hamburgers, fried chicken, and sugary soft drinks now dominate street corners from Tokyo to London, Bangkok, and Nairobi. This worldwide spread of standardized, ultra-processed food creates a serious nutritional and cultural crisis. Traditional local markets are disappearing, and younger generations are losing their appetite for ancestral dishes, leading to skyrocketing rates of obesity, heart disease, and diabetes.""",
        "b2": """The globalization of the modern agrifood system has triggered an unprecedented dietary transition characterized by the worldwide homogenization of culinary cultures. Multinational food conglomerates distribute ultra-processed, calorie-dense, and nutrient-poor commodities packaged in uniform corporate branding across every continent. This corporate food regime displaces regionally adapted agroecological food systems, replacing culinary diversity with what sociologists term the 'McDonaldization' of global dining.

The systemic ramifications of culinary homogenization are both physiological and ecological. Physiologically, the transition away from nutrient-dense traditional diets toward mass-produced palm oils, refined sugars, and hydrogenated fats has precipitated an explosion in global non-communicable lifestyle illnesses. Ecologically, global food standardization relies upon industrial agricultural monocultures—predominantly genetically uniform corn, soy, and wheat—that drive catastrophic deforestation and biodiversity loss. In response, culinary resistance movements, such as the international 'Slow Food' movement, actively defend heritage seed varieties, artisanal fermentation, and local gastronomic sovereignty.""",
        "c1": """The erosion of regional foodways represents a quintessential manifestation of globalized corporate imperialism. Food is never merely a biological fuel; it is a profoundly social, liturgical, and ecological semiotic system through which human communities encode their relationship to territory, season, and ancestry. By financializing agriculture into global commodity supply chains optimized exclusively for shelf-life stability and corporate profit margins, capitalist globalization severs food from its ecological terroir.

Reclaiming gastronomic sovereignty requires confronting the structural hegemony of transnational agribusiness monopolies. Public policy must move beyond consumer-centric lifestyle choices to dismantle agricultural subsidies that artificially cheapen industrial commodities while penalizing diversified regenerative farming. Revitalizing regional food systems entails supporting municipal farmers' markets, mandating local procurement in public school lunch programs, and safeguarding ancestral culinary techniques as invaluable intangible heritage essential to human ecological resilience.""",
        "c2": """To sit at a table with an ancient dish—a steaming bowl of noodle broth simmering with mountain herbs, or a loaf of crusty sourdough bread baked from heirloom grains—is to taste the soil, the rain, and the quiet labor of generations. Food is the most intimate conversation we share with the earth and with each other. It is the laughter of grandmother's kitchen, the celebration of autumn harvest, and the comforting medicine of maternal love.

When a city trades its lively open-air markets and family-run noodle stalls for sterile plastic drive-throughs selling engineered frozen burgers, it sells its cultural birthright for a mess of pottage. We must refuse to let the global machine flatten the joyful, spicy, fragrant banquet of human culinary diversity into a grey, standardized paste. To cook a traditional recipe with fresh local ingredients is a glorious, radical act of love—a celebration that keeps our bodies healthy, our farmers proud, and our souls free.""",
        "questions": [
            ("1", "The widespread expansion of global fast food has contributed to the dietary homogenization of cultures."),
            ("2", "The 'Slow Food' movement actively campaigns to replace traditional local dishes with factory-made fast food."),
            ("3", "The shift toward standardized, ultra-processed diets is linked to rising rates of diabetes and heart disease."),
            ("4", "Industrial food standardization relies heavily on massive agricultural monocultures like corn and soy.")
        ],
        "answers": [
            ("1", "TRUE", "B1 and B2 state multinational fast food has produced a worldwide homogenization of culinary cultures.", "ពិត (TRUE) — ការរីករាលដាលនៃអាហាររហ័សសកលបានធ្វើឱ្យវប្បធម៌ម្ហូបអាហារតាមតំបន់ក្លាយជាដូចគ្នា និងបាត់បង់ភាពសម្បូរបែប។"),
            ("2", "FALSE", "B2 states the Slow Food movement defends heritage seeds and artisanal cooking, opposing industrial food.", "មិនពិត (FALSE) — ចលនា 'Slow Food' ការពារគ្រាប់ពូជបុរាណ និងមុខម្ហូបប្រពៃណី មិនមែនផ្សព្វផ្សាយអាហារកែច្នៃរហ័សឡើយ។"),
            ("3", "TRUE", "B1 and B2 link the transition to ultra-processed foods directly to rising rates of diabetes, obesity, and heart disease.", "ពិត (TRUE) — ការងាកមកទទួលទានអាហារកែច្នៃស្ដង់ដារបង្កឱ្យមានការកើនឡើងនៃជំងឺមិនឆ្លង ដូចជា ជំងឺទឹកនោមផ្អែម និងបេះដូង។"),
            ("4", "TRUE", "B2 states global food standardization relies upon industrial agricultural monocultures like corn, soy, and wheat.", "ពិត (TRUE) — ឧស្សាហកម្មអាហារកែច្នៃសកលពឹងផ្អែកលើដំណាំកសិកម្មទោលខ្នាតធំ ដូចជា ពោត សណ្តែកសៀង និងស្រូវសាលី។")
        ]
    },
    {
        "num": 88,
        "title": "Public Broadcasting and National Cultural Identity",
        "title_kh": "ការផ្សាយសាធារណៈ និងអត្តសញ្ញាណវប្បធម៌ជាតិ",
        "theme_name": "Media & National Identity",
        "qtype": "True / False / Not Given",
        "vocab": [
            ("broadcasting", "noun", "B1/B2", "the transmission of radio or television programs for public reception", "ការផ្សាយតាមវិទ្យុ ឬទូរទស្សន៍"),
            ("impartiality", "noun", "C1", "the quality of not favoring one side over another; fairness; neutrality", "អព្យាក្រឹតភាព"),
            ("civic", "adj", "B2", "relating to a city, town, or the duties and activities of citizens", "ខាងពលរដ្ឋ, ផ្នែកសង្គម"),
            ("polarization", "noun", "C1", "division into two sharply contrasting groups or sets of opinions", "ការបែកខ្ញែកទស្សនៈ, បន្ទាត់នយោបាយ"),
            ("sensationalism", "noun", "C1", "the use of exciting or shocking stories to provoke public interest", "ការផ្សាយបែបភ្ញាក់ផ្អើល, សេនសេសិន"),
            ("solvency", "noun", "C2", "the ability to pay all one's debts; long-term financial viability", "លទ្ធភាពទូទាត់បំណុល, ស្ថិរភាពហិរញ្ញវត្ថុ")
        ],
        "b1": """In the twentieth century, democratic nations created public broadcasting networks—such as the BBC in the United Kingdom, PBS in the United States, and NHK in Japan. Unlike private commercial television stations that make money by selling advertisements, public broadcasters are funded by public license fees or government grants. Because they do not need to chase commercial ratings, their primary mission is to educate, inform, and entertain all citizens fairly.

Public broadcasters play a crucial role in creating shared national identity and supporting democracy. They produce high-quality news documentaries, broadcast in-depth investigations, and invest in children's educational programs like Sesame Street. Furthermore, public channels support homegrown arts, drama, and regional cultural celebrations that private commercial stations often ignore because they are not profitable enough. During national emergencies and natural disasters, citizens rely heavily on public stations for accurate, life-saving information.""",
        "b2": """Public service broadcasting (PSB) was established on the democratic principle that access to impartial news, informative cultural programming, and rigorous civic discourse is a public good, not a commercial commodity. Broadcasters such as Britain's BBC, Japan's NHK, and Germany's ARD operate under statutory charters mandating universal geographic coverage, editorial independence, and high journalistic standards free from partisan government influence and corporate commercial advertisers.

In contemporary digital media landscapes dominated by algorithmic social platforms and hyper-partisan cable networks, public broadcasters provide a critical democratic anchor. Commercial media algorithms systematically reward sensationalism, rage, and ideological polarization to maximize user screen engagement and ad revenues. In contrast, well-funded public broadcasters have been empirically demonstrated to foster higher civic knowledge, lower partisan hostility, and greater democratic trust. However, public broadcasters currently face severe funding cuts, political interference from populist governments, and intense competition from multinational streaming giants.""",
        "c1": """The epistemic crisis facing contemporary liberal democracies underscores the indispensable democratic necessity of public service media. Private communicative ecosystems are driven by surveillance capitalism, which weaponizes affective polarization and algorithmic clickbait to harvest user attention for corporate profit. This algorithmic fragmentation destroys the shared informational commons essential for deliberative democracy, dividing citizens into isolated, radicalized echo chambers susceptible to disinformation campaigns.

Public broadcasters function as an epistemic firewall, curating verified factual reporting and broadcasting nuanced national cultural programming that bridges deep social fractures. Nevertheless, public broadcasters must continuously prove their institutional legitimacy in a multi-platform streaming era. To survive, they must transition from legacy broadcast models into dynamic digital public spaces that champion investigative journalism, elevate marginalized cultural voices, and maintain absolute independence from executive political retaliation and budgetary extortion.""",
        "c2": """In an age of endless digital noise, screaming political headlines, and viral outrage engineered by algorithms to turn brother against brother, the quiet voice of truthful public journalism is like a lighthouse in a stormy sea. A democratic nation cannot survive if its citizens cannot even agree on basic facts: on whether the bridge is safe, on whether the water is clean, or on what truly happened in the halls of power.

Public broadcasting is the town square of a free society: a space belonging to everyone, where the poor and the rich receive the exact same quality of truth. It is where we share great stories, celebrate our national poets, and ask hard questions of our leaders without fear or favor. To dismantle our public broadcasters to save a few coins or avoid political scrutiny is to blindfold our democracy and leave our cultural soul in the hands of foreign advertisers.""",
        "questions": [
            ("1", "Public service broadcasters are funded primarily to maximize commercial corporate advertising revenue."),
            ("2", "The BBC in Britain and NHK in Japan operate under mandates that require universal service and editorial independence."),
            ("3", "Empirical studies show well-funded public broadcasters contribute to higher civic knowledge and lower partisan hostility."),
            ("4", "Public broadcasters are currently facing financial and political pressures, as well as competition from streaming platforms.")
        ],
        "answers": [
            ("1", "FALSE", "B1 and B2 state public broadcasters are funded by license fees or grants to serve citizens, not commercial ad profits.", "មិនពិត (FALSE) — ស្ថាប័នផ្សាយសាធារណៈត្រូវបានបង្កើតឡើងដើម្បីបម្រើពលរដ្ឋដោយអព្យាក្រឹត មិនមែនដើម្បីស្វែងរកប្រាក់ចំណេញពីពាណិជ្ជកម្មឡើយ។"),
            ("2", "TRUE", "B2 mentions the BBC and NHK operate under statutory charters requiring universal coverage and editorial independence.", "ពិត (TRUE) — ស្ថាប័ន BBC នៅអង់គ្លេស និង NHK នៅជប៉ុន មានធម្មនុញ្ញច្បាប់ចែងឱ្យបំពេញការងារប្រកបដោយឯករាជ្យភាព និងវិជ្ជាជីវៈសារព័ត៌មានខ្ពស់។"),
            ("3", "TRUE", "B2 states well-funded public broadcasters foster higher civic knowledge, lower hostility, and greater democratic trust.", "ពិត (TRUE) — ការស្រាវជ្រាវបង្ហាញថាប្រព័ន្ធផ្សព្វផ្សាយសាធារណៈជួយបង្កើនការយល់ដឹងរបស់ពលរដ្ឋ និងកាត់បន្ថយភាពតានតឹងផ្នែកនយោបាយ។"),
            ("4", "TRUE", "B2 and C1 state public broadcasters face severe budget cuts, political pressure, and fierce competition from streaming services.", "ពិត (TRUE) — ប្រព័ន្ធផ្សព្វផ្សាយសាធារណៈកំពុងប្រឈមនឹងការកាត់បន្ថយថវិកា ការជ្រៀតជ្រែកនយោបាយ និងការប្រកួតប្រជែងពីសេវាស្ទ្រីមមីងអន្តរជាតិ។")
        ]
    },
    {
        "num": 89,
        "title": "Adaptive Conservation of Archaeological Sites",
        "title_kh": "ការអភិរក្សសម្របខ្លួននៃតំបន់បុរាណវិទ្យា",
        "theme_name": "Archaeology & Conservation",
        "qtype": "True / False / Not Given",
        "vocab": [
            ("conservation", "noun", "B2", "the preservation and careful management of historic sites and nature", "ការអភិរក្ស"),
            ("deterioration", "noun", "C1", "the process of becoming progressively worse or decaying over time", "ការទ្រុឌទ្រោម, ការរេចរឹល"),
            ("archaeological", "adj", "B2", "relating to the study of human history through excavation of sites", "ខាងបុរាណវិទ្យា"),
            ("in situ", "adj/adv", "C1/C2", "in its original place or situated in its natural position", "នៅកន្លែងដើម (ឡាតាំង)"),
            ("microclimate", "noun", "C1", "the climate of a very small or restricted area", "អាកាសធាតុខ្នាតតូច"),
            ("non-invasive", "adj", "B2/C1", "not requiring entering, cutting, or damaging the original fabric", "ដែលមិនប៉ះពាល់/មិនបំផ្លាញដើម")
        ],
        "b1": """Ancient ruins and archaeological monuments—such as Pompeii in Italy, Petra in Jordan, and the temples of Angkor in Cambodia—provide stunning windows into the daily lives, art, and engineering of our ancestors. However, once buried stone walls and delicate plaster carvings are excavated by archaeologists and exposed to the open air, they immediately begin to decay. Rainwater, blazing sun, desert winds, and humid jungle climates rapidly erode ancient stone masonry.

To safeguard these irreplaceable monuments, modern conservation scientists practice adaptive conservation. Instead of rebuilding ruined temples with modern concrete or painting over old stones, conservators focus on stabilizing and protecting what survives in its original location, a principle called preservation in situ. Conservators now construct protective canopy shelters that regulate humidity, install drainage pipes to divert flash floods, and use laser scanners to monitor microscopic wall cracks without touching the delicate ancient stone.""",
        "b2": """Archaeological conservation has evolved from invasive aesthetic restoration toward sophisticated preventive material science. Historical interventions often caused catastrophic unintended damage: nineteenth-century excavators frequently used caustic acid washes, sandblasting, and rigid Portland cement mortars that trapped moisture inside porous ancient limestone and sandstone blocks, causing explosive subterranean fracturing during seasonal freeze-thaw or dry-wet cycles.

Contemporary conservation protocols, codified in international charters like the Venice and Burra Charters, strictly mandate minimum intervention and material reversibility. Conservators prioritize in situ preservation, deploying non-invasive diagnostic technologies such as ground-penetrating radar (GPR), drone LiDAR mapping, and multispectral imaging to investigate subsurface structures without disturbing stratigraphic contexts. Furthermore, in response to climate change, engineers design climate-responsive protective enclosures that stabilize subterranean microclimates and buffer fragile ruins against extreme weather anomalies.""",
        "c1": """The philosophical paradigm governing archaeological conservation reflects an epistemological humility that recognizes the irreversible material fragility of cultural heritage. Nineteenth-century romantic restoration sought to reconstruct an idealized, fictive completeness, often obliterating authentic historical layers in pursuit of aesthetic perfection. Modern heritage science, by contrast, conceptualizes the ruin not as an architectural deficiency to be corrected, but as a palimpsest of historical time whose physical decay must be managed with scientific precision.

Adaptive conservation requires balancing the thermodynamic inevitability of material entropy against the public imperative for educational accessibility. Overzealous physical interventions must be replaced by sophisticated thermodynamic environmental conditioning, passive seismic dampening, and biological bioconsolidation using calcite-precipitating bacteria. Conservation is ultimately an ethical pact with the future: an obligation to preserve the material authenticity of human history so that future generations may interpret its meanings with analytical technologies far superior to our own.""",
        "c2": """When we stand before an ancient stone temple whose carved pillars have been worn smooth by a thousand years of rain and wind, we are humbled by the passage of time. A ruined monument is not a broken toy waiting to be glued back together; it is a sacred poem written in stone, bearing the scars of wars, earthquakes, and time. To slap modern cement across an ancient carved face in order to make it look 'new' is to erase the very history that gives the stone its soul.

True conservation is an act of gentle, patient love. It is the skilled scientist who spends weeks brushing away a single speck of moss with a camel-hair brush, who studies the breath of the wind through ancient doorways, and who builds a quiet roof over a fragile mosaic to shelter it from the burning sun. In preserving ancient stones just as they are, we honor the craftsmen who carved them and remind ourselves of our own fleeting place in the grand stream of time.""",
        "questions": [
            ("1", "Excavating buried archaeological ruins can immediately accelerate their physical decay due to weather exposure."),
            ("2", "Nineteenth-century restorations frequently utilized Portland cement which inadvertently damaged ancient porous stone."),
            ("3", "Modern heritage conventions encourage complete and irreversible structural overhauls of ancient monuments."),
            ("4", "Non-invasive technologies like LiDAR and ground-penetrating radar permit structural analysis without excavation.")
        ],
        "answers": [
            ("1", "TRUE", "B1 states once buried ruins are excavated and exposed to the elements, they immediately begin to decay.", "ពិត (TRUE) — នៅពេលកកាយវត្ថុបុរាណចេញពីក្រោមដី ការប៉ះផ្ទាល់នឹងអាកាសធាតុ ទឹកភ្លៀង និងពន្លឺថ្ងៃ ធ្វើឱ្យថ្មរេចរឹលកាន់តែលឿន។"),
            ("2", "TRUE", "B2 explains rigid Portland cement trapped moisture inside porous stone, causing explosive subterranean fracturing.", "ពិត (TRUE) — ការប្រើប្រាស់ស៊ីម៉ងត៍ Portland ក្នុងសតវត្សរ៍ទី ១៩ បានបង្កការខូចខាតយ៉ាងធ្ងន់ធ្ងរដល់ថ្មបុរាណដោយសារការដក់សំណើម។"),
            ("3", "FALSE", "B2 states international charters strictly mandate minimum intervention and material reversibility, not irreversible overhauls.", "មិនពិត (FALSE) — អនុសញ្ញាបេតិកភណ្ឌសម័យទំនើបតម្រូវឱ្យមានការអន្តរាគមន៍តិចបំផុត និងអាចកែប្រែឡើងវិញបាន មិនមែនផ្លាស់ប្តូរទាំងស្រុងឡើយ។"),
            ("4", "TRUE", "B2 confirms non-invasive technologies like GPR and drone LiDAR investigate structures without disturbing soil strata.", "ពិត (TRUE) — បច្ចេកវិទ្យាដូចជា LiDAR និងរ៉ាដាស្កេនដី អាចវិភាគសំណង់បុរាណវិទ្យាបានដោយមិនបាច់ជីកកកាយបំផ្លាញដីឡើយ។")
        ]
    },
    {
        "num": 90,
        "title": "Dark Tourism and the Ethics of Commemoration",
        "title_kh": "ទេសចរណ៍ទីតាំងសោកនាដកម្ម និងសីលធម៌នៃការចងចាំ",
        "theme_name": "Tourism & Ethics",
        "qtype": "True / False / Not Given",
        "vocab": [
            ("dark tourism", "noun", "B2/C1", "tourism involving travel to places historically associated with death and tragedy", "ទេសចរណ៍ទីតាំងសោកនាដកម្ម"),
            ("commemoration", "noun", "C1", "remembrance, typically expressed in a ceremony or memorial", "ការរំលឹកវិញ្ញាណក្ខន្ធ/ការចងចាំ"),
            ("voyeurism", "noun", "C2", "the practice of gaining pleasure from watching others' suffering or private distress", "ការសម្លឹងមើលការឈឺចាប់របស់អ្នកដទៃដើម្បីសប្បាយ"),
            ("somber", "adj", "B2/C1", "dark, gloomy, or solemn in character; expressing serious sadness", "ដែលស្ងប់ស្ងាត់សោកសៅ"),
            ("sanctity", "noun", "C1", "the state or quality of being holy, sacred, or of ultimate importance", "ភាពពិសិដ្ឋ"),
            ("commodification", "noun", "C1", "the action of treating something sacred as a mere commercial commodity", "ទំនិញភាវូបនីយកម្ម")
        ],
        "b1": """While most vacationers look for sunny tropical beaches or exciting amusement parks, millions of tourists choose to visit places linked to terrible human tragedies, wars, and suffering. Known as dark tourism, this travel phenomenon includes visiting Nazi concentration camps like Auschwitz in Poland, the Tuol Sleng Genocide Museum in Cambodia, the 9/11 Memorial in New York, and the nuclear ruins of Chernobyl in Ukraine.

People visit these somber locations for many profound reasons: to honor innocent victims, understand the brutal realities of history, and pay solemn respect to human resilience. However, dark tourism creates immense ethical challenges. In recent years, memorial curators have expressed anger over tourists taking smiling, disrespectful selfies or commercial vendors selling ice cream outside mass execution sites. Memorial directors work hard to ensure visitors maintain quiet, reverent behavior so that historic tragedy is never turned into cheap entertainment.""",
        "b2": """Dark tourism—academically conceptualized as thanatourism—encompasses the visitation of memorial sites, battlefields, mass atrocity locations, and disaster zones. From the killing fields of the Cambodian genocide and the Hiroshima Peace Memorial to the ruins of Pompeii, these spaces exist at the delicate intersection of historical pedagogy, collective grief, and commercial travel. Proponents argue that thanatourism serves an essential pedagogical imperative, fostering historical empathy, counteracting historical denialism, and generating tourist revenues dedicated to site preservation.

However, the commercialization of atrocity sites precipitates profound ethical transgressions. When sacred commemorative spaces are commodified within mass tourism itineraries, they risk degenerating into sensationalist voyeurism. The proliferation of irreverent smartphone photography, commercial souvenir kiosks, and theatrical tourist staging desecrates the sanctity of mass graves and causes acute distress to surviving victim communities. Curators must navigate these tensions by enforcing strict behavioral codes, curating somber interpretive exhibitions, and prioritizing victim commemoration above tourist entertainment.""",
        "c1": """The philosophical critique of thanatourism interrogates the delicate dialectic between ethical memorialization and morbid consumer voyeurism. Under the gaze of contemporary mass culture, spaces of incomprehensible human catastrophe are perpetually threatened by commodification, which converts unquantifiable trauma into marketable tourist spectacles. This consumption of atrocity risks desensitizing the public, packaging historical horrors as consumable aesthetic thrills while domesticating the radical political critique that genuine commemoration ought to provoke.

Transforming dark tourism into transformative moral witness requires radical institutional de-commercialization. Curatorial authorities must actively subvert voyeuristic impulses by designing reflective memorial architectures that center the lived testimony and agency of victims rather than the morbid machinery of their executioners. Commemoration must reject sanitized historical reconciliation and instead mobilize collective memory as an urgent moral warning against the recurring perils of fascism, dehumanization, and state terror.""",
        "c2": """There are places on this earth where the ground is so steeped in human tears and innocent blood that we should only walk upon them in bare feet and hushed silence. When we stand beneath the razor wire of a concentration camp, look upon the mass graves of a genocide memorial, or gaze at the ruined wall of an atomic explosion, our hearts should shatter in profound grief. These places do not belong to travel agencies, souvenir sellers, or Instagram influencers; they belong to the martyrs whose lives were cruelly extinguished.

To visit a site of tragedy is not a vacation excursion; it is a sacred pilgrimage of moral reckoning. When we look into the haunting eyes of victims pictured on museum walls, their silent gaze demands an answer from each of us: What kind of human being are you? What will you do to protect the vulnerable in your own time? True commemoration requires us to leave these sacred spaces not entertained, but transformed—vowing with our whole lives that such darkness will never rise again.""",
        "questions": [
            ("1", "Dark tourism involves traveling to destinations historically associated with death, war, and tragedy."),
            ("2", "Memorial directors encourage visitors to pose for playful, smiling selfies directly in front of execution walls."),
            ("3", "Tuol Sleng Genocide Museum and the Hiroshima Peace Memorial are prominent examples of dark tourism sites."),
            ("4", "Ethicists emphasize that memorial spaces must prioritize victim dignity and pedagogical remembrance over commercial profit.")
        ],
        "answers": [
            ("1", "TRUE", "B1 and B2 define dark tourism as travel to sites associated with tragedy, genocide, and human disasters.", "ពិត (TRUE) — ទេសចរណ៍ទីតាំងសោកនាដកម្ម (Dark tourism) គឺជាការធ្វើដំណើរទៅកាន់ទីតាំងប្រវត្តិសាស្ត្រដែលទាក់ទងនឹងសង្គ្រាម និងសោកនាដកម្ម។"),
            ("2", "FALSE", "B1 and B2 state memorial curators are angered by disrespectful selfies, demanding quiet, reverent behavior.", "មិនពិត (FALSE) — អ្នកគ្រប់គ្រងទីតាំងចងចាំថ្កោលទោសការថតរូបសែលហ្វីលែបខាយនៅមុខទីតាំងពិឃាដ ហើយទាមទារឱ្យមានការគោរពយ៉ាងម៉ឺងម៉ាត់។"),
            ("3", "TRUE", "B1 and B2 explicitly cite Tuol Sleng in Cambodia and Hiroshima in Japan as prominent commemorative sites.", "ពិត (TRUE) — សារមន្ទីរប្រល័យពូជសាសន៍ទួលស្លែងនៅកម្ពុជា និងស្តូបសន្តិភាពហ៊ីរ៉ូស៊ីម៉ានៅជប៉ុន គឺជាឧទាហរណ៍ជាក់ស្តែងនៃទីតាំងចងចាំប្រវត្តិសាស្ត្រ។"),
            ("4", "TRUE", "B2 and C1 stress the importance of prioritizing victim commemoration and dignity over commercial entertainment.", "ពិត (TRUE) — អ្នកឯកទេសសីលធម៌សង្កត់ធ្ងន់ថាទីតាំងសោកនាដកម្មត្រូវតែផ្តល់អាទិភាពដល់សេចក្តីថ្លៃថ្នូររបស់ជនរងគ្រោះ និងការរៀនសូត្រជាជាងផលប្រយោជន៍ពាណិជ្ជកម្ម។")
        ]
    }
]

write_theme_file(
    filename="ielts_09_culture_globalisation.md",
    theme_title="Culture, Heritage & Global Tourism (Topics 81–90)",
    theme_kh="វប្បធម៌ បេតិកភណ្ឌ និងទេសចរណ៍សកល (ប្រធានបទ ៨១ ដល់ ៩០)",
    theme_desc="This volume presents 10 comprehensive academic reading topics on Overtourism, Indigenous Language Revitalization, Museum Ethics and Artifact Repatriation, Cultural Appropriation vs Appreciation, Ecotourism, Intangible Cultural Heritage, Culinary Homogenization, Public Broadcasting, Adaptive Archaeological Conservation, and Dark Tourism. Each topic contains an authentic IELTS/CEFR reading passage adapted across four CEFR levels (B1, B2, C1, C2), key academic vocabulary with Khmer translations, 4 mock exam questions, and full explanatory walkthroughs.",
    topics=TOPICS
)
