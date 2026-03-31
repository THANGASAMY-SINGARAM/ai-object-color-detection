##  Configuration

###  System Requirements
- Python 3.8 or higher
- Webcam (for real-time detection)
- Minimum 4GB RAM (8GB recommended)

###  Dependencies
The project uses the following libraries:
- OpenCV
- NumPy
- Ultralytics YOLO
- Pillow

Install all dependencies using:

pip install -r requirements.txt

###  Model Configuration
- The system uses the YOLOv8 pre-trained model (`yolov8n.pt`)
- The model is automatically downloaded when the program runs for the first time
- No manual training is required

###  Color Configuration
- Colors are defined in `main.py` using BGR values
- HSV ranges are dynamically generated using the `get_limits()` function in `util.py`
- Special handling is implemented for red color due to HSV hue wrapping

###  Execution Setup
1. Activate virtual environment:
   - Windows: .venv\Scripts\activate
   - Mac/Linux: source .venv/bin/activate

2. Run the application:
   python main.py

###  Notes
- Ensure proper lighting for better color detection accuracy
- Avoid background colors similar to object colors
