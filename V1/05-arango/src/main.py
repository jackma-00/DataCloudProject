from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "upload your file to /arango"}


@app.post("/arango/")
async def arango_file(file: UploadFile):
    # 1. arango uploaded csv file
    print("Processing (Arango) uploaded file ...")
    # 2. save the processed file to a common storage location
    print("Saving processed file to common storage location ...")

    return {"response": "ok"}
