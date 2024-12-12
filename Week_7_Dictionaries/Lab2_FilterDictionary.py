"""
Create a dictionary with population data for counties in Northern Ireland.
Calculate the male-to-female population for each county using given ratios.
Save the data in a CSV file.
"""

import csv

# Step 1: Create population data for counties in Northern Ireland
county_population_data = {
    "Antrim": 618108,
    "Armagh": 174792,
    "Down": 531665,
    "Fermanagh": 116835,
    "Londonderry": 247132,
    "Tyrone": 181858
}

# Step 2: Define male-to-female ratio
# Example ratio: 49% males, 51% females
male_ratio = 0.49
female_ratio = 0.51

# Step 3: Calculate male and female populations for each county
county_gender_population = []
for county, population in county_population_data.items():
    males = int(population * male_ratio)
    females = int(population * female_ratio)
    county_gender_population.append({
        "County": county,
        "Population": population,
        "Males": males,
        "Females": females
    })

# Step 4: Save the data to a CSV file
csv_file = "northern_ireland_population.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["County", "Population", "Males", "Females"])
    writer.writeheader()
    writer.writerows(county_gender_population)

print(f"Population data saved to {csv_file}")
