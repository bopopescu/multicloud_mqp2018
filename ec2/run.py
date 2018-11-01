from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

AWS_EC2_ACCESS_ID = "AKIAIOQPA3IHXFUOFF7A"
AWS_EC2_SECRET_KEY = "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"

cls = get_driver(Provider.EC2)
driver = cls(AWS_EC2_ACCESS_ID, AWS_EC2_SECRET_KEY)

#returns a list of all the OS images that are available for our current driver
images = driver.list_images()
"""
for image in images:
    print(image)
"""

ACCESS_KEY_NAME = "test"

SECURITY_GROUP_NAMES = []
SECURITY_GROUP_NAMES.append("ssh_access")

MY_SIZE = 'm1.small'
#from list of images
MY_IMAGE = "ami-fe338696"

sizes = driver.list_sizes()
images = driver.list_images()

size = [s for s in sizes if s.id == MY_SIZE][0]
image = [i for i in images if i.id == MY_IMAGE][0]

node = driver.create_node(name="My Instance", image=image, size=size)

print(node)
