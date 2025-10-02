"""Ticker validation and normalization utilities for supporting multiple markets."""
import re
from typing import Literal

MarketType = Literal["US", "NSE", "BSE", "UNKNOWN"]


def normalize_ticker(ticker: str) -> str:
    """
    Normalize ticker format to support both US and Indian stocks.
    
    Indian stocks typically use formats like:
    - RELIANCE.NS (NSE - National Stock Exchange of India)
    - RELIANCE.BO (BSE - Bombay Stock Exchange)
    
    US stocks are typically just the ticker symbol (e.g., AAPL, MSFT)
    
    Args:
        ticker: Raw ticker string
        
    Returns:
        Normalized ticker string in uppercase
        
    Examples:
        >>> normalize_ticker("aapl")
        'AAPL'
        >>> normalize_ticker("reliance.ns")
        'RELIANCE.NS'
        >>> normalize_ticker("TCS.BO")
        'TCS.BO'
    """
    ticker = ticker.strip().upper()
    
    # Check if it's already in proper format
    if re.match(r'^[A-Z0-9]+(\.(NS|BO))?$', ticker):
        return ticker
    
    # Remove any invalid characters
    ticker = re.sub(r'[^A-Z0-9.]', '', ticker)
    
    return ticker


def validate_ticker(ticker: str) -> tuple[bool, MarketType]:
    """
    Validate ticker format and identify market.
    
    Args:
        ticker: Ticker string to validate
        
    Returns:
        Tuple of (is_valid, market) where market is 'US', 'NSE', 'BSE', or 'UNKNOWN'
        
    Examples:
        >>> validate_ticker("AAPL")
        (True, 'US')
        >>> validate_ticker("RELIANCE.NS")
        (True, 'NSE')
        >>> validate_ticker("TCS.BO")
        (True, 'BSE')
        >>> validate_ticker("invalid!")
        (False, 'UNKNOWN')
    """
    ticker = ticker.strip().upper()
    
    # Check for Indian NSE stocks (National Stock Exchange)
    if ticker.endswith('.NS'):
        base = ticker[:-3]
        if re.match(r'^[A-Z0-9]+$', base):
            return True, 'NSE'
    
    # Check for Indian BSE stocks (Bombay Stock Exchange)
    if ticker.endswith('.BO'):
        base = ticker[:-3]
        if re.match(r'^[A-Z0-9]+$', base):
            return True, 'BSE'
    
    # Check for US stocks (no suffix, 1-5 characters)
    if re.match(r'^[A-Z]{1,5}$', ticker):
        return True, 'US'
    
    return False, 'UNKNOWN'


def get_market_type(ticker: str) -> MarketType:
    """
    Get the market type for a given ticker.
    
    Args:
        ticker: Ticker string
        
    Returns:
        Market type: 'US', 'NSE', 'BSE', or 'UNKNOWN'
        
    Examples:
        >>> get_market_type("AAPL")
        'US'
        >>> get_market_type("RELIANCE.NS")
        'NSE'
    """
    _, market = validate_ticker(ticker)
    return market


def is_indian_ticker(ticker: str) -> bool:
    """
    Check if a ticker is from an Indian stock exchange.
    
    Args:
        ticker: Ticker string
        
    Returns:
        True if the ticker is from NSE or BSE, False otherwise
        
    Examples:
        >>> is_indian_ticker("RELIANCE.NS")
        True
        >>> is_indian_ticker("AAPL")
        False
    """
    market = get_market_type(ticker)
    return market in ('NSE', 'BSE')


def parse_and_validate_tickers(tickers_str: str) -> tuple[list[str], list[str]]:
    """
    Parse and validate a comma-separated string of tickers.
    
    Args:
        tickers_str: Comma-separated ticker string (e.g., "AAPL,RELIANCE.NS,TCS.BO")
        
    Returns:
        Tuple of (valid_tickers, invalid_tickers)
        
    Examples:
        >>> parse_and_validate_tickers("AAPL,RELIANCE.NS,invalid!")
        (['AAPL', 'RELIANCE.NS'], ['INVALID'])
    """
    if not tickers_str:
        return [], []
    
    valid_tickers = []
    invalid_tickers = []
    
    for ticker in tickers_str.split(','):
        ticker = ticker.strip()
        if not ticker:
            continue
            
        normalized = normalize_ticker(ticker)
        is_valid, _ = validate_ticker(normalized)
        
        if is_valid:
            valid_tickers.append(normalized)
        else:
            invalid_tickers.append(normalized)
    
    return valid_tickers, invalid_tickers
