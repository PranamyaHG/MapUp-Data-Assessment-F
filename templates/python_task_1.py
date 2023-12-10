import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
# Load the dataset into a DataFrame
df = pd.read_csv('dataset-1.csv')

# Create a pivot table
pivot_df = df.pivot_table(index='id_1', columns='id_2', values='car', fill_value=0)

# Set diagonal values to zero
for i in range(min(pivot_df.shape)):
    pivot_df.iloc[i, i] = 0

print(pivot_df)

return df


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
   # Create a new categorical column 'car_type' based on values in 'car' column
    conditions = [
        (df['car'] <= 15),
        (df['car'] > 15) & (df['car'] <= 25),
        (df['car'] > 25)
    ]
    choices = ['low', 'medium', 'high']
    df['car_type'] = pd.Series(
        np.select(conditions, choices, default='Unknown'), dtype='category'
    )

    # Calculate count of occurrence for each car type category
    count_dict = df['car_type'].value_counts().sort_index().to_dict()
    return count_dict

# Load the dataset into a DataFrame
df = pd.read_csv('dataset-1.csv')

# Get the count of car types
result = get_type_count(df)
print(result)

return dict()


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
  # Calculate the mean value of the 'bus' column
    mean_bus = df['bus'].mean()

    # Identify indices where 'bus' values are greater than twice the mean value
    bus_indexes = df[df['bus'] > 2 * mean_bus].index.tolist()

    return bus_indexes

# Load the dataset into a DataFrame
df = pd.read_csv('dataset-1.csv')

# Get the indices where 'bus' values are greater than twice the mean
result = get_bus_indexes(df)
print(result)

return list()


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
# Calculate the average of 'truck' grouped by 'route'
    route_avg = df.groupby('route')['truck'].mean()

    # Filter routes where the average is greater than 7
    filtered_routes = route_avg[route_avg > 7].index.tolist()

    # Sort the list of routes
    filtered_routes.sort()

    return filtered_routes

# Load the dataset into a DataFrame
df = pd.read_csv('dataset-1.csv')

# Get the sorted list of routes where the average of 'truck' is greater than 7
result = filter_routes(df)
print(result)

return list()


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
  # Modify values based on the logic provided
    df_modified = df.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    
    # Round the modified values to one decimal place
    df_modified = df_modified.round(1)
    
    return df_modified

# Assuming 'result_df' contains the resulting DataFrame from the solution to question 1
# Replace 'result_df' with the actual resulting DataFrame obtained from question 1
result_df = ...  # Replace this with the actual resulting DataFrame

# Apply the multiplication logic and rounding to the DataFrame
modified_df = multiply_matrix(result_df)
print(modified_df)

 return matrix


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()
