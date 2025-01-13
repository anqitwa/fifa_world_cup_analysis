import os
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure output/plots directory exists
output_dir = "output/plots"
os.makedirs(output_dir, exist_ok=True)

def plot_goals_trend(cups_df):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=cups_df, x='Year', y='GoalsScored', marker='o')
    plt.title('Trend of Goals Scored Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Goals Scored')
    plt.grid()
    plot_path = os.path.join(output_dir, 'goals_trend.png')
    plt.savefig(plot_path)
    plt.close()
    print(f"Saved: {plot_path}")

def plot_avg_attendance(cups_df):
    plt.figure(figsize=(12, 6))
    sns.barplot(data=cups_df, x='Year', y='AvgAttendance', palette='viridis')
    plt.title('Average Attendance Per Match Per World Cup')
    plt.xlabel('Year')
    plt.ylabel('Average Attendance')
    plt.xticks(rotation=45)
    plot_path = os.path.join(output_dir, 'avg_attendance.png')
    plt.savefig(plot_path)
    plt.close()
    print(f"Saved: {plot_path}")

def plot_goals_distribution(matches_df):
    plt.figure(figsize=(12, 6))
    sns.histplot(matches_df['Home Team Goals'], color='blue', label='Home Team Goals', kde=True)
    sns.histplot(matches_df['Away Team Goals'], color='orange', label='Away Team Goals', kde=True)
    plt.title('Distribution of Goals Scored by Teams')
    plt.xlabel('Goals')
    plt.ylabel('Frequency')
    plt.legend()
    plot_path = os.path.join(output_dir, 'goals_distribution.png')
    plt.savefig(plot_path)
    plt.close()
    print(f"Saved: {plot_path}")

def plot_winning_team_goals(cups_df):
    plt.figure(figsize=(12, 6))
    sns.barplot(data=cups_df, x='Winner', y='GoalsScored', palette='coolwarm')
    plt.title('Goals Scored by Winning Teams')
    plt.xlabel('Winning Team')
    plt.ylabel('Goals Scored')
    plt.xticks(rotation=90)
    plot_path = os.path.join(output_dir, 'winning_team_goals.png')
    plt.savefig(plot_path)
    plt.close()
    print(f"Saved: {plot_path}")

def plot_top_teams_with_most_players(players_df):
    # Replace 'Team' with the actual column name, e.g., 'Country'
    player_counts = players_df['Team Initials'].value_counts().head(10)
    plt.figure(figsize=(12, 6))
    player_counts.plot(kind='bar', color='teal')
    plt.title('Top 10 Teams with Most Players')
    plt.xlabel('Team')
    plt.ylabel('Number of Players')
    plot_path = os.path.join(output_dir, 'top_teams_with_most_players.png')
    plt.savefig(plot_path)
    plt.close()
    print(f"Saved: {plot_path}")

