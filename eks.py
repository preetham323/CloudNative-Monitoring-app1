from kubernetes import client, config

config.load_kube_config()

api_client = client.Apiclient()

#Define Deployment
deployment = client.V1Deployment(
    metadata = client.V1ObjectMeta(name="my-flask-app"),
    spec = client.V1DeploymentSoec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "my-flask-app"}
        ),
        template = client.V1PodTemplateSpec(
            metadata = client.V1ObjectMeta(
                labels = {"app":"my-flask-app"}
            ),
            spec = client.V1PodSpec(
                containers = [
                    client.V1Container(
                        name = "my-flask-app",
                        image = "346141603601.dkr.ecr.us-east-1.amazonaws.com/kalangi-cloud-native-repo:latest",
                        ports = client.V1ContainerPort(container_port=5000)
                    )
                ]
            )
        )
    )
)

#create Deployment
api_instance = client.AppsV1Api(api_client)
api_instance.create_namespaced_deployment(
    namespace = "default"
    body = deployment
)

# Define service
service = client.V1Service(
    metadata = client.V1ObjectMetadata(name="my-flask-service")
    spec = client.V1ServiceSpec(
        selector = {"app": "my-flask-app"}
        ports = [client.V1ServicePort(port=5000)]
    )
)

#create the service
api_instance = client.coreV1Api(api_client)
api_instance.create_namespaced_service(
    namespace = "default"
    body = service
)