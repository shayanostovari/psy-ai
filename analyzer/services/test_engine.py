from analyzer.tests.beck_anxiety import calculate_score as bai_score

TEST_REGISTRY = {
    "BAI_21": bai_score,
}

def run_test(test_code: str, answers: dict) -> dict:
    if test_code not in TEST_REGISTRY:
        return {"error": "Unknown test code"}

    score_data = TEST_REGISTRY[test_code](answers)

    return {
        "test_code": test_code,
        "result": score_data,
    }
