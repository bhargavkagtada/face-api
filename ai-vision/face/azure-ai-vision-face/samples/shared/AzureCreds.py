

from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.face import FaceClient

endpoint = "https://eus-face-api.cognitiveservices.azure.com/"
credential = AzureKeyCredential("172a66e425914a92b4acdc064e5d9d26")
face_client = FaceClient(endpoint, credential)