from typing import Optional

from fastapi import FastAPI

app = FastAPI()


from pytube import YouTube

@app.get("/{idUrl}")
def read_root(idUrl):
    yt = YouTube('https://youtu.be/'+idUrl).streams.filter(res="720p").first().download('Video')
    return {"Video": yt}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
