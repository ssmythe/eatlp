class MSJE:
    """
    MSJE is a class for determining energy requirements based on the
    Mifflin - St. Jeor Equation
    https://academic.oup.com/ajcn/article-abstract/51/2/241/4695104

    BMR=(10*WeightLbs*KgPerPound)+(6.25*HeightInCm)-(5*Age)+MSJEYIntercept
    KgPerPound  0.45359237
    HeightInCm  190.50
    Age 54.00
    Sex Male
    MSJEMenYIntercept   5.00
    MSJEWomenYIntercept -161.00

    T2Kcals=BMR*MSJEActivityFactor-WeightLossPerWeekLbs*500
    MSJEActivityFactor  1.20
    WeightLossPerWeekLbs    2.00
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
        return inches * 2.54

    @staticmethod
    def yintercept(sex):
        return {'male': 5, 'female': -161}[sex.strip().lower()]

    @staticmethod
    def dict_of_activity_factor():
        return {
            'sedentary': 1.2,
            'light activity': 1.375,
            'moderate activity': 1.55,
            'very active': 1.725,
            'exceedingly active': 1.9
        }

    @staticmethod
    def activity_factor(af):
        return MSJE.dict_of_activity_factor()[af.strip().lower()]

    @staticmethod
    def bmr(weight_lbs, height_inches, age, sex):
        kg_per_pound = 0.45359237
        weight_kg = weight_lbs * kg_per_pound
        height_cm = MSJE.inches_to_cm(height_inches)
        return (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + MSJE.yintercept(sex)

    @staticmethod
    def target_kcal_user_target_weight_lbs(user, target_weight_lbs=None):
        """
        Calculates daily target calories based on current weight, TDEE, 
        and desired weekly weight loss rate.
        Note: target_weight_lbs is retained as an optional argument to maintain 
        backwards compatibility with existing caller signatures.
        """
        current_weight_lbs = float(user.dict_of_user['current_weight_lbs'])
        height_inches = float(user.dict_of_user['height_inches'])
        current_age = int(user.dict_of_user['current_age'])
        sex = user.dict_of_user['sex']
        msje_activity_factor = user.dict_of_user['msje_activity_factor']
        weight_loss_per_week_lbs = float(user.dict_of_user['weight_loss_per_week_lbs'])

        bmr_val = MSJE.bmr(current_weight_lbs, height_inches, current_age, sex)
        tdee = bmr_val * MSJE.activity_factor(msje_activity_factor)
        
        # 1 lb/week of fat loss requires ~500 kcal daily deficit
        daily_deficit = weight_loss_per_week_lbs * 500.0
        
        return int(round(tdee - daily_deficit))

    