import re

def mask_pii(text):
    entities = []

    def _mask(pattern, label, text, group_idx=0, flags=0):
        matches = list(re.finditer(pattern, text, flags))
        offset = 0
        for match in matches:
            # determine which span to mask
            if group_idx == 0:
                start, end = match.start(0) + offset, match.end(0) + offset
                entity_text = match.group(0)
            else:
                start, end = match.start(group_idx) + offset, match.end(group_idx) + offset
                entity_text = match.group(group_idx)

            entities.append({
                "position": [start, end],
                "classification": label,
                "entity": entity_text
            })

            replacement = f"[{label}]"
            text = text[:start] + replacement + text[end:]
            offset += len(replacement) - (end - start)

        return text

    # 1) Two-word full names (skip "Dear Support")
    two_word_name = r"\b(?!Dear )[A-Z][a-z]+ [A-Z][a-z]+\b"
    text = _mask(two_word_name, "full_name", text)

    # 2) Single-word names in context (capture group 1)
    name_context = (
        r"(?:\b(?:my name is|I am|I(?:'|’)m|this is|my friend is)\s+)"
        r"([A-Z][a-z]+)\b"
    )
    text = _mask(name_context, "full_name", text, group_idx=1, flags=re.IGNORECASE)

    # 3) Emails (word-boundary so trailing punctuation isn’t swallowed)
    email_pattern = r"\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b"
    text = _mask(email_pattern, "email", text, flags=re.IGNORECASE)

    # 4) Phone numbers (10 digits)
    text = _mask(r"\b\d{10}\b", "phone_number", text)

    # 5) Date of birth (dd/mm/yyyy or dd-mm-yyyy)
    text = _mask(r"\b\d{2}[-/]\d{2}[-/]\d{4}\b", "dob", text)

    # 6) Aadhar numbers (xxxx xxxx xxxx)
    text = _mask(r"\b\d{4}\s\d{4}\s\d{4}\b", "aadhar_num", text)

    # 7) Credit/Debit card numbers (16 digits)
    text = _mask(r"\b\d{16}\b", "credit_debit_no", text)

    # 8) CVV (3 digits)
    text = _mask(r"\b\d{3}\b", "cvv_no", text)

    # 9) Expiry dates (MM/YY or MM/YYYY)
    text = _mask(r"\b(0[1-9]|1[0-2])\/\d{2,4}\b", "expiry_no", text)

    return text, entities

def demask_email(masked_email, entities):
    for ent in sorted(entities, key=lambda x: -x["position"][0]):
        start, end = ent["position"]
        masked_email = masked_email[:start] + ent["entity"] + masked_email[end:]
    return masked_email
