import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_time_series(df):
    """
    Visualizes the time series of transactions over time.
    
    Args:
        df (pd.DataFrame): The preprocessed DataFrame.
    """
    # Group by date and count the number of transactions
    daily_sales = df.groupby('InvoiceDate').size()
    
    # Plot the time series
    plt.figure(figsize=(12, 6))
    plt.plot(daily_sales.index, daily_sales.values, marker='o')
    plt.title('Daily Number of Transactions Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Transactions')
    plt.grid(True)
    plt.show()

def visualize_quantity_distribution(df):
    """
    Visualizes the distribution of quantities sold.
    
    Args:
        df (pd.DataFrame): The preprocessed DataFrame.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Quantity'], bins=50, kde=True)
    plt.title('Distribution of Quantities Sold')
    plt.xlabel('Quantity')
    plt.ylabel('Frequency')
    plt.show()

def visualize_price_distribution(df):
    """
    Visualizes the distribution of prices.
    
    Args:
        df (pd.DataFrame): The preprocessed DataFrame.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Price'], bins=50, kde=True)
    plt.title('Distribution of Prices')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.show()

def visualize_correlations(df):
    """
    Visualizes the correlation matrix between numerical columns.
    
    Args:
        df (pd.DataFrame): The preprocessed DataFrame.
    """
    plt.figure(figsize=(10, 8))
    correlation_matrix = df[['Quantity', 'Price', 'Year', 'Month', 'Day']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()

if __name__ == "__main__":
    # Load the preprocessed data
    filepath = '../data/preprocessed_data.csv'  # Update with the correct path
    df = pd.read_csv(filepath)
    
    # Visualize various aspects of the data
    visualize_time_series(df)
    visualize_quantity_distribution(df)
    visualize_price_distribution(df)
    visualize_correlations(df)
