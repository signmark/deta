from typing import Union

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/")
async def read_items(user_agent: Union[str, None] = Header(default=None)):
    # with open("user_agent.txt", "a") as f:
    #     f.write(user_agent)
    return {"User-Agent": user_agent}
