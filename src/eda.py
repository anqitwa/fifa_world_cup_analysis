def describe_data(matches_df, players_df, cups_df):
    """
    Print initial insights from the datasets.
    """
    print("World Cup Matches Dataset:")
    print(matches_df.head())
    print("\nWorld Cup Players Dataset:")
    print(players_df.head())
    print("\nWorld Cups Dataset:")
    print(cups_df.head())

    print("\nNull values in World Cup Matches Dataset:")
    print(matches_df.isnull().sum())

    print("\nNull values in World Cup Players Dataset:")
    print(players_df.isnull().sum())

    print("\nNull values in World Cups Dataset:")
    print(cups_df.isnull().sum())
