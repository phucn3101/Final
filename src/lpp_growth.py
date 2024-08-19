import pandas as pd
from collections import defaultdict

class LPPGrowth:
    def __init__(self, min_support, min_period):
        self.min_support = min_support
        self.min_period = min_period
        self.patterns = []

    def fit(self, data):
        # Step 1: Preprocess the data
        transactions = self._preprocess_data(data)
        
        # Step 2: Find frequent items
        frequent_items = self._find_frequent_patterns(transactions)
        
        # Step 3: Grow patterns from frequent items
        self.patterns = self._grow_patterns(frequent_items, transactions)
    
    def _preprocess_data(self, data):
        # Convert data into a suitable format for pattern mining
        # For example, group transactions by day or period
        transactions = defaultdict(list)
        for _, row in data.iterrows():
            key = (row['Year'], row['Month'], row['Day'])
            transactions[key].append(row['StockCode'])
        return transactions
    
    def _find_frequent_patterns(self, transactions):
        # Count the occurrences of each item
        item_count = defaultdict(int)
        for transaction in transactions.values():
            for item in set(transaction):  # Use set to avoid counting duplicates in the same transaction
                item_count[item] += 1
        
        # Filter items that meet the minimum support
        frequent_items = {item: count for item, count in item_count.items() if count >= self.min_support}
        return frequent_items
    
    def _grow_patterns(self, frequent_items, transactions):
        # Grow patterns based on frequent items and periodicity
        patterns = []
        
        # Example: simple pattern growing
        for item in frequent_items:
            pattern = [item]
            last_occurrence = None
            is_periodic = True
            
            for period, transaction in transactions.items():
                if item in transaction:
                    if last_occurrence:
                        period_diff = (period[0] * 365 + period[1] * 30 + period[2]) - (last_occurrence[0] * 365 + last_occurrence[1] * 30 + last_occurrence[2])
                        if period_diff < self.min_period:
                            is_periodic = False
                            break
                    last_occurrence = period
            
            if is_periodic:
                patterns.append(pattern)
        
        return patterns

    def get_patterns(self):
        return self.patterns

if __name__ == "__main__":
    # Example usage
    from preprocess import load_and_preprocess
    df = load_and_preprocess('../data/dataset.csv')
    
    lpp_growth = LPPGrowth(min_support=5, min_period=7)  # Example values for min_support and min_period
    lpp_growth.fit(df)
    patterns = lpp_growth.get_patterns()
    
    print("Discovered Patterns:", patterns)
