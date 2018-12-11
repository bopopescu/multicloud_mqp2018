from libcloud.compute.drivers.ec2 import BaseEC2NodeDriver
from datetime import datetime, timedelta
from .gather_prices import gather_prices, read_prices_from_file, gather_images
from .config import GCP_PRICE_FILE, AWS_PRICE_FILE

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
        gather_images()
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


def find_instance_workload(workload):
    current_time = datetime.now()
    gcp_sizes = []
    aws_sizes = []

    if current_time > (get_timestamp() + margin):
        gather_prices()
        gather_images()
        aws_sizes = read_prices_from_file(AWS_PRICE_FILE)
        gcp_sizes = read_prices_from_file(GCP_PRICE_FILE)
        write_timestamp(current_time)
    else:
        aws_sizes = read_prices_from_file(AWS_PRICE_FILE)
        gcp_sizes = read_prices_from_file(GCP_PRICE_FILE)

    for s in aws_sizes:
        # check s to see if it is of the workload we need
        if workload == "ml":
            if "Deep Learning" in s.name:
                print("Here")
                valid_instances.append(s)
        elif workload == "im":
            if ("r4."or "r5."or "r5a."or "r5d."or "x1."or "x1e."or "z1d") in s.id:
                valid_instances.append(s)
        elif workload == "gp":
            # general purpose = all AMIs are technically ok to use
            # append them all, algo will find cheapest one
            valid_instances.append(s)

    for gcp in gcp_sizes:
        # check gcp to see if it is of the workload we need
        if workload == "ml":
            print("machine learning")

    instance = find_lowest_price(valid_instances)
    top_three = find_three_choices(valid_instances)
    print("------")
    print(top_three)
    print("------")

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
