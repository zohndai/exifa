"""

All code contributed to Exifa.net is © 2024 by Sahir Maharaj. 
The content is licensed under the Creative Commons Attribution 4.0 International License. 
This allows for sharing and adaptation, provided appropriate credit is given, and any changes made are indicated.

When using the code from Exifa.net, please credit as follows: "Code sourced from Exifa.net, authored by Sahir Maharaj, 2024."

For reporting bugs, requesting features, or further inquiries, please reach out to Sahir Maharaj at sahir@sahirmaharaj.com.

Connect with Sahir Maharaj on LinkedIn for updates and potential collaborations: https://www.linkedin.com/in/sahir-maharaj/

Hire Sahir Maharaj: https://topmate.io/sahirmaharaj/362667
"""

import streamlit as st
import replicate
import os
import pdfplumber
from docx import Document
import pandas as pd
from io import BytesIO
from transformers import AutoTokenizer
import exifread
import requests
from PIL import Image
import numpy as np
import plotly.express as px
import matplotlib.colors as mcolors
import plotly.graph_objs as go
import streamlit.components.v1 as components
import random

config = {
    "toImageButtonOptions": {
        "format": "png",
        "filename": "custom_image",
        "height": 720,
        "width": 480,
        "scale": 6,
    }
}

icons = {
    "assistant": "https://raw.githubusercontent.com/sahirmaharaj/exifa/2f685de7dffb583f2b2a89cb8ee8bc27bf5b1a40/img/assistant-done.svg",
    "user": "https://raw.githubusercontent.com/sahirmaharaj/exifa/2f685de7dffb583f2b2a89cb8ee8bc27bf5b1a40/img/user-done.svg",
}

