

from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.face import FaceClient

endpoint = "https://xxx.cognitiveservices.azure.com/"
credential = AzureKeyCredential("xxx")
face_client = FaceClient(endpoint, credential)