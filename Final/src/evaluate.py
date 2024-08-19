import pandas as pd

def load_and_preprocess(filepath):
    # Load the dataset
    df = pd.read_csv(filepath)
    
    # Convert InvoiceDate to datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    
    # Create a Year, Month, and Day column for easier grouping
    df['Year'] = df['InvoiceDate'].dt.year
    df['Month'] = df['InvoiceDate'].dt.month
    df['Day'] = df['InvoiceDate'].dt.day
    
    # Optionally, you could group by Customer ID or Country depending on the use case.
    # For now, we'll assume we're just working with Invoice and StockCode.
    
    return df[['Invoice', 'StockCode', 'Quantity', 'Year', 'Month', 'Day']]

if __name__ == "__main__":
    # Example usage of preprocessing
    filepath = 'data/online_retail_II.csv'  # Update with the correct path to your .csv file
    data = load_and_preprocess(filepath)
    
    # The rest of the evaluation can be done with the processed data
    # compare_algorithms(data)
