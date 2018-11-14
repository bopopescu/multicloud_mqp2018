from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from datetime import timedelta
import pickle


# AWS Authentication Keys
EC2_ACCESS_ID = 'your key'
EC2_SECRET_KEY = 'your secret'

# Google Cloud Platform Authentication Keys
GCP_EMAIL = 'your email'
GCP_PROJECT_ID = 'your project'
GCP_CLIENT_ID = 'your client'
GCP_SECRET_KEY = 'your secret'

margin = timedelta(days = 10)


def gather_prices():

    # AWS Connection
    cls = get_driver(Provider.EC2)
    aws_driver = cls(EC2_ACCESS_ID, EC2_SECRET_KEY)
    aws_sizes = aws_driver.list_sizes()

    # Google Cloud Connection
    ComputeEngine = get_driver(Provider.GCE)
    gcp_driver = ComputeEngine(GCP_CLIENT_ID, GCP_SECRET_KEY,
                           project=GCP_PROJECT_ID)
    gcp_sizes = gcp_driver.list_sizes()

    write_prices_to_file("aws_sizes.txt", aws_sizes)
    write_prices_to_file("gcp_sizes.txt", gcp_sizes)


def write_prices_to_file(filename, sizes):
    f = open(filename, 'w')
    pickle.dump(sizes, f)
    f.close()

def read_prices_from_file(filename):
    f = open(filename, 'r')
    sizes = pickle.load(f)
    f.close()
    return sizes



