import pandas as pd
from analysis import answer_questions


def load_data():
    """Load the music dataset from the data folder."""
    return pd.read_csv("data/music_data.csv")


def show_title():
    """Display the program title."""
    print("=" * 55)
    print("        EAST AFRICAN MUSIC DATA ANALYZER")
    print("=" * 55)


def main():
    """Run the data analysis program."""
    show_title()

    try:
        data = load_data()

        print("\nDataset loaded successfully.")
        print("Rows:", len(data))
        print("Columns:", len(data.columns))

        answer_questions(data)

    except FileNotFoundError:
        print("\nError: The file data/music_data.csv was not found.")
        print("Make sure music_data.csv is inside the data folder.")

    except Exception as error:
        print("\nAn error occurred:", error)


if __name__ == "__main__":
    main()