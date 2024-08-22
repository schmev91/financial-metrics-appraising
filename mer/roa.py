print("===ROA")
from stash import Statement, symbol_list


def basic(stm: Statement):
    try:
        attribute_to_parent = int(stm.income["Attributable to parent company"])
        total_asset = int(stm.balance["TOTAL ASSETS (Bn. VND)"])

        result = (attribute_to_parent / total_asset) * 100
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
