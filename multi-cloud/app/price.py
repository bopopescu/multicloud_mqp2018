from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from libcloud.compute.drivers.ec2 import BaseEC2NodeDriver
from datetime import datetime, timedelta
from .gather_prices import gather_prices, gather_prices, read_prices_from_file

# AWS Authentication Keys
EC2_ACCESS_ID = ''
EC2_SECRET_KEY = ''
AWS_PRICE_FILE = ""

# AWS Amazon Machine Images
# Access using aws_images["linux"]
aws_images = {
    "linux": "ami-061e7ebbc234015fe",
    "win": "ami-017bf00eb0d4c7182",
    "rhel": "ami-28e07e50",
    "unix": "ami-0bbe6b35405ecebdb"
}

# Google Cloud Platform Authentication Keys
GCP_EMAIL = ''
GCP_PROJECT_ID = ''
GCP_CLIENT_ID = ''
GCP_SECRET_KEY = ''
GCP_PRICE_FILE = ""

# GCP OS Images
gcp_images = {
    "linux": " sles-12-sp2-sap-v20180816	",
    "win": " sql-2012-standard-windows-2012-r2-dc-v20181009",
    "rhel": "rhel-7-v20181011",
    "unix": "ubuntu-1404-trusty-v20181022"
}

TIMESTAMP_FILE = "app/timestamp.txt"

margin = timedelta(days = 10)


# Example Output for pricing
# >>> sizes[:2]
# [<NodeSize: id=t1.micro, name=Micro Instance, ram=613 disk=15 bandwidth=None
#   price=0.02 driver=Amazon EC2 ...>,
# <NodeSize: id=m1.small, name=Small Instance, ram=1740 disk=160 bandwidth=None
#  price=0.065 driver=Amazon EC2 ...>,
# >>> sizes[0].price
# 0.02
# >>>

# AWS Connection
# cls = get_driver(Provider.EC2)
# aws_driver = cls(EC2_ACCESS_ID, EC2_SECRET_KEY)
#
#
# # Google Cloud Connection
# ComputeEngine = get_driver(Provider.GCE)
# gcp_driver = ComputeEngine(GCP_CLIENT_ID, GCP_SECRET_KEY,
#

valid_instances = []


def find_instance(memory, storage):
    current_time = datetime.now()
    gcp_sizes = []
    aws_sizes = []

    if current_time > (get_timestamp() + margin):
        gather_prices()
        aws_sizes = read_prices_from_file(AWS_PRICE_FILE)
        gcp_sizes = read_prices_from_file(GCP_PRICE_FILE)
        write_timestamp(current_time)
    else:
        aws_sizes = read_prices_from_file(AWS_PRICE_FILE)
        gcp_sizes = read_prices_from_file(GCP_PRICE_FILE)

    for s in aws_sizes:
        if s.ram >= memory and (s.ram <= (memory + 1000)):
            if s.disk >= storage:
                if s not in valid_instances:
                    valid_instances.append(s)

    for gcp in gcp_sizes:
        if gcp.ram >= memory and (gcp.ram <= (memory + 1000)):
            if gcp.disk >= storage:
                if gcp not in valid_instances:
                    valid_instances.append(gcp)

    instance = find_lowest_price(valid_instances)
    top_three = find_three_choices(valid_instances)

    if instance != None:
        print_instance_stats(instance)
        return instance, top_three, valid_instances
    else:
        return None, None, None


def find_lowest_price(valid_instances):
    min = 100
    instance = None
    for i in valid_instances:
        if i.price < min:
            min = i.price
            instance = i
    return instance


def find_three_choices(valid_instances):
    all_instances = valid_instances
    top_three = []
    print_all_valid_instances(valid_instances)

    while len(top_three) != 3 and len(all_instances) != 0:
        instance = find_lowest_price(all_instances)
        flag = 0
        if instance != None:
            if instance not in top_three:
                for i in top_three:
                    if i.id == instance.id:
                        flag = 2
                if flag == 0:
                    top_three.append(instance)
        all_instances.remove(instance)

    return top_three



def print_instance_stats(instance):
    print("Instance ID: " + str(instance.id))
    print("Instance Name: " + str(instance.name))
    print("Instance RAM: " + str(instance.ram))
    print("Instance Disk: " + str(instance.disk))
    print("Instance bandwidth: " + str(instance.bandwidth))
    print("Instance price: " + str(instance.price))


def print_all_valid_instances(valid_instances):
    for i in valid_instances:
        print("")
        print_instance_stats(i)


def write_timestamp(timestamp):
    f = open(TIMESTAMP_FILE, "w")
    f.write(str(timestamp))
    f.close()


def get_timestamp():
    f = open(TIMESTAMP_FILE, "r")
    input = f.read()
    timestamp = datetime.strptime(input, "%Y-%m-%d %H:%M:%S.%f")
    return timestamp


def detect_type(instance):
    if isinstance(instance.driver,BaseEC2NodeDriver):
        return "Amazon"
    else:
        return "Google"

