'''
Utilizing conditional statements to to guide program execution based on the input regarding weather conditions
'''

condition = input("What's the weather like today? (sunny/rainy/cold): ")

if condition == 'sunny':
    recomend = "Wear a t-shirt and sunglasses."
elif condition == 'rainy':
    recomend = "Don't forget your umbrella and a raincoat."
elif condition == 'cold':
    recomend = 'Make sure to wear a warm coat and a scarf.'
else:
    recomend = "Sorry, I don't have recommendations for this weather."

print(recomend)