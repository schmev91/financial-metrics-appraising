import json
import pandas
from pandas import DataFrame
from vnstock3 import Vnstock

# ===
symbol = "vnm"
stock = Vnstock().stock(symbol=symbol, source="VCI")

# # BALANCE SHEET
# data: DataFrame = stock.finance.balance_sheet(period="quarter", lang="en")
# # Dump the data into the JSON file
# data = data.loc[:, ~data.columns.duplicated()]
# data.to_json(
#     f"data/{symbol}-balance.json", orient="records", indent=4, force_ascii=False
# )


# # INCOME STATEMENT
# data: DataFrame = stock.finance.income_statement(period="quarter", lang="en")
# # Dump the data into the JSON file
# data = data.loc[:, ~data.columns.duplicated()]
# data.to_json(
#     f"data/{symbol}-income.json", orient="records", indent=4, force_ascii=False
# )


# # CASHFLOW STATEMENT
# data: DataFrame = stock.finance.cash_flow(period="quarter", lang="en")
# # Dump the data into the JSON file
# data = data.loc[:, ~data.columns.duplicated()]
# data.to_json(
#     f"data/{symbol}-cashflow.json", orient="records", indent=4, force_ascii=False
# )

# Ratio
data: DataFrame = stock.finance.ratio(symbol=symbol, period="quarter", lang="en")
# Dump the data into the JSON file
data = data.loc[:, ~data.columns.duplicated()]
data.to_json(f"data/{symbol}-ratio.json", orient="records", indent=4, force_ascii=False)
