from src.data_loader import load_data, clean_data

def test_load_data():
    matches_df, players_df, cups_df = load_data()
    assert not matches_df.empty, "Matches dataset is empty."
    assert not players_df.empty, "Players dataset is empty."
    assert not cups_df.empty, "Cups dataset is empty."
