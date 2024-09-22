from fastapi import FastAPI, File, UploadFile, Form, HTTPException,Request
from fastapi.responses import JSONResponse
import os
import time
import google.generativeai as genai
import uvicorn
from chatbot import chatbot_response
import requests

app = FastAPI()

@app.post("/chat")
async def chat(user_input: str = Form(None)):
    try:
        if not user_input:
            raise HTTPException(status_code=400, detail="No query asked")

        response = chatbot_response(user_input)
        return {"response": response}


    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)



