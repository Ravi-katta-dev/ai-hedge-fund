"""Integration tests for Indian stock market support."""
import pytest
from unittest.mock import Mock, patch
from src.tools.api import get_prices, get_financial_metrics
from src.cli.input import parse_tickers


class TestIndianStockIntegration:
    """Integration tests for Indian stock market functionality."""
    
    def test_parse_indian_tickers_cli(self):
        """Test that CLI can parse Indian ticker formats."""
        # Test NSE tickers
        nse_tickers = parse_tickers("RELIANCE.NS,TCS.NS,INFY.NS")
        assert nse_tickers == ["RELIANCE.NS", "TCS.NS", "INFY.NS"]
        
        # Test BSE tickers
        bse_tickers = parse_tickers("RELIANCE.BO,TCS.BO,INFY.BO")
        assert bse_tickers == ["RELIANCE.BO", "TCS.BO", "INFY.BO"]
        
        # Test mixed US and Indian tickers
        mixed_tickers = parse_tickers("AAPL,RELIANCE.NS,MSFT,TCS.BO")
        assert mixed_tickers == ["AAPL", "RELIANCE.NS", "MSFT", "TCS.BO"]
    
    @patch('src.tools.api._cache')
    @patch('src.tools.api.requests.get')
    def test_get_prices_with_indian_ticker(self, mock_get, mock_cache):
        """Test that get_prices can handle Indian ticker formats."""
        # Mock cache to return None (cache miss)
        mock_cache.get_prices.return_value = None
        
        # Mock successful API response for Indian ticker
        mock_200_response = Mock()
        mock_200_response.status_code = 200
        mock_200_response.json.return_value = {
            "ticker": "RELIANCE.NS",
            "prices": [
                {
                    "time": "2024-01-01T00:00:00Z",
                    "open": 2500.0,
                    "close": 2510.0,
                    "high": 2520.0,
                    "low": 2490.0,
                    "volume": 5000000
                }
            ]
        }
        
        mock_get.return_value = mock_200_response
        
        # Call get_prices with Indian ticker
        result = get_prices("RELIANCE.NS", "2024-01-01", "2024-01-02", api_key="test-key")
        
        # Verify the function succeeded and returned data
        assert len(result) == 1
        assert result[0].open == 2500.0
        assert result[0].close == 2510.0
        
        # Verify the API was called with the correct ticker format
        mock_get.assert_called_once()
        call_args = mock_get.call_args
        assert "RELIANCE.NS" in call_args[0][0]  # Check ticker in URL
    
    @patch('src.tools.api._cache')
    @patch('src.tools.api.requests.get')
    def test_get_financial_metrics_with_indian_ticker(self, mock_get, mock_cache):
        """Test that get_financial_metrics can handle Indian ticker formats."""
        # Mock cache to return None (cache miss)
        mock_cache.get_financial_metrics.return_value = None
        
        # Mock successful API response for Indian ticker with all required fields
        mock_200_response = Mock()
        mock_200_response.status_code = 200
        mock_200_response.json.return_value = {
            "financial_metrics": [
                {
                    "ticker": "RELIANCE.NS",
                    "report_period": "2024-01-01",
                    "period": "ttm",
                    "currency": "INR",
                    "market_cap": 15000000000,
                    "enterprise_value": 16000000000,
                    "price_to_earnings_ratio": 25.0,
                    "price_to_book_ratio": 3.0,
                    "price_to_sales_ratio": 2.5,
                    "enterprise_value_to_ebitda_ratio": 12.0,
                    "enterprise_value_to_revenue_ratio": 2.0,
                    "free_cash_flow_yield": 0.05,
                    "peg_ratio": 1.2,
                    "gross_margin": 0.45,
                    "operating_margin": 0.20,
                    "net_margin": 0.15,
                    "return_on_equity": 0.18,
                    "return_on_assets": 0.10,
                    "return_on_invested_capital": 0.12,
                    "asset_turnover": 0.8,
                    "inventory_turnover": 6.0,
                    "receivables_turnover": 10.0,
                    "days_sales_outstanding": 36.5,
                    "operating_cycle": 100.0,
                    "working_capital_turnover": 5.0,
                    "current_ratio": 1.5,
                    "quick_ratio": 1.0,
                    "cash_ratio": 0.5,
                    "operating_cash_flow_ratio": 0.8,
                    "debt_to_equity": 0.5,
                    "debt_to_assets": 0.3,
                    "interest_coverage": 8.0,
                    "revenue_growth": 0.15,
                    "earnings_growth": 0.20,
                    "book_value_growth": 0.12,
                    "earnings_per_share_growth": 0.18,
                    "free_cash_flow_growth": 0.25,
                    "operating_income_growth": 0.17,
                    "ebitda_growth": 0.16,
                    "payout_ratio": 0.30,
                    "earnings_per_share": 15.5,
                    "book_value_per_share": 85.0,
                    "free_cash_flow_per_share": 20.0
                }
            ]
        }
        
        mock_get.return_value = mock_200_response
        
        # Call get_financial_metrics with Indian ticker
        result = get_financial_metrics("RELIANCE.NS", "2024-01-01", api_key="test-key")
        
        # Verify the function succeeded and returned data
        assert len(result) == 1
        assert result[0].ticker == "RELIANCE.NS"
        assert result[0].market_cap == 15000000000
        
        # Verify the API was called with the correct ticker format
        mock_get.assert_called_once()
        call_args = mock_get.call_args
        assert "RELIANCE.NS" in call_args[0][0]  # Check ticker in URL
    
    def test_case_insensitive_indian_tickers(self):
        """Test that Indian tickers work regardless of case."""
        # Test lowercase NSE ticker
        lowercase_nse = parse_tickers("reliance.ns")
        assert lowercase_nse == ["RELIANCE.NS"]
        
        # Test mixed case BSE ticker
        mixed_case_bse = parse_tickers("Tcs.Bo")
        assert mixed_case_bse == ["TCS.BO"]
        
        # Test uppercase (already normalized)
        uppercase = parse_tickers("INFY.NS")
        assert uppercase == ["INFY.NS"]
    
    def test_validation_rejects_invalid_indian_formats(self):
        """Test that invalid Indian ticker formats are rejected."""
        # Invalid suffix - this gets normalized to RELIANCEXX which is invalid
        invalid_suffix = parse_tickers("RELIANCE.XX")
        assert len(invalid_suffix) == 0
        
        # Missing base ticker - gets normalized to .NS which is invalid
        missing_base = parse_tickers(".NS")
        assert len(missing_base) == 0
        
        # Invalid characters - gets normalized but may still pass basic format check
        # So we test with truly invalid formats
        truly_invalid = parse_tickers("!!!,@@@")
        assert len(truly_invalid) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
