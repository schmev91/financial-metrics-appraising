print("===EV to EBIT")
from stash import Statement, symbol_list


def basic(stm: Statement):
    try:
        market_cap = int(stm.ratio["('Chỉ tiêu định giá', 'Market Capital (Bn. VND)')"])
        cash = int(stm.balance["Cash and cash equivalents (Bn. VND)"])

        shortterm_bor = int(stm.balance["Short-term borrowings (Bn. VND)"])
        longterm_bor = int(stm.balance["Long-term borrowings (Bn. VND)"])

        profit_bef_tax = int(stm.income["Profit before tax"])
        interest_expense = abs(int(stm.income["Interest Expenses"]))

        if 0 in [
            market_cap,
        ]:
            raise Exception()

        total_debt = shortterm_bor + longterm_bor

        # result = (market_cap + liabilities - cash) / (profit_bef_tax + interest_expense)
        result = (market_cap + total_debt - cash) / (profit_bef_tax + interest_expense)
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
