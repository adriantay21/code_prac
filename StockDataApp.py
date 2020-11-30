from urllib.request import Request, urlopen
from json import loads
from time import sleep

# NOTE:
# I've put a triple quote """ """ string inside each function.
# This is called a Docstring, which is a standard way to provide documentation
# about how a function works. There are a few different documentation standards
# out there. You will NOT be quizzed on this format, nor are you required to use
# it, but you may if you wish. When calling these functions, you can mouse over
# the function name and it will present the docstring content in the intellisense
# which pops up.


def raise_data_error(data, stock_symbol):
    """Raises an appropriate error based on an unexpected API result.

    Parameters
    ----------
    data : dict
        The unexpected data result from an API call.
    stock_symbol : str
        The stock symbol which resulted in the unexpected data.

    Raises
    ------
    ValueError
        If the stock symbol provded doesn't exist.
    RuntimeError
        If the API error message received cannot be understood.

    Warns
    -----
    RuntimeWarning
        If the API request limit has been reached.

    Notes
    -----
    Do not call the raise_data_error function! It is a utility function for the two
    functions that get data via the API.
    """
    data_keys = list(data.keys())
    if len(data_keys) == 0:
        # If we get nothing back it means we have an error message.
        data_keys.append('Error Message')
    error_key = data_keys[0]
    # "Error Message" means the URL was incorrect which would mean a bad symbol was provided.
    if error_key == 'Error Message':
        raise ValueError(f'Stock symbol {stock_symbol} does not exist!')
    # "Note" means they are telling us we ran out of requests and we need to wait.
    elif error_key == 'Note':
        raise RuntimeWarning(data)
    # Everything else can just be an unhandled error.
    else:
        raise RuntimeError(data[error_key])


def get_company_data(stock_symbol):
    """Gets the company information for the supplied stock symbol.

    Parameters
    ----------
    stock_symbol : str
        The stock symbol for which to retieve company information.

    Raises
    ------
    ValueError
        If the stock symbol provided doesn't exist.
    RuntimeError
        If the API error message received cannot be understood.

    Warns
    -----
    RuntimeWarning
        If the API request limit has been reached.

    Notes
    -----
    Data supplied by Alpha Vantage using their OVERVIEW API function.
    """

    # Build the url to get the initial price from real data online
    company_url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={stock_symbol.strip()}&apikey=2BRY6EIMLFRMU1D3'
    with urlopen(company_url) as url:
        data = loads(url.read().decode())
        if isinstance(data, dict) and len(data) > 1:
            return list(data.values())
        else:
            raise_data_error(data, stock_symbol)


def get_trade_data(stock_symbol):
    """Gets the time-series close price data for the supplied stock symbol.

    Parameters
    ----------
    stock_symbol : str
        The stock symbol for which to retieve time-series data.

    Raises
    ------
    ValueError
        If the stock symbol provided doesn't exist.
    RuntimeError
        If the API error message received cannot be understood.

    Warns
    -----
    RuntimeWarning
        If the API request limit has been reached.

    Notes
    -----
    Data supplied by Alpha Vantage using their TIME_SERIES_INTRADAY API function with an intervale of 5 minutes.
    """

    # Build the url to get the initial price from real data online
    stock_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol.strip()}&interval=5min&apikey=2BRY6EIMLFRMU1D3'
    with urlopen(stock_url) as url:
        data = loads(url.read().decode())
        if isinstance(data, dict) and len(data) > 1:
            # Close prices are nested under 2 levels in the second top level dictionary value
            # This list comprehension grabs the second value, then
            # grabs all the close prices from the second level values.
            data = [price['4. close']
                    for price in list(data.values())[1].values()]
            # The data comes from the API in reverse chronoligical order (most recent first)
            # so we need to reverse it to be oldest first.
            data.reverse()
            # List comprehension will create a new list with each value converted
            # to float since it will execute that function for each item in list.
            return [float(value) for value in data]
        else:
            raise_data_error(data, stock_symbol)


def countdown(delay_seconds):
    """Pauses the application and displays a count down on the screen for the supplied number of seconds.

    Parameters
    ----------
    delay_seconds : float
        The number of seconds to wait and count down for.

    """
    # Loop starting at the delay second value,
    # then go down 1 at a time, but stop at 0.
    for i in range(delay_seconds, 0, -1):
        # Print where we are at currently using a carriage return to begin
        # printing at the start of the line so we overwrite.
        print(f'\rToo many requests, waiting {i:02.0f} seconds...', end='')
        # Wait almost a second (need a little buffer for processing time).
        sleep(.999999)
    # Set it up so the next line will print on top of our last count.
    print('\r' + ' '*40 + '\r', end='')

def get_open_price():
    open_price = float(stock_trade_data[0])
    return (open_price)

def get_close_price():
    close_price = float(stock_trade_data[-1])
    return (close_price)

def get_lowest_price():
    price_list = stock_trade_data.copy()
    price_list.sort()
    lowest_price = float(price_list[0])
    return (lowest_price)

def get_highest_price():
    price_list = stock_trade_data.copy()
    price_list.sort()
    highest_price = float(price_list[-1])
    return (highest_price)

def get_combined_data(num):
    company_data_list = stock_company_data[:8]
    return company_data_list[num]

# YOUR PROGRAM STARTS HERE

print("Welcome to the Stock Data Application")

stock_inputs = input("\nEnter stock symbols seperated by commas: ")

print("\nPlease wait as the program gathers data from the API...")

#split the stocks by the "," symbol and create an empty output list
stock_list = stock_inputs.split(",")
output_list = []

#Format specification mini-language for table formatting
header_format = "{:<8}{:>14}{:>24}{:>8}{:>8}{:>8}{:>8}"
row_format = "{:<8}{:>14}{:>24}{:>8.2f}{:>8.2f}{:>8.2f}{:>8.2f}"

#splits the stocks individually and returns stock symbols in uppercase
for stocks in stock_list:
    stock = stocks.strip().upper()
    while True:
        try:    
            #Test for errors and download trade and company data into two variables
            stock_trade_data = get_trade_data(stock)
            stock_company_data = get_company_data(stock)
        except RuntimeWarning:
            #countdown 61 seconds if exceed API request limit
            countdown(61)
            continue
        except ValueError:
            #print error message if stock entered is invalid
            print(f"{stock} is not a valid stock symbol!")
            break
        else:
            #print message if stock was successfully downloaded
            print(f"Data for {stock} successfully downloaded!")
            #save the data into variables
            stock_symbol = str(get_combined_data(0))
            asset_type = str(get_combined_data(1))
            stock_sector = str(get_combined_data(-1))
            #append the data as a single string into a list
            output_list.append(row_format.format(stock_symbol,asset_type,stock_sector,
            get_open_price(),get_close_price(),get_highest_price(),get_lowest_price()))
            
            break   

#print table with headers and proper formatting
print("_"*80 + "\n")
print(header_format.format("Symbol","Asset Type","Sector","Open","Close","High","Low"))
#print the strings in the output list one by one seperated by a new line
print(*output_list, sep= "\n")
print("_"*80 + "\n")

input("Press enter to quit...")

        

    

