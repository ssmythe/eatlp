from src.user import *


class MSJE:
    """
    MSJE is a class for determining energy requirements based on the Mifflin - St. Jeor Equation
    https://academic.oup.com/ajcn/article-abstract/51/2/241/4695104

    BMR=(10*WeightLbs*KgPerPound)+(6.25*HeightInCm)-(5*Age)+MSJEYIntercept
    KgPerPound	0.45
    HeightInCm	190.50
    Age	54.00
    Sex Male
    MSJEMenYIntercept	5.00
    MSJEWomenYIntercept	-161.00


    T2Kcals=BMR*MSJEActivityFactor-WeightLossPerWeekLbs*500
    MSJEActivityFactor	1.20
    WeightLossPerWeekLbs	2.00
    ----
    MSJEActivityFactor (Physical Activity Factors)
    Sedentary (1.2) - desk job and little to no exercise
    Light Activity (1.375) - light exercise/sports 1-3 days/week
    Moderate Activity (1.55) - moderate exercise/sports 3-5 days/week
    Very Active (1.725) - hard exercise/sports 6-7 days/week
    Exceedingly Active (1.9) - hard daily exercise/sports and physical job or training
    ----
    """

    @staticmethod
    def inches_to_cm(inches):
        return round(inches * 2.54, 1)

    @staticmethod
    def height_inches_to_meters(height):
        return round(height / 39.37, 3)

    @staticmethod
    def weight_kg_to_lbs(weight):
        return round(weight * 2.205, 0)

    @staticmethod
    def yintercept(sex):
        return {'male': 5, 'female': -161}[sex]

    @staticmethod
    def dict_of_activity_factor():
        return {'sedentary': 1.2, 'light activity': 1.375, 'moderate activity': 1.55, 'very active': 1.75, 'exceedingly active': 1.9}

    @staticmethod
    def activity_factor(af):
        return MSJE.dict_of_activity_factor()[af]

    @staticmethod
    def bmr(weight_lbs, height_inches, age, sex):
        kg_per_pound = 0.453592
        return round((10 * weight_lbs * kg_per_pound) +
                     (6.25 * MSJE.inches_to_cm(height_inches)) -
                     (5 * age) + MSJE.yintercept(sex), 0)

    @staticmethod
    def target_kcals(starting_weight_lbs, current_weight_lbs, target_weight_lbs, height_inches, age, sex, activity_factor_str, weight_loss_per_week_lbs):
        curve_modifier = (current_weight_lbs - target_weight_lbs) / \
            (starting_weight_lbs - target_weight_lbs) * weight_loss_per_week_lbs
        return (round(MSJE.bmr(current_weight_lbs, height_inches, age, sex) *
                      MSJE.activity_factor(activity_factor_str) - curve_modifier * 500, 0))

    @staticmethod
    def target_kcal_user_target_weight_lbs(user, target_weight_lbs):
        start_weight_lbs = float(user.dict_of_user['start_weight_lbs'])
        current_weight_lbs = float(user.dict_of_user['current_weight_lbs'])
        height_inches = float(user.dict_of_user['height_inches'])
        current_age = int(user.dict_of_user['current_age'])
        sex = user.dict_of_user['sex']
        msje_activity_factor = user.dict_of_user['msje_activity_factor']
        weight_loss_per_week_lbs = float(user.dict_of_user['weight_loss_per_week_lbs'])
        curve_modifier = (current_weight_lbs - target_weight_lbs) / \
            (start_weight_lbs - target_weight_lbs) * weight_loss_per_week_lbs
        return (int(round(MSJE.bmr(current_weight_lbs, height_inches, current_age, sex) *
                      MSJE.activity_factor(msje_activity_factor) - curve_modifier * 500, 0)))
