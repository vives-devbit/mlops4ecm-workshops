import requests
import dash
from dash import html, dcc
from dash.dependencies import Output, Input
import base64
import io
from PIL import Image

# URL of the FastAPI backend
API_URL = "http://backend:8000"

# Create the Dash app
app = dash.Dash(__name__)
app.title = "Grocery Classifier Frontend"

# App layout: title, button, and output area
app.layout = html.Div([
    html.H1("🍎 Grocery Image Classifier"),
    html.Button("Predict random image", id="predict-button", n_clicks=0),
    html.Div(id="output"),
])

def get_random_image():
    """
    TODO: Fetch a random image from the FastAPI backend.
    You need to make a GET request to the /random-image endpoint
    and return the image as raw bytes.
    """
    response = requests.get(f"{API_URL}/random-image")
    response.raise_for_status()
    return response.content

def predict_image(image_bytes):
    """
    This part is done for you.
    Sends image bytes to the /predict endpoint and returns the predicted class.
    """
    files = {"file": ("image.jpg", image_bytes, "image/jpeg")}
    response = requests.post(f"{API_URL}/predict", files=files)
    response.raise_for_status()
    return response.json()["prediction"]

@app.callback(
    Output("output", "children"),
    Input("predict-button", "n_clicks"),
)
def update_output(n_clicks):
    if n_clicks == 0:
        return ""
    try:
        # Get a random image from the backend (you will fix this!)
        image_bytes = get_random_image()

        # Predict the image class
        prediction = predict_image(image_bytes)

        # Convert image bytes to base64 for display in browser
        encoded = base64.b64encode(image_bytes).decode()
        img_src = f"data:image/jpeg;base64,{encoded}"

        return html.Div([
            html.Img(src=img_src, style={"width": "300px", "margin": "20px 0"}),
            html.H3(f"Prediction: {prediction}"),
        ])
    except Exception as e:
        return html.Div([
            html.P("❌ Something went wrong:"),
            html.Pre(str(e))
        ])

# Start the app server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)

