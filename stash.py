class Statement:
    def __init__(self, symbol, balance, income, cashflow) -> None:
        self.symbol = symbol
        self.balance = balance
        self.income = income
        self.cashflow = cashflow


import json


def get_statement(path):
    with open(f"{path}", "r") as file:
        data = json.load(file)
        return data[0]


hpg = Statement(
    symbol="hpg",
    balance=get_statement("data/hpg-balance.json"),
    income=get_statement("data/hpg-income.json"),
    cashflow=get_statement("data/hpg-cashflow.json"),
)
vcb = Statement(
    symbol="vcb",
    balance=get_statement("data/vcb-balance.json"),
    income=get_statement("data/vcb-income.json"),
    cashflow=get_statement("data/vcb-cashflow.json"),
)
ssi = Statement(
    symbol="ssi",
    balance=get_statement("data/ssi-balance.json"),
    income=get_statement("data/ssi-income.json"),
    cashflow=get_statement("data/ssi-cashflow.json"),
)
vci = Statement(
    symbol="vci",
    balance=get_statement("data/vci-balance.json"),
    income=get_statement("data/vci-income.json"),
    cashflow=get_statement("data/vci-cashflow.json"),
)
vnm = Statement(
    symbol="vnm",
    balance=get_statement("data/vnm-balance.json"),
    income=get_statement("data/vnm-income.json"),
    cashflow=get_statement("data/vnm-cashflow.json"),
)
bvh = Statement(
    symbol="bvh",
    balance=get_statement("data/bvh-balance.json"),
    income=get_statement("data/bvh-income.json"),
    cashflow=get_statement("data/bvh-cashflow.json"),
)
pvi = Statement(
    symbol="pvi",
    balance=get_statement("data/pvi-balance.json"),
    income=get_statement("data/pvi-income.json"),
    cashflow=get_statement("data/pvi-cashflow.json"),
)
mbb = Statement(
    symbol="mbb",
    balance=get_statement("data/mbb-balance.json"),
    income=get_statement("data/mbb-income.json"),
    cashflow=get_statement("data/mbb-cashflow.json"),
)

symbol_list = [vnm, hpg, vcb, mbb, ssi, vci, bvh, pvi]
