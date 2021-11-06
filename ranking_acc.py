import numpy as np
import pandas as pd


def ranking_acc(row, user_data, w=[10, 5, 10, -100, 20, 20, 20, 20, 20, 20, 60]):

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

    name = str(row['Название объекта'])
    min_funding = int(str(row['Объем инвестиций ОТ, $']).replace(" ", "")) if not pd.isna(
        row['Объем инвестиций ОТ, $']) else 0
    max_funding = int(str(row['Объем инвестиций ДО, $']).replace(" ", "")) if not pd.isna(
        row['Объем инвестиций ДО, $']) else 0

    cond_funding = (user_requested_money_max > min_funding) and (user_requested_money_max < max_funding) or (
                user_requested_money_min > min_funding) and (user_requested_money_min < max_funding)
    cond_market = user_market in str(row['Рынок'])
    cond_stage = user_stage in str(row['Стадия стартапа'])
    cond_closed = not pd.isna(row['Дата закрытия'])

    importance_consultation = int('Консульт' in str(row['Сервисы'])) * user_required_consultation
    importance_networking = int('нетворкинг' in str(row['Сервисы'])) * user_required_networking
    importance_education = int('Образова' in str(row['Сервисы'])) * user_required_education
    importance_orders = int('заказчик' in str(row['Сервисы'])) * user_required_orders
    importance_marketing = int('маркетинг' in str(row['Сервисы'])) * user_required_marketing
    importance_testing = int('Тестирование' in str(row['Сервисы'])) * user_required_testing
    importance_legal_accounting = int(
        'юридическим / бухгалтерским' in str(row['Сервисы'])) * user_required_legal_accounting

    features = [cond_funding, cond_market, cond_stage, cond_closed,
                importance_consultation,
                importance_networking,
                importance_education,
                importance_orders,
                importance_marketing,
                importance_testing,
                importance_legal_accounting]

    rank = np.dot(w, features)

    return rank
