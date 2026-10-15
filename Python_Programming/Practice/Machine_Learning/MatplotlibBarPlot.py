import matplotlib.pyplot as plt

def main():
    Language = ["C","C++","Java","Python"]
    Students = [30,20,35,55]

    plt.bar(
        Language,                   # Values of X axis
        Students,                   # Values of Y axis
        width = 0.6,                # Width of bars
        edgecolor = "black",        # border color of bal
        linewidth = 1,              # width of bar border   
        alpha = 0.8,                # Transparency 0.0 to 1.0
        label = "Students"          # legend text
    )

    plt.title("Marvellous Bar Plot")
    plt.xlabel("Languages")
    plt.ylabel("Number of students")
    plt.legend()
    plt.show()

if(__name__ == "__main__"):
    main()