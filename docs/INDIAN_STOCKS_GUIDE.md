# Indian Stock Market Support Guide

This guide explains how to use the AI Hedge Fund with Indian stocks from NSE (National Stock Exchange) and BSE (Bombay Stock Exchange).

## Overview

The AI Hedge Fund now supports Indian stock markets alongside US stocks. You can analyze Indian stocks, mix them with US stocks, and leverage the dedicated Rakesh Jhunjhunwala agent that uses investment principles from India's legendary investor.

## Ticker Format

Indian stocks use the following ticker formats:

### NSE (National Stock Exchange)
Add `.NS` suffix to the ticker symbol:
- `RELIANCE.NS` - Reliance Industries
- `TCS.NS` - Tata Consultancy Services
- `INFY.NS` - Infosys
- `HDFCBANK.NS` - HDFC Bank
- `ICICIBANK.NS` - ICICI Bank
- `BHARTIARTL.NS` - Bharti Airtel
- `ITC.NS` - ITC Limited
- `SBIN.NS` - State Bank of India
- `LT.NS` - Larsen & Toubro
- `WIPRO.NS` - Wipro

### BSE (Bombay Stock Exchange)
Add `.BO` suffix to the ticker symbol:
- `RELIANCE.BO` - Reliance Industries
- `TCS.BO` - Tata Consultancy Services
- `INFY.BO` - Infosys
- `HDFCBANK.BO` - HDFC Bank

**Note:** Most major Indian companies are listed on both NSE and BSE. NSE (`.NS`) is generally preferred for better liquidity.

## Usage Examples

### Command Line Interface

#### Analyze Only Indian Stocks
```bash
poetry run python src/main.py --tickers RELIANCE.NS,TCS.NS,INFY.NS
```

#### Mix US and Indian Stocks
```bash
poetry run python src/main.py --tickers AAPL,RELIANCE.NS,MSFT,TCS.NS,GOOGL,INFY.NS
```

#### Run Backtesting with Indian Stocks
```bash
poetry run python src/backtester.py --tickers RELIANCE.NS,TCS.NS,INFY.NS --start-date 2024-01-01 --end-date 2024-03-01
```

#### Use Specific Analysts for Indian Stocks
The Rakesh Jhunjhunwala agent is specifically designed for Indian market analysis:
```bash
poetry run python src/main.py --tickers RELIANCE.NS,TCS.NS --analysts rakesh_jhunjhunwala,warren_buffett
```

### Web Application

In the web application, you can enter Indian tickers in the same format:

1. Open the Stock Analyzer node
2. Enter tickers: `RELIANCE.NS,TCS.NS,INFY.NS`
3. Or mix with US stocks: `AAPL,RELIANCE.NS,MSFT,TCS.NS`
4. Run analysis or backtest as usual

## API Key Requirements

For Indian stocks, you'll need a `FINANCIAL_DATASETS_API_KEY` as these tickers are not included in the free tier.

