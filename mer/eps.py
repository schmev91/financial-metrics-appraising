print("===EPS")
from stash import Statement, symbol_list


def basic(stm: Statement):
    try:
        # net_profit = int(stm.income["Net Profit For the Year"])
        net_profit = int(stm.income["Attributable to parent company"])
        shares = int(
            stm.ratio["('Chỉ tiêu định giá', 'Outstanding Share (Mil. Shares)')"]
        )

        result = net_profit / shares
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
