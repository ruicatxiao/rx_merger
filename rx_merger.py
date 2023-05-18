import pandas as pd
import sys

def merge_files(file1_path, file2_path, output_path, file1_column_index, file2_column_index):
    # Read file 1
    file1 = pd.read_csv(file1_path, delimiter='\t')
    # Read file 2
    file2 = pd.read_csv(file2_path, delimiter='\t')

    # Get the column names based on the provided indices
    file1_column_name = file1.columns[file1_column_index]
    file2_column_name = file2.columns[file2_column_index]

    # Merge the two files based on the specified columns
    merged = file1.merge(file2, left_on=file1_column_name, right_on=file2_column_name, how='left')

    # Replace missing values in the newly added columns with "not_found"
    new_columns = file2.columns.drop(file2_column_name)
    for col in new_columns:
        merged[col].fillna('not_found', inplace=True)

    # Save the merged file to a new TSV
    merged.to_csv(output_path, sep='\t', index=False)
    print(f"Merged file saved as {output_path}")

if __name__ == '__main__':
    if len(sys.argv) < 6:
        print("Usage: python rx_merger.py <file1_path> <file2_path> <output_path> <file1_column_index> <file2_column_index>")
        sys.exit(1)

    file1_path = sys.argv[1]
    file2_path = sys.argv[2]
    output_path = sys.argv[3]
    file1_column_index = int(sys.argv[4])
    file2_column_index = int(sys.argv[5])

    merge_files(file1_path, file2_path, output_path, file1_column_index, file2_column_index)
