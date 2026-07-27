import re


def extract_parameters(text):
    report = {}

    VALID_PARAMETERS = [
        "Hemoglobin (Hb)",
        "Total RBC count",
        "Total WBC count",
        "Platelet Count",
        "Packed Cell Volume (PCV)",
        "Mean Corpuscular Volume (MCV)",
        "MCH",
        "MCHC",
        "RDW",
        "Neutrophils",
        "Lymphocytes",
        "Monocytes",
        "Eosinophils",
        "Basophils"
    ]

    # -------------------------
    # Patient Details
    # -------------------------

    name_match = re.search(r"([A-Z][A-Za-z. ]+)\nAge", text)
    age_match = re.search(r"Age\s*:\s*(\d+)", text)
    sex_match = re.search(r"Sex\s*:\s*(Male|Female|Other)", text)
    pid_match = re.search(r"PID\s*:\s*(\d+)", text)

    patient = {
        "name": name_match.group(1).strip() if name_match else None,
        "age": age_match.group(1) if age_match else None,
        "sex": sex_match.group(1) if sex_match else None,
        "pid": pid_match.group(1) if pid_match else None
    }

    # -------------------------
    # Blood Parameters
    # -------------------------

    pattern = r"([A-Za-z ()/%-]+?)\s+([0-9.]+)\s*(High|Low|Borderline)?"

    matches = re.findall(pattern, text)

    for parameter, value, status in matches:

        parameter = parameter.strip()

        # Ignore unwanted matches
        if parameter not in VALID_PARAMETERS:
            continue

        if status:
            report[parameter] = f"{value} {status}"
        else:
            report[parameter] = value

    return {
        "patient": patient,
        "report": report
    }