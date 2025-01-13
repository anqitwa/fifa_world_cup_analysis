def add_features(cups_df):
    """
    Add engineered features to the World Cups dataset.
    Args:
        cups_df (DataFrame): The World Cups dataset.
    Returns:
        DataFrame: Updated dataset with new features.
    """
    cups_df['AvgGoalsPerMatch'] = cups_df['GoalsScored'] / cups_df['MatchesPlayed']
    cups_df['AvgAttendance'] = cups_df['Attendance'] / cups_df['MatchesPlayed']
    return cups_df
