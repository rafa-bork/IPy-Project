import pandas as pd
import sys

def welcome_message():
    print("Welcome to the Forest Inventory Analyst!")
    print("Please add your tree data to the tree_data.csv file in the correct format")
    while True:
        print("If help is needed type 'help', if the information was correctly added press <Enter>")
        welcome = input().strip().casefold()
        if welcome == "help": 
            help()
        elif welcome == "exit":
            print("Exiting program...")
            sys.exit()
        elif welcome == "":
            return
        else:
            print("If you want to close the program type 'exit'")

def help():
    print("---")
    print("This Program is a tool to help in the characterization and analysis of a tree stand")
    print("This tool uses mathematical and statistical tools to calculate and infer the features of the stand from a short grouping of the tree's accurate measurements")
    print("These measurements, the height and the diameter of each tree in the plot, need to be inserted into the tree_data.csv file in the correct order")
    print("This file is in the same folder as this python script")
    print("")
    print("This file has 5 columns: 'tree_ID', 'species', 'DBH', 'height' and 'COD_Status'")
    print("The 'tree_ID' column must have a sequential numerical order to uniquely identify each tree in the plot")
    print("The 'species' column must have a code that corresponds to the tree's species")
    print("         species Code             Common Name                Scientific Name")
    print("         Pb                       Maritime Pine              Pinus pinaster")
    print("         Pm                       Stone Pine                 Pinus pinea")
    print("         Ec                       Southern Blue Gum          Eucalyptus globulus")
    print("         Sb                       Cork Oak                   Quercus suber")
    print("The 'DBH' column must have the trunk's measured diameter at breast hight (1.30m), in centimetres")
    print("The 'height' column must have the tree's measured total height, in meters")
    print("     You should at least provide one of these measurements")
    print("The 'COD_status' column must have a code tahts represents the tree's capacity. The correspondence is in the following table")
    print("         COD_status              Tree Status")
    print("         1                       Alive")
    print("         2                       Dead")
    print("         3                       Missing (relevant in stands planted with a regular step)")
    print("         4                       Stump")
    print("---")

class Tree:
    def __init__(self, tree_ID, species, dbh, height, cod_status):
        self.tree_ID = tree_ID
        self.species = species
        self.dbh = dbh
        self.height = height
        self.cod_status = cod_status

    def __repr__(self):
        return f"Tree(tree_ID={self.tree_ID}, species={self.species}, dbh={self.dbh}, height={self.height}, cod_status={self.cod_status})"

def read_my_data(filepath=None):
    print("Importing the Datatable...")
    try:
        # Attempt to read the CSV file into a pandas DataFrame
        df = pd.read_csv(filepath)
        print("\nHere is the table:\n")
        print(df.to_string(index=False))  # Display the DataFrame as a formatted table

        # Create a list to store Tree objects
        trees = []

        # Iterate over each row in the DataFrame and create Tree objects
        for _, row in df.iterrows():
            tree_ID = row.get("tree_ID", None)
            species = row.get("species", "Unknown")

            # Convert DBH to float; if it fails, set to 0
            try:
                dbh = float(row.get("DBH", 0))
            except ValueError:
                dbh = 0.0

            # Convert height to float
            try:
                height = float(row.get("height", 0))
            except ValueError:
                height = 0.0

            # Tree status (COD_Status)
            cod_status = row.get("COD_Status", "ALIVE")

            # Create a Tree object and add it to the list
            tree = Tree(tree_ID, species, dbh, height, cod_status)
            trees.append(tree)

        # Return the list of Tree objects
        return trees

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    except pd.errors.ParserError as e:
        print(f"Error parsing CSV: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    welcome_message()  
    trees = read_my_data()  
    for tree in trees:
        print(tree)  


if __name__ == "__main__":
    main()