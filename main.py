from fastapi import FastAPI

from ranking_vc import ranking_vc
import dataset_initialization

services = dataset_initialization.initialize()


app = FastAPI()


@app.get("/vc/")
def recommend_vc(
        user_market: str,
        user_stage: str,
        user_requested_money_min: int,
        user_requested_money_max: int,
        user_required_consultation: bool,
        user_required_networking: bool,
        user_required_small_scale_production: bool,
        user_required_education: bool,
        user_required_orders: bool,
        user_required_quarters: bool,
        user_required_marketing: bool,
        user_required_value_proposition: bool,
        user_required_testing: bool,
        user_required_world: bool,
        user_required_legal_accounting: bool,
        user_required_scaling: bool,
        user_required_prototype_refinement: bool
):
    user_data = [
        user_market,
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
        user_required_legal_accounting,
        user_required_scaling,
        user_required_prototype_refinement
    ]

    service_type = 'Список венчурных фондов'
    df = services[service_type]
    rank_col_name = 'Rank'
    df[rank_col_name] = services[service_type].apply(lambda row :ranking_vc(row, user_data), axis=1)
    df = df[[rank_col_name] + df.columns[:-1].tolist()]

    rec_vc = df.sort_values(by=[rank_col_name], ascending=0)

    output = rec_vc.head(1).reset_index().to_json('json_vc_rec', force_ascii=False, orient='index')

    return output #{"Stage": user_stage, "Market": user_market, "user_data": user_data}
