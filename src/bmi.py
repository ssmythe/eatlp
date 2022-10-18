class BMI:
    """
    BMI is a class for determining target BMI weight
    """

    @staticmethod
    def height_meters_bmi_to_weight_kg(meters, bmi):
        return round(bmi * meters ** 2, 1)

    @staticmethod
    def height_inches_bmi_to_weight_lbs(inches, bmi):
        meters = BMI.height_inches_to_meters(inches)
        kg = bmi * meters ** 2
        return round(BMI.weight_kg_to_lbs(kg), 0)

    @staticmethod
    def height_inches_to_meters(height):
        return round(height / 39.37, 3)

    @staticmethod
    def weight_kg_to_lbs(weight):
        return round(weight * 2.205, 0)

