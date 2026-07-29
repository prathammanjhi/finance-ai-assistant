from src.core.engine import analyze_finances
from src.cli.printer import print_finance_report


def main():

    results = analyze_finances()

    print_finance_report(results)


if __name__ == "__main__":
    main()