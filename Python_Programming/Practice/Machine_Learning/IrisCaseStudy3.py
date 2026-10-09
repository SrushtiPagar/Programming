from sklearn.datasets import load_iris

def main():
    print("-"*30)
    print("Iris Classification Case Study")
    print("-"*30)

    Dataset = load_iris()

    # Metadata of the dataset
    print("Independent Variables are : ")
    print(Dataset.feature_names)
    print("Length of Independent Variable : ",len(Dataset.feature_names))

    print("Dependent Variables are : ")
    print(Dataset.target_names)
    print("Length of Dependent Variable : ",len(Dataset.target_names))

    

if(__name__ == "__main__"):
    main()