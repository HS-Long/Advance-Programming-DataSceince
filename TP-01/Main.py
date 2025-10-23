import pandas as pd
from Exercise1 import CSVReader
from Exercise2 import DataCleaner, DropMissing, FillMean, FillMode
from Exercise3 import CSVReaderWithLogging
from Exercise4 import TransformFactory
from Exercise5 import CSVDataPipeline


def run_ex1():
    print("\n=== Exercise 1: CSV Reader ===")
    file_path = input("Enter CSV file path: ").strip()
    reader = CSVReader(file_path)
    reader.read()
    n = int(input("Enter number of rows to preview: "))
    reader.preview(n)


def run_ex2():
    print("\n=== Exercise 2: Missing Value Strategies ===")
    file_path = input("Enter CSV file path: ").strip()
    df = pd.read_csv(file_path)
    cleaner = DataCleaner(DropMissing())

    df_clean = cleaner.clean(df)
    print("\nAfter DropMissing:\n", df_clean)

    cleaner.set_strategy(FillMean())
    df_clean = cleaner.clean(df)
    print("\nAfter FillMean:\n", df_clean)

    cleaner.set_strategy(FillMode())
    df_clean = cleaner.clean(df)
    print("\nAfter FillMode:\n", df_clean)


def run_ex3():
    print("\n=== Exercise 3: CSV Reader with Logging and Timing ===")
    file_path = input("Enter CSV file path: ").strip()
    reader = CSVReaderWithLogging(file_path)
    reader.read()
    n = int(input("Enter number of rows to preview: "))
    reader.preview(n)


def run_ex4():
    print("\n=== Exercise 4: Data Transformation Factory ===")
    data = {
        "Name": ["Alice", "Bob", "alice", "Bob"],
        "Age": [25, 30, 25, 30],
        "Salary": [50000, 60000, 50000, 60000]
    }
    df = pd.DataFrame(data)
    factory = TransformFactory()

    while True:
        print("\nSelect transformation:")
        print("1. NormalizeColumns")
        print("2. StandardizeText")
        print("3. RemoveDuplicates")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            transform = factory.get_transform("normalize")
        elif choice == "2":
            transform = factory.get_transform("standardize_text")
        elif choice == "3":
            transform = factory.get_transform("remove_duplicates")
        elif choice == "4":
            print("Returning to main menu...\n")
            break
        else:
            print("Invalid choice, please try again.")
            continue

        df = transform.apply(df)
        print("\nResult:\n", df)


def run_ex5():
    print("\n=== Exercise 5: Full Data Cleaning Pipeline ===")
    input_path = input("Enter input CSV path: ").strip()
    output_path = input("Enter output CSV path (e.g., cleaned_data.csv): ").strip()

    print("\nSelect missing value handling strategy:")
    print("1. DropMissing")
    print("2. FillMean")
    print("3. FillMode")
    clean_choice = input("Enter choice: ")

    if clean_choice == "1":
        cleaning_strategy = DropMissing()
    elif clean_choice == "2":
        cleaning_strategy = FillMean()
    elif clean_choice == "3":
        cleaning_strategy = FillMode()
    else:
        print("Invalid choice! Defaulting to FillMean.")
        cleaning_strategy = FillMean()

    print("\nSelect transformation:")
    print("1. NormalizeColumns")
    print("2. StandardizeText")
    print("3. RemoveDuplicates")
    trans_choice = input("Enter choice: ")

    if trans_choice == "1":
        transform_type = "normalize"
    elif trans_choice == "2":
        transform_type = "standardize_text"
    elif trans_choice == "3":
        transform_type = "remove_duplicates"
    else:
        print("Invalid choice! Defaulting to 'standardize_text'.")
        transform_type = "standardize_text"

    pipeline = CSVDataPipeline(input_path, output_path, cleaning_strategy, transform_type)
    pipeline.run()


def main():
    while True:
        print("\n" + "="*40)
        print("Advanced Programming — TP-01 Menu")
        print("="*40)
        print("1. Exercise 1 — CSV Reader")
        print("2. Exercise 2 — Missing Value Strategies")
        print("3. Exercise 3 — CSV Reader with Logging/Timing")
        print("4. Exercise 4 — Transformation Factory")
        print("5. Exercise 5 — Full Cleaning Pipeline")
        print("6. Exit")
        print("="*40)

        choice = input("Select an exercise (1–6): ").strip()

        if choice == "1":
            run_ex1()
        elif choice == "2":
            run_ex2()
        elif choice == "3":
            run_ex3()
        elif choice == "4":
            run_ex4()
        elif choice == "5":
            run_ex5()
        elif choice == "6":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main()

