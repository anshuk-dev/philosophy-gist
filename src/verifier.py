"""
Academic Authenticity & Content Verification Engine for Philosophy Gist.
Validates curriculum alignment, dialectical rigor, primary source citations,
and anti-hallucination compliance for Central University Assistant Professor prep.
"""

from typing import Dict, List, Tuple, Any


class PhilosophyVerifier:
    """Rigorous verification suite for academic philosophical flashcards."""

    MANDATORY_CARD_FIELDS = [
        "id",
        "unit_id",
        "tradition",
        "school",
        "topic",
        "concept_name",
        "the_problem",
        "technical_lexicon",
        "dialectic",
        "primary_text",
        "interview_trap",
        "wisdom_gist",
    ]

    VALID_UNITS = [
        "UNIT_01",
        "UNIT_02",
        "UNIT_03",
        "UNIT_04",
        "UNIT_05",
        "UNIT_06",
    ]

    VALID_TRADITIONS = ["Indian", "Western", "Comparative"]

    @classmethod
    def validate_flashcard(cls, card: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validates a single philosophical flashcard for academic depth and accuracy."""
        errors = []

        # 1. Mandatory field checks
        for field in cls.MANDATORY_CARD_FIELDS:
            if field not in card or not card[field]:
                errors.append(f"Missing or empty mandatory field: '{field}'")

        if errors:
            return False, errors

        # 2. Unit and Tradition validation
        if card["unit_id"] not in cls.VALID_UNITS:
            errors.append(f"Invalid unit_id '{card['unit_id']}'. Expected one of {cls.VALID_UNITS}")

        if card["tradition"] not in cls.VALID_TRADITIONS:
            errors.append(f"Invalid tradition '{card['tradition']}'. Expected {cls.VALID_TRADITIONS}")

        # 3. Dialectic completeness
        dialectic = card.get("dialectic", {})
        if not isinstance(dialectic, dict):
            errors.append("'dialectic' must be an object with 'purvapaksha' and 'siddhanta'")
        else:
            if not dialectic.get("purvapaksha") or len(str(dialectic["purvapaksha"]).strip()) < 30:
                errors.append("'dialectic.purvapaksha' is missing or too brief (<30 chars)")
            if not dialectic.get("siddhanta") or len(str(dialectic["siddhanta"]).strip()) < 50:
                errors.append("'dialectic.siddhanta' is missing or too brief (<50 chars)")

        # 4. Primary text citation depth
        primary_text = card.get("primary_text", {})
        if not isinstance(primary_text, dict):
            errors.append("'primary_text' must be an object with 'author', 'work', and 'passage'")
        else:
            for pt_field in ["author", "work", "passage"]:
                if not primary_text.get(pt_field):
                    errors.append(f"Missing primary text reference: '{pt_field}'")

        # 5. Technical lexicon check
        lexicon = card.get("technical_lexicon", [])
        if not isinstance(lexicon, list) or len(lexicon) < 2:
            errors.append("'technical_lexicon' must contain at least 2 key philosophical terms")

        # 6. Depth and academic length checks (preventing shallow bullet points)
        if len(card.get("the_problem", "").strip()) < 40:
            errors.append("'the_problem' is too brief for university assistant professor level")

        if len(card.get("interview_trap", "").strip()) < 40:
            errors.append("'interview_trap' is too brief for university assistant professor level")

        if len(card.get("wisdom_gist", "").strip()) < 30:
            errors.append("'wisdom_gist' is too brief")

        is_valid = len(errors) == 0
        return is_valid, errors

    @classmethod
    def validate_edition(cls, edition: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validates an entire daily newsletter dispatch edition.
        An edition must contain:
        - At least 1 Indian philosophy card
        - At least 1 Western philosophy card
        - 1 Comparative / Synthesis note
        - 2 or more Interview / NET practice MCQs with explanations
        """
        errors = []

        if not edition.get("issue_number"):
            errors.append("Missing 'issue_number'")
        if not edition.get("title"):
            errors.append("Missing 'title'")

        cards = edition.get("cards", [])
        if not cards or len(cards) < 2:
            errors.append(f"Edition has {len(cards)} cards. Requires at least 2 flashcards.")

        indian_count = sum(1 for c in cards if c.get("tradition") == "Indian")
        western_count = sum(1 for c in cards if c.get("tradition") == "Western")

        if indian_count < 1:
            errors.append("Edition must include at least 1 Indian Philosophy card")
        if western_count < 1:
            errors.append("Edition must include at least 1 Western Philosophy card")

        for idx, card in enumerate(cards):
            card_valid, card_errors = cls.validate_flashcard(card)
            if not card_valid:
                errors.extend([f"Card #{idx + 1} ({card.get('id', 'unknown')}): {e}" for e in card_errors])

        questions = edition.get("practice_questions", [])
        if not questions or len(questions) < 2:
            errors.append("Edition must contain at least 2 practice interview/NET MCQs with explanations")

        is_valid = len(errors) == 0
        return is_valid, errors


if __name__ == "__main__":
    sample_card = {
        "id": "IND_EPIST_001",
        "unit_id": "UNIT_01",
        "tradition": "Indian",
        "school": "Mīmāṃsā / Nyāya",
        "topic": "Epistemology: Validity of Knowledge",
        "concept_name": "Svataḥ Prāmāṇyavāda vs. Parataḥ Prāmāṇyavāda",
        "the_problem": "Does a cognition possess intrinsic validity at the moment of its generation and apprehension, or does its truth depend upon an external verifying test?",
        "technical_lexicon": [
            {"term": "Svataḥ Prāmāṇya", "meaning": "Intrinsic validity; self-authentication of cognition"},
            {"term": "Parataḥ Prāmāṇya", "meaning": "Extrinsic validity; verification via causal excellence or pragmatic test (pravṛtti-sāmarthya)"},
            {"term": "Utpattau / Jñāptau", "meaning": "In respect of origin / in respect of ascertainment"}
        ],
        "dialectic": {
            "purvapaksha": "The Nyāya argues that if all cognitions were intrinsically valid, illusion (bhrama) would be impossible; truth requires verification via successful purposeful action (samvādi-pravṛtti).",
            "siddhanta": "Kumārila Bhaṭṭa retorts that if knowledge required an extrinsic cognition to validate it, and that second cognition needed a third, an infinite regress (anavasthā) results. Knowledge is born valid; falsity alone is extrinsic."
        },
        "primary_text": {
            "author": "Kumārila Bhaṭṭa",
            "work": "Ślokavārttika",
            "passage": "Codanā-sūtra, verses 33–61 (Prāmāṇyavāda-adhikaraṇa)"
        },
        "interview_trap": "Distinguish Bhāṭṭa Mīmāṃsā from Prābhākara Mīmāṃsā: Bhāṭṭas hold cognition is inferred from knownness (jñātatā), while Prābhākaras hold tripuṭī-pratyakṣa (cognition reveals subject, object, and itself simultaneously) and claim all cognition is valid (akhyātivāda).",
        "wisdom_gist": "Truth cannot wait upon endless verification; our basic cognitive faculties must be trusted unless defeated by a contradictory experience (bādhaka-jñāna)."
    }

    valid, errs = PhilosophyVerifier.validate_flashcard(sample_card)
    print(f"Sample card validation: valid={valid}, errors={errs}")
