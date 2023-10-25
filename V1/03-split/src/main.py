from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "upload your file to /split"}


@app.post("/split/")
async def split_file(file: UploadFile):
    # 1. split uploaded csv file
    print("Splitting uploaded file ...")
    # 2. save the processed file to a common storage location
    print("Saving processed file to common storage location ...")

    return {"response": "ok"}
