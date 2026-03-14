import boto3
import json
from botocore.exceptions import ClientError


class Secret:
    def __init__(self, region_name="us-east-2"):
        # "Ohio" en el pizarrón corresponde a la región us-east-2
        self.region_name = region_name
        self.client = boto3.client(
            service_name="secretsmanager",
            region_name=self.region_name,
        )

    def _get_sm_(self, secret_name):
        """Este es el 'Get' del pizarrón: Trae el secreto de la nube"""
        try:
            response = self.client.get_secret_value(SecretId=secret_name)
            # Convierte el texto que pusiste en AWS (Imagen 2) a un diccionario
            return json.loads(response["SecretString"])
        except ClientError as e:
            print(f"Error en el Get: {e}")
            return None

    def _set_sm_(self, secret_name, secret_dict):
        """Este es el 'Set' del pizarrón: Guarda o actualiza secretos"""
        try:
            return self.client.put_secret_value(
                SecretId=secret_name,
                SecretString=json.dumps(secret_dict),
            )
        except ClientError as e:
            print(f"Error en el Set: {e}")
            return None

    # Backwards compatible helper
    def get_secret(self, secret_name):
        return self._get_sm_(secret_name)
