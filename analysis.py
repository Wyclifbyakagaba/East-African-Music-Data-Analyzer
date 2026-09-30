import pandas as pd
import matplotlib.pyplot as plt


# Question 1:
# Which East African countries have the most artists?
def question_one(data):
    """Count artists by country using aggregation."""

    # Select the East African countries used in this project.
    east_africa = data[data["Country"].isin(
        ["Uganda", "Kenya", "Tanzania", "Rwanda"]
    )]

    # Count how many records belong to each country.
    country_counts = east_africa["Country"].value_counts()

    print("\nQUESTION 1")
    print("Which East African countries have the most artists?")
    print(country_counts)

    return country_counts


# Question 2:
# Which music genres have the highest average streaming numbers?
def question_two(data):
    """Calculate average streams for each genre."""

    # Filter the dataset to East African countries.
    east_africa = data[data["Country"].isin(
        ["Uganda", "Kenya", "Tanzania", "Rwanda"]
    )]

    # Group the records by genre and calculate average streams.
    genre_streams = east_africa.groupby("Genre")["Streams"].mean()

    # Sort genres from the highest average to the lowest.
    genre_streams = genre_streams.sort_values(ascending=False)

    print("\nQUESTION 2")
    print("Which genres have the highest average streams?")
    print(genre_streams)

    return genre_streams


# Stretch requirement:
# Create a graph showing one of the analysis results.
def create_country_chart(country_counts):
    """Create a bar chart showing artists by country."""

    # Convert the country counts into a bar chart.
    country_counts.plot(kind="bar")

    plt.title("East African Artists by Country")
    plt.xlabel("Country")
    plt.ylabel("Number of Artists")
    plt.tight_layout()

    # Save the chart inside the charts folder.
    plt.savefig("charts/artists_by_country.png")

    # Display the chart.
    plt.show()


# Optional third question:
# Which artist has the highest number of streams?
def question_three(data):
    """Find the artist with the highest number of streams."""

    # Filter the dataset to East African countries.
    east_africa = data[data["Country"].isin(
        ["Uganda", "Kenya", "Tanzania", "Rwanda"]
    )]

    # Sort artists by streams from highest to lowest.
    top_artist = east_africa.sort_values(
        by="Streams",
        ascending=False
    ).iloc[0]

    print("\nQUESTION 3")
    print("Which artist has the highest number of streams?")
    print("Artist:", top_artist["Artist"])
    print("Country:", top_artist["Country"])
    print("Streams:", top_artist["Streams"])


def clean_data(data):
    """Remove rows with missing important analysis values."""

    # Remove rows without artist, country, genre, or stream information.
    data = data.dropna(
        subset=["Artist", "Country", "Genre", "Streams"]
    )

    # Convert the Streams column into numbers.
    data["Streams"] = pd.to_numeric(
        data["Streams"],
        errors="coerce"
    )

    # Remove records that could not be converted to numbers.
    data = data.dropna(subset=["Streams"])

    return data


def show_summary(data):
    """Display basic information about the dataset."""

    print("\nDATASET SUMMARY")
    print("-" * 30)

    # Display the total number of records.
    print("Total records:", len(data))

    # Count the number of different artists.
    print("Unique artists:", data["Artist"].nunique())

    # Count the number of countries.
    print("Unique countries:", data["Country"].nunique())

    # Count the number of music genres.
    print("Unique genres:", data["Genre"].nunique())

    # Calculate the total streams.
    print("Total streams:", data["Streams"].sum())


def answer_questions(data):
    """Clean the data and run all project analysis questions."""

    # Clean the dataset before performing analysis.
    data = clean_data(data)

    # Show a summary of the dataset.
    show_summary(data)

    # Answer the first project question.
    country_counts = question_one(data)

    # Answer the second project question.
    question_two(data)

    # Answer the optional third question.
    question_three(data)

    # Create the visualization.
    create_country_chart(country_counts)