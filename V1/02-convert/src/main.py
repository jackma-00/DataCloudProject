from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "upload your file to /convert"}


@app.post("/convert/")
async def convert_file(file: UploadFile):
    # 1. convert uploaded csv file
    print("Converting uploaded file ...")
    # 2. save the processed file to a common storage location
    print("Saving processed file to common storage location ...")

    return {"response": "ok"}
