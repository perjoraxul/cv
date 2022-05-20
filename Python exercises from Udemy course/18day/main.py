import colorgram
# import os


# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print(f"Files in {cwd}: {files}")

colors = colorgram.extract('dots.jpg' , 6)

first_color = colors[0]

rgb = first_color.rgb[0]
print(rgb)