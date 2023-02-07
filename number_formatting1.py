'''✨ Number formatting in Python ✨'''

population = 80000000
in_city = 55222222
in_village = population - in_city
in_city_percentage = in_city/population
in_village_percentage = in_village/population

print(f"{population:.2f}")          # 80000000.00
print(f"{population:g}")
print(f"{in_city:,}")               # 55, 222, 222
print(f"{in_village:,.2f}")         # 24, 777, 778.00
print(f"{in_city_percentage:.4f}")  # 0.6903(out of 1)
print(f"{in_village_percentage:.2%}")  # 30.97%


# For more on Python follow: https://twitter.com/CodingMantras
