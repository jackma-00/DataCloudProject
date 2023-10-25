
# 1. load the file
file = open("./data/sample.txt", "w")

# 2. transform uploaded file
print("Transforming uploaded file ...")
file.write("transformed")

# 3. save the processed file
file.close()