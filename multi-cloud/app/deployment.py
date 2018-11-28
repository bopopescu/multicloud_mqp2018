from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from app.gather_prices import read_prices_from_file

# AWS Authentication Keys
EC2_ACCESS_ID = ''
EC2_SECRET_KEY = ''
AWS_PRICE_FILE = "app/aws_sizes.txt"
AWS_IMAGES_FILE = "app/aws_images.txt"


# Google Cloud Platform Authentication Keys
GCP_EMAIL = ''
GCP_PROJECT_ID = ''
GCP_CLIENT_ID = ''
GCP_SECRET_KEY = ''
GCP_PRICE_FILE = "app/gcp_sizes.txt"
GCP_IMAGES_FILE = "app/gcp_images.txt"


def deployment(NodeSize, os):
    # create driver

    if NodeSize.driver == get_driver(Provider.GCE):
        ComputeEngine = get_driver(Provider.GCE)
        gcp_driver = ComputeEngine(GCP_CLIENT_ID, GCP_SECRET_KEY, project=GCP_PROJECT_ID, datacenter="us-east1", auth_type="IA")
        images = read_prices_from_file(GCP_IMAGES_FILE)
        image = images[os]
        node = gcp_driver.create_node(name="testGCP", size=NodeSize, image=image)

    else:
        cls = get_driver(Provider.EC2)
        driver = cls(EC2_ACCESS_ID, EC2_SECRET_KEY, region="us-east-1")
        images = read_prices_from_file(AWS_IMAGES_FILE)
        image = images[os]
        node = driver.create_node(name="testAWS", image=image, size=NodeSize)




