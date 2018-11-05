from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

# AWS Authentication Keys
EC2_ACCESS_ID = 'your aws key'
EC2_SECRET_KEY = 'your aws secret key'

# AWS Amazon Machine Images
# Access using aws_images["linux"]
aws_images = {
    "linux":"ami-061e7ebbc234015fe",
    "win":"ami-017bf00eb0d4c7182",
    "rhel":"ami-28e07e50",
    "unix":"ami-0bbe6b35405ecebdb"
}


# Google Cloud Platform Authentication Keys
GCP_PROJECT_ID = 'your project id'
GCP_CLIENT_ID = 'your client id'
GCP_SECRET_KEY = 'your secret key'


# GCP OS Images
gcp_images = {
    "linux":" sles-12-sp2-sap-v20180816	",
    "win":" sql-2012-standard-windows-2012-r2-dc-v20181009",
    "rhel":"rhel-7-v20181011",
    "unix":"ubuntu-1404-trusty-v20181022"
}


# AWS Connection
cls = get_driver(Provider.EC2)
aws_driver = cls(EC2_ACCESS_ID, EC2_SECRET_KEY)
sizes = aws_driver.list_sizes()

valid_instances = []

# Google Cloud Connection
ComputeEngine = get_driver(Provider.GCE)
gcp_driver = ComputeEngine(GCP_CLIENT_ID, GCP_SECRET_KEY,
                       project=GCP_PROJECT_ID)
gcp_sizes = gcp_driver.list_sizes()


# Example Output for pricing
# >>> sizes[:2]
# [<NodeSize: id=t1.micro, name=Micro Instance, ram=613 disk=15 bandwidth=None
#   price=0.02 driver=Amazon EC2 ...>,
# <NodeSize: id=m1.small, name=Small Instance, ram=1740 disk=160 bandwidth=None
#  price=0.065 driver=Amazon EC2 ...>,
# >>> sizes[0].price
# 0.02
# >>>


def find_instance(memory, storage):
    for s in sizes:
        if s.ram >= memory and (s.ram <= (memory + 1000)):
            if s.disk >= storage:
                valid_instances.append(s)

    for gcp in gcp_sizes:
        if gcp.ram >= memory and (gcp.ram <= (memory + 1000)):
            if gcp.disk >= storage:
                valid_instances.append(gcp)

    instance = find_lowest_price(valid_instances)

    if instance != None:
        print_instance_stats(instance)
        return instance



def find_lowest_price(valid_instances):
    min = 100
    instance = None
    for i in valid_instances:
        if i.price < min:
            min = i.price
            instance = i
    return instance


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


# find_instance(8000, 145)




