import numpy as np
import pandas as pd


def ranking_engineering(row, user_data, w_eng=[80, -100, 20, 20, 20, 20, 20, 20, 20, 20, 20]):

    [user_market,
     user_stage,
     user_requested_money_min,
     user_requested_money_max,
     user_required_consultation,
     user_required_networking,
     user_required_small_scale_production,
     user_required_education,
     user_required_orders,
     user_required_quarters,
     user_required_marketing,
     user_required_value_proposition,
     user_required_testing,
     user_required_world,
     user_required_scaling,
     user_required_legal_accounting,
     user_required_prototype_refinement] = user_data

    cond_market = user_market in str(row['Рынок'])
    cond_closed = not pd.isna(row['Дата закрытия'])

    importance_consultation = int('Консульт' in str(row['Сервисы.1'])) * user_required_consultation
    importance_networking = int('нетворкинг' in str(row['Сервисы.1'])) * user_required_networking
    importance_education = int('Образова' in str(row['Сервисы.1'])) * user_required_education
    importance_orders = int('заказчик' in str(row['Сервисы.1'])) * user_required_orders
    importance_marketing = int('маркетинг' in str(row['Сервисы.1'])) * user_required_marketing
    importance_testing = int('Тестирование' in str(row['Сервисы.1'])) * user_required_testing
    importance_legal_accounting = int(
        'юридическим / бухгалтерским' in str(row['Сервисы.1'])) * user_required_legal_accounting
    importance_small_scale_production = int('Мелкосерийное' in str(row['Сервисы.1'])) * user_required_small_scale_production
    importance_prototype_refinement = int('Прототип' in str(row['Сервисы.1'])) * user_required_prototype_refinement


    features = [cond_market, cond_closed,
                importance_consultation,
                importance_networking,
                importance_education,
                importance_orders,
                importance_marketing,
                importance_testing,
                importance_legal_accounting,
                importance_small_scale_production,
                importance_prototype_refinement]

    rank = np.dot(w_eng, features)

    return rank
