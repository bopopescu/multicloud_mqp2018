from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from datetime import timedelta
import pickle
from app.config import GCP_PROJECT_ID, GCP_SECRET_KEY, GCP_CLIENT_ID, GCP_IMAGES_FILE, GCP_PRICE_FILE, EC2_ACCESS_ID, EC2_SECRET_KEY, AWS_IMAGES_FILE, AWS_PRICE_FILE

# AWS Amazon Machine Images
# Access using aws_images["linux"]
aws_images = {
    "linux": "ami-09479453c5cde9639",
    "win": "ami-05f5c28bb6992ab4b",
    "rhel": "ami-011b3ccf1bd6db744",
    "unix": "ami-0ac019f4fcb7cb7e6"
}

# GCP OS Images
gcp_images = {
    "linux": "sles-12-sp2-sap-v20180816",
    "win": "sql-2014-standard-windows-2012-r2-dc-v20181113",
    "rhel": "rhel-6-v20181113",
    "unix": "ubuntu-1404-trusty-v20181114"
}

margin = timedelta(days = 10)


def gather_prices():

    # AWS Connection
    cls = get_driver(Provider.EC2)
    aws_driver = cls(EC2_ACCESS_ID, EC2_SECRET_KEY, region="us-east-1")
    aws_sizes = aws_driver.list_sizes()

    # Google Cloud Connection
    ComputeEngine = get_driver(Provider.GCE)
    gcp_driver = ComputeEngine(GCP_CLIENT_ID, GCP_SECRET_KEY, project=GCP_PROJECT_ID, datacenter="us-east1", auth_type="IA")
    gcp_sizes = gcp_driver.list_sizes()

    write_prices_to_file("aws_sizes.txt", aws_sizes)
    write_prices_to_file("gcp_sizes.txt", gcp_sizes)



def gather_images():
    # AWS Connection
    cls = get_driver(Provider.EC2)
    aws_driver = cls(EC2_ACCESS_ID, EC2_SECRET_KEY, region="us-east-1")
    aws_image_list = aws_driver.list_images()

    images = {
        "linux": None,
        "win": None,
        "rhel": None,
        "unix": None
    }

    for i in aws_image_list:
        if i.id == aws_images["linux"]:
            images["linux"] = i
        if i.id == aws_images["win"]:
            images["win"] = i
        if i.id == aws_images["rhel"]:
            images["rhel"] = i
        if i.id == aws_images["unix"]:
            images["unix"] = i

    # Google Cloud Connection
    ComputeEngine = get_driver(Provider.GCE)
    gcp_driver = ComputeEngine(GCP_CLIENT_ID, GCP_SECRET_KEY, project=GCP_PROJECT_ID, auth_type="IA")
    gcp_image_list = gcp_driver.list_images()

    images_gcp = {
        "linux": None,
        "win": None,
        "rhel": None,
        "unix": None
    }

    for i in gcp_image_list:
        if i.name == gcp_images["linux"]:
            images_gcp["linux"] = i
        if i.name == gcp_images["win"]:
            images_gcp["win"] = i
        if i.name == gcp_images["rhel"]:
            images_gcp["rhel"] = i
        if i.name == gcp_images["unix"]:
            images_gcp["unix"] = i

    write_prices_to_file("aws_images.txt", images)
    write_prices_to_file("gcp_images.txt", images_gcp)



def write_prices_to_file(filename, sizes):
    f = open(filename, 'w')
    pickle.dump(sizes, f)
    f.close()


def read_prices_from_file(filename):
    f = open(filename, 'r')
    sizes = pickle.load(f)
    f.close()
    return sizes

