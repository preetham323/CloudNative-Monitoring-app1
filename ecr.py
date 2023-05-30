import boto3
ecr_client = boto3.client('ecr')

repository_name = "my-cloud-native-repo"
repository_uri = reponse['repository'] ['repositoryUri']
prin(repository_uri)