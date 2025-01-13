import pandas as pd

def load_data():
    """
    Load the datasets into pandas DataFrames.
    Returns:
        matches_df, players_df, cups_df (DataFrames): Cleaned dataframes for analysis.
    """
    matches_df = pd.read_csv('data/WorldCupMatches.csv')
    players_df = pd.read_csv('data/WorldCupPlayers.csv')
    cups_df = pd.read_csv('data/WorldCups.csv')

    return matches_df, players_df, cups_df

def clean_data(matches_df, players_df, cups_df):
    """
    Perform basic cleaning on the datasets.
    Args:
        matches_df, players_df, cups_df (DataFrames): Original datasets.
    Returns:
        Cleaned DataFrames.
    """
    # Clean column names
    matches_df.columns = matches_df.columns.str.strip()
    players_df.columns = players_df.columns.str.strip()
    cups_df.columns = cups_df.columns.str.strip()
    
    # Convert numerical columns to proper types
    cups_df['GoalsScored'] = pd.to_numeric(cups_df['GoalsScored'], errors='coerce')
    cups_df['MatchesPlayed'] = pd.to_numeric(cups_df['MatchesPlayed'], errors='coerce')
    cups_df['Attendance'] = cups_df['Attendance'].str.replace('.', '').astype(float)

    return matches_df, players_df, cups_df
