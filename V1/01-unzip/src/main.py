from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "upload your file to /unzip"}


@app.post("/unzip/")
async def unzip_file(file: UploadFile):
    # 1. unzip uploaded file
    print("Unzip uploaded file ...")
    # 2. save the processed file to a common storage location
    print("Saving processed file to common storage location ...")

    return {"response": "ok"}
