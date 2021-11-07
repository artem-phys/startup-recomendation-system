import numpy as np
import pandas as pd


def ranking_acc(row, user_data, w_acc=[80, 80, 80, -1000, 10, 10, 10, 10, 10, 10, 10, 40]):

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

    min_funding = int(str(row['Объем инвестиций ОТ, $']).replace(" ", "")) if not pd.isna(
        row['Объем инвестиций ОТ, $']) else 0
    max_funding = int(str(row['Объем инвестиций ДО, $']).replace(" ", "")) if not pd.isna(
        row['Объем инвестиций ДО, $']) else 0

    cond_funding = (user_requested_money_max > min_funding) and (user_requested_money_max < max_funding) or (
                user_requested_money_min > min_funding) and (user_requested_money_min < max_funding)
    cond_market = user_market in str(row['Рынок'])
    cond_stage = user_stage in str(row['Стадия стартапа'])
    cond_closed = int('закрыта' in str(row['Статус программы']))

    target_importance = 3 # additional cost for existence of a requirement in program targets

    importance_consultation = (int('Консульт' in str(row['Сервисы'])) + 3 * int('Консульт' in str(row['Цель программы']))) * user_required_consultation
    importance_networking = (int('нетворкинг' in str(row['Сервисы'])) + 3 * int('нетворкинг' in str(row['Цель программы']))) * user_required_networking
    importance_education = (int('Образова' in str(row['Сервисы'])) + 3 * int('Образова' in str(row['Цель программы']))) * user_required_education
    importance_orders = (int('заказчик' in str(row['Сервисы'])) + 3 * int('заказчик' in str(row['Цель программы']))) * user_required_orders
    importance_marketing = (int('маркетинг' in str(row['Сервисы'])) + 3 * int('маркетинг' in str(row['Цель программы']))) * user_required_marketing
    importance_testing = (int('Тестирование' in str(row['Сервисы'])) + 3 * int('Тестирование' in str(row['Цель программы']))) * user_required_testing
    importance_legal_accounting = (int(
        'юридическим / бухгалтерским' in str(row['Сервисы'])) + 3 * int('юридическим / бухгалтерским' in str(row['Цель программы']))) * user_required_legal_accounting

    is_free = row['Условия участия'] == 'Бесплатно'

    features = [cond_funding, cond_market, cond_stage, cond_closed,
                importance_consultation,
                importance_networking,
                importance_education,
                importance_orders,
                importance_marketing,
                importance_testing,
                importance_legal_accounting,
                is_free]

    rank = np.dot(w_acc, features)

    return rank
