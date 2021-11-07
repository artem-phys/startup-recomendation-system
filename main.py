import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import dataset_initialization
from ranking_acc import ranking_acc
from ranking_engineering import ranking_engineering
from ranking_incubators import ranking_incubators
from ranking_institutes import ranking_institutes
from ranking_vc import ranking_vc

services = dataset_initialization.initialize()


app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    df[rank_col_name] = services[service_type].apply(lambda row: ranking_vc(row, user_data), axis=1)
    df = df[[rank_col_name] + df.columns[:-1].tolist()]

    rec_vc = df.sort_values(by=[rank_col_name], ascending=0)

    output_json = rec_vc.iloc[:10, :].reset_index().to_json(force_ascii=False, orient='index')

    return JSONResponse(content=json.loads(output_json))


@app.get("/acc/")
def recommend_acc(
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

    service_type = 'Список акселераторов'
    df = services[service_type]
    rank_col_name = 'Rank'
    df[rank_col_name] = services[service_type].apply(lambda row: ranking_acc(row, user_data), axis=1)
    df = df[[rank_col_name] + df.columns[:-1].tolist()]

    rec_acc = df.sort_values(by=[rank_col_name], ascending=0)

    output_json = rec_acc.iloc[:10, :].reset_index().to_json(force_ascii=False, orient='index')

    return JSONResponse(content=json.loads(output_json))


@app.get("/incubators/")
def recommend_incubators(
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

    service_type = 'Список бизнес-инкубаторов'
    df = services[service_type]
    rank_col_name = 'Rank'
    df[rank_col_name] = services[service_type].apply(lambda row: ranking_incubators(row, user_data), axis=1)
    df = df[[rank_col_name] + df.columns[:-1].tolist()]

    rec_incubators = df.sort_values(by=[rank_col_name], ascending=0)

    output_json = rec_incubators.iloc[:10, :].reset_index().to_json(force_ascii=False, orient='index')

    return JSONResponse(content=json.loads(output_json))


@app.get("/institutes/")
def recommend_institutes(
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

    service_type = 'Список институтов развития'
    df = services[service_type]
    rank_col_name = 'Rank'
    df[rank_col_name] = services[service_type].apply(lambda row: ranking_institutes(row, user_data), axis=1)
    df = df[[rank_col_name] + df.columns[:-1].tolist()]

    rec_institutes = df.sort_values(by=[rank_col_name], ascending=0)

    output_json = rec_institutes.iloc[:10, :].reset_index().to_json(force_ascii=False, orient='index')

    return JSONResponse(content=json.loads(output_json))


@app.get("/engineering/")
def recommend_engineering(
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

    service_type = 'Список инжиниринговых центров'
    df = services[service_type]
    rank_col_name = 'Rank'
    df[rank_col_name] = services[service_type].apply(lambda row: ranking_engineering(row, user_data), axis=1)
    df = df[[rank_col_name] + df.columns[:-1].tolist()]

    rec_engineering = df.sort_values(by=[rank_col_name], ascending=0)

    output_json = rec_engineering.iloc[:10, :].reset_index().to_json(force_ascii=False, orient='index')

    return JSONResponse(content=json.loads(output_json))
