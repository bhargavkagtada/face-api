# Azure AI Face client library for Python

The Azure AI Face service provides AI algorithms that detect, recognize, and analyze human faces in images. It includes the following main features:

- Face detection and analysis
- Liveness detection
- Face recognition
  - Face verification ("one-to-one" matching)
- Find similar faces
- Group faces

## Getting started

### Prerequisites

- Python 3.8 or later is required to use this package.
- You need an [Azure subscription][azure_sub] to use this package.
- Your Azure account must have a `Cognitive Services Contributor` role assigned in order for you to agree to the responsible AI terms and create a resource. To get this role assigned to your account, follow the steps in the [Assign roles][azure_role_assignment] documentation, or contact your administrator.
- Once you have sufficient permissions to control your Azure subscription, you need either
  * an [Azure Face account][azure_portal_list_face_account] or
  * an [Azure AI services multi-service account][azure_portal_list_cognitive_service_account]

### Create a Face or an Azure AI services multi-service account

Azure AI Face supports both [multi-service][azure_cognitive_service_account] and single-service access. Create an Azure AI services multi-service account if you plan to access multiple Azure AI services under a single endpoint/key. For Face access only, create a Face resource.

* To create a new Face or Azure AI services multi-service account, you can use [Azure Portal][azure_portal_create_face_account], [Azure PowerShell][quick_start_create_account_via_azure_powershell], or [Azure CLI][quick_start_create_account_via_azure_cli].

### Install the package

```bash
python -m pip install azure-ai-vision-face
```
## Key concepts

### FaceClient

`FaceClient` provides operations for:

 - Face detection and analysis: Detect human faces in an image and return the rectangle coordinates of their locations,
   and optionally with landmarks, and face-related attributes. This operation is required as a first step in all the
   other face recognition scenarios.
 - Face recognition: Confirm that a user is who they claim to be based on how closely their face data matches the target face.
   It includes Face verification ("one-to-one" matching).
 - Finding similar faces from a smaller set of faces that look similar to the target face.
 - Grouping faces into several smaller groups based on similarity.


### FaceSessionClient

`FaceSessionClient` is provided to interact with sessions which is used for Liveness detection.

 - Create, query, and delete the session.
 - Query the liveness and verification result.
 - Query the audit result.

### Additional documentation

For more extensive documentation on Azure AI Face, see the [Face documentation][face_product_docs] on learn.microsoft.com.

[azure_sub]: https://azure.microsoft.com/free/
[azure_role_assignment]: https://learn.microsoft.com/azure/role-based-access-control/role-assignments-steps
[azure_portal_list_face_account]: https://portal.azure.com/#blade/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/Face
[azure_portal_list_cognitive_service_account]: https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/AllInOne
[azure_cognitive_service_account]: https://learn.microsoft.com/azure/ai-services/multi-service-resource?tabs=windows&pivots=azportal#supported-services-with-a-multi-service-resource
[azure_portal_create_face_account]: https://ms.portal.azure.com/#create/Microsoft.CognitiveServicesFace
[quick_start_create_account_via_azure_cli]: https://learn.microsoft.com/azure/ai-services/multi-service-resource?tabs=windows&pivots=azcli
[quick_start_create_account_via_azure_powershell]: https://learn.microsoft.com/azure/ai-services/multi-service-resource?tabs=windows&pivots=azpowershell

[get_key_via_azure_portal]: https://learn.microsoft.com/azure/ai-services/multi-service-resource?tabs=windows&pivots=azportal#get-the-keys-for-your-resource
[get_key_via_azure_cli]: https://learn.microsoft.com/azure/ai-services/multi-service-resource?tabs=windows&pivots=azcli#get-the-keys-for-your-resource
[regional_endpoints]: https://azure.microsoft.com/global-infrastructure/services/?products=cognitive-services
[how_to_migrate_resource_to_custom_subdomain]: https://learn.microsoft.com/azure/ai-services/cognitive-services-custom-subdomains#how-does-this-impact-existing-resources
[azure_sdk_python_azure_key_credential]: https://aka.ms/azsdk/python/core/azurekeycredential
[azure_sdk_python_identity]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity
[custom_subdomain]: https://docs.microsoft.com/azure/cognitive-services/authentication#create-a-resource-with-a-custom-subdomain
[azure_sdk_python_default_azure_credential]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity#defaultazurecredential
[register_aad_app]: https://docs.microsoft.com/azure/cognitive-services/authentication#assign-a-role-to-a-service-principal

[face_verification]: https://learn.microsoft.com/azure/ai-services/computer-vision/overview-identity#verification

[evaluate_different_detection_models]: https://learn.microsoft.com/azure/ai-services/computer-vision/how-to/specify-detection-model#evaluate-different-models
[recommended_recognition_model]: https://learn.microsoft.com/azure/ai-services/computer-vision/how-to/specify-recognition-model#recommended-model
[liveness_tutorial]: https://learn.microsoft.com/azure/ai-services/computer-vision/tutorials/liveness

[python_azure_core_exceptions]: https://aka.ms/azsdk/python/core/docs#module-azure.core.exceptions
[face_errors]: https://aka.ms/face-error-codes-and-messages
[python_logging]: https://docs.python.org/3/library/logging.html
[sdk_logging_docs]: https://docs.microsoft.com/azure/developer/python/sdk/azure-sdk-logging
[azure_core_ref_docs]: https://aka.ms/azsdk/python/core/docs

[code_of_conduct]: https://opensource.microsoft.com/codeofconduct/
[authenticate_with_token]: https://docs.microsoft.com/azure/cognitive-services/authentication?tabs=powershell#authenticate-with-an-authentication-token
[azure_identity_credentials]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity#credentials
[azure_identity_pip]: https://pypi.org/project/azure-identity/
[default_azure_credential]: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity#defaultazurecredential
[pip]: https://pypi.org/project/pip/
