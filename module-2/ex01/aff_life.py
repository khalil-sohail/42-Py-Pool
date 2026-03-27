from load_csv import load
import matplotlib.pyplot as plt

def main():
    df = load('./../life_expectancy_years.csv')
    
    country = 'Morocco'
    # country = 'France'
    if country in df['country'].values:
        country_data = df[df['country'] == country].iloc[0, 1:]
        
        years = country_data.index.astype(int)
        life_expectancy = country_data.values
        
        plt.plot(years, life_expectancy, label=country)
        plt.title(f"{country} Life Expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.show()
    else:
        print(f"Error: Country {country} not found in the dataset.")

if __name__ == '__main__':
    main()