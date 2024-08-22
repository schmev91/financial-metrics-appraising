print("===Asset Turnover")
from stash import Statement, symbol_list


def basic(stm: Statement):
    try:
        net_sale = int(stm.income["Net Sales"])
        equity = int(stm.balance["TOTAL ASSETS (Bn. VND)"])

        if 0 in [net_sale, equity]:
            raise Exception()

        result = net_sale / equity
        return result
    except:
        return None


def second(stm: Statement):
    try:
        equity = int(stm.balance["TOTAL ASSETS (Bn. VND)"])
        sales = abs(int(stm.income["Sales"]))
        deduction = abs(int(stm.income["Sales deductions"]))

        if 0 in [sales, equity]:
            raise Exception()

        result = (sales - deduction) / equity
        return result
    except:
        return None


formulars = [basic, second]

for stm in symbol_list:
    for formulation in formulars:
        result = formulation(stm)
        if result is not None:
            break
    print(f"{stm.symbol}: {result}")
