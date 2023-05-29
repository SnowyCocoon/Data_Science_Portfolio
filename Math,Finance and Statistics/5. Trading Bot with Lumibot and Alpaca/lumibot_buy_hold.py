from config import ALPACA_CONFIG
from datetime import datetime
from lumibot.backtesting import YahooDataBacktesting
from lumibot.brokers import Alpaca
from lumibot.strategies import Strategy
from lumibot.traders import Trader

#'Buy-and-hold' is a strategy that means staying invested even when the markets look uncertain, with the hope that stocks will gradually increase in value over a long period of time.
class BuyHold(Strategy): #https://lumibot.lumiwealth.com/
    def initialize(self, parameters=None):
        self.sleeptime = "1D"
    
    def on_trading_iteration(self):
        if self.first_iteration:
            symbol = "GOOG"
            price = self.get_last_price(symbol)
            quantity = self.cash // price
            order = self.create_order(symbol, quantity, "buy")
            self.submit_order(order)

if __name__ == "__main__":
    trade = False
    if trade:
        broker = Alpaca(ALPACA_CONFIG)
        strategy = BuyHold(broker=broker)
        trader = Trader()
        trader.add_strategy(strategy)
        trader.run_all()
    else:
        start = datetime(2022,1,1)
        end = datetime(2022,12,31)
        BuyHold.backtest(YahooDataBacktesting,start,end)