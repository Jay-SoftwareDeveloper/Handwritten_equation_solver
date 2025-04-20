import streamlit as st
import cv2
import pytesseract
from PIL import Image
import numpy as np
import sympy as sp

# OCR and Equation Solver Functions

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blur, 255,
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 2)
    return thresh

def extract_equation_from_image(image):
    processed = preprocess_image(image)
    text = pytesseract.image_to_string(processed, config='--psm 7')
    return text.strip()

def solve_equation(equation_text):
    try:
        x = sp.symbols('x')
        lhs, rhs = equation_text.split('=')
        eq = sp.Eq(sp.sympify(lhs), sp.sympify(rhs))
        solutions = sp.solve(eq, x)
        steps = sp.pretty(eq) + "\n\nSolutions: " + str(solutions)
        return eq, solutions, steps
    except Exception as e:
        return None, None, f"Error: {e}"

# Streamlit UI
st.set_page_config(page_title="🧮 Handwritten Equation Solver", layout="centered")
st.title("🧠 AI-Based Handwritten Equation Solver")
st.markdown("Upload an image of a handwritten linear or quadratic equation, and get the solution!")

uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    img_np = np.array(image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Processing Image..."):
        extracted_text = extract_equation_from_image(img_np)

    st.subheader("📝 Extracted Equation")
    st.code(extracted_text)

    if extracted_text:
        st.subheader("🔍 Solution")
        eq, sol, steps = solve_equation(extracted_text)
        st.text(steps)
    else:
        st.warning("Couldn't extract an equation from the image. Try another image.")


