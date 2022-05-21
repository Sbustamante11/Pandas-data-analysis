import pandas as pd
from matplotlib import pyplot as plt


def read_file(filename):

    df = pd.read_csv(filename)

    return df

def calculate_total(dataframe):
    item_total_sum = dataframe["Item Total"].sum()

    return item_total_sum

def calculate_min(dataframe):
    min_value = dataframe["Item Total"].min()

    return min_value

def calculate_mean(dataframe):
    mean_sum = dataframe["Item Total"].mean()

    return mean_sum

def calculate_median(dataframe):
    median_sum = dataframe["Item Total"].median()

    return median_sum

def calculate_max(dataframe):
    max_sum = dataframe["Item Total"].max()

    return max_sum

def describe_data(dataframe):
    data_description = dataframe.describe()

    return data_description

def calculate_monthly_spending(dataframe):
    sum_monthly = dataframe.groupby('Order Date')['Item Total'].sum()
    return sum_monthly


def main():
    
    df = read_file('amazon_orders.csv')

    #edits our csv file to remove all NaN values
    #all NaN values are changed to 0
    #these changes are loaded into our data frame resulting in a permanent change

    df = df.fillna(0)

    #removes all $ sybols from our 'Item Total' column.
    #converts the data in this column to a float - allows us to work with our data as an integer
    df["Item Total"] = df["Item Total"].str.replace('$', '').astype(float)

    #strips all $ symbols from 'Item Subtotal Tax' column
    #converts all values in 'Item Subtotal Tax' column to floats
    df["Item Subtotal Tax"]= df["Item Subtotal Tax"].str.replace('$', '').astype(float)

    print(calculate_monthly_spending(df))
    print()

    print("Overview of data")
    print("============================================")
    print()
    print(describe_data(df))
    print()

    # new dataframe created to only include the following columns
    # this dataframe will be used to display sorted data
    df_sorted = df[['Order Date', 'Order ID', 'Title', 'Shipment Date', 'Item Total']]
    # sorted data by item total in descending order
    print("Item Total sorted by descending order")
    print("============================================")
    print(df_sorted.sort_values(by='Item Total', ascending=False))
    print()

    total_sum = calculate_total(df)

    min_order = calculate_min(df)

    mean_order = calculate_mean(df)

    median_order = calculate_median(df)

    max_order = calculate_max(df)

    print(f'Total Sum: ${total_sum:.2f}')
    print()

    
    print(f'Smallest Purchase: ${min_order:.2f}')
    print()

    print(f'Mean Sum: ${mean_order:.2f}')
    print()

    print(f'Median Sum: ${median_order:.2f}')
    print()

    print(f'Largest Purchase: ${max_order}')
    print()
    

    tax_rate = df["Item Subtotal Tax"].sum() / df["Item Total"].sum()
    avg_tax_perc = tax_rate * 100
    print(f'Average Tax Rate: {avg_tax_perc:.2f}%')


    # df["Order Date"] = pd.to_datetime(df["Order Date"]).dt.to_period('Y')


    # df.plot(kind = 'bar', x='Order Date', y='Item Total', color = 'green', rot=90, figsize=(18,12))

    # plt.title('Yearly Spending')

    # plt.show()

    df['month_year'] =pd.to_datetime(df['Order Date']).dt.to_period('M')
    df.plot(kind = 'bar', x='Order Date', y='Item Total', color = 'blue', rot=90, figsize=(18,12))

    plt.title('Spending History')
    plt.show()


if __name__ == '__main__':
    main()