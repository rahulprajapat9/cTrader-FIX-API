import random
import matplotlib
import matplotlib.pyplot as plt
import time
import pandas

def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        print roll, 'roll was 100, you lose. what are the odds? play again.'
        return False
    elif roll <=40:
        print roll, 'roll was 1-50, you lose again, play again'
        return False
    elif 100>roll>40:
        print roll, 'roll was 51-99, you win, play more'
        return True

def read_gold_data():
    gold_data = pandas.DataFrame.from_csv("gold_data.csv")
    gold_data = gold_data[['open','high','low','close']]
    gold_data.reset_index()

    return gold_data

def doubler_bettor_gold(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager

    wX = []
    vY = []

    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            print 'We won last wager. wohoo!'
            if rollDice():
                value+=wager
                print value
                wX.append(currentWager)
                vY.append(value)
            else:
                value-=wager
                previousWager='loss'
                print value
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value<0:
                    print 'we went broke after ',currentWager,' bets'
                    break


        elif previousWager == 'loss':
            print 'We lost the last one, so we will double it now'
            if rollDice():
                wager = previousWagerAmount*2
                print 'We won ', wager
                value += wager
                print value
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount*2
                print 'we lost ', wager
                value -= wager
                if value < 0:
                    print 'We went broke after ', currentWager, 'bets'
                    break

                print value
                previousWager = 'loss'

                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)

        currentWager += 1

    print value
    plt.plot(wX,vY)

doubler_bettor_gold(10000,)
time.sleep(55)

def doubler_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager

    wX = []
    vY = []

    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            print 'We won last wager. wohoo!'
            if rollDice():
                value+=wager
                print value
                wX.append(currentWager)
                vY.append(value)
            else:
                value-=wager
                previousWager='loss'
                print value
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value<0:
                    print 'we went broke after ',currentWager,' bets'
                    break


        elif previousWager == 'loss':
            print 'We lost the last one, so we will double it now'
            if rollDice():
                wager = previousWagerAmount*2
                print 'We won ', wager
                value += wager
                print value
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount*2
                print 'we lost ', wager
                value -= wager
                if value < 0:
                    print 'We went broke after ', currentWager, 'bets'
                    break

                print value
                previousWager = 'loss'

                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)

        currentWager += 1

    print value
    plt.plot(wX,vY)

doubler_bettor(10000,100,1000)
plt.show()

time.sleep(555)


def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager

    wX = []
    vY = []

    currentWager = 1

    while currentWager < wager_count:
        if rollDice():
            value += wager
            wX.append(currentWager)
            vY.append(value)
        else:
            value -= wager
            wX.append(currentWager)
            vY.append(value)

        currentWager += 1

    if value < 100:
        value = 'broke'

    #print 'funds', value
    plt.plot(wX,vY)


x = 0

#while x<100:
simple_bettor(10000, 100, 1000)
#x+=1

plt.ylabel('Account value')
plt.xlabel('Wager count')
plt.show()

