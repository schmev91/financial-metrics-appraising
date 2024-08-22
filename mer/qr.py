print("===Quick Ratio")
from stash import Statement, symbol_list


def basic(stm: Statement):
    try:
        curr_asset = int(stm.balance["CURRENT ASSETS (Bn. VND)"])
        curr_liabilities = int(stm.balance["Current liabilities (Bn. VND)"])
        inventories = int(stm.balance["Net Inventories"])

        if 0 in [curr_asset, inventories, curr_liabilities]:
            raise Exception()

        result = (curr_asset - inventories) / curr_liabilities
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
