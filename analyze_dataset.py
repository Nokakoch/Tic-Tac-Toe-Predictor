import pandas as pd

def analye_data(file_path):
    try:
        dataset = pd.read_csv(file_path)
        print(f"Dataset shape: {dataset.shape[0]} Row, {dataset.shape[1]} Col\n")
        for col in dataset.columns:
            print(f"Analyz column: {col}\n")
            coldata = dataset[col]
            type = coldata.dtype
            print(f"- Type: {type}")
            if type == "str":
                print(f"- Unique values count: {coldata.nunique()} (", end='')
                uniqueValues = coldata.unique()
                for uniqeue in uniqueValues:
                    print(uniqeue,end=', ')
                print(f")\n- Missing values: {coldata.isnull().sum()}")
                print(f"- Values data:")
                counts = coldata.value_counts()
                percentages = coldata.value_counts(normalize=True) * 100
                
                for index, val in counts.items():
                    print(f"- {index}: {val} records ({percentages[index]:.1f}%)")
                
                top_value = counts.index[0]
                print(f"\n- '{top_value}' is the most repeated value.")
            else:
                print(f"- Missing values: {coldata.isnull().sum()}")
                print(f"- Statistics:")
                print(f" - Mini: {coldata.min()}")
                print(f" - Max: {coldata.max()}")
                print(f" - Average: {coldata.mean():.2f}")
            
            print("=" * 50)
    
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    analye_data("tictactoe_games.csv")
