from load_csv import load
import matplotlib.pyplot as plt

def main():
    df = load('./../population_total.csv')
    
    countries = ['Belgium', 'France']
    # countries = ['Morocco', 'United States']

    for country in countries:
        if country in df['country'].values:
            country_data = df[df['country'] == country].iloc[0, 1:252]
            country_data = ( country_data.str.replace('M', '', regex=True).astype(float) )

            years = country_data.index.astype(float)
            population = country_data.values
            
            plt.plot(years, population, label=country)
        else:
            print(f"Error: Country {country} not found in the dataset.")

    plt.title(f"population Projections")
    plt.xlabel("Year")
    plt.ylabel("population (in Millions)")
    plt.legend(loc='best')
    plt.show()

if __name__ == '__main__':
    main()