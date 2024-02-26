

class MSJE:
    """
    MSJE is a class for determining energy requirements based on the
    Mifflin - St. Jeor Equation
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
    sedentary (1.2) - desk job and little to no exercise
    light activity (1.375) - light exercise/sports 1-3 days/week
    moderate activity (1.55) - moderate exercise/sports 3-5 days/week
    very active (1.725) - hard exercise/sports 6-7 days/week
    exceedingly active (1.9) - hard daily exercise/sports and physical job
      or training
    ----
    https://www.ncbi.nlm.nih.gov/books/NBK278991/?report=printable
    Table 12:
    Activity Factors for Different Physical Activity Levels
    -------------------------------------------------------
    Sedentary:      Light physical activity associated with typical
                    day-to-day life.
    Low Active:     Walking about 1.5 to 3 miles per day at 3 to 4
                    miles per hour, in addition to the light physical activity
                    associated with typical day-to-day life.
    Active:         Walking more than 3 miles per day at 3 to 4 miles per hour,
                    in addition to light physical activity associated with
                    typical day-to-day life: 60 minutes of at least moderate
                    intensity physical activity
    Very Active:    Walking more than 7.5 miles per day at 3 to 4 miles per
                    hour, in addition to light physical activity associated
                    with typical day-to-day life: 60 minutes of at least
                    moderate to vigorous intensity physical activity
    ----
    """

    @staticmethod
    def inches_to_cm(inches):
        return round(inches * 2.54, 1)

    @staticmethod
    def yintercept(sex):
        return {'male': 5, 'female': -161}[sex]

    @staticmethod
    def dict_of_activity_factor():
        return {'sedentary': 1.2, 'light activity': 1.375,
                'moderate activity': 1.55, 'very active': 1.75,
                'exceedingly active': 1.9}

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
    def target_kcal_user_target_weight_lbs(user, target_weight_lbs):
        start_weight_lbs = float(user.dict_of_user['start_weight_lbs'])
        current_weight_lbs = float(user.dict_of_user['current_weight_lbs'])
        height_inches = float(user.dict_of_user['height_inches'])
        current_age = int(user.dict_of_user['current_age'])
        sex = user.dict_of_user['sex']
        msje_activity_factor = user.dict_of_user['msje_activity_factor']
        weight_loss_per_week_lbs = float(
            user.dict_of_user['weight_loss_per_week_lbs'])
        if weight_loss_per_week_lbs == 0:
            weight_loss_per_week_lbs = 0.01
        curve_modifier = (current_weight_lbs - target_weight_lbs) / \
            (start_weight_lbs - target_weight_lbs) * weight_loss_per_week_lbs
        return (int(round(MSJE.bmr(
            current_weight_lbs, height_inches, current_age, sex
        ) * MSJE.activity_factor(
            msje_activity_factor) - curve_modifier * 500, 0)
        )
        )
