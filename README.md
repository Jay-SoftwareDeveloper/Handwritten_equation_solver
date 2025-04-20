# AI-Based Handwritten Equation Solver 🧠🧮

This is a simple and interactive Streamlit web app that helps you solve handwritten linear or quadratic equations. Just upload an image of your handwritten equation—the app will read it using OCR (powered by Tesseract), process it, and solve it step-by-step using SymPy.

## 🚀 Features
- Upload an image of a handwritten equation
- Automatically processes the image using OpenCV
- Uses Tesseract to extract the text (OCR)
- Solves both linear and quadratic equations
- Shows the step-by-step solution using SymPy so you can understand how it's done

## 🛠 Installation
```bash
1. Clone this repo: git clone https://github.com/your-username/handwritten-equation-solver.git
2. Navigate to the folder: cd handwritten-equation-solver
3. Install: pip install -r requirements.txt
4. Run: streamlit run streamlit_app.py
```

## 🔧 Requirements
Make sure you have the following libraries installed:
- streamlit
- opencv-python
- pytesseract
- numpy
- sympy
- pillow

Don’t forget: Tesseract OCR must be installed on your system and added to your system PATH for this to work correctly.

#### Important
- The project was initially hosted on a GitHub account linked to my college email (COG domain), which has since been deleted. I've now reuploaded it here on my new GitHub to preserve and showcase the work.
