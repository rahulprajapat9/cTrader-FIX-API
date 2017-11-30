import random
import matplotlib
from matplotlib import pyplot
import time
import pandas

def read_gold_data():
    gold_data = pandas.DataFrame.from_csv("gold_data_more.csv")
    gold_data = gold_data[['open','high','low','close']]
    gold_data.reset_index()

    gold_data = gold_data.iloc[::-1]

    return gold_data

def doubler_bettor_gold(funds, gold_data):

    initial_wager = 100

    value = funds
    wager = initial_wager
    previousWagerAmount = initial_wager

    total_loss = 0
    total_profit = 0

    shares = 1
    trade_init = gold_data.iloc[0]['open']
    print '\nBOUGHT the very first at ', trade_init

    SL_pct = 0.22
    TP_pct = 0.4

    wX = []
    vY = []

    number_of_trades = 1
    if number_of_trades % 2:
        SL = trade_init - trade_init * SL_pct / 100
        TP = trade_init + trade_init * TP_pct / 100
        target = [SL, TP]

        event = ['Stop loss', 'Target point']
        print 'SL: ',SL,', TP:',TP,'\n'
        next_trade = 'SOLD'

        wX.append(number_of_trades)
        vY.append(value)

    else:
        SL = trade_init + trade_init * SL_pct / 100
        TP = trade_init - trade_init * TP_pct / 100
        target = [TP, SL]

        event = ['Target point', 'Stop loss']
        print 'TP:',TP,', SL: ',SL,'\n'
        next_trade = 'BOUGHT'

        wX.append(number_of_trades)
        vY.append(value)

    for i in range(gold_data.shape[0]):
        min_of_trade = min(
            gold_data.iloc[i]['open'],
            gold_data.iloc[i]['low'],
            gold_data.iloc[i]['high'],
            gold_data.iloc[i]['close'],
        )
        max_of_trade = max(
            gold_data.iloc[i]['open'],
            gold_data.iloc[i]['low'],
            gold_data.iloc[i]['high'],
            gold_data.iloc[i]['close'],
        )

        # 0 : Buy
        # 1 : Sell
        # If else statement are devided on the basis of buy and sell only

        if min_of_trade < target[0]:
            print 'Trade number: ', number_of_trades
            print next_trade+' number of shares ', shares
            print event[0],' triggered at ',i+1,' number. Trade executed at value ', target[0]

            trade_init = target[0]

            if event[0] == 'Stop loss':

                loss = abs(trade_init-SL)
                loss = loss*shares
                total_loss += loss
                print 'Loss: ', loss

                shares = shares*2
                value -= wager
                wager = previousWagerAmount * 2
                previousWagerAmount = wager

            else:

                profit = abs(trade_init - TP)
                profit = profit*shares
                total_profit += profit
                print 'Profit: ', profit

                shares = 1
                value += wager
                wager = initial_wager
                previousWagerAmount = wager

            number_of_trades += 1
            if number_of_trades % 2:
                SL = trade_init - trade_init * SL_pct / 100
                TP = trade_init + trade_init * TP_pct / 100
                target = [SL, TP]

                event = ['Stop loss', 'Target point']
                print 'SL: ', SL, ', TP:', TP, '\n'
                print 'Total funds ', value
                print '\n'
                next_trade = 'SOLD'

                wX.append(number_of_trades)
                vY.append(value)

            else:
                SL = trade_init + trade_init * SL_pct / 100
                TP = trade_init - trade_init * TP_pct / 100
                target = [TP, SL]

                event = ['Target point', 'Stop loss']
                print 'TP:', TP, ', SL: ', SL, '\n'
                print 'Total funds ', value
                print '\n'
                next_trade = 'BOUGHT'

                wX.append(number_of_trades)
                vY.append(value)


        elif max_of_trade > target[1]:
            print 'Trade number: ', number_of_trades
            print next_trade+' number of shares ', shares
            print event[1],' triggered at ',i+1,' number of trade. Executed at value ', target[1]

            trade_init = target[1]

            if event[1] == 'Stop loss':

                loss = abs(trade_init - SL)
                loss = loss*shares
                total_loss += loss
                print 'Loss: ', loss

                shares = shares*2
                value -= wager
                wager = previousWagerAmount * 2
                previousWagerAmount = wager
            else:

                profit = abs(trade_init - TP)
                profit = profit*shares
                total_profit += profit
                print 'Profit: ', profit

                shares = 1
                value += wager
                wager = initial_wager
                previousWagerAmount = wager

            number_of_trades += 1
            if number_of_trades % 2:
                SL = trade_init - trade_init * SL_pct / 100
                TP = trade_init + trade_init * TP_pct / 100
                target = [SL, TP]

                event = ['Stop loss', 'Target point']
                print 'SL: ', SL, ', TP:', TP, '\n'
                print 'Total funds ', value
                print '\n'
                next_trade = 'SOLD'

                wX.append(number_of_trades)
                vY.append(value)

            else:
                SL = trade_init + trade_init * SL_pct / 100
                TP = trade_init - trade_init * TP_pct / 100
                target = [TP, SL]

                event = ['Target point', 'Stop loss']
                print 'TP:', TP, ', SL: ', SL, '\n'
                print 'Total funds ', value
                print '\n'
                next_trade = 'BOUGHT'

                wX.append(number_of_trades)
                vY.append(value)

    print 'Total number of trades: ', number_of_trades
    print 'Total Loss ', total_loss
    print 'Total profit ', total_profit

    pyplot.plot(wX, vY,'o')

gold_data = read_gold_data()
doubler_bettor_gold(10000,gold_data)
pyplot.show()