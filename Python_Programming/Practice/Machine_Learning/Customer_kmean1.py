import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():
    df = pd.read_csv("Mall_Customers.csv")

    print("Dataset loaded with values")
    print(df.head())

    X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
    scalar = StandardScaler()
    X_scaled = scalar.fit_transform(X)

    print("Scaled data : ")

    # step 4
    WCSS = []

    for i in range(1, 11):
        model = KMeans(n_clusters=i, n_init=10, random_state=42)
        model.fit(X_scaled)
        WCSS.append(model.inertia_)

    print("WCSS values : ")

    for i in range(len(WCSS)):
        print(f"{i+1} : {WCSS[i]}")

    # Plot the elbow curve
    plt.plot(range(1, 11), WCSS,marker='o', linestyle='--')
    plt.title('Marvellous Elbow Method')
    plt.xlabel('Number of Clusters : k')
    plt.ylabel('WCSS')
    plt.grid(True)
    plt.show()

    # step 6 final model
    model = KMeans(n_clusters=4, n_init=10, random_state=42)
    clusters = model.fit_predict(X_scaled)
    df['Cluster'] = clusters

    print("Dataset with clusters : ")
    print(df.head(20))


if __name__ == "__main__":
    main()