TEST_CODE = "BAI_21"
QUESTION_COUNT = 21
SCALE_MIN = 0
SCALE_MAX = 3

LEVELS = [
    (0, 7, "حداقل اضطراب"),
    (8, 15, "اضطراب خفیف"),
    (16, 25, "اضطراب متوسط"),
    (26, 63, "اضطراب شدید"),
]

def calculate_score(answers: dict) -> dict:
    total = 0

    for i in range(1, QUESTION_COUNT + 1):
        value = answers.get(str(i))
        if value is None:
            raise ValueError(f"Missing answer for question {i}")

        if not (SCALE_MIN <= value <= SCALE_MAX):
            raise ValueError(f"Invalid value for question {i}")

        total += value

    level = next(
        label for low, high, label in LEVELS if low <= total <= high
    )

    return {
        "total_score": total,
        "level": level,
    }
