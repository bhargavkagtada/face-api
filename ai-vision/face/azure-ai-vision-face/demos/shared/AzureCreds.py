

from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.face import FaceClient

endpoint = "https://xyz.cognitiveservices.azure.com/"
credential = AzureKeyCredential("abc")
face_client = FaceClient(endpoint, credential)