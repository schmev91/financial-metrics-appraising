print("===Return on Capital Employed")
from stash import Statement, symbol_list


def basic(stm: Statement):
    try:
        profit_bef_tax = int(stm.income["Profit before tax"])
        interest_expense = abs(int(stm.income["Interest Expenses"]))

        total_asset = int(stm.balance["TOTAL ASSETS (Bn. VND)"])
        curr_liabilities = int(stm.balance["Current liabilities (Bn. VND)"])

        if 0 in [profit_bef_tax, total_asset, curr_liabilities]:
            raise Exception()

        # result = ebit / (total_asset - curr_liabilities) * 100
        result = (
            (profit_bef_tax + interest_expense) / (total_asset - curr_liabilities) * 100
        )
        return result
    except:
        return None


formulars = [basic]

for stm in symbol_list:
    for formulation in formulars:
        result = formulation(stm)
        if result is not None:
            break
    print(f"{stm.symbol}: {result}")
