from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="DreamForge 3D Engine", version="1.0.0")

class Generate3DRequest(BaseModel):
    prompt: str
    export_format: str = "glb"
    pbr_textures: bool = True

@app.get("/")
def index():
    return {"service": "DreamForge 3D Gaussian Splatting API", "status": "ready"}

@app.post("/api/generate")
def generate_3d(req: Generate3DRequest):
    return {
        "status": "completed",
        "prompt": req.prompt,
        "format": req.export_format,
        "download_url": f"/outputs/{req.prompt.lower().replace(' ', '_')}.{req.export_format}",
        "splats_count": 348200
    }
