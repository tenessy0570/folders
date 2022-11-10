import uvicorn
from fastapi import FastAPI

from config import folder_for_app

app = FastAPI()


@app.get("/api/meta")
async def get_folder_items():
    items = {"data": []}

    for item in folder_for_app.iterdir():
        type_ = "folder" if item.is_dir() else "file"
        timestamp = item.stat().st_mtime

        items["data"].append({
            "name": item.name,
            "type": type_,
            "time": round(timestamp)
        })

    return items

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000, log_level="info")
