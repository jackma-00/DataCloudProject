
# 1. load the file
file = open("./data/sample.txt", "w")

# 2. unzip uploaded file
print("Unzip uploaded file ...")
file.write("unzipped")

# 3. save the processed file
file.close()