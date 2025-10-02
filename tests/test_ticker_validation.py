"""Tests for ticker validation and normalization utilities."""
import pytest
from src.utils.ticker import (
    normalize_ticker,
    validate_ticker,
    get_market_type,
    is_indian_ticker,
    parse_and_validate_tickers,
)


class TestNormalizeTicker:
    """Tests for normalize_ticker function."""
    
    def test_us_ticker_uppercase(self):
        """Test US ticker already in uppercase."""
        assert normalize_ticker("AAPL") == "AAPL"
    
    def test_us_ticker_lowercase(self):
        """Test US ticker conversion to uppercase."""
        assert normalize_ticker("aapl") == "AAPL"
    
    def test_indian_nse_ticker_uppercase(self):
        """Test Indian NSE ticker already in uppercase."""
        assert normalize_ticker("RELIANCE.NS") == "RELIANCE.NS"
    
    def test_indian_nse_ticker_lowercase(self):
        """Test Indian NSE ticker conversion to uppercase."""
        assert normalize_ticker("reliance.ns") == "RELIANCE.NS"
    
    def test_indian_bse_ticker_uppercase(self):
        """Test Indian BSE ticker already in uppercase."""
        assert normalize_ticker("TCS.BO") == "TCS.BO"
    
    def test_indian_bse_ticker_lowercase(self):
        """Test Indian BSE ticker conversion to uppercase."""
        assert normalize_ticker("tcs.bo") == "TCS.BO"
    
    def test_ticker_with_whitespace(self):
        """Test ticker with leading/trailing whitespace."""
        assert normalize_ticker("  AAPL  ") == "AAPL"
        assert normalize_ticker("  reliance.ns  ") == "RELIANCE.NS"
    
    def test_ticker_with_invalid_chars(self):
        """Test ticker with invalid characters removed."""
        assert normalize_ticker("A@APL!") == "AAPL"


class TestValidateTicker:
    """Tests for validate_ticker function."""
    
    def test_valid_us_ticker(self):
        """Test validation of valid US tickers."""
        assert validate_ticker("AAPL") == (True, "US")
        assert validate_ticker("MSFT") == (True, "US")
        assert validate_ticker("GOOGL") == (True, "US")
    
    def test_valid_nse_ticker(self):
        """Test validation of valid NSE tickers."""
        assert validate_ticker("RELIANCE.NS") == (True, "NSE")
        assert validate_ticker("TCS.NS") == (True, "NSE")
        assert validate_ticker("INFY.NS") == (True, "NSE")
    
    def test_valid_bse_ticker(self):
        """Test validation of valid BSE tickers."""
        assert validate_ticker("RELIANCE.BO") == (True, "BSE")
        assert validate_ticker("TCS.BO") == (True, "BSE")
        assert validate_ticker("INFY.BO") == (True, "BSE")
    
    def test_invalid_ticker(self):
        """Test validation of invalid tickers."""
        assert validate_ticker("INVALID!") == (False, "UNKNOWN")
        assert validate_ticker("123456") == (False, "UNKNOWN")
        assert validate_ticker("") == (False, "UNKNOWN")
    
    def test_case_insensitive(self):
        """Test that validation is case-insensitive."""
        assert validate_ticker("aapl") == (True, "US")
        assert validate_ticker("reliance.ns") == (True, "NSE")


class TestGetMarketType:
    """Tests for get_market_type function."""
    
    def test_us_market(self):
        """Test identifying US market."""
        assert get_market_type("AAPL") == "US"
    
    def test_nse_market(self):
        """Test identifying NSE market."""
        assert get_market_type("RELIANCE.NS") == "NSE"
    
    def test_bse_market(self):
        """Test identifying BSE market."""
        assert get_market_type("TCS.BO") == "BSE"
    
    def test_unknown_market(self):
        """Test identifying unknown market."""
        assert get_market_type("INVALID!") == "UNKNOWN"


class TestIsIndianTicker:
    """Tests for is_indian_ticker function."""
    
    def test_us_ticker_not_indian(self):
        """Test US tickers are not identified as Indian."""
        assert is_indian_ticker("AAPL") is False
        assert is_indian_ticker("MSFT") is False
    
    def test_nse_ticker_is_indian(self):
        """Test NSE tickers are identified as Indian."""
        assert is_indian_ticker("RELIANCE.NS") is True
        assert is_indian_ticker("TCS.NS") is True
    
    def test_bse_ticker_is_indian(self):
        """Test BSE tickers are identified as Indian."""
        assert is_indian_ticker("RELIANCE.BO") is True
        assert is_indian_ticker("TCS.BO") is True


class TestParseAndValidateTickers:
    """Tests for parse_and_validate_tickers function."""
    
    def test_single_us_ticker(self):
        """Test parsing single US ticker."""
        valid, invalid = parse_and_validate_tickers("AAPL")
        assert valid == ["AAPL"]
        assert invalid == []
    
    def test_multiple_us_tickers(self):
        """Test parsing multiple US tickers."""
        valid, invalid = parse_and_validate_tickers("AAPL,MSFT,GOOGL")
        assert valid == ["AAPL", "MSFT", "GOOGL"]
        assert invalid == []
    
    def test_multiple_indian_tickers(self):
        """Test parsing multiple Indian tickers."""
        valid, invalid = parse_and_validate_tickers("RELIANCE.NS,TCS.BO,INFY.NS")
        assert valid == ["RELIANCE.NS", "TCS.BO", "INFY.NS"]
        assert invalid == []
    
    def test_mixed_us_and_indian_tickers(self):
        """Test parsing mix of US and Indian tickers."""
        valid, invalid = parse_and_validate_tickers("AAPL,RELIANCE.NS,MSFT,TCS.BO")
        assert valid == ["AAPL", "RELIANCE.NS", "MSFT", "TCS.BO"]
        assert invalid == []
    
    def test_with_invalid_tickers(self):
        """Test parsing with some invalid tickers."""
        valid, invalid = parse_and_validate_tickers("AAPL,INVALID!,RELIANCE.NS")
        assert valid == ["AAPL", "RELIANCE.NS"]
        assert invalid == ["INVALID"]
    
    def test_case_normalization(self):
        """Test that tickers are normalized to uppercase."""
        valid, invalid = parse_and_validate_tickers("aapl,reliance.ns,msft")
        assert valid == ["AAPL", "RELIANCE.NS", "MSFT"]
        assert invalid == []
    
    def test_empty_string(self):
        """Test parsing empty string."""
        valid, invalid = parse_and_validate_tickers("")
        assert valid == []
        assert invalid == []
    
    def test_whitespace_handling(self):
        """Test that whitespace is handled correctly."""
        valid, invalid = parse_and_validate_tickers("  AAPL  ,  RELIANCE.NS  ,  MSFT  ")
        assert valid == ["AAPL", "RELIANCE.NS", "MSFT"]
        assert invalid == []
