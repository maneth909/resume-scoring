SCHEMA = {
    "UUID": "string",
    "Personal Data": {
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "phone": "string",
        "linkedin": "string",
        "portfolio": "string",
        "location": {"city": "string", "country": "string"},
    },
    "Experiences": [
        {
            "jobTitle": "string",
            "company": "string",
            "location": "string",
            "startDate": "YYYY-MM-DD",
            "endDate": "YYYY-MM-DD or Present",
            "description": ["string", "..."],
            "technologiesUsed": ["string", "..."],
        }
    ],
    # --- NEW SECTION ---
    # We add this new field to specifically capture extracurriculars and volunteer work.
    "Extracurricular Activities": [
        {
            "jobTitle": "string (e.g., 'Member', 'Volunteer', 'Trainer')",
            "company": "string (e.g., 'AIESEC', 'Spark project')",
            "location": "string",
            "startDate": "YYYY-MM-DD",
            "endDate": "YYYY-MM-DD or Present",
            "description": ["string", "..."],
            "technologiesUsed": ["string", "..."],
        }
    ],
    # --- END NEW SECTION ---
    "Projects": [
        {
            "projectName": "string",
            "description": "string",
            "technologiesUsed": ["string", "..."],
            "link": "string",
            "startDate": "YYYY-MM-DD",
            "endDate": "YYYY-MM-DD",
        }
    ],
    "Skills": [{"category": "string", "skillName": "string"}],
    "Research Work": [
        {
            "title": "string | null",
            "publication": "string | null",
            "date": "YYYY-MM-DD | null",
            "link": "string | null",
            "description": "string | null",
        }
    ],
    # --- RENAMED SECTION ---
    # Renamed to match your CV section and improve accuracy
    "Honors and Awards": ["string", "..."],
    # --- END RENAMED SECTION ---
    "Education": [
        {
            "institution": "string",
            "degree": "string | null",
            "fieldOfStudy": "string | null",
            "startDate": "YYYY-MM-DD",
            "endDate": "YYYY-MM-DD",
            "grade": "string",
            "description": "string",
        }
    ],
    "Extracted Keywords": ["string", "..."],
}