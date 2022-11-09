class BMI:
    """
    BMI is a class for determining target BMI weight
    """

    @staticmethod
    def inches_to_meters(inches):
        return round(inches / 39.37, 3)

    @staticmethod
    def kg_to_lbs(kg):
        return round(kg * 2.205, 1)

    @staticmethod
    def lbs_to_kg(lbs):
        return round(lbs / 2.205, 1)

    @staticmethod
    def height_meters_bmi_to_weight_kg(meters, bmi):
        return round(bmi * meters ** 2, 1)

    @staticmethod
    def height_inches_bmi_to_weight_lbs(inches, bmi_num):
        meters = BMI.inches_to_meters(inches)
        kg = bmi_num * meters * meters
        return round(BMI.kg_to_lbs(kg), 0)

    @staticmethod
    def height_inches_weight_lbs_to_bmi(inches, weight_lbs):
        meters = BMI.inches_to_meters(inches)
        kg = BMI.lbs_to_kg(weight_lbs)
        return round(kg / meters ** 2, 2)
