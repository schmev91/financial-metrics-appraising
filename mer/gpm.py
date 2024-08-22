print("===GPM")
from stash import Statement, symbol_list


def basic(stm: Statement):
    try:
        gross_profit = int(stm.income["Gross Profit"])
        revenue = int(stm.income["Net Sales"])

        result = (gross_profit / revenue) * 100
        return result
    except:
        return None


def using_cogs(stm: Statement):
    try:
        sales = abs(int(stm.income["Sales"]))
        deduction = abs(int(stm.income["Sales deductions"]))
        cogs = abs(int(stm.income["Cost of Sales"]))
        return (sales - deduction - cogs) / (sales - deduction) * 100
    except:
        return None


formulars = [basic, using_cogs]

for stm in symbol_list:
    for formulation in formulars:
        result = formulation(stm)
        if result is not None:
            break
    print(f"{stm.symbol}: {result}")
