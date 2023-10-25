
# 1. load the file
file = open("./data/sample.txt", "w")

# 2. convert uploaded file
print("Converting uploaded file ...")
file.write("converted")

# 3. save the processed file
file.close()