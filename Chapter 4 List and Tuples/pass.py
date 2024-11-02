import pandas as pd
import numpy as np
from astroquery.ned import Ned
from astropy.coordinates import SkyCoord
import astropy.units as u
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

def fetch_galaxy_data(max_results=1000):
    """
    Fetches galaxy data from the NASA/IPAC Extragalactic Database (NED).

    Parameters:
        max_results (int): Maximum number of galaxy records to fetch.

    Returns:
        pd.DataFrame: DataFrame containing galaxy data.
    """
    print("Fetching galaxy data from NED...")
    # Example query: All galaxies within a certain RA and Dec range
    # For demonstration, we'll query a region around the Virgo Cluster
    ra_center = "12h30m00s"
    dec_center = "+12d00m00s"
    radius = "10d"  # 10 degrees radius

    result_table = Ned.query_region(f"{ra_center} {dec_center}", radius=radius, equinox='J2000', table='galaxies', maxmax=max_results)
    df = result_table.to_pandas()
    print(f"Fetched {len(df)} galaxy records.")
    return df

def preprocess_data(df):
    """
    Cleans and preprocesses the galaxy data.

    Parameters:
        df (pd.DataFrame): Raw galaxy data.

    Returns:
        pd.DataFrame: Cleaned and preprocessed data.
    """
    print("Preprocessing data...")
    # Select relevant columns
    columns_needed = ['RA(deg)', 'DEC(deg)', 'Redshift']
    df = df[columns_needed]

    # Drop rows with missing values
    df = df.dropna(subset=columns_needed)

    # Reset index
    df.reset_index(drop=True, inplace=True)

    print(f"Data after preprocessing: {len(df)} records.")
    return df

def perform_clustering(df, eps=0.5, min_samples=5):
    """
    Identifies galaxy clusters using the DBSCAN clustering algorithm.

    Parameters:
        df (pd.DataFrame): Preprocessed galaxy data.
        eps (float): Maximum distance between two samples for one to be considered as in the neighborhood of the other.
        min_samples (int): Number of samples in a neighborhood for a point to be considered as a core point.

    Returns:
        np.ndarray: Cluster labels for each galaxy.
    """
    print("Performing clustering using DBSCAN...")
    # Convert RA and Dec to Cartesian coordinates for clustering
    coords = SkyCoord(ra=df['RA(deg)']*u.degree, dec=df['DEC(deg)']*u.degree, frame='icrs')
    cartesian = coords.cartesian
    X = np.vstack((cartesian.x.value, cartesian.y.value, cartesian.z.value)).T

    # Apply DBSCAN
    db = DBSCAN(eps=eps, min_samples=min_samples, metric='euclidean').fit(X)
    labels = db.labels_
    df['Cluster'] = labels
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    print(f"Number of clusters found: {n_clusters}")
    return df

def analyze_clusters(df):
    """
    Analyzes the identified galaxy clusters.

    Parameters:
        df (pd.DataFrame): Galaxy data with cluster labels.

    Returns:
        pd.DataFrame: Summary statistics of each cluster.
    """
    print("Analyzing clusters...")
    clusters = df[df['Cluster'] != -1]  # Exclude noise points
    summary = clusters.groupby('Cluster').agg(
        Number_of_Galaxies=pd.NamedAgg(column='Cluster', aggfunc='count'),
        Average_Redshift=pd.NamedAgg(column='Redshift', aggfunc='mean'),
        Min_RA=pd.NamedAgg(column='RA(deg)', aggfunc='min'),
        Max_RA=pd.NamedAgg(column='RA(deg)', aggfunc='max'),
        Min_DEC=pd.NamedAgg(column='DEC(deg)', aggfunc='min'),
        Max_DEC=pd.NamedAgg(column='DEC(deg)', aggfunc='max')
    ).reset_index()

    print("Cluster Summary:")
    print(summary)
    return summary

def visualize_clusters(df):
    """
    Visualizes galaxy distributions and identified clusters.

    Parameters:
        df (pd.DataFrame): Galaxy data with cluster labels.
    """
    print("Visualizing clusters...")
    sns.set(style="darkgrid")

    # Scatter plot of RA vs DEC colored by cluster
    plt.figure(figsize=(12, 8))
    palette = sns.color_palette('hsv', np.unique(df['Cluster']).max()+1)
    sns.scatterplot(data=df, x='RA(deg)', y='DEC(deg)', hue='Cluster', palette=palette, legend='full', s=50, alpha=0.6)
    plt.title('Galaxy Cluster Identification using DBSCAN')
    plt.xlabel('Right Ascension (degrees)')
    plt.ylabel('Declination (degrees)')
    plt.legend(title='Cluster', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

    # Histogram of redshifts for clusters
    plt.figure(figsize=(12, 6))
    sns.histplot(data=df[df['Cluster'] != -1], x='Redshift', hue='Cluster', multiple='stack', palette=palette)
    plt.title('Redshift Distribution by Cluster')
    plt.xlabel('Redshift')
    plt.ylabel('Number of Galaxies')
    plt.tight_layout()
    plt.show()

def main():
    print("=== Galaxy Cluster Identification and Analysis Tool ===")
    # Step 1: Fetch Data
    df = fetch_galaxy_data(max_results=2000)

    # Step 2: Preprocess Data
    df = preprocess_data(df)

    # Step 3: Perform Clustering
    df = perform_clustering(df, eps=0.02, min_samples=10)  # Adjust eps based on data density

    # Step 4: Analyze Clusters
    summary = analyze_clusters(df)

    # Step 5: Visualize Clusters
    visualize_clusters(df)

    print("Analysis complete.")

if __name__ == "__main__":
    main()
