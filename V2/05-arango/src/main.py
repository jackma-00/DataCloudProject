
# 1. load the file
file = open("./data/sample.txt", "w")

# 2. arango uploaded file
print("Processing (Arango) uploaded file ...")
file.write("arango")

# 3. save the processed file
file.close()