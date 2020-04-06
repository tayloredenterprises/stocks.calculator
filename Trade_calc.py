import time
loop = True;

    # determines number of shares
def shares():
    print("\033[0;33m")
    print("Number of Shares\n")
    print("\033[1;34m")
    time.sleep(1)
    buy_limit1 = input("Enter Buy Price: ")
    invest_amt1 = input("Consideration Amount: ")
    # convert to number of shares
    shares1 = int(round(invest_amt1 / buy_limit1))
    print("\033[1;35m")
    print("Crunching the Numbers...")
    time.sleep(1)
    print("\033[1;31;32m")
    print("Results:")
    print("---------------------------")
    print("Number of Shares = " + str(shares1))
    print("---------------------------")

    # determines gross profit or loss for a buy and sell situation
def profit_calc():
    print("\033[0;33m")
    print("Profit & Loss Calculator\n")
    print("\033[1;34m")
    time.sleep(1)
    buy_limit2 = input("Enter Buy Price: ")
    invest_amt2 = input("Consideration Amount: ")
    # convert to number of shares
    shares2 = int(round(invest_amt2 / buy_limit2))
    # enter sell price
    sell_price = input("Enter Sell Price: ")
    # include broker costs and add to broker_fees2 variable. Return function later.
    def broker1():
        if invest_amt2 <= 1000:
            broker2_fees = 20
        else:
            broker2_fees = 40
        return broker2_fees
    broker2_fees = broker1()
    gross_profit = int(round(shares2 * sell_price - invest_amt2))
    net_profit = (gross_profit - broker2_fees)
    print("\033[1;35m")
    print("Crunching the Numbers...")
    time.sleep(1)
    print("\033[1;31;32m")
    print("Results:")
    print("------------------------------")
    print("Shares = " + str(shares2))
    print("------------------------------")
    print("Gross P\L = $" + str(gross_profit))
    print("Net P\L   = $" + str(net_profit))
    print("------------------------------")
    print("")

    # provides sell price per share based on number of shares owned, purchase price, and investment amount
def sell_calc():
    print("\033[1;33m")
    p
    ("\033[1;34m")
    time.sleep(1)
    buy_limit = input("Enter Buy Price: ")
    invest_amt = input("Enter consideration: ")
    # convert to number of shares
    shares = int(round(invest_amt / buy_limit, 0))
    # input desired profit
    profit_amt = input("How much profit (in $) ")
    # include broker costs and add to broker_fees variable. Return function later.
    def broker2():
        if invest_amt <= 1000:
           broker_fees = 20
        else:
           broker_fees = 40
        return broker_fees
    broker_fees = broker2()
    # convert original buy price to adjusted price to account for brokerage fees.
    adjusted_buy = float(invest_amt + broker_fees) / shares
    #round adjusted buy separately to allow sub dollar figures 
    adjusted_buy_rounded = round(adjusted_buy, 2)
    # convert amount desired to percent profit and a whole percent
    profit_percent = float(profit_amt) / float(invest_amt)
    profit_percent_whole = int(profit_percent * 100)
    # calculate sell price and round
    sell = float(adjusted_buy_rounded + (adjusted_buy_rounded * profit_percent))
    sell_rounded = round(sell, 2)
    print("\033[1;35m")
    print("Crunching the Numbers...")
    time.sleep(1)
    print("\033[1;31;32m")
    print("Results:")
    print("------------------------------")
    print("Number of shares = " + str(shares))
    time.sleep(0.3)
    print("Desired Profit = " + str(profit_percent_whole) + '%')
    time.sleep(0.3)
    print("------------------------------")
    print("Brokerage fees = $" + str(broker_fees))
    time.sleep(0.3)
    print("Adjusted Buy Price = " + str(adjusted_buy_rounded))
    time.sleep(0.3)
    print("------------------------------")
    print("Optimal Sell Price = " + str(sell_rounded))
    print("------------------------------")

    # calculates the average purchase price, number of shares, and P/L for combined share purchases
def weighted_buy():
    print("\033[0;33m")
    print("Weighted Average Price\n")
    print("\033[1;34m")
    time.sleep(1)
    buy_limit3 = input("Transaction #1 Buy: ")
    invest_amt3 = input("Transaction #1 Consideration: ")
    buy_limit4 = input("Transaction #2 Buy: ")
    invest_amt4 = input("Transaction #2 Consideration: ")
    # convert to number of shares
    shares3 = int(round(invest_amt3 / buy_limit3))
    shares4 = int(round(invest_amt4 / buy_limit4))
    shares_total = (shares3 + shares4)
    investment_total = (invest_amt3 + invest_amt4)
    # enter sell price
    sell_price2 = input("Enter Final Sell Price: ")
    # include broker costs and add to broker_fees2 variable. Return function later.
    def broker3():
        if invest_amt3 <= 1000:
            broker3_fees = 10
        else:
            broker3_fees = 20
        return broker3_fees
    broker3_fees = broker3()
    # second broker fee calculation required for second stock
    # args: adds invest_amt4 to broker3_fees to produce figure for broker_total variable
    def broker4():
        if invest_amt4 <= 1000:
            broker4_fees = 10
        else:
            broker4_fees = 20
        return broker4_fees
    broker4_fees = broker4()
    # broker5 adds broker sale fee to overall calculation
    def broker5():
        if investment_total <= 1000:
            broker5_fees = 10
        else:
            broker5_fees = 20
        return broker5_fees
    broker5_fees = broker5()
    broker_total = broker3_fees + broker4_fees + broker5_fees
    # convert original buy price to adjusted price to account for brokerage fees.
    price_by_shares3 = (buy_limit3 * shares3)
    price_by_shares4 = (buy_limit4 * shares4)
    combined = round((price_by_shares3 + price_by_shares4) / shares_total, 2)
    gross_profit2 = int(round((shares_total * sell_price2) - (investment_total)))
    net_profit2 = int(gross_profit2 - broker_total)
    print("\033[1;35m")
    print("Crunching the Numbers...")
    time.sleep(1)
    print("\033[1;31;32m")
    print("Results: \n")
    print("------------------------------")
    print("Weighted Average Price: " + str(combined))
    print("------------------------------")
    print("Shares:")
    print("Transaction #1 Shares = " + str(shares3))
    print("Transaction #2 Shares = " + str(shares4))
    print("Total Shares          = " + str(shares_total))
    print("------------------------------")
    print("Profit or Loss:")
    print("Gross = $" + str(gross_profit2))
    print("Net   = $" + str(net_profit2))
    print("------------------------------")
    print("")

# menu
while loop:
    def menu():
        print("")
        print("\033[0;37;36mWelcome to Aaron's Trade Calculator!")
        print("\033[0;32m")
        print('1) Number of Shares')
        print('2) Profit & Loss')
        print('3) Sell Price')
        print('4) Weighted Average Price')

        ans = 0
        while not ans:
            try:
                ans = int(input('Choose an option: '))
                if ans not in (1, 2, 3, 4):
                    raise ValueError
            except ValueError:
                ans = 0
                print("That's not an option!")

        if ans == 1:
            shares()
        elif ans == 2:
            profit_calc()
        elif ans == 3:
            sell_calc()
        elif ans == 4:
            weighted_buy()
        return None
    menu()
loop = False;