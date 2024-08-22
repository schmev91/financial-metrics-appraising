print("===Debt to Equity")
from stash import Statement, symbol_list


def basic(stm: Statement):
    try:
        liabilities = int(stm.balance["LIABILITIES (Bn. VND)"])
        equity = int(stm.balance["OWNER'S EQUITY(Bn.VND)"])

        result = (liabilities / equity) * 100
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
