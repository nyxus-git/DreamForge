# DreamForge 🌌🧊
> Generative Text-to-3D World & Asset Synthesis Engine using 3D Gaussian Splatting and PBR baking.

## 🚀 Overview
DreamForge generates textured, game-engine-ready 3D assets from text prompts and reference photos. Built on 3D Gaussian Splatting (3DGS) and NeRF reconstruction, it automatically retopologizes geometry, unrolls UVs, bakes 4K PBR textures, and exports clean `.glb` assets.

## 🛠️ Tech Stack
- **3D Generation**: PyTorch, 3D Gaussian Splatting, NeRF, Marching Tetrahedra
- **Packaging & Meshing**: Blender Python headless API, Trimesh, Open3D
- **Viewer**: Three.js WebGL Gaussian Splat viewer

## ⚡ Quick Start (Arch Linux)
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --port 8000 --reload
```
