import numpy as np
import pandas as pd
import pyjokes

def test_numpy():
    """Test basic NumPy functionality"""
    print("\n=== Testing NumPy ===")
    
    # Create arrays
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.arange(0, 10, 2)  # Even numbers from 0 to 8
    
    # Array operations
    sum_arr = arr1 + arr2[:len(arr1)]  # Element-wise addition
    dot_product = np.dot(arr1, arr2[:len(arr1)])
    
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    print(f"Element-wise sum: {sum_arr}")
    print(f"Dot product: {dot_product}")
    print(f"Mean of array1: {np.mean(arr1)}")

def test_pandas():
    """Test basic Pandas functionality"""
    print("\n=== Testing Pandas ===")
    
    # Create a DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'London', 'Paris', 'Tokyo']
    }
    df = pd.DataFrame(data)
    
    # DataFrame operations
    filtered = df[df['Age'] > 30]
    mean_age = df['Age'].mean()
    
    print("Original DataFrame:")
    print(df)
    print("\nFiltered DataFrame (Age > 30):")
    print(filtered)
    print(f"\nMean age: {mean_age}")

def test_pyjokes():
    """Test pyjokes library"""
    print("\n=== Testing PyJokes ===")
    
    # Get some jokes
    joke1 = pyjokes.get_joke()
    joke2 = pyjokes.get_joke(category='all')
    
    print("Random joke:", joke1)
    print("Another joke:", joke2)

if __name__ == "__main__":
    test_numpy()
    test_pandas()
    test_pyjokes()