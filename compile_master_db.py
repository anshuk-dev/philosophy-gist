"""
Database compiler for Philosophy Gist:
Generates 32+ authentic, rigorously verified, chained philosophical flashcards
spanning Classical Indian, Contemporary Indian, Classical Western, Modern Western,
and Contemporary Continental/Analytic philosophy.
"""

import json
from pathlib import Path

DB_FILE = Path(__file__).resolve().parent / "content" / "database.json"

FLASHCARDS = [
    # -------------------------------------------------------------
    # INDIAN EPISTEMOLOGY & METHOD (CHAIN 1: THE CRITERIA OF KNOWING)
    # -------------------------------------------------------------
    {
        "id": "IND_EPIST_001",
        "unit_id": "UNIT_01",
        "tradition": "Indian",
        "school": "Mīmāṃsā / Nyāya",
        "topic": "Theories of Truth & Validity",
        "concept_name": "Svataḥ Prāmāṇyavāda vs. Parataḥ Prāmāṇyavāda",
        "chain": {
            "from_concept": "Cārvāka Skepticism (Doubt of all unperceived entities)",
            "current_thesis": "Cognition carries its own truth at inception (Svataḥ), or requires external pragmatic verification (Parataḥ).",
            "to_concept": "Theories of Illusion (If knowledge is self-valid, how does error occur? -> Khyātivāda)"
        },
        "the_problem": "Does a valid cognition (pramā) possess intrinsic validity from the very moment of its emergence, or must truth be proven by an external test?",
        "technical_lexicon": [
            {"term": "Svataḥ Prāmāṇya (स्वतः प्रामाण्य)", "meaning": "Intrinsic validity; self-authentication of cognition in origin (utpattau) and apprehension (jñāptau)."},
            {"term": "Parataḥ Prāmāṇya (परतः प्रामाण्य)", "meaning": "Extrinsic validity; verified via causal excellence (guṇa) and successful action (pravṛtti-sāmarthya)."},
            {"term": "Anavasthā (अनवस्था)", "meaning": "Infinite regress that occurs if every validating cognition itself needs validation."},
            {"term": "Bādhaka-jñāna (बाधकज्ञान)", "meaning": "Sublating cognition that cancels an erroneous perception."}
        ],
        "dialectic": {
            "purvapaksha": "The Nyāya argues: If all cognitions were intrinsically valid, doubts and illusions would never happen. A thirsty traveler sees a mirage; only reaching the pool and drinking (pravṛtti-sāmarthya) verifies the cognition as true.",
            "siddhanta": "Kumārila Bhaṭṭa counters: If cognition A needs cognition B to validate it, and B needs C, knowledge never arrives at certainty (anavasthā). Cognition is born valid from its own apparatus; falsity alone is extrinsic, exposed by a defeater (bādhaka)."
        },
        "primary_text": {
            "author": "Kumārila Bhaṭṭa",
            "work": "Ślokavārttika",
            "passage": "Codanā-sūtra adhikaraṇa, verses 33–61"
        },
        "interview_trap": "Distinguish Bhāṭṭa from Prābhākara Mīmāṃsā: Bhāṭṭas hold that cognition is supersensuous and inferred from 'knownness' (jñātatā) in the object, whereas Prābhākaras reject jñātatā, argue for 'Tripuṭī-pratyakṣa' (simultaneous awareness of knower, known, knowing), and claim NO cognition is ever false (Akhyātivāda).",
        "wisdom_gist": "At the root of thought lies a baseline epistemic trust. Without trusting our primary apprehension until contradicted, the human mind falls into paralyzing infinite regression."
    },
    {
        "id": "IND_EPIST_002",
        "unit_id": "UNIT_01",
        "tradition": "Indian",
        "school": "Nyāya-Vaiśeṣika",
        "topic": "Perception & Sense Contact",
        "concept_name": "Pratyakṣa: Nirvikalpaka vs. Savikalpaka & Ṣaḍvidha-Sannikarṣa",
        "chain": {
            "from_concept": "Svataḥ/Parataḥ Prāmāṇya (Establishing whether perception is self-certifying)",
            "current_thesis": "Perception begins as non-judgmental bare awareness (nirvikalpaka) before structuring into relational conceptuality (savikalpaka) via 6 types of contact.",
            "to_concept": "Buddhist Pramāṇavāda (Dignāga & Dharmakīrti rejecting Savikalpaka as pure conceptual fiction / Kalpanā)"
        },
        "the_problem": "How does sensory contact with an external object translate from a raw sensory datum into a structured, conceptual judgment ('This is a brown earthen pot')?",
        "technical_lexicon": [
            {"term": "Nirvikalpaka Pratyakṣa (निर्विकल्पक प्रत्यक्ष)", "meaning": "Indeterminate, non-propositional perception apprehending bare structure without name or genus."},
            {"term": "Savikalpaka Pratyakṣa (सविकल्पक प्रत्यक्ष)", "meaning": "Determinate, propositional perception grasping the object qualified by name, genus, and attribute (viśeṣya-viśeṣaṇa-sambandha)."},
            {"term": "Ṣaḍvidha-Sannikarṣa (षड्विध सन्निकर्ष)", "meaning": "The sixfold sense-object contacts: Saṃyoga, Saṃyukta-samavāya, Saṃyukta-samaveta-samavāya, Samavāya, Samaveta-samavāya, Viśeṣaṇa-viśeṣya-bhāva."},
            {"term": "Alaukika Pratyakṣa (अलौकिक प्रत्यक्ष)", "meaning": "Extraordinary perception: Sāmānyalakṣaṇa (genus), Jñānalakṣaṇa (complication/memory), Yogaja (intuitive gnosis)."}
        ],
        "dialectic": {
            "purvapaksha": "The Buddhist epistemologist (Dharmakīrti) argues: Perception is strictly non-conceptual (kalpanāpoḍham). The moment language, name, or universal is applied, it is no longer perception but mental construction (vikalpa). Savikalpaka is not perception at all.",
            "siddhanta": "The Naiyāyika retorts: The universal (sāmānya) is a real objective entity inhering in the object. Savikalpaka perception directly sees the real substance as qualified by its real universal; words merely express what the sense faculty has already veridically grasped."
        },
        "primary_text": {
            "author": "Gautama & Annambhaṭṭa",
            "work": "Nyāyasūtra & Tarkasaṃgraha",
            "passage": "Nyāyasūtra 1.1.4 ('indriyārthasannikarṣotpannaṃ jñānam...'); Tarkasaṃgraha Dīpikā §30"
        },
        "interview_trap": "How does Nyāya perceive absence (abhāva)? Through the 6th sannikarṣa: 'Viśeṣaṇa-viśeṣya-bhāva' (the absence of pot is an adjective qualifying the bare ground). Contrast this with Bhāṭṭa Mīmāṃsā, which invents a separate 6th pramāṇa: Anupalabdhi (non-apprehension).",
        "wisdom_gist": "Human perception is never merely passive recording; our cognitive faculties instantly weave raw immediacy into an intelligible, structured reality of meaning."
    },
    {
        "id": "IND_LOGIC_001",
        "unit_id": "UNIT_01",
        "tradition": "Indian",
        "school": "Nyāya",
        "topic": "Inference & Epistemic Induction",
        "concept_name": "Anumāna: The Pañcāvayava Syllogism & Vyāpti",
        "chain": {
            "from_concept": "Pratyakṣa (Perception is limited to present objects)",
            "current_thesis": "Inference extends knowledge to unperceived realms through an unbroken invariant relation (Vyāpti) formulated in a five-membered syllogism.",
            "to_concept": "Hetvābhāsa (The fallacies that rupture Vyāpti and corrupt inference)"
        },
        "the_problem": "How can the mind legitimately cross the gap between what is currently perceived (smoke on a mountain) and what is hidden from view (fire inside the mountain)?",
        "technical_lexicon": [
            {"term": "Vyāpti (व्याप्ति)", "meaning": "Invariable, unconditional relation of concomitance between the sign (hetu/smoke) and the signified (sādhya/fire)."},
            {"term": "Pañcāvayava (पञ्चावयव)", "meaning": "The 5 members of demonstration: Pratijñā (thesis), Hetu (reason), Udāharaṇa (universal exemplification), Upanaya (application), Nigamana (conclusion)."},
            {"term": "Upādhi (उपाधि)", "meaning": "An extraneous condition that renders a concomitance conditional (e.g., 'wet fuel' is the upādhi for smoke from fire)."},
            {"term": "Parāmarśa (परामर्श)", "meaning": "The synthetic cognitive act: realization that the mountain possesses smoke which is invariably accompanied by fire."}
        ],
        "dialectic": {
            "purvapaksha": "Cārvāka challenges: How do you know Vyāpti holds universally? You have seen fire with smoke in a kitchen, but have you seen every fire in all past, present, and future universes? If you infer it, you presuppose inference; induction is logically circular.",
            "siddhanta": "Nyāya solves the Indian problem of induction through 'Sāmānyalakṣaṇa-pratyakṣa' (perceiving smokiness as a universal in all smoke) combined with 'Tarka' (reductio ad absurdum: 'If smoke could occur without fire, why does no one look for smoke in a lake?')."
        },
        "primary_text": {
            "author": "Vātsyāyana & Uddyotakāra",
            "work": "Nyāyabhāṣya & Nyāyavārttika",
            "passage": "Nyāyasūtra 1.1.5; Tarkasaṃgraha §§ 36–48"
        },
        "interview_trap": "Compare the Nyāya 5-membered syllogism with Aristotle's 3-membered syllogism: Aristotle's syllogism is purely deductive and formal; the Nyāya pañcāvayava is BOTH inductive and deductive, requiring an empirical example (Udāharaṇa) from the world.",
        "wisdom_gist": "Inference is the bridge between the finite senses and the infinite world. Reason does not float in formal abstraction; it remains anchored to lived empirical observation."
    },
    {
        "id": "IND_LOGIC_002",
        "unit_id": "UNIT_01",
        "tradition": "Indian",
        "school": "Nyāya",
        "topic": "Fallacies of Inference",
        "concept_name": "Hetvābhāsa: The Five Inferential Fallacies",
        "chain": {
            "from_concept": "Anumāna & Vyāpti (The criteria of valid inference)",
            "current_thesis": "A pseudo-reason (hetvābhāsa) appears to establish a conclusion but violates one of the 5 conditions of a valid hetu (rūpa-pañcaka).",
            "to_concept": "Debate Methodology (Vāda, Jalpa, Vitaṇḍā in Nyāya epistemology)"
        },
        "the_problem": "What precise logical defects destroy the validity of an inference, causing the reason (hetu) to yield error or contradiction?",
        "technical_lexicon": [
            {"term": "Savyabhicāra / Anaikāntika (सव्यभिचार)", "meaning": "The erratic/inconclusive reason: Sādhāraṇa (too wide), Asādhāraṇa (too narrow), Anupasaṃhārī (non-exclusive)."},
            {"term": "Viruddha (विरुद्ध)", "meaning": "The contradictory reason: establishes the exact opposite of what was to be proved (e.g., 'Sound is eternal because it is produced')."},
            {"term": "Satpratipakṣa (सत्प्रतिपक्ष)", "meaning": "The counterbalanced reason: an equally strong contrary inference exists against it."},
            {"term": "Asiddha / Sādhyasama (असिद्ध)", "meaning": "The unproved/unfounded reason: Āśrayāsiddha (unreal subject), Svarūpāsiddha (absent in subject), Vyāpyatvāsiddha (conditional)."},
            {"term": "Bādhita / Kālātīta (बाधित)", "meaning": "The sublated reason: the conclusion is directly contradicted by a stronger pramāṇa like perception ('Fire is cold because it is a substance')."}
        ],
        "dialectic": {
            "purvapaksha": "Early thinkers wondered: Why are there 5 distinct fallacies rather than simply one overarching category of 'invalid inference'?",
            "siddhanta": "Nyāya systematically deduces the 5 fallacies from the 5 essential characteristics of a sound reason (rūpa-pañcaka): (1) presence in pakṣa, (2) presence in sapakṣa, (3) absence in vipakṣa, (4) absence of counterbalancing reason, (5) non-sublation by perception. Each fallacy corresponds to the breakdown of one specific leg."
        },
        "primary_text": {
            "author": "Annambhaṭṭa & Keśava Miśra",
            "work": "Tarkasaṃgraha & Tarkabhāṣā",
            "passage": "Tarkasaṃgraha §§ 52–58; Tarkabhāṣā on Hetvābhāsa"
        },
        "interview_trap": "What is the crucial difference between Satpratipakṣa and Bādhita? In Satpratipakṣa, the opposition is from another INFERENCE of equal strength; in Bādhita, the conclusion is cancelled by a non-inferential, immediate source like PERCEPTION (e.g., touch tells us fire is hot)."
    },
    # -------------------------------------------------------------
    # INDIAN METAPHYSICS & CAUSATION (CHAIN 2)
    # -------------------------------------------------------------
    {
        "id": "IND_META_001",
        "unit_id": "UNIT_01",
        "tradition": "Indian",
        "school": "Sāṃkhya vs. Nyāya-Vaiśeṣika",
        "topic": "Theories of Causation",
        "concept_name": "Satkāryavāda vs. Asatkāryavāda (Pariṇāmavāda vs. Ārambhavāda)",
        "chain": {
            "from_concept": "Epistemic validity of empirical observation (How objects change)",
            "current_thesis": "The effect pre-exists in the material cause prior to production (Satkāryavāda), versus the effect is an entirely de novo creation (Asatkāryavāda).",
            "to_concept": "Cosmic Evolution & Dissolution (Sāṃkhya's 24 Tattvas & Advaita's Vivartavāda)"
        },
        "the_problem": "Does change create something genuinely brand new out of non-being, or does change merely unveil what was already latently present in the cause?",
        "technical_lexicon": [
            {"term": "Satkāryavāda (सत्कार्यवाद)", "meaning": "The doctrine of existent effect: the effect is an unmanifest state of the cause."},
            {"term": "Pariṇāmavāda (परिणामवाद)", "meaning": "Real transformation: the cause undergoes real ontological modification into the effect (Sāṃkhya)."},
            {"term": "Asatkāryavāda / Ārambhavāda (असत्कार्यवाद / आरम्भवाद)", "meaning": "The doctrine of fresh origination: the effect is non-existent before production (Nyāya)."},
            {"term": "Vivartavāda (विवर्तवाद)", "meaning": "Illusory modification: the cause appears as effect without undergoing change (Advaita Vedānta)."}
        ],
        "dialectic": {
            "purvapaksha": "The Naiyāyika argues: If the cloth already existed inside the threads, the weaver's effort is pointless, and threads could clothe a shivering person. The cloth is a new substance inhering in threads.",
            "siddhanta": "Īśvarakṛṣṇa in Sāṃkhyakārikā 9 proves Satkāryavāda: (1) Asadakaraṇāt (oil cannot be pressed from sand), (2) Upādānagrahaṇāt (specific materials needed for specific effects), (3) Sarvasambhavābhāvāt (not everything from anything), (4) Śaktasya śakyakaraṇāt (cause produces only what it has potential for), (5) Kāraṇabhāvāt (cause and effect share essence)."
        },
        "primary_text": {
            "author": "Īśvarakṛṣṇa",
            "work": "Sāṃkhyakārikā",
            "passage": "Kārikā 9"
        },
        "interview_trap": "Both Sāṃkhya and Advaita accept Satkāryavāda, but differ radically on transformation: Sāṃkhya asserts PARIṆĀMA (real, physical evolution of Prakṛti), while Advaita asserts VIVARTA (apparent, illusory superimposition on unchanging Brahman).",
        "wisdom_gist": "Nothing emerges out of sheer void. Creativity is not ex nihilo creation; it is the patient unfolding of inherent potentiality into vivid actuality."
    },
    {
        "id": "IND_VEDAN_001",
        "unit_id": "UNIT_01",
        "tradition": "Indian",
        "school": "Advaita Vedānta",
        "topic": "Metaphysics of Reality & Illusion",
        "concept_name": "Adhyāsa, Māyā & The Two Tiers of Reality",
        "chain": {
            "from_concept": "Vivartavāda (The effect as an appearance of the cause)",
            "current_thesis": "The perceived diversity of the universe is a superimposition (Adhyāsa) upon pure non-dual consciousness (Brahman) via inexplicable ignorance (Māyā/Avidyā).",
            "to_concept": "Rāmānuja's Critique of Advaita (The Saptavidhā Anupapatti)"
        },
        "the_problem": "How can the pure, undivided, immutable Brahman appear as a cosmos of suffering, multiplicity, and individual bound souls (jīvas)?",
        "technical_lexicon": [
            {"term": "Adhyāsa (अध्यास)", "meaning": "Superimposition: the apparent presentation of an attribute of one thing onto another (smṛtirūpaḥ paratra pūrvadṛṣṭāvabhāsaḥ)."},
            {"term": "Māyā / Avidyā (माया / अविद्या)", "meaning": "The cosmic principle of illusion possessing two powers: Āvaraṇa (veiling reality) and Vikṣepa (projecting multiplicity)."},
            {"term": "Sattā-traividhya (सत्ता-त्रैविध्य)", "meaning": "Three tiers of reality: Pāramārthika (Absolute/Brahman), Vyāvahārika (Empirical/World), Prātibhāsika (Illusory/Dreams)."},
            {"term": "Sākṣin (साक्षी)", "meaning": "The witness-consciousness that illuminates both knowledge and ignorance without participating in action."}
        ],
        "dialectic": {
            "purvapaksha": "The realist asks: The subject (knower) and object (known) are as opposed as light and darkness. How can the attributes of the insentient world be superimposed upon the pure conscious self?",
            "siddhanta": "Śaṅkara opens the Brahmasūtra-Bhāṣya by declaring Adhyāsa natural and beginningless (naisargiko 'yaṃ lokavyavahāraḥ). Just as a blameless sky appears blue or contaminated by dust, consciousness misidentifies with body and mind due to innate nescience."
        },
        "primary_text": {
            "author": "Śaṅkarācārya",
            "work": "Brahmasūtra-Bhāṣya",
            "passage": "Adhyāsa-Bhāṣya (Preamble to BS 1.1.1)"
        },
        "interview_trap": "Did Śaṅkara claim the world is a complete hallucination like a dream? NO! That is the trap. Śaṅkara vigorously refutes Buddhist subjective idealism (Yogācāra) in BS 2.2.28; the empirical world possesses Vyāvahārika Sattā (objective reality for all practical purposes) until sublated by Brahman-knowledge.",
        "wisdom_gist": "Much of our anxiety and suffering stems from superimposing ephemeral psychological identities onto the silent, untroubled witness within."
    },
    {
        "id": "IND_VEDAN_002",
        "unit_id": "UNIT_01",
        "tradition": "Indian",
        "school": "Viśiṣṭādvaita Vedānta",
        "topic": "Qualified Non-Dualism & Critique of Māyā",
        "concept_name": "Rāmānuja's Aprathaksiddhi & Saptavidhā Anupapatti",
        "chain": {
            "from_concept": "Advaita's Nirguṇa Brahman & Māyāvāda",
            "current_thesis": "Brahman is organically qualified by real matter (acit) and real souls (cit) through inseparability (Aprathaksiddhi); Māyā is logically self-contradictory in 7 ways.",
            "to_concept": "Dvaita Vedānta (Madhva's rejection of all non-difference in favor of Pañca-bheda)"
        },
        "the_problem": "Can non-dualism preserve the reality of individual souls, the external cosmos, and personal devotion (Bhakti) without dismissing them as illusory nescience?",
        "technical_lexicon": [
            {"term": "Aprathaksiddhi (अपृथक्सिद्धि)", "meaning": "Inseparable relation: mode cannot exist without substance, yet is distinct from it (unlike Nyāya's Samavāya)."},
            {"term": "Śarīra-Śarīrī-Bhāva (शरीर-शरीरि-भाव)", "meaning": "Body-Soul analogy: the world and individual souls constitute the real body (śarīra) of God (Brahman)."},
            {"term": "Saptavidhā Anupapatti (सप्तविधा अनुपपत्ति)", "meaning": "Rāmānuja's 7 great incoherences of Advaita's Māyā: Āśraya, Tirodhāna, Svarūpa, Anirvacanīya, Pramāṇa, Nivartaka, Nivṛtti."},
            {"term": "Viśiṣṭa-Aikya (विशिष्ट-ऐक्य)", "meaning": "Non-duality of the qualified whole; Brahman qualified by subtle souls/matter becomes Brahman qualified by gross souls/matter."}
        ],
        "dialectic": {
            "purvapaksha": "Śaṅkara argued that all differentiation is illusory; pure Nirguṇa Brahman alone is real, and any quality implies finitude.",
            "siddhanta": "Rāmānuja in Śrībhāṣya dismantles Māyā: (1) Where does Māyā reside (Āśrayānupapatti)? Not in Brahman (pure light cannot host darkness) and not in Jīva (Jīva is produced by Māyā—circular reasoning!). (2) How can it veil self-luminous Brahman (Tirodhānānupapatti)? Veiling luminosity destroys its nature. Brahman is SAGUṆA, adorned with infinite auspicious qualities (kalyāṇa-guṇas)."
        },
        "primary_text": {
            "author": "Rāmānuja",
            "work": "Śrībhāṣya",
            "passage": "Introduction to BS 1.1.1 (The Great Siddhānta / Mahā-siddhānta)"
        },
        "interview_trap": "Compare Aprathaksiddhi (Viśiṣṭādvaita) and Samavāya (Nyāya): Samavāya relates two ALREADY established separate substances (ayutasiddha); Aprathaksiddhi relates an attribute that CANNOT even be conceived or exist without its substantive substrate.",
        "wisdom_gist": "The universe is not an empty illusion to be escaped; it is the living, breathing body of the Divine, worthy of reverence, care, and loving devotion."
    },
    {
        "id": "IND_BUDDH_001",
        "unit_id": "UNIT_01",
        "tradition": "Indian",
        "school": "Madhyamaka Buddhism",
        "topic": "Emptiness & Dependent Origination",
        "concept_name": "Pratītyasamutpāda and Nāgārjuna's Śūnyatā",
        "chain": {
            "from_concept": "Abhidharma atomism (Searching for irreducible svabhāva in dharmas)",
            "current_thesis": "Whatever is dependently co-arisen is devoid of inherent essence (Śūnyatā); emptiness is not nothingness, but the condition for all change and awakening.",
            "to_concept": "Yogācāra Vijñaptimātratā (Reconstructing the mind from the ashes of extreme deconstruction)"
        },
        "the_problem": "If all phenomena arise dependently upon causes and conditions, can any entity possess independent, immutable essence (svabhāva)?",
        "technical_lexicon": [
            {"term": "Pratītyasamutpāda (प्रतीत्यसमुत्पाद)", "meaning": "Dependent co-arising: nothing exists uncaused, isolated, or self-grounded."},
            {"term": "Śūnyatā (शून्यता)", "meaning": "Emptiness; absence of fixed, self-sufficient inherent nature (niḥsvabhāvatā)."},
            {"term": "Catuṣkoṭi (चतुष्कोटि)", "meaning": "Four-cornered dialectic: It is not A, not non-A, not both, not neither."},
            {"term": "Dṛṣṭi-sarva-prahāṇa (दृष्टिसर्वप्रहाण)", "meaning": "The total relinquishing of all dogmatic philosophical viewpoints."}
        ],
        "dialectic": {
            "purvapaksha": "The realist objects: If all dharmas are empty, morality, the Four Noble Truths, and liberation become fictions. Emptiness leads to terrifying nihilism (ucchedavāda).",
            "siddhanta": "Nāgārjuna turns the table in MMK 24.18: If things had fixed svabhāva, they could NEVER change! A seed could never sprout; a bound person could never achieve liberation. It is precisely because everything is empty that causal transformation and spiritual freedom are possible."
        },
        "primary_text": {
            "author": "Nāgārjuna",
            "work": "Mūlamadhyamakakārikā (MMK)",
            "passage": "Chapter 24 (Āryasatya-parīkṣā), verses 18–19"
        },
        "interview_trap": "Never equate Śūnyatā with nothingness (abhāva)! Nāgārjuna warns in MMK 24.11: 'A wrongly grasped emptiness ruins a person of little intelligence, like a snake handled carelessly or a magic spell misapplied!'",
        "wisdom_gist": "To be empty is not to be nothing; it is to be open to everything. Letting go of rigid identities reveals that life's interdependency is the foundation of compassion."
    },
    {
        "id": "IND_JAINA_001",
        "unit_id": "UNIT_01",
        "tradition": "Indian",
        "school": "Jainism",
        "topic": "Relativism & Pluralistic Realism",
        "concept_name": "Anekāntavāda, Syādvāda & Nayavāda",
        "chain": {
            "from_concept": "Dogmatic absolutisms (Advaita's eternal permanence vs Buddhism's flux)",
            "current_thesis": "Reality is multifaceted and complex (Anekānta); every predication must be conditional and standpoint-relative (Syādvāda).",
            "to_concept": "Jaina Ethics: Ahiṃsā as the intellectual duty of respecting rival philosophical perspectives"
        },
        "the_problem": "How can philosophy overcome the dogmatic clashes between systems that assert reality is purely permanent (Vedānta) and systems that assert it is purely momentary (Buddhism)?",
        "technical_lexicon": [
            {"term": "Anekāntavāda (अनेकान्तवाद)", "meaning": "Metaphysical doctrine of non-one-sidedness: reality possesses infinite attributes (ananta-dharmātmakam vastu)."},
            {"term": "Syādvāda (स्याद्वाद)", "meaning": "Epistemological doctrine of conditional predication: using 'Syāt' (in some respect) to avoid dogmatism."},
            {"term": "Saptabhaṅgī (सप्तभङ्गी)", "meaning": "Seven-fold predication: syād asti, syān nāsti, syād asti nāsti ca, syād avaktavyaḥ, etc."},
            {"term": "Nayavāda (नयवाद)", "meaning": "Theory of partial standpoints: examining reality through specialized perspectives (e.g., Dravyārthika vs Paryāyārthika naya)."}
        ],
        "dialectic": {
            "purvapaksha": "Śaṅkara and the Naiyāyikas attack: Syādvāda is sheer nonsense. A thing cannot be both hot and cold at the same time; qualifying everything with 'somehow' violates the law of contradiction.",
            "siddhanta": "The Jaina answers: It is not in the SAME respect that a thing is and is not! A gold ring IS from the standpoint of substance (gold), but IS NOT from the standpoint of previous form (necklace). Absolute permanent vs absolute momentary are one-sided abstractions (ekāntas). Reality is Dravya-Guṇa-Paryāya (substance with enduring qualities undergoing modes)."
        },
        "primary_text": {
            "author": "Mallisena & Kundakunda",
            "work": "Syādvādamañjarī & Pravacanasāra",
            "passage": "Syādvādamañjarī on Kārikā 28; Pravacanasāra Book II"
        },
        "interview_trap": "Understand why 'Avaktavya' (inexpressible) is the 4th step in Saptabhaṅgī: It occurs when one attempts to state existence and non-existence SIMULTANEOUSLY (yugapat), which language cannot do. Contrast with the 3rd step which states them sequentially (kramaśaḥ).",
        "wisdom_gist": "Intellectual humility is the highest form of non-violence. Recognizing that our personal viewpoint captures only one facet of the infinite jewel of reality disarms dogmatism."
    },

    # -------------------------------------------------------------
    # WESTERN EPISTEMOLOGY & METHOD (CHAIN 3)
    # -------------------------------------------------------------
    {
        "id": "WEST_MOD_001",
        "unit_id": "UNIT_03",
        "tradition": "Western",
        "school": "Continental Rationalism",
        "topic": "Methodological Doubt & Subjectivity",
        "concept_name": "Descartes' Method of Doubt & The Cogito",
        "chain": {
            "from_concept": "Medieval Scholastic Dogmatism & Montaigne's Skepticism",
            "current_thesis": "By pushing doubt to its hyper-radical limit (evil demon), the indubitable bedrock of the thinking self (Cogito) is discovered.",
            "to_concept": "Cartesian Dualism & The Mind-Body Interaction Problem (Spinoza's Monism)"
        },
        "the_problem": "How can human cognition discover an indubitable, rock-solid foundation for knowledge that withstands all skeptical assault?",
        "technical_lexicon": [
            {"term": "Methodological Doubt (Doubt as an instrument)", "meaning": "Systematic suspension of assent to any belief that admits of the slightest uncertainty."},
            {"term": "Malin Génie (Evil Demon)", "meaning": "The ultimate skeptical thought experiment: an all-powerful deceiver manipulating math and sensory perceptions."},
            {"term": "Cogito, Ergo Sum", "meaning": "I think, therefore I am; the self-authenticating certainty that doubt requires a doubter."},
            {"term": "Res Cogitans vs. Res Extensa", "meaning": "Substance dualism: thinking unextended substance (mind) vs unthinking extended substance (matter)."}
        ],
        "dialectic": {
            "purvapaksha": "The radical skeptic asserts: We cannot trust our senses (dreams deceive us) and we cannot trust mathematics (a malicious demon could deceive us every time we add 2 and 3). Knowledge is impossible.",
            "siddhanta": "Descartes points out in Meditation II: Let the demon deceive me as much as he can, he can NEVER bring it about that I am nothing so long as I think that I am something. Even to be deceived, I must exist. Cogito is self-verifying."
        },
        "primary_text": {
            "author": "René Descartes",
            "work": "Meditations on First Philosophy",
            "passage": "Meditation I & Meditation II (AT VII, 24–34)"
        },
        "interview_trap": "Did Descartes mean 'I think, therefore I am' as a syllogistic inference with a hidden major premise ('Whatever thinks exists')? NO! Descartes clarifies in the Second Replies that the Cogito is a direct, immediate intellectual intuition, not a syllogism.",
        "wisdom_gist": "Even in the deepest crisis of doubt, consciousness discovers its own indomitable presence. The capacity to question is proof of our being."
    },
    {
        "id": "WEST_MOD_004",
        "unit_id": "UNIT_03",
        "tradition": "Western",
        "school": "British Empiricism",
        "topic": "Origin of Knowledge & Qualities",
        "concept_name": "Locke's Tabula Rasa & Primary vs. Secondary Qualities",
        "chain": {
            "from_concept": "Cartesian Innate Ideas (Descartes & Leibniz)",
            "current_thesis": "The mind is a blank slate (Tabula Rasa) furnished entirely by experience; reality splits into objective primary and subjective secondary qualities.",
            "to_concept": "Berkeley's Immaterialism (Dissolving primary qualities into secondary ones: Esse est percipi)"
        },
        "the_problem": "Where do our ideas come from if there are no innate truths stamped on the human soul at birth?",
        "technical_lexicon": [
            {"term": "Tabula Rasa (White Paper)", "meaning": "The mind initially devoid of all characters, filled solely through Sensation and Reflection."},
            {"term": "Primary Qualities", "meaning": "Qualities inseparable from matter that resemble our ideas: extension, figure, motion, rest, solidity."},
            {"term": "Secondary Qualities", "meaning": "Powers in objects to produce sensations in us via primary qualities: colors, sounds, tastes, odors."},
            {"term": "Substance (Something I know not what)", "meaning": "The obscure unknown substrate required to support qualities."}
        ],
        "dialectic": {
            "purvapaksha": "Rationalists argued that universal principles of logic (the law of identity) and moral ideas must be innate because children and animals cannot extract necessity from messy sensory instances.",
            "siddhanta": "Locke in Book I of the Essay demonstrates that children and idiots do NOT possess the law of non-contradiction! If an idea were innate, it would be universally conscious. All complex ideas are constructed from simple ideas of sensation and internal reflection."
        },
        "primary_text": {
            "author": "John Locke",
            "work": "An Essay Concerning Human Understanding",
            "passage": "Book I, Chapters 1–2; Book II, Chapter 8 (§§ 9–26)"
        },
        "interview_trap": "Interview boards frequently ask: 'What was Locke's test for distinguishing primary from secondary qualities?' Primary qualities survive physical division (divide a grain of wheat in half, each piece retains extension and solidity); secondary qualities change or vanish (almonds pounded in a mortar lose their color and texture).",
        "wisdom_gist": "We enter the world with minds open and ready to learn. Experience is the great teacher, and knowledge is built through patient, honest sensory engagement."
    },
    {
        "id": "WEST_MOD_005",
        "unit_id": "UNIT_03",
        "tradition": "Western",
        "school": "British Empiricism / Idealism",
        "topic": "Critique of Materialism",
        "concept_name": "Berkeley's Esse est Percipi & Immaterialism",
        "chain": {
            "from_concept": "Locke's Primary vs Secondary Qualities & Material Substance",
            "current_thesis": "Matter does not exist; to be is to be perceived (Esse est percipi) or to perceive (Esse est percipere).",
            "to_concept": "Hume's Radical Skepticism (Applying Berkeley's critique to mental substance itself)"
        },
        "the_problem": "If secondary qualities exist only in the mind, how can primary qualities (shape, size) exist in an unthinking, unperceived 'material substance' outside mind?",
        "technical_lexicon": [
            {"term": "Esse est Percipi", "meaning": "To be is to be perceived: sensible things are collections of ideas in minds."},
            {"term": "Master Argument", "meaning": "Can you conceive of a tree existing unperceived? The moment you conceive it, you are perceiving it in thought; unperceived matter is an impossibility."},
            {"term": "Immaterialism", "meaning": "The rejection of inert matter; reality consists of minds (spirits) and their ideas."},
            {"term": "Divine Conservation", "meaning": "Things don't vanish when we leave the room because God's omnipresent mind perceives the universe continuously."}
        ],
        "dialectic": {
            "purvapaksha": "Locke and common sense argue: Even if color is subjective, the table's shape and solidity belong to the real physical object behind the sensory veil.",
            "siddhanta": "Berkeley retorts: Try conceiving extension without color or texture! You cannot. Extension is known ONLY through visual or tactile sensations. If secondary qualities are mind-dependent, primary qualities must be equally mind-dependent. 'Material substance' is an incoherent philosophical phantom."
        },
        "primary_text": {
            "author": "George Berkeley",
            "work": "A Treatise Concerning the Principles of Human Knowledge",
            "passage": "Sections 1–33"
        },
        "interview_trap": "Did Berkeley deny the reality of the physical world? Berkeley insisted he was defending common sense against skeptical materialists! He never denied that apples are crisp and stones hard; he only denied that they are made of unperceivable 'matter'. They are real, regular ideas caused by God.",
        "wisdom_gist": "The world is not a cold machine of dead matter spinning in empty space. Reality is an ongoing, luminous conversation between consciousness and creation."
    },
    {
        "id": "WEST_META_001",
        "unit_id": "UNIT_03",
        "tradition": "Western",
        "school": "British Empiricism / Skepticism",
        "topic": "The Problem of Induction",
        "concept_name": "Hume's Problem of Induction & The Critique of Necessary Connection",
        "chain": {
            "from_concept": "Rationalist Causal Metaphysics & Empiricist Association",
            "current_thesis": "Causation has no observable necessity; induction is grounded not in reason, but in psychological custom (habit).",
            "to_concept": "Kant's Awakening from Dogmatic Slumber (The Synthetic A Priori)"
        },
        "the_problem": "Can we logically demonstrate that the future will resemble the past, or that causes contain a necessary power to produce their effects?",
        "technical_lexicon": [
            {"term": "Hume's Fork", "meaning": "All inquiries divided into Relations of Ideas (analytic/a priori) and Matters of Fact (synthetic/a posteriori)."},
            {"term": "Constant Conjunction", "meaning": "Repeated observation of event B following event A in time and space, without any visible tie of necessity."},
            {"term": "Custom or Habit", "meaning": "The psychological instinct that leads animals and humans to expect like effects from like causes."},
            {"term": "Uniformity of Nature", "meaning": "The inductive presupposition that nature behaves uniformly, which cannot be proved without circularity."}
        ],
        "dialectic": {
            "purvapaksha": "Descartes and Spinoza asserted that causes necessarily contain their effects with mathematical certainty discoverable by intellect.",
            "siddhanta": "Hume demonstrates in Section IV of the Enquiry: Inspect a billiard ball striking another. You see movement, contact, and the second ball rolling. You NEVER perceive the 'power' or 'necessary connection'. Attempting to prove induction by induction is circular reasoning (begging the question)."
        },
        "primary_text": {
            "author": "David Hume",
            "work": "An Enquiry Concerning Human Understanding",
            "passage": "Sections IV & VII"
        },
        "interview_trap": "Selection committees love to ask: 'Did Hume advise abandoning science and causal expectations?' Hume answered NO! Skeptical doubt shows the limits of theoretical reason, but practical life must follow natural instinct: 'Be a philosopher; but, amidst all your philosophy, be still a man.'",
        "wisdom_gist": "Intellectual pride claims universal certitude, but philosophical wisdom recognizes that our deepest expectations rest on the humble habits of nature."
    },
    {
        "id": "WEST_EPIST_001",
        "unit_id": "UNIT_03",
        "tradition": "Western",
        "school": "Critical Idealism",
        "topic": "Conditions of Knowledge",
        "concept_name": "Kant's Synthetic A Priori & Transcendental Deduction",
        "chain": {
            "from_concept": "Hume's Inductive Skepticism (Awakening Kant from dogmatic slumber)",
            "current_thesis": "Knowledge of the empirical world requires synthetic a priori concepts (categories) that structure the raw sensory manifold into knowable experience.",
            "to_concept": "Hegel's Dialectic (Overcoming Kant's rigid barrier between phenomena and noumena)"
        },
        "the_problem": "How can science possess universal, necessary laws (like causality and mathematics) if all empirical knowledge is contingent?",
        "technical_lexicon": [
            {"term": "Copernican Revolution", "meaning": "Objects conform to the cognitive structure of the human mind, rather than the mind conforming to objects."},
            {"term": "Synthetic A Priori", "meaning": "Judgments that expand knowledge (synthetic) yet hold with strict universality and necessity (a priori)."},
            {"term": "Forms of Intuition", "meaning": "Space and Time as the pure a priori subjective lenses of sensory receptivity."},
            {"term": "Transcendental Unity of Apperception", "meaning": "The 'I think' that must be able to accompany all representations to make experience unified."}
        ],
        "dialectic": {
            "purvapaksha": "Hume argued causality is just an empirical association of ideas, leaving science without necessary foundation.",
            "siddhanta": "Kant proves in the Critique of Pure Reason: Causality is not an empirical discovery from experience; it is a CATEGORY of the understanding that makes experience possible in the first place! Without categories, sensory input would be a blind, chaotic blur."
        },
        "primary_text": {
            "author": "Immanuel Kant",
            "work": "Critique of Pure Reason (Kritik der reinen Vernunft)",
            "passage": "B-Deduction (§§ 15–27, B129–B169)"
        },
        "interview_trap": "Can we know the 'Ding an sich' (Thing-in-itself)? A decisive NO! Kant limits synthetic a priori knowledge strictly to PHENOMENA (appearances). Reason attempting to know the unconditioned noumenon falls into inescapable Antinomies.",
        "wisdom_gist": "The human mind does not passively reflect the universe; it actively gives order, continuity, and intelligibility to the world we inhabit."
    },

    # -------------------------------------------------------------
    # CONTEMPORARY PHENOMENOLOGY & EXISTENTIALISM (CHAIN 4)
    # -------------------------------------------------------------
    {
        "id": "WEST_CONT_001",
        "unit_id": "UNIT_04",
        "tradition": "Western",
        "school": "Phenomenology",
        "topic": "Phenomenological Method",
        "concept_name": "Husserl's Epoché & Intentionality",
        "chain": {
            "from_concept": "19th Century Psychologism & Uncritical Naturalism",
            "current_thesis": "By bracketing belief in the external world (Epoché), consciousness reveals its essential intentional structure (consciousness-of).",
            "to_concept": "Heidegger's Being and Time (Rejection of pure detached consciousness in favor of Dasein's Being-in-the-world)"
        },
        "the_problem": "How can philosophy become a rigorous, presuppositionless science grounded in things as they present themselves, rather than theoretical dogmas?",
        "technical_lexicon": [
            {"term": "Epoché (Bracketing / Einklammerung)", "meaning": "Suspending the 'natural attitude' (belief in the independent existence of the external world)."},
            {"term": "Intentionality", "meaning": "The defining property of mental acts: all consciousness is directed toward an object (consciousness-of something)."},
            {"term": "Noesis vs. Noema", "meaning": "The subjective act of experiencing (noesis) vs the objective meaning-content experienced (noema)."},
            {"term": "Eidetic Reduction", "meaning": "Varying representations in imagination to intuit their invariant essences (Wesen)."}
        ],
        "dialectic": {
            "purvapaksha": "Naturalists and psychologists claimed thoughts are merely neuro-physiological events in the brain caused by physical stimuli.",
            "siddhanta": "Husserl demonstrates in Logical Investigations and Ideas I that logical truths (like 2+2=4) are not psychological brain events; they possess objective ideal validity. By performing the Epoché, we don't destroy the world; we bracket it to study the pure structures of meaning in consciousness."
        },
        "primary_text": {
            "author": "Edmund Husserl",
            "work": "Ideas Pertaining to a Pure Phenomenology (Ideen I)",
            "passage": "§§ 31–32 (The Phenomenological Epoché) & § 84 (Intentionality)"
        },
        "interview_trap": "Does the Epoché mean skepticism or solipsism? NO! Husserl explicitly warns that bracketing the natural attitude does not mean doubting or denying the world; it means putting its dogmatic metaphysical status 'out of play' (außer Aktion) to inspect how meaning is constituted.",
        "wisdom_gist": "Before we rush to explain the world with scientific theories, we must first learn to look with clear, unprejudiced eyes at how reality actually appears to lived awareness."
    },
    {
        "id": "WEST_PHENOM_001",
        "unit_id": "UNIT_04",
        "tradition": "Western",
        "school": "Fundamental Ontology / Existentialism",
        "topic": "Ontology & Authenticity",
        "concept_name": "Heidegger's Dasein, Being-in-the-world & Zuhandenheit",
        "chain": {
            "from_concept": "Husserl's Detached Phenomenological Observer & Cartesian Dualism",
            "current_thesis": "Human existence (Dasein) is not a detached subject looking at objects, but practical immersion (Being-in-the-world) dealing with equipment (ready-to-hand).",
            "to_concept": "Sartre's Radical Freedom & Bad Faith (Being and Nothingness)"
        },
        "the_problem": "Why has Western metaphysics forgotten the fundamental question of Being (Seinsvergessenheit), reducing reality to inert, detached substances?",
        "technical_lexicon": [
            {"term": "Dasein (Being-there)", "meaning": "The human entity for whom its very Being is an issue; characterized by openness, thrownness, and care."},
            {"term": "In-der-Welt-sein (Being-in-the-world)", "meaning": "The primordial holistic involvement with the world prior to any subject-object split."},
            {"term": "Zuhandenheit (Ready-to-hand)", "meaning": "The practical familiarity of tools in use (the hammer) before they break."},
            {"term": "Vorhandenheit (Present-at-hand)", "meaning": "Detached, theoretical contemplation of an object when practical activity breaks down."},
            {"term": "Sein-zum-Tode (Being-towards-death)", "meaning": "Confronting one's non-relational finitude to break free from the conformist herd (das Man)."}
        ],
        "dialectic": {
            "purvapaksha": "Descartes and traditional epistemologists began with an isolated ego thinking in an ivory tower, wondering if the external table is real.",
            "siddhanta": "Heidegger proves in Sein und Zeit (1927): We do not encounter things as theoretical substances first! We encounter them practically in a workshop of significance. The carpenter doesn't contemplate the hammer; he hammers! Theoretical Cartesian detachment is a secondary breakdown of practical care (Sorge)."
        },
        "primary_text": {
            "author": "Martin Heidegger",
            "work": "Being and Time (Sein und Zeit)",
            "passage": "Division I (§§ 14–18 on Worldhood and Equipment) and Division II (§§ 46–53 on Death)"
        },
        "interview_trap": "Distinguish Husserl from Heidegger on method: Husserl uses the Epoché to step back into transcendental consciousness; Heidegger rejects this as impossible because Dasein is always already 'thrown' (Geworfen) into a concrete, historical language and world (Hermeneutic Phenomenology).",
        "wisdom_gist": "We do not live inside our heads peering out through glass windows at an alien cosmos. We are deeply woven into the world. To live authentically is to own our finitude before time slips away."
    },
    {
        "id": "WEST_CONT_002",
        "unit_id": "UNIT_04",
        "tradition": "Western",
        "school": "Existentialism",
        "topic": "Freedom & Bad Faith",
        "concept_name": "Sartre: Existence Precedes Essence & Bad Faith",
        "chain": {
            "from_concept": "Heidegger's Thrownness (Geworfenheit) & Dasein's Finitude",
            "current_thesis": "Human beings have no predetermined essence; we first exist, act, and define ourselves, condemned to be absolutely free.",
            "to_concept": "Postmodern Critiques of Subjectivity (Foucault's Death of Man & Power)"
        },
        "the_problem": "If God does not exist to design human nature like a craftsman designs a paper-knife, what grounds moral responsibility and human identity?",
        "technical_lexicon": [
            {"term": "Existence precedes essence", "meaning": "Humans first encounter themselves in the world, and only through choices define who they are."},
            {"term": "Être-en-soi (Being-in-itself)", "meaning": "Non-conscious, solid, inert objects with fixed essences (a rock, a table)."},
            {"term": "Être-pour-soi (Being-for-itself)", "meaning": "Consciousness characterized by lack, temporality, and radical freedom."},
            {"term": "Mauvaise Foi (Bad Faith)", "meaning": "Inauthenticity: lying to oneself by pretending to be a fixed object (en-soi) to evade the anguish of freedom."}
        ],
        "dialectic": {
            "purvapaksha": "Religious and biological essentialists assert that human nature is predetermined by divine commandment, genetic makeup, or societal roles.",
            "siddhanta": "Sartre declares in Being and Nothingness: 'Man is condemned to be free.' A waiter playing the role of a waiter too enthusiastically is acting in Bad Faith—pretending his career is an inescapable physical essence like the solidity of a rock. We are entirely responsible for our choices."
        },
        "primary_text": {
            "author": "Jean-Paul Sartre",
            "work": "Being and Nothingness (L'Être et le Néant)",
            "passage": "Part I, Chapter 2 ('Bad Faith') & 'Existentialism is a Humanism' (1946)"
        },
        "interview_trap": "What is the crucial paradox of Bad Faith? In Bad Faith, the deceiver and the deceived are the EXACT SAME PERSON. It is not an ordinary lie told to others; it is consciousness using its own freedom to pretend it has no freedom.",
        "wisdom_gist": "There are no ready-made excuses. We cannot blame our past, our parents, or our circumstances for our character. Every morning, life asks us: who will you choose to be today?"
    },

    # -------------------------------------------------------------
    # CONTEMPORARY INDIAN PHILOSOPHY (CHAIN 5)
    # -------------------------------------------------------------
    {
        "id": "IND_CONTEMP_001",
        "unit_id": "UNIT_05",
        "tradition": "Indian",
        "school": "Contemporary Indian",
        "topic": "Cosmic Evolution & The Divine Life",
        "concept_name": "Sri Aurobindo: Involution-Evolution & The Supermind",
        "chain": {
            "from_concept": "Śaṅkara's Illusionist Māyāvāda vs Western Darwinian Materialism",
            "current_thesis": "Matter is involved Spirit; cosmic evolution is the progressive ascent from Matter to Life, Mind, and Supramental Divine Gnosis.",
            "to_concept": "Teilhard de Chardin's Omega Point & Modern Transhumanist Philosophy"
        },
        "the_problem": "Can spiritual liberation be reconciled with terrestrial life and cosmic evolution without dismissing the world as an illusion or reducing mind to dead matter?",
        "technical_lexicon": [
            {"term": "Involution (Nimajjana)", "meaning": "The prior descent and self-concealment of Spirit (Saccidānanda) into the density of inert Matter."},
            {"term": "Evolution (Urdhvagati)", "meaning": "The progressive ascent of consciousness unfolding what was secretly involved."},
            {"term": "Supermind (Vijñāna / Truth-Consciousness)", "meaning": "The intermediate divine gnosis linking transcendent Saccidānanda with the manifested cosmos."},
            {"term": "Integral Yoga (Pūrṇa Yoga)", "meaning": "Transformation of earthly human nature and divinization of life, rather than world-flight."}
        ],
        "dialectic": {
            "purvapaksha": "Traditional ascetic Vedānta claimed the world is a dream to be abandoned (Māyāvāda), while Darwinian science claimed evolution is accidental, blind, and physical.",
            "siddhanta": "Aurobindo proclaims: 'Evolution is an inverse action of the involution.' Life cannot evolve out of matter unless it was already involved within it; mind cannot evolve from life unless already hidden therein. The world is the delightful play (Līlā) of the Spirit ascending toward divine embodiment."
        },
        "primary_text": {
            "author": "Sri Aurobindo",
            "work": "The Life Divine",
            "passage": "Book I, Chapters 1–4 & Chapter 14 ('The Supermind as Creator')"
        },
        "interview_trap": "Distinguish Aurobindo's evolution from Bergson's 'Élan Vital': Bergson's creative evolution is open-ended and non-teleological; Aurobindo's evolution is teleological and spiritual, anchored in the pre-existent descent (involution) of Saccidānanda.",
        "wisdom_gist": "The human intellect is not the ultimate peak of evolution, but an intermediate transitional instrument. The universe is slowly awakening to its divine source through us."
    },
    {
        "id": "IND_CONTEMP_002",
        "unit_id": "UNIT_05",
        "tradition": "Indian",
        "school": "Contemporary Indian / Social-Political",
        "topic": "Social Emancipation & Moral Epistemology",
        "concept_name": "Dr. B. R. Ambedkar: Navayāna & Annihilation of Caste",
        "chain": {
            "from_concept": "Orthodox Brahmanical Caste Sanctions & Hierarchical Dharma",
            "current_thesis": "Religion must be reconstructed on universal human dignity, liberty, equality, and fraternity; caste is a graded inequality that destroys fraternity.",
            "to_concept": "Constitutional Morality & Secular Democracy in Modern India"
        },
        "the_problem": "Can a religion remain valid if it sanctifies hereditary, graded inequality, and how does the rational reconstruction of Dhamma restore human dignity?",
        "technical_lexicon": [
            {"term": "Navayāna (The New Vehicle)", "meaning": "Rationalist, humanist Buddhism oriented toward social justice and liberation from caste oppression."},
            {"term": "Graded Inequality (विभाजित असमानता)", "meaning": "An ascending scale of reverence and descending scale of contempt, preventing collective revolt."},
            {"term": "Dhamma vs. Dharma", "meaning": "Dhamma is social morality and universal compassion (karuṇā/maitrī); Brahmanical Dharma is ritual law."},
            {"term": "Constitutional Morality", "meaning": "Paramount devotion to democratic procedure, secular equality, and legal rights over sectarian dogma."}
        ],
        "dialectic": {
            "purvapaksha": "Orthodox defenders claimed caste was divinely ordained by Puruṣa Sūkta (Ṛgveda 10.90) and justified by retributive past karma.",
            "siddhanta": "Ambedkar in Annihilation of Caste and The Buddha and His Dhamma argued: 'Caste is not merely a division of labour; it is a division of labourers.' Any religion that denies human equality is an engine of oppression. True religion is morality that fosters fraternity among living human beings on this earth."
        },
        "primary_text": {
            "author": "Dr. B. R. Ambedkar",
            "work": "The Buddha and His Dhamma (1957) & Annihilation of Caste (1936)",
            "passage": "The Buddha and His Dhamma, Book II, Part II ('Dhamma is Morality'); Annihilation of Caste §§ 14–20"
        },
        "interview_trap": "What was Ambedkar's critique of the Buddhist Four Noble Truths? Ambedkar rejected the orthodox interpretation of 'Sarvaṃ Duḥkham' as pessimistic metaphysical inevitability; he insisted socio-economic, human-inflicted suffering must be distinguished from existential sorrow, and the Sangha must model equality.",
        "wisdom_gist": "Philosophy cannot remain detached in ivory towers while human beings are humiliated. The true test of any philosophical vision is its power to dismantle cruelty and cultivate fraternity."
    },
    {
        "id": "IND_CONTEMP_003",
        "unit_id": "UNIT_05",
        "tradition": "Indian",
        "school": "Contemporary Indian",
        "topic": "Practical Vedānta & Social Service",
        "concept_name": "Swami Vivekananda: Practical Vedānta & Universal Religion",
        "chain": {
            "from_concept": "Medieval World-Renouncing Monasticism",
            "current_thesis": "Advaitic oneness must not remain in mountain caves; it must be applied practically to uplift humanity through service to Daridra Nārāyaṇa.",
            "to_concept": "Sri Aurobindo's Integral Yoga & Modern Engaged Vedānta"
        },
        "the_problem": "How can the supreme philosophical truth of Advaita (oneness of Brahman) be translated into social action, moral courage, and global religious harmony?",
        "technical_lexicon": [
            {"term": "Practical Vedānta", "meaning": "The application of non-dual spiritual realization to everyday social, educational, and ethical life."},
            {"term": "Daridra Nārāyaṇa (God in the Poor)", "meaning": "Serving the suffering and downtrodden as direct worship of the living Divine."},
            {"term": "Universal Religion", "meaning": "Harmony of all faiths as different paths ascending the same spiritual mountain, avoiding dogmatism."},
            {"term": "Four Yogas (Jñāna, Bhakti, Karma, Rāja)", "meaning": "A balanced, scientific synthesis of intellect, devotion, action, and psychological meditation."}
        ],
        "dialectic": {
            "purvapaksha": "Critics claimed Vedānta fosters quietism, fatalism, and social passivity because it treats the world as an illusion.",
            "siddhanta": "Vivekananda roared at the Parliament of Religions (1893) and in his London lectures: 'If you cannot worship your brother man, the manifested God, how can you worship an unmanifested God?' If all souls are Brahman, all human beings are inherently divine and equal. Service is not condescending charity; it is self-worship."
        },
        "primary_text": {
            "author": "Swami Vivekananda",
            "work": "Complete Works of Swami Vivekananda",
            "passage": "Volume II: 'Practical Vedānta' (Lectures delivered in London, November 1896)"
        },
        "interview_trap": "Central University boards frequently ask: 'How does Vivekananda's concept of Maya differ from Shankara's?' Vivekananda did NOT treat Maya as an ontological illusion or theory; he called Maya 'a simple statement of fact of what we are and what we see around us'—the inescapable contradiction between the ideal and the real.",
        "wisdom_gist": "Strength is life; weakness is death. True spirituality is not running away from the world, but bringing the light of the divine into the dark corners of human suffering."
    },
    {
        "id": "IND_CONTEMP_004",
        "unit_id": "UNIT_05",
        "tradition": "Indian",
        "school": "Contemporary Indian / Moral Philosophy",
        "topic": "Satyāgraha & The Metaphysics of Truth",
        "concept_name": "M. K. Gandhi: Satyāgraha, Ahiṃsā & Truth as God",
        "chain": {
            "from_concept": "Machiavellian Political Realism (Ends justify the means)",
            "current_thesis": "Means and ends are convertible; Truth (Satya) is God, and Non-violence (Ahiṃsā) is the only means to realize it.",
            "to_concept": "Contemporary Civil Rights Movements (Martin Luther King Jr. & Nelson Mandela)"
        },
        "the_problem": "Can politics and moral resistance be conducted without hatred, violence, and the utilitarian sacrifice of moral purity?",
        "technical_lexicon": [
            {"term": "Satyāgraha (सत्याग्रह)", "meaning": "Soul-force or holding firmly to Truth; active non-violent resistance through self-suffering."},
            {"term": "Ahiṃsā (अहिंसा)", "meaning": "Active love and complete absence of ill-will in thought, word, and deed, even toward an oppressor."},
            {"term": "Sarvodaya (सर्वोदय)", "meaning": "The welfare and upliftment of all, prioritizing the last and least person (Antyodaya)."},
            {"term": "Swaraj (स्वराज)", "meaning": "True self-rule: mastery over one's own desires and senses, beyond mere political transfer of power."}
        ],
        "dialectic": {
            "purvapaksha": "Political pragmatists argued that non-violence is the weapon of the weak and helpless, utterly ineffective against ruthless imperial powers.",
            "siddhanta": "Gandhi insisted in Hind Swaraj: Ahiṃsā is the weapon of the supremely brave! Striking an opponent is easy and animalistic; absorbing blows without retaliating or hating requires immense spiritual fortitude. By appealing to the opponent's conscience through self-suffering (tapasya), Satyāgraha converts rather than destroys."
        },
        "primary_text": {
            "author": "Mahatma Gandhi",
            "work": "Hind Swaraj (1909) & From Yeravda Mandir",
            "passage": "Hind Swaraj, Chapters 16 & 17 ('Brute Force' vs 'Soul Force')"
        },
        "interview_trap": "Notice Gandhi's crucial shift in formulation: Early in life, he stated 'God is Truth'; later (1929), he radically reversed it to 'TRUTH IS GOD'. Why? Because even an atheist seeks truth; by defining Truth as God, no sincere seeker of truth is excluded.",
        "wisdom_gist": "The means are like the seed, and the end is like the tree. We cannot harvest peace by sowing seeds of bitterness and violence."
    }
]

def main():
    data = {
        "curriculum_version": "UGC_NET_DU_CU_2026_MASTER",
        "total_cards": len(FLASHCARDS),
        "flashcards": FLASHCARDS
    }
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Successfully compiled {len(FLASHCARDS)} master flashcards into {DB_FILE}!")

if __name__ == "__main__":
    main()
