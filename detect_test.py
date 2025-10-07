import torch
import cv2
from ultralytics import YOLO

# --- 1. Check PyTorch/GPU Setup ---
print("\n--- PyTorch Setup Check ---")
if torch.cuda.is_available():
    print(f"✅ GPU is available. Device Name: {torch.cuda.get_device_name(0)}")
    device = 'cuda'
else:
    print("⚠️ GPU not found. Running on CPU.")
    device = 'cpu'

# --- 2. Check OpenCV (cv2) ---
print("\n--- OpenCV Check ---")
print(f"✅ OpenCV version: {cv2.__version__}")

# --- 3. Check Ultralytics (YOLOv8) ---
print("\n--- Ultralytics/YOLOv8 Test ---")
try:
    # Load a pretrained detection model (this downloads the weights if not present)
    model = YOLO('yolov8n.pt')
    print("✅ YOLOv8 Model loaded successfully (yolov8n.pt).")
    
    # Run a simple check (replace '0' with your video path if you want to test immediately)
    print(f"Model will run on: {device.upper()}")
    
    # Optional: If you have a video in the 'videos' folder, use this for a real test:
    # results = model.predict(source='../videos/traffic_cam.mp4', save=True, device=device)
    # print("✅ Prediction test complete.")
    
except Exception as e:
    print(f"❌ ERROR loading YOLO model: {e}")

print("\nDay 2 Test Script finished.")