from src.bmi import BMI


def test_height_meters_bmi_to_weight_kg():
    assert BMI.height_meters_bmi_to_weight_kg(1.905, 21.7) == 78.7


def test_inches_to_meters():
    assert BMI.inches_to_meters(75) == 1.905


def test_kg_to_lbs():
    assert BMI.kg_to_lbs(78.7) == 173.5


def test_height_inches_bmi_to_weight_lbs():
    assert BMI.height_inches_bmi_to_weight_lbs(75, 21.7) == 174


def test_height_inches_weight_lbs_to_bmi():
    assert BMI.height_inches_weight_lbs_to_bmi(75, 174) == 21.74
