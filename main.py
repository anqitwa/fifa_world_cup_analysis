from src.data_loader import load_data, clean_data
from src.eda import describe_data
from src.feature_engineering import add_features
from src.visualization import (
    plot_goals_trend,
    plot_avg_attendance,
    plot_goals_distribution,
    plot_winning_team_goals,
    plot_top_teams_with_most_players
)

def main():
    # Load and clean data
    matches_df, players_df, cups_df = load_data()
    matches_df, players_df, cups_df = clean_data(matches_df, players_df, cups_df)

    # Perform EDA
    describe_data(matches_df, players_df, cups_df)

    # Add features
    cups_df = add_features(cups_df)

    # Visualize data and save plots
    plot_goals_trend(cups_df)
    plot_avg_attendance(cups_df)
    plot_goals_distribution(matches_df)
    plot_winning_team_goals(cups_df)
    plot_top_teams_with_most_players(players_df)

if __name__ == '__main__':
    main()
