from prettytable import PrettyTable

# Specify the Column Names while initializing the Table
myTable = PrettyTable(["Student Name", "Class", "Section", "Percentage"])

# Add rows
myTable.add_row(["Leo", "X", "B", "91.2%"])
myTable.add_row(["Juan", "X", "C", "10.2%"])
myTable.add_row(["Host", "X", "A", "19.3%"])
myTable.add_row(["Local", "X", "B", "23.5%"])
myTable.add_row(["Meow", "X", "B", "56.8%"])
myTable.add_row(["Gua", "X", "C", "37.7%"])
myTable.add_row(["Kennedy", "X", "D", "29.4%"])
myTable.add_row(["Lucas", "X", "A", "97.2%"])
myTable.add_row(["Boss Bonny", "X", "B", "90.1%"])

print(myTable)