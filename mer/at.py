print("===Asset Turnover")
from stash import Statement, symbol_list


def basic(stm: Statement):
    try:
        net_sale = int(stm.income["Net Sales"])
        equity = int(stm.balance["TOTAL ASSETS (Bn. VND)"])

        result = (net_sale / equity) * 100
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
