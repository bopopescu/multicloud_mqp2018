from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver


"""
Function that will create an Amazon AWS EC2 instance.
Parameters: @id user's AWS Access ID
            @key user's AWS Secret Key
            @image source AMI specified by user, i.e. linux, redhat, etc.
            @size size of image specified by user
            @name name of the instance
"""


def initiate_aws(id, key, image, size, name):
    cls = get_driver(Provider.EC2_US_EAST_OHIO)
    Driver = cls(id, key)

    sizes = Driver.list_sizes()
    images = Driver.list_images()

    size = [s for s in sizes if s.id == size][0]
    image = [i for i in images if i.id == image][0]

    node = Driver.create_node(name=name, image=image, size=size)

    print(node)


"""
Function that will create an Amazon AWS EC2 instance.
Parameters: @id user's GCP Access ID
            @image source AMI specified by user, i.e. linux, redhat, etc.
            @size size of image specified by user
            @name name of the instance
            @sa_email service account email
            @path path to pem file AKA key file
            @datacenter
"""


def initiate_gcp(id, path, image, size, name, sa_email, datacenter):
    # create driver
    Driver = get_driver(Provider.GCE)
    gce = Driver(sa_email, path, datacenter=datacenter, project=id)

    # list sizes and images 
    sizes = gce.list_sizes()
    images = gce.list_images()

    size_obj = [s for s in sizes if s.id == size][0]
    image_obj = [i for i in images if i.name == image][0]

    node = gce.create_node(name=name, size=size_obj, image=image_obj)

    print(node)
