import csv
import io
from fastapi import FastAPI, File, HTTPException, UploadFile
import uvicorn

app = FastAPI()

@app.post("/top-threats")
def upload_csv(file: UploadFile = File(...)):
    if file.content_type != "text/csv":
        raise HTTPException(status_code=400, detail="File must be a CSV")

    content = file.file.read()

    try:
        decoded = content.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="not decode")

    reader = csv.reader(io.StringIO(decoded))
    rows = [row for row in reader]

    return {
        "message": "CSV load",
        "rows_count": len(rows),
        "data": rows,
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)