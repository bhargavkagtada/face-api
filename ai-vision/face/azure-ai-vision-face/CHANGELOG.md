# Release History

## 1.0.0b2 (Unreleased)

### Features Added

### Breaking Changes

### Bugs Fixed

### Other Changes

## 1.0.0b1 (07-29-2024)

This is the first preview of the `azure-ai-vision-face` client library that follows the [Azure Python SDK Design Guidelines](https://azure.github.io/azure-sdk/python_design.html).
This library replaces the package [azure-cognitiveservices-vision-face](https://pypi.org/project/azure-cognitiveservices-vision-face/).

### Features Added

- Added support to initiate a Liveness detection session.

### Breaking Changes

- This library only supports the API of the the operation groups below of [Azure AI Face v1.1-preview.1](https://learn.microsoft.com/rest/api/face/operation-groups?view=rest-face-v1.1-preview.1):
  - Face Detection Operations
  - Face Recognition Operations: only `Find Similiar`, `Group` and `Verify Face To Face`.
  - Liveness Session Operations
- The namespace/package name for Azure AI Face has changed from `azure.cognitiveservices.vision.face` to `azure.ai.vision.face`.
- Two client design:
  - `FaceClient` to perform core Face functions such as face detection, verification, finding similar faces and grouping faces.
  - `FaceSessionClient` to interact with sessions which is used for Liveness detection.