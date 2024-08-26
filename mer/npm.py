print("===NPM")
from stash import Statement, symbol_list


def basic(stm: Statement):
    try:
        net_profit = int(stm.income["Net Profit For the Year"])
        revenue = int(stm.income["Net Sales"])

        result = (net_profit / revenue) * 100
        return result
    except:
        return None


def secondary(stm: Statement):
    try:
        net_profit = int(stm.income["Net Profit For the Year"])
        revenue = int(stm.income["Total operating revenue"])
        return net_profit / revenue * 100
    except:
        return None


def third(stm: Statement):
    try:
        net_profit = int(stm.income["Net Profit For the Year"])
        sales = int(stm.income["Sales"])
        deduction = int(stm.income["Sales deductions"])
        return net_profit / (sales - deduction) * 100
    except:
        return None


formulars = [basic, secondary, third]

for stm in symbol_list:
    for formulation in formulars:
        result = formulation(stm)
        if result is not None:
            break
    print(f"{stm.symbol}: {result}")