1. Sign up at [Financial Datasets](https://financialdatasets.ai/)
2. Get your API key
3. Add it to your `.env` file:
   ```
   FINANCIAL_DATASETS_API_KEY=your-api-key-here
   ```

## Understanding the Output

When analyzing Indian stocks, the system provides:

### Standard Analysis
- **Valuation Metrics**: P/E ratio, P/B ratio, market cap (in INR or USD equivalent)
- **Fundamental Analysis**: Revenue growth, earnings growth, ROE, debt ratios
- **Technical Analysis**: Price trends, momentum indicators
- **Sentiment Analysis**: News sentiment, market sentiment

### Rakesh Jhunjhunwala Agent
The Rakesh Jhunjhunwala agent uses investment principles specific to Indian markets:
- **Circle of Competence**: Focus on understandable businesses
- **Margin of Safety**: Minimum 30% discount to intrinsic value
- **Quality Management**: Shareholder-friendly management teams
- **Growth Focus**: Consistent revenue and earnings growth
- **Financial Strength**: Low debt, strong ROE (>15% preferred)
- **Long-term Horizon**: Multi-year investment perspective

## Important Considerations

### Market Hours
Indian stock markets operate in IST (Indian Standard Time):
- Regular trading: 9:15 AM - 3:30 PM IST
- Pre-open: 9:00 AM - 9:15 AM IST

### Currency
- Financial data is typically reported in INR (Indian Rupees)
- Market cap and valuations may be converted to USD for comparison

### Regulations
Indian markets operate under SEBI (Securities and Exchange Board of India) regulations, which differ from US SEC regulations in areas like:
- Disclosure requirements
- Corporate governance norms
- Trading restrictions
- Settlement cycles

### Liquidity
- NSE generally offers better liquidity than BSE
- Some small-cap stocks may have lower trading volumes
- Consider liquidity when backtesting or planning trades

## Popular Indian Stocks by Sector

### Technology
- TCS.NS (Tata Consultancy Services)
- INFY.NS (Infosys)
- WIPRO.NS (Wipro)
- HCLTECH.NS (HCL Technologies)
- TECHM.NS (Tech Mahindra)

### Banking & Finance
- HDFCBANK.NS (HDFC Bank)
- ICICIBANK.NS (ICICI Bank)
- SBIN.NS (State Bank of India)
- KOTAKBANK.NS (Kotak Mahindra Bank)
- AXISBANK.NS (Axis Bank)

### Energy & Resources
- RELIANCE.NS (Reliance Industries)
- ONGC.NS (Oil and Natural Gas Corporation)
- NTPC.NS (NTPC Limited)
- POWERGRID.NS (Power Grid Corporation)

### Consumer Goods
- ITC.NS (ITC Limited)
- HINDUNILVR.NS (Hindustan Unilever)
- NESTLEIND.NS (Nestle India)
- BRITANNIA.NS (Britannia Industries)

### Telecommunications
- BHARTIARTL.NS (Bharti Airtel)
- IDEA.NS (Vodafone Idea)

### Automobiles
- MARUTI.NS (Maruti Suzuki)
- TATAMOTORS.NS (Tata Motors)
- M&M.NS (Mahindra & Mahindra)
- BAJAJ-AUTO.NS (Bajaj Auto)

### Infrastructure
- LT.NS (Larsen & Toubro)
- ULTRACEMCO.NS (UltraTech Cement)
- ADANIPORTS.NS (Adani Ports)

## Troubleshooting

### Invalid Ticker Error
If you get an invalid ticker error:
- Verify the ticker symbol is correct
- Ensure you're using the correct suffix (`.NS` or `.BO`)
- Check that the company is actively traded
- Try the NSE (`.NS`) version if BSE (`.BO`) doesn't work

### No Data Available
If no data is returned:
- Verify your `FINANCIAL_DATASETS_API_KEY` is set correctly
- Check the date range - ensure it's within available data
- Try a different date range or more recent dates
- Some stocks may have limited historical data

### API Rate Limiting
If you encounter rate limiting:
- The system automatically retries with backoff
- Reduce the number of tickers analyzed at once
- Space out your requests over time
- Consider upgrading your API plan for higher limits

## Best Practices

1. **Start with Well-Known Stocks**: Begin with large-cap, liquid stocks like RELIANCE.NS, TCS.NS, INFY.NS
2. **Mix Markets Carefully**: When mixing US and Indian stocks, consider currency fluctuations
3. **Use Appropriate Analysts**: The Rakesh Jhunjhunwala agent is optimized for Indian market analysis
4. **Check Data Quality**: Verify the data for Indian stocks, especially for smaller companies
5. **Consider Time Zones**: Indian market hours differ significantly from US markets
6. **Understand Currency Impact**: Financial metrics may be in INR; consider USD conversion for comparison

## Example Workflow

Here's a complete workflow for analyzing Indian stocks:

```bash
# 1. Set up your environment
export FINANCIAL_DATASETS_API_KEY=your-api-key
export OPENAI_API_KEY=your-openai-key

# 2. Analyze a portfolio of Indian tech stocks
poetry run python src/main.py \
  --tickers TCS.NS,INFY.NS,WIPRO.NS,HCLTECH.NS \
  --analysts rakesh_jhunjhunwala,peter_lynch,warren_buffett \
  --start-date 2024-01-01 \
  --end-date 2024-03-01

# 3. Run a backtest with mixed portfolio
poetry run python src/backtester.py \
  --tickers AAPL,RELIANCE.NS,MSFT,TCS.NS,GOOGL,INFY.NS \
  --start-date 2023-01-01 \
  --end-date 2024-01-01 \
  --initial-cash 100000

# 4. Use local LLM with Ollama
poetry run python src/main.py \
  --tickers RELIANCE.NS,TCS.NS \
  --analysts rakesh_jhunjhunwala \
  --ollama
```

## Support and Resources

- **Financial Data API**: [https://financialdatasets.ai/](https://financialdatasets.ai/)
- **NSE India**: [https://www.nseindia.com/](https://www.nseindia.com/)
- **BSE India**: [https://www.bseindia.com/](https://www.bseindia.com/)
- **SEBI**: [https://www.sebi.gov.in/](https://www.sebi.gov.in/)

## Feedback

If you encounter issues with Indian stock support or have suggestions for improvements, please open an issue on the GitHub repository with the `enhancement` tag.
