def rule_based(score, documents_complete, attendance, discipline_clear):
    if (score >= 70 and
        documents_complete and
        attendance >= 75 and
        discipline_clear):

        return "Review"
    else:
        return "Hold"
test_cases = [
    {
        "score": 85,
        "documents_complete": True,
        "attendance": 80,
        "discipline_clear": True,
        "expected": "Review",
        "reason": "All conditions are satisfied."
    },
    {
        "score": 85,
        "documents_complete": True,
        "attendance": 70,
        "discipline_clear": True,
        "expected": "Hold",
        "reason": "Attendance is below the required 75%."
    },
    {
        "score": 85,
        "documents_complete": True,
        "attendance": 80,
        "discipline_clear": False,
        "expected": "Hold",
        "reason": "Discipline condition is not satisfied."
    },
    {
        "score": 70,
        "documents_complete": True,
        "attendance": 75,
        "discipline_clear": True,
        "expected": "Review",
        "reason": "Score is exactly at the threshold of 70."
    }
]
for i, case in enumerate(test_cases, 1):

    actual = rule_based(
        case["score"],
        case["documents_complete"],
        case["attendance"],
        case["discipline_clear"]
    )

    print("Case", i)
    print("Input:", {
        "score": case["score"],
        "documents_complete": case["documents_complete"],
        "attendance": case["attendance"],
        "discipline_clear": case["discipline_clear"]
    })
    print("Expected Result:", case["expected"])
    print("Actual Result:", actual)
    print("Reason:", case["reason"])
    print()