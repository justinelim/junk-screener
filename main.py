from funcs import *

def main(ticker_query:list) -> str:
    output = []
    for tq in ticker_query:
       output = output.append(get_morning_star(tq))
    return output

if __name__ == "__main__":
    ticker_query = ["FB", "AMZN"]
    print(main(ticker_query))
    print(type(main(ticker_query)))
