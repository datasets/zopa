from pathlib import Path

import requests


MARKET_QUOTE_URL = "https://uk.zopa.com/ZopaWeb/ashx/MarketQuoteReport.ashx"


def market_quote_report():
    response = requests.get(MARKET_QUOTE_URL, timeout=60)
    response.raise_for_status()
    out_path = Path("data") / "market_quote_report.csv"
    out_path.write_bytes(response.content)


def main():
    market_quote_report()


if __name__ == "__main__":
    main()
