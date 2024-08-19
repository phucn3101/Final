import pandas as pd
from collections import defaultdict

class LPPMDepth:
    def __init__(self, min_support, min_period, max_depth):
        self.min_support = min_support
        self.min_period = min_period
        self.max_depth = max_depth
        self.patterns = []

    def fit(self, data):
        # Step 1: Preprocess the data
        transactions = self._preprocess_data(data)
        
        # Step 2: Find initial frequent items
        frequent_items = self._find_frequent_patterns(transactions)
        
        # Step 3: Grow patterns by exploring depth
        self.patterns = self._mine_patterns_depth(frequent_items, transactions)
    
    def _preprocess_data(self, data):
        # Convert data into a suitable format for pattern mining
        transactions = defaultdict(list)
        for _, row in data.iterrows():
            key = (row['Year'], row['Month'], row['Day'])
            transactions[key].append(row['StockCode'])
        return transactions
    
    def _find_frequent_patterns(self, transactions):
        # Count the occurrences of each item
        item_count = defaultdict(int)
        for transaction in transactions.values():
            for item in set(transaction):
                item_count[item] += 1
        
        # Filter items that meet the minimum support
        frequent_items = {item: count for item, count in item_count.items() if count >= self.min_support}
        return frequent_items
    
    def _mine_patterns_depth(self, frequent_items, transactions):
        # Example method to mine patterns by exploring depth
        patterns = []
        
        for item in frequent_items:
            current_pattern = [item]
            self._explore_pattern(current_pattern, item, transactions, patterns, depth=1)
        
        return patterns

    def _explore_pattern(self, current_pattern, last_item, transactions, patterns, depth):
        if depth > self.max_depth:
            return
        
        is_periodic = True
        last_occurrence = None
        periodic_count = 0
        
        for period, transaction in transactions.items():
            if last_item in transaction:
                if last_occurrence:
                    period_diff = (period[0] * 365 + period[1] * 30 + period[2]) - (last_occurrence[0] * 365 + last_occurrence[1] * 30 + last_occurrence[2])
                    if period_diff < self.min_period:
                        is_periodic = False
                        break
                    else:
                        periodic_count += 1
                last_occurrence = period
        
        if is_periodic and periodic_count >= self.min_support:
            patterns.append(current_pattern.copy())
        
        # Explore adding new items to the pattern
        for new_item in transactions:
            if new_item not in current_pattern:
                current_pattern.append(new_item)
                self._explore_pattern(current_pattern, new_item, transactions, patterns, depth + 1)
                current_pattern.pop()

    def get_patterns(self):
        return self.patterns

if __name__ == "__main__":
    # Example usage
    from preprocess import load_and_preprocess
    df = load_and_preprocess('../data/dataset.csv')
    
    lppm_depth = LPPMDepth(min_support=5, min_period=7, max_depth=3)  # Example values for min_support, min_period, and max_depth
    lppm_depth.fit(df)
    patterns = lppm_depth.get_patterns()
    
    print("Discovered Patterns:", patterns)
