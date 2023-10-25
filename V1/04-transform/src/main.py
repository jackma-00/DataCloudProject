from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "upload your file to /transform"}


@app.post("/transform/")
async def transform_file(file: UploadFile):
    # 1. transform uploaded csv file
    print("Transforming uploaded file ...")
    # 2. save the processed file to a common storage location
    print("Saving processed file to common storage location ...")

    return {"response": "ok"}
