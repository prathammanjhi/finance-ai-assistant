def print_finance_report(results):

    print("\n" + "=" * 70)
    print("                 FINANCE AI REPORT")
    print("=" * 70)

    for section_name, section in results.items():

        print("\n" + "-" * 70)
        print(section_name.replace("_", " ").upper())
        print("-" * 70)

        if isinstance(section, dict):
            print_section(section)
        else:
            print(section)


def print_section(data, indent=0):

    spacing = " " * indent

    for key, value in data.items():

        if isinstance(value, dict):

            print(f"\n{spacing}{key.replace('_',' ').title()}")

            print_section(value, indent + 4)

        elif isinstance(value, list):

            print(f"{spacing}{key.replace('_',' ').title()}:")

            for item in value:

                if isinstance(item, dict):

                    print_section(item, indent + 4)

                else:

                    print(" " * (indent + 4) + str(item))

        else:

            print(f"{spacing}{key.replace('_',' ').title():30}: {value}")

