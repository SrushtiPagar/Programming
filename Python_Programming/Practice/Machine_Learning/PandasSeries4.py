import pandas as pd

def main():
    # Heteroginity is allowed because everything is treated as a Object

    sobj = pd.Series([11.2,21,'51.2',True])

    print(sobj)

if(__name__ == "__main__"):
    main()