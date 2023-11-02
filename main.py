# Import necessary libraries
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from api.classify import router as classify_router
import uvicorn

# Initialize the FastAPI app
app = FastAPI()

# Add CORS middleware to allow connections to the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Reroute / to /docs
@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")

# The classification endpoint
app.include_router(classify_router)

#Run the app using uvicorn (from the command line) with the following command:
# uvicorn main:app --reload

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
