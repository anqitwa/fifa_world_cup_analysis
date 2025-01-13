def export_cleaned_data(world_cups, matches, players):
    """Export cleaned data for Tableau."""
    world_cups.to_csv('Cleaned_WorldCups.csv', index=False)
    matches.to_csv('Cleaned_WorldCupMatches.csv', index=False)
    players.to_csv('Cleaned_WorldCupPlayers.csv', index=False)
