#!/usr/bin/env python3
"""
Example script demonstrating Indian stock market support.

This script shows how to use the AI Hedge Fund with Indian stocks from
NSE (National Stock Exchange) and BSE (Bombay Stock Exchange).

Requirements:
- FINANCIAL_DATASETS_API_KEY environment variable must be set
- At least one LLM API key (OPENAI_API_KEY, etc.)
"""

from src.utils.ticker import (
    normalize_ticker,
    validate_ticker,
    is_indian_ticker,
    parse_and_validate_tickers,
    get_market_type
)


def main():
    print("=" * 80)
    print("AI Hedge Fund - Indian Stock Market Support Demo")
    print("=" * 80)
    print()
    
    # Example 1: Normalize tickers
    print("1. Ticker Normalization")
    print("-" * 40)
    test_tickers = ["reliance.ns", "TCS.bo", "aapl", "INFY.NS"]
    for ticker in test_tickers:
        normalized = normalize_ticker(ticker)
        print(f"   {ticker:15s} → {normalized}")
    print()
    
    # Example 2: Validate tickers
    print("2. Ticker Validation")
    print("-" * 40)
    test_tickers = ["RELIANCE.NS", "TCS.BO", "AAPL", "INVALID!"]
    for ticker in test_tickers:
        is_valid, market = validate_ticker(ticker)
        status = "✓" if is_valid else "✗"
        print(f"   {status} {ticker:15s} → Market: {market}")
    print()
    
    # Example 3: Identify Indian tickers
    print("3. Identify Indian Stocks")
    print("-" * 40)
    test_tickers = ["RELIANCE.NS", "TCS.BO", "INFY.NS", "AAPL", "MSFT"]
    for ticker in test_tickers:
        is_indian = is_indian_ticker(ticker)
        market = get_market_type(ticker)
        flag = "🇮🇳" if is_indian else "🇺🇸"
        print(f"   {flag} {ticker:15s} → Market: {market}")
    print()
    
    # Example 4: Parse mixed portfolio
    print("4. Parse Mixed Portfolio")
    print("-" * 40)
    portfolio_str = "AAPL,RELIANCE.NS,MSFT,TCS.BO,GOOGL,INFY.NS,invalid!"
    print(f"   Input: {portfolio_str}")
    valid, invalid = parse_and_validate_tickers(portfolio_str)
    print(f"   Valid tickers: {', '.join(valid)}")
    if invalid:
        print(f"   Invalid tickers: {', '.join(invalid)}")
    print()
    
    # Example 5: Market distribution
    print("5. Portfolio Market Distribution")
    print("-" * 40)
    us_stocks = [t for t in valid if not is_indian_ticker(t)]
    indian_stocks = [t for t in valid if is_indian_ticker(t)]
    print(f"   US Stocks ({len(us_stocks)}): {', '.join(us_stocks)}")
    print(f"   Indian Stocks ({len(indian_stocks)}): {', '.join(indian_stocks)}")
    print()
    
    # Example 6: Sample commands
    print("6. Example CLI Commands")
    print("-" * 40)
    print("   # Analyze Indian stocks:")
    print("   poetry run python src/main.py --tickers RELIANCE.NS,TCS.NS,INFY.NS")
    print()
    print("   # Mix US and Indian stocks:")
    print("   poetry run python src/main.py --tickers AAPL,RELIANCE.NS,MSFT,TCS.BO")
    print()
    print("   # Backtest with Indian stocks:")
    print("   poetry run python src/backtester.py --tickers RELIANCE.NS,TCS.NS \\")
    print("     --start-date 2024-01-01 --end-date 2024-03-01")
    print()
    print("   # Use Rakesh Jhunjhunwala agent (Indian market specialist):")
    print("   poetry run python src/main.py --tickers RELIANCE.NS,TCS.NS \\")
    print("     --analysts rakesh_jhunjhunwala,warren_buffett")
    print()
    
    # Example 7: Popular Indian stocks
    print("7. Popular Indian Stocks by Sector")
    print("-" * 40)
    sectors = {
        "Technology": ["TCS.NS", "INFY.NS", "WIPRO.NS", "HCLTECH.NS"],
        "Banking": ["HDFCBANK.NS", "ICICIBANK.NS", "SBIN.NS", "KOTAKBANK.NS"],
        "Energy": ["RELIANCE.NS", "ONGC.NS", "NTPC.NS"],
        "Consumer": ["ITC.NS", "HINDUNILVR.NS", "BRITANNIA.NS"],
        "Telecom": ["BHARTIARTL.NS", "IDEA.NS"],
        "Auto": ["MARUTI.NS", "TATAMOTORS.NS", "M&M.NS"],
    }
    
    for sector, tickers in sectors.items():
        print(f"   {sector:15s}: {', '.join(tickers)}")
    print()
    
    print("=" * 80)
    print("📖 For more information, see docs/INDIAN_STOCKS_GUIDE.md")
    print("=" * 80)


if __name__ == "__main__":
    main()
