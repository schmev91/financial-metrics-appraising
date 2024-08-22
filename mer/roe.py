print("===ROE")
from stash import Statement, symbol_list


def basic(stm: Statement):
    try:
        attribute_to_parent = int(stm.income["Attributable to parent company"])
        equity = int(stm.balance["OWNER'S EQUITY(Bn.VND)"])

        result = (attribute_to_parent / equity) * 100
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
