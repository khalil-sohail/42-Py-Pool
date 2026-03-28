from load_csv import load
import matplotlib.pyplot as plt


def main():
    path = './../income_per_person_gdppercapita_ppp_inflation_adjusted.csv'
    income_per_person = load(path)
    life_expectancy_years = load('./../life_expectancy_years.csv')

    income_per_person = income_per_person['1900']
    life_expectancy_years = life_expectancy_years['1900']

    plt.scatter(income_per_person, life_expectancy_years)

    plt.title('1900')
    plt.xlabel('gross domestic product')
    plt.ylabel('Life Expectancy (years)')

    plt.xscale('log')
    plt.show()


if __name__ == '__main__':
    main()
