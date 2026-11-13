"""
Appends additional chained philosophical cards to content/database.json.
"""

import json
from pathlib import Path

DB_FILE = Path(__file__).resolve().parent / "content" / "database.json"

MORE_CARDS = [
    {
        "id": "IND_VEDAN_003",
        "unit_id": "UNIT_01",
        "tradition": "Indian",
        "school": "Dvaita Vedānta",
        "topic": "Radical Dualism & Pluralism",
        "concept_name": "Madhvācārya: Pañca-Bheda & Svatantra-Asvatantra Tattva",
        "chain": {
            "from_concept": "Śaṅkara's Non-Dualism & Rāmānuja's Qualified Non-Dualism",
            "current_thesis": "Reality is governed by five absolute, eternal, unbridgeable differences (Pañca-Bheda); God alone is independent.",
            "to_concept": "Bhakti & Eternal Predestination (Tāratamya)"
        },
        "the_problem": "Can scriptural assertions of difference between the finite soul and the infinite God be taken literally without being dissolved into non-dualism?",
        "technical_lexicon": [
            {"term": "Pañca-Bheda (पञ्च-भेद)", "meaning": "Five eternal differences: God-Soul, God-Matter, Soul-Soul, Soul-Matter, Matter-Matter."},
            {"term": "Svatantra vs. Asvatantra", "meaning": "The sole Independent Reality (Viṣṇu) vs Dependent Realities (souls and world)."},
            {"term": "Viśeṣa (विशेष)", "meaning": "Internal differentiating power that accounts for distinction without multiplying substances."},
            {"term": "Bimba-Pratibimba-Bhāva", "meaning": "Soul is an eternal reflection of God, distinct yet totally dependent."}
        ],
        "dialectic": {
            "purvapaksha": "Advaita claims 'Tat Tvam Asi' (Thou Art That) teaches non-dual identity between Jīva and Brahman.",
            "siddhanta": "Madhva reads the Chāndogya text as 'Atat Tvam Asi' (Thou art NOT that!) or interprets it as similarity in essence. Perception and scripture everywhere confirm difference. Difference (Bheda) is the constitutional nature of reality (svarūpa-bheda)."
        },
        "primary_text": {
            "author": "Madhvācārya",
            "work": "Viṣṇutattvanirṇaya",
            "passage": "Section on the five eternal differences (Pañca-bheda)"
        },
        "interview_trap": "How does Madhva explain the relation between God and His qualities without multiplying entities? Madhva introduces 'Viśeṣa'—an internal differentiator that functions in place of difference without being an independent entity.",
        "wisdom_gist": "Acknowledging our finitude and honoring the reality of the other is not spiritual defeat; it is the humble foundation of reverence, gratitude, and devotion."
    },
    {
        "id": "IND_YOGA_001",
        "unit_id": "UNIT_01",
        "tradition": "Indian",
        "school": "Pātañjala Yoga",
        "topic": "Psychology & Liberation",
        "concept_name": "Patañjali: Citta-Vṛtti-Nirodha & Aṣṭāṅga Yoga",
        "chain": {
            "from_concept": "Sāṃkhya Metaphysical Discrimination (Viveka-khyāti)",
            "current_thesis": "Liberation requires the practical cessation of mental fluctuations (citta-vṛtti-nirodha) through an eight-limbed methodology.",
            "to_concept": "Kaivalya (Absolute isolation of pure consciousness / Puruṣa from Prakṛti)"
        },
        "the_problem": "How can consciousness free itself from the continuous psychological turbulence and false identification with mental states?",
        "technical_lexicon": [
            {"term": "Citta-Vṛtti-Nirodha (चित्तवृत्तिनिरोध)", "meaning": "The cessation of the modifications/fluctuations of the mind-stuff."},
            {"term": "Kleśas (क्लेश)", "meaning": "The five afflictions: Avidyā (ignorance), Asmitā (egoism), Rāga (attachment), Dveṣa (aversion), Abhiniveśa (fear of death)."},
            {"term": "Aṣṭāṅga Yoga (अष्टाङ्ग योग)", "meaning": "Eight limbs: Yama, Niyama, Āsana, Prāṇāyāma, Pratyāhāra, Dhāraṇā, Dhyāna, Samādhi."},
            {"term": "Saṃprajñāta vs. Asaṃprajñāta Samādhi", "meaning": "Cognitive absorption (with seed) vs Supracognitive absorption (seedless/nirbīja)."}
        ],
        "dialectic": {
            "purvapaksha": "Can the mind be quieted by intellectual knowledge alone, as Sāṃkhya suggests?",
            "siddhanta": "Patañjali emphasizes in YS 1.2 and 1.12 that mere philosophical reflection cannot halt subconscious impressions (saṃskāras). Cessation requires systematic 'Abhyāsa' (repeated practice) and 'Vairāgya' (dispassion), culminating in stilling the mental vortex."
        },
        "primary_text": {
            "author": "Patañjali & Vyāsa",
            "work": "Yogasūtra & Yogabhāṣya",
            "passage": "Yogasūtra 1.2 ('Yogaścittavṛttinirodhaḥ') & 2.28–2.29"
        },
        "interview_trap": "What is the precise role of God (Īśvara) in Patañjali's Yoga compared to Nyāya? In Nyāya, God is the efficient creator of the universe; in Yoga, Īśvara is NOT a creator, but a special Puruṣa untouched by afflictions, serving as an optional object of meditation (Īśvara-praṇidhāna).",
        "wisdom_gist": "When the churning waters of the lake grow still, the pebbles at the bottom become visible. Stilling mental turbulence reveals the quiet, untroubled luminosity of consciousness."
    },
    {
        "id": "IND_CARVK_001",
        "unit_id": "UNIT_01",
        "tradition": "Indian",
        "school": "Cārvāka (Lokāyata)",
        "topic": "Materialism & Anti-Transcendentalism",
        "concept_name": "Cārvāka: Dehātmavāda & The Emergence of Consciousness",
        "chain": {
            "from_concept": "Vedic Sacrificialism & Post-Mortem Escapism",
            "current_thesis": "Consciousness is an emergent property of the four physical elements; there is no soul, afterlife, or transcendent realm.",
            "to_concept": "Epistemic Positivism & The Indian Problem of Induction"
        },
        "the_problem": "Can consciousness and psychological experience be fully accounted for without positing an eternal, non-physical soul entity?",
        "technical_lexicon": [
            {"term": "Dehātmavāda (देहात्मवाद)", "meaning": "The body itself is the self; consciousness is an attribute of the physical body."},
            {"term": "Kinva Analogy (किण्व सादृश्य)", "meaning": "Just as intoxicating power emerges from yeast and molasses, consciousness emerges from physical elements."},
            {"term": "Catur-Bhūta (चतुर्भूत)", "meaning": "Only 4 elements are real: Earth, Water, Fire, Air (rejecting unperceived Space/Ākāśa)."},
            {"term": "Sukhavāda (Hedonism)", "meaning": "Kāma (pleasure) is the only rational Puruṣārtha; virtue and wealth are mere instrumental means."}
        ],
        "dialectic": {
            "purvapaksha": "Realists argue: Consciousness cannot emerge from insentient matter! If matter had consciousness, a dead corpse would also be conscious.",
            "siddhanta": "Cārvāka retorts in Sarvadarśanasaṃgraha: Intoxication is absent in individual ingredients, yet emerges when combined in specific organic proportions. A dead body lacks the vital breath and organic integration. 'I am fat, I am thin'—ordinary linguistic usage proves the self is the living body, nothing more."
        },
        "primary_text": {
            "author": "Mādhava (doxographer) & Jayarāśi Bhaṭṭa",
            "work": "Sarvadarśanasaṃgraha & Tattvopaplavasiṃha",
            "passage": "Sarvadarśanasaṃgraha, Chapter 1 (Cārvāka-darśanam)"
        },
        "interview_trap": "Did Cārvāka accept Ākāśa (Ether/Space) as an element? NO! Because space is not directly perceived by the senses, Cārvāka accepts only 4 elements (pṛthivī, ap, tejas, vāyu). Another trap: Jayarāśi Bhaṭṭa's Tattvopaplavasiṃha goes further, rejecting even perception, leading to radical skepticism.",
        "wisdom_gist": "Do not sacrifice this precious, fragile, living embodiment on the altar of unprovable otherworldly promises. Cherish life with honesty and courage here and now."
    },
    {
        "id": "WEST_ANC_001",
        "unit_id": "UNIT_02",
        "tradition": "Western",
        "school": "Platonism",
        "topic": "Metaphysics of Forms & The Divided Line",
        "concept_name": "Plato: The Theory of Forms, Divided Line & Allegory of the Cave",
        "chain": {
            "from_concept": "Heraclitean Flux vs. Parmenidean Changeless Being",
            "current_thesis": "Sensory things are imperfect shadows of eternal, immutable, intelligible archetypes (Forms / Ideai) accessible only to reason.",
            "to_concept": "Aristotle's Hylomorphism (Grounding forms inside physical substances)"
        },
        "the_problem": "How can objective truth, knowledge, and moral ideals exist if everything in the sensory physical universe is constantly decaying and changing?",
        "technical_lexicon": [
            {"term": "Eidos / Idea (Form)", "meaning": "The transcendent, non-spatial, eternal essence of things (Justice, Beauty, Equality, The Good)."},
            {"term": "Divided Line (Grammē)", "meaning": "Four epistemic states: Eikasia (imagination), Pistis (belief), Dianoia (thought/math), Noesis (direct dialectical insight)."},
            {"term": "Methexis (Participation)", "meaning": "Sensory particulars exist by 'participating' in their transcendent Form."},
            {"term": "Anamnesis (Recollection)", "meaning": "Learning is not acquiring new data, but recollecting what the immortal soul knew before embodiment."}
        ],
        "dialectic": {
            "purvapaksha": "Sophists like Protagoras claimed 'Man is the measure of all things'—truth is subjective and relative to individual sensory impressions.",
            "siddhanta": "Plato proves in the Republic and Phaedo: Two sticks are never perfectly equal; they strive toward the concept of Equality itself. We could not judge things as imperfect unless our intellect already possessed the perfect standard. The Form of the Good is the sun of the intelligible universe."
        },
        "primary_text": {
            "author": "Plato",
            "work": "The Republic (Politeia)",
            "passage": "Books VI & VII (The Sun, the Divided Line, and the Cave: 507b–518d)"
        },
        "interview_trap": "What is the 'Third Man Argument' against the Theory of Forms? (Posed by Plato himself in the Parmenides): If particulars resemble a Form, must there not be a third Form to account for the resemblance between the particulars and the Form, ad infinitum?",
        "wisdom_gist": "We live chained to shadows on the wall of habit and convention. True education is the difficult, courageous ascent into the bright light of truth."
    },
    {
        "id": "WEST_ANC_002",
        "unit_id": "UNIT_02",
        "tradition": "Western",
        "school": "Aristotelianism",
        "topic": "Substance, Hylomorphism & Causes",
        "concept_name": "Aristotle: The Four Causes, Hylomorphism & Actuality/Potentiality",
        "chain": {
            "from_concept": "Plato's Transcendent Dual-World Theory of Forms",
            "current_thesis": "Forms do not float in a separate heaven; they are immanent in matter (Hylomorphism), realizing potentiality into actuality.",
            "to_concept": "Medieval Scholasticism (Aquinas's Five Ways & Essence-Existence)"
        },
        "the_problem": "How does natural change occur without creating reality out of nothing or freezing reality into Parmenidean immobility?",
        "technical_lexicon": [
            {"term": "Hylomorphism", "meaning": "Every concrete substance (ousia) is an indissoluble composite of Matter (potency) and Form (actuality)."},
            {"term": "Four Causes (Aitia)", "meaning": "Material (bronze), Formal (statue shape), Efficient (sculptor), Final (telos/honor)."},
            {"term": "Dunamis vs. Energeia", "meaning": "The acorn is potentially an oak tree; the mature oak tree is the realized actuality."},
            {"term": "Telos (Teleology)", "meaning": "Nature does nothing in vain; every entity is pulled forward by its inherent purpose or natural goal."}
        ],
        "dialectic": {
            "purvapaksha": "Plato separated the Form from the concrete horse, creating an unbridgeable metaphysical chasm.",
            "siddhanta": "Aristotle in Metaphysics Book VII argues: If forms exist separately, how do they cause change? Forms exist ONLY when instantiated in matter (except for the Unmoved Mover). Change is not impossible; change is the actualization of potentiality (energeia of dunamis)."
        },
        "primary_text": {
            "author": "Aristotle",
            "work": "Physics & Metaphysics",
            "passage": "Physics II.3 (Four Causes); Metaphysics VII–IX (Substance and Actuality)"
        },
        "interview_trap": "What is 'Primary Substance' (Prōtē Ousia) for Aristotle in the Categories vs Metaphysics? In the Categories, primary substance is the individual concrete particular (this man, this horse); in Metaphysics VII, it is identified with the essential Form that makes the matter this specific thing.",
        "wisdom_gist": "Growth is not an arbitrary accident. Within every seed, every thought, and every human being lies a slumbering potential waiting to flower into its true form."
    },
    {
        "id": "WEST_ANC_003",
        "unit_id": "UNIT_02",
        "tradition": "Western",
        "school": "Aristotelian Virtue Ethics",
        "topic": "Ethics & The Good Life",
        "concept_name": "Aristotle: Eudaimonia, Aretē & The Doctrine of the Mean",
        "chain": {
            "from_concept": "Platonic Idea of the Transcendent Good & Hedonism",
            "current_thesis": "The highest good is human flourishing (Eudaimonia) achieved through virtuous activity (Aretē) adhering to the Golden Mean.",
            "to_concept": "Modern Virtue Ethics (MacIntyre & Foot) vs Deontology/Utilitarianism"
        },
        "the_problem": "What is the ultimate end (telos) of human action that is desired for its own sake and never as a means to something else?",
        "technical_lexicon": [
            {"term": "Eudaimonia (Human Flourishing)", "meaning": "Activity of the soul in accordance with complete virtue across a complete life."},
            {"term": "Aretē (Excellence / Virtue)", "meaning": "The disposition of character that makes a human perform their unique function (ergon) well."},
            {"term": "Mesotēs (Doctrine of the Mean)", "meaning": "Virtue is the intermediate state between two vices: an excess and a deficiency."},
            {"term": "Phronēsis (Practical Wisdom)", "meaning": "The intellectual virtue that perceives the appropriate action, in the right way, for the right purpose."}
        ],
        "dialectic": {
            "purvapaksha": "Common men seek pleasure, politicians seek honor, and merchants seek wealth as the ultimate good of human life.",
            "siddhanta": "Aristotle dismantles these in Book I of Nicomachean Ethics: Pleasure reduces us to grazing cattle; honor depends on others rather than ourselves; wealth is merely a means to buy things. The supreme good must fulfill the unique human function (ergon)—which is rational activity in accordance with virtue."
        },
        "primary_text": {
            "author": "Aristotle",
            "work": "Nicomachean Ethics (Ēthika Nikomacheia)",
            "passage": "Book I (The Function Argument: 1097a–1098b) & Book II (The Mean: 1106a–1107a)"
        },
        "interview_trap": "Is the Golden Mean a rigid mathematical midpoint? ABSOLUTELY NOT! Aristotle emphasizes it is the mean 'relative to us' (pros hēmas). What is courageous for a seasoned soldier may be rash for an untrained child; practical wisdom (phronesis) discerns the context.",
        "wisdom_gist": "Virtue is not a sporadic act or a burdensome rule; it is an enduring habit of excellence. We become just by practicing just actions, and courageous by practicing courage."
    },
    {
        "id": "WEST_MOD_002",
        "unit_id": "UNIT_03",
        "tradition": "Western",
        "school": "Continental Rationalism",
        "topic": "Substance Monism & Pantheism",
        "concept_name": "Spinoza: Substance Monism (Deus sive Natura) & Intellectual Love of God",
        "chain": {
            "from_concept": "Cartesian Mind-Body Dualism (The pineal gland interaction problem)",
            "current_thesis": "There is only one infinite, eternal substance: God or Nature (Deus sive Natura); Mind and Matter are two of its infinite attributes.",
            "to_concept": "Leibniz's Monadology (Recovering pluralism and individual agency)"
        },
        "the_problem": "How can mind and body interact if they are completely separate Cartesian substances with zero common properties?",
        "technical_lexicon": [
            {"term": "Deus sive Natura (God or Nature)", "meaning": "Substance monism: God and the physical-mental universe are identical."},
            {"term": "Natura Naturans vs. Natura Naturata", "meaning": "Nature as active creating cause (substance) vs Nature as passive manifested modes."},
            {"term": "Conatus", "meaning": "The fundamental striving of every entity to persevere in its own being."},
            {"term": "Sub Specie Aeternitatis", "meaning": "Viewing events under the aspect of eternity, free from personal egoic bias."}
        ],
        "dialectic": {
            "purvapaksha": "Descartes posited two created substances (res cogitans and res extensa) needing God to mediate interaction in the brain.",
            "siddhanta": "Spinoza proves geometrically in the Ethics: By definition, a substance is that which is conceived through itself and needs no other concept. Two distinct substances with different attributes cannot affect each other. Therefore, only ONE infinite substance can exist: God. Mind and Body are not two separate things, but two parallel expressions of the same reality."
        },
        "primary_text": {
            "author": "Baruch Spinoza",
            "work": "Ethics (Ethica Ordine Geometrico Demonstrata)",
            "passage": "Part I (De Deo), Propositions 1–15 & Part V (On Human Freedom)"
        },
        "interview_trap": "Was Spinoza an atheist or a pantheist? Novalis called him 'a God-intoxicated man'! Spinoza rejected a transcendent personal creator who acts with human-like emotions or purposes; for Spinoza, teleology is human vanity projected onto the impersonal, beautiful necessity of Nature.",
        "wisdom_gist": "Freedom does not come from rebellious illusions of an uncaused free will, but from understanding the magnificent necessity of the cosmos and aligning our hearts with the whole."
    },
    {
        "id": "WEST_LANG_001",
        "unit_id": "UNIT_04",
        "tradition": "Western",
        "school": "Analytic Philosophy / Philosophy of Language",
        "topic": "Sense, Reference & Descriptions",
        "concept_name": "Frege: Sense (Sinn) & Reference (Bedeutung)",
        "chain": {
            "from_concept": "Locke's Ideational Theory of Meaning (Words refer to private ideas)",
            "current_thesis": "Meaning splits into the mode of presentation (Sense/Sinn) and the actual worldly object or truth-value (Reference/Bedeutung).",
            "to_concept": "Russell's Theory of Definite Descriptions (On Denoting)"
        },
        "the_problem": "How can an identity statement like 'The Morning Star is the Evening Star' be an informative discovery, while 'The Morning Star is the Morning Star' is a boring tautology?",
        "technical_lexicon": [
            {"term": "Sinn (Sense)", "meaning": "The objective cognitive mode of presentation (Art des Gegebenseins) contained within an expression."},
            {"term": "Bedeutung (Reference)", "meaning": "The actual object picked out in the world, or the truth-value (True or False) of a sentence."},
            {"term": "Context Principle (Kontextprinzip)", "meaning": "Never ask for the meaning of a word in isolation, but only in the context of a proposition."},
            {"term": "Truth-Value Gap", "meaning": "Sentences containing non-referring terms have a sense but lack a truth-value for Frege."}
        ],
        "dialectic": {
            "purvapaksha": "Mill claimed names are mere tags with denotation but no connotation. If 'Morning Star' and 'Evening Star' just denote the planet Venus, then 'a = b' says nothing more than 'a = a'.",
            "siddhanta": "Frege proves in 1892: 'Morning Star' and 'Evening Star' have the IDENTICAL Bedeutung (Venus), but totally DIFFERENT senses (Sinn). Identity statements expand knowledge when they inform us that two different modes of presentation pick out the same worldly object."
        },
        "primary_text": {
            "author": "Gottlob Frege",
            "work": "On Sense and Reference (Über Sinn und Bedeutung)",
            "passage": "Zeitschrift für Philosophie und philosophische Kritik (1892): 25–50"
        },
        "interview_trap": "What is the reference of a declarative sentence for Frege? The TRUTH-VALUE (The True or The False)! The sense of a sentence is the PROPOSITION or Thought (Gedanke). This is a standard UGC NET / Central University test question.",
        "wisdom_gist": "Words are not transparent glass. How we present a truth shapes what we understand. Two paths may lead to the same mountain, yet reveal completely different landscapes along the journey."
    },
    {
        "id": "WEST_ETH_001",
        "unit_id": "UNIT_04",
        "tradition": "Western",
        "school": "Kantian Moral Philosophy",
        "topic": "Deontology & Moral Autonomy",
        "concept_name": "Kant: The Categorical Imperative & Kingdom of Ends",
        "chain": {
            "from_concept": "Utilitarianism & Moral Sentimentalism (Hume: Reason is slave of passions)",
            "current_thesis": "Morality is grounded in pure practical reason; act only on maxims that can be willed as universal laws, treating persons as ends.",
            "to_concept": "Hegel's Critique of Kantian Moral Rigorism (Sittlichkeit vs Moralität)"
        },
        "the_problem": "Can moral duty hold unconditional necessity if moral rules depend on human desires, consequences, or emotional inclinations?",
        "technical_lexicon": [
            {"term": "Categorical vs. Hypothetical Imperative", "meaning": "Unconditional duty ('Do X!') vs Conditional prudence ('If you want Y, do X')."},
            {"term": "Formula of Universal Law", "meaning": "Act only according to that maxim whereby you can at the same time will that it should become a universal law."},
            {"term": "Formula of Humanity", "meaning": "Act in such a way that you treat humanity, whether in your own person or another, always as an end and never merely as a means."},
            {"term": "Autonomy of the Will", "meaning": "The moral agent is both author and subject of the moral law, free from heteronomous desires."}
        ],
        "dialectic": {
            "purvapaksha": "Utilitarians argue: An act is good because of its beneficial consequences; lying to save an innocent life produces net happiness.",
            "siddhanta": "Kant insists in the Groundwork: Only a GOOD WILL is good without qualification. If everyone made lying promises when in trouble, the very institution of promising would logically self-destruct (contradiction in conception). Moral worth lies in duty for duty's sake, not consequences."
        },
        "primary_text": {
            "author": "Immanuel Kant",
            "work": "Groundwork of the Metaphysics of Morals",
            "passage": "Sections I & II (Akademie 4:393–440)"
        },
        "interview_trap": "Distinguish 'Perfect Duties' from 'Imperfect Duties' in Kant: Perfect duties (do not lie, do not commit suicide) result in a 'contradiction in CONCEPTION' if universalized; Imperfect duties (cultivate talents, help others) result in a 'contradiction in the WILL'.",
        "wisdom_gist": "Human beings possess dignity, not a price. To treat another human being as a mere tool for our own convenience is to betray the sacred light of reason within ourselves."
    },
    {
        "id": "WEST_POL_001",
        "unit_id": "UNIT_04",
        "tradition": "Western",
        "school": "Political Philosophy / Liberalism",
        "topic": "Theories of Justice",
        "concept_name": "John Rawls: Justice as Fairness & The Veil of Ignorance",
        "chain": {
            "from_concept": "Classical Utilitarianism (Sacrificing minority rights for aggregate happiness)",
            "current_thesis": "Principles of justice are those that free and rational persons would agree to in an initial position of equality behind a Veil of Ignorance.",
            "to_concept": "Robert Nozick's Libertarian Entitlement Theory & Sen's Capabilities Approach"
        },
        "the_problem": "How can a democratic society construct fair, non-arbitrary terms of social cooperation among citizens divided by conflicting religious and philosophical doctrines?",
        "technical_lexicon": [
            {"term": "Original Position", "meaning": "A hypothetical thought experiment of pure procedural fairness ensuring impartial agreement."},
            {"term": "Veil of Ignorance", "meaning": "Parties know nothing of their own class, race, gender, intelligence, or conception of the good."},
            {"term": "First Principle (Equal Liberty)", "meaning": "Each person has an equal right to the most extensive system of equal basic liberties."},
            {"term": "Difference Principle", "meaning": "Social and economic inequalities are permissible ONLY if they work to the greatest benefit of the least-advantaged."}
        ],
        "dialectic": {
            "purvapaksha": "Utilitarians argue that social arrangements should maximize the total or average well-being of the majority, even if some suffer.",
            "siddhanta": "Rawls opens A Theory of Justice: 'Justice is the first virtue of social institutions, as truth is of systems of thought.' Each person possesses an inviolability founded on justice that even the welfare of society cannot override. Behind the veil, rational agents choose the MAXIMIN rule—protecting the worst-off position."
        },
        "primary_text": {
            "author": "John Rawls",
            "work": "A Theory of Justice (1971)",
            "passage": "Chapter 1 (§§ 1–4) & Chapter 2 (§§ 11–13 on Two Principles)"
        },
        "interview_trap": "What is the 'Lexical Priority' (lexicographical order) in Rawls? The First Principle (Equal Liberty) has absolute priority over the Second Principle! You cannot trade away fundamental civil and political liberties for economic gains.",
        "wisdom_gist": "A just society is measured not by the luxury of its billionaires or the grandeur of its monuments, but by the dignity and security it guarantees to its most vulnerable citizens."
    }
]

def main():
    with open(DB_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing_ids = {c["id"] for c in data.get("flashcards", [])}
    added_count = 0
    for card in MORE_CARDS:
        if card["id"] not in existing_ids:
            data["flashcards"].append(card)
            existing_ids.add(card["id"])
            added_count += 1

    data["total_cards"] = len(data["flashcards"])

    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Added {added_count} cards. Total flashcards in database: {data['total_cards']}!")

if __name__ == "__main__":
    main()
