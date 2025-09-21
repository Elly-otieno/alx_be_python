'''
Utilizing conditional statements to to guide program execution based on the input regarding weather conditions
'''

weather = input("What's the weather like today? (sunny/rainy/cold): ")

if weather == "sunny":
    recomend = "Wear a t-shirt and sunglasses."
elif weather == "rainy":
    recomend = "Don't forget your umbrella and a raincoat."
elif weather == "cold":
    recomend = 'Make sure to wear a warm coat and a scarf.'
else:
    recomend = "Sorry, I don't have recommendations for this weather."

print(recomend)