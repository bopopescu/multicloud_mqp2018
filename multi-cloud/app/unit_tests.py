from price import find_instance
from datetime import datetime
from .deployment import *

# Set flag to 1 for optimized way
# Set flag to 2 for the unoptimized way
test_flag = 1

# ------------------------------------------------------------------------------------
#                                     FIND_INSTANCE
# ------------------------------------------------------------------------------------

# TEST 1
start = datetime.now() * 1000
find_instance(800, 0)
end = datetime.now() * 1000
final = end - start
print(final)

# TEST 2
start = datetime.now().millisecond
find_instance(800, 0)
end = datetime.now().millisecond
final = end - start

# TEST 3
start = datetime.now().millisecond
find_instance(800, 0)
end = datetime.now().millisecond
final = end - start

# TEST 4
start = datetime.now().millisecond
find_instance(800, 0)
end = datetime.now().millisecond
final = end - start

# ------------------------------------------------------------------------------------
#                                  FIND_INSTANCE_WORKLOAD
# ------------------------------------------------------------------------------------


# TEST 1
start = datetime.now().millisecond
find_instance_workload('ml')
end = datetime.now().millisecond
final = end - start

# TEST 2
start = datetime.now().millisecond
find_instance_workload('gp')
end = datetime.now().millisecond
final = end - start

# TEST 3
start = datetime.now().millisecond
find_instance_workload('im')
end = datetime.now().millisecond
final = end - start

# TEST 4
start = datetime.now().millisecond
find_instance_workload('ml')
end = datetime.now().millisecond
final = end - start

# ------------------------------------------------------------------------------------
#                                     FULL DEPLOYMENT TEST
# ------------------------------------------------------------------------------------

# TEST 1
start = datetime.now().millisecond
instance_options = find_instance(800, 0)
node = instance_options[0]
deployment(node, 'linux', 'test1')
end = datetime.now().millisecond
final = end - start

# TEST 2
start = datetime.now().millisecond
instance_options = find_instance(800, 0)
node = instance_options[0]
deployment(node, 'linux', 'test1')
end = datetime.now().millisecond
final = end - start


# ------------------------------------------------------------------------------------
#                                     AWS DEPLOYMENT TESTS
# ------------------------------------------------------------------------------------

# PUT HERE


# ------------------------------------------------------------------------------------





# ------------------------------------------------------------------------------------
#                                     GCP DEPLOYMENT TEST
# ------------------------------------------------------------------------------------


#PUT HERE




# ------------------------------------------------------------------------------------






