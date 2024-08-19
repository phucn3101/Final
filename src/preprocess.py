import pandas as pd
import csv

def load_and_preprocess(filepath):
    try:
        # Load the dataset with additional error handling
        df = pd.read_csv(
            filepath, 
            sep=",",  # Specify comma as the delimiter
            quoting=csv.QUOTE_MINIMAL,  # Handle quoted strings properly
            error_bad_lines=False,  # Skip lines with too many fields
            warn_bad_lines=True,  # Warn about bad lines
            engine='python'  # Use Python engine to handle complex cases
        )
        
        # Convert InvoiceDate to datetime
        df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
        
        # Drop rows with invalid dates
        df = df.dropna(subset=['InvoiceDate'])
        
        # Create Year, Month, and Day columns for easier grouping
        df['Year'] = df['InvoiceDate'].dt.year
        df['Month'] = df['InvoiceDate'].dt.month
        df['Day'] = df['InvoiceDate'].dt.day
        
        # Return the necessary columns
        return df[['Invoice', 'StockCode', 'Quantity', 'Year', 'Month', 'Day']]
    
    except pd.errors.ParserError as e:
        print(f"Error parsing file: {e}")
        return None

# if __name__ == "__main__":
#     # Example usage of preprocessing
#     filepath = 'data/online_retail_II.csv'  # Update with the correct path to your .csv file
#     data = load_and_preprocess(filepath)
    
#     if data is not None:
#         # The rest of the evaluation can be done with the processed data
#         print(data.head())
