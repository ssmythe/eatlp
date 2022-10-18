class BMI:
    """
    BMI is a class for determining target BMI weight
    """

    @staticmethod
    def inches_to_meters(inches):
        return round(inches / 39.37, 3)

    @staticmethod
    def kg_to_lbs(kg):
        return round(kg * 2.205, 0)

    @staticmethod
    def lbs_to_kg(lbs):
        return round(lbs / 2.205, 0)

    @staticmethod
    def height_meters_bmi_to_weight_kg(meters, bmi):
        return round(bmi * meters ** 2, 1)

    @staticmethod
    def height_inches_bmi_to_weight_lbs(inches, bmi):
        meters = BMI.inches_to_meters(inches)
        kg = bmi * meters ** 2
        return round(BMI.kg_to_lbs(kg), 0)

    @staticmethod
    def height_inches_weight_lbs_to_bmi(inches, weight_lbs):
        meters = BMI.height_inches_to_meters(inches)
        return round(BMI.lbs_to_kg(weight_lbs) * meters ** 2, 0)
