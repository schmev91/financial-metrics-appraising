print("===Capital Employed")
from stash import Statement, symbol_list


def basic(stm: Statement):
    try:
        curr_liabilities = int(stm.balance["Current liabilities (Bn. VND)"])
        total_asset = int(stm.balance["TOTAL ASSETS (Bn. VND)"])

        if 0 in [total_asset, curr_liabilities]:
            raise Exception()

        result = total_asset - curr_liabilities

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
