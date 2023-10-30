# pip install yfinance

import yfinance as yf

def main():
    tw0050 = yf.Ticker("0050.tw")
    tw0050his = tw0050.history(period="max")
    print(tw0050his)

if __name__ == '__main__':
    main()
