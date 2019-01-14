from datetime import datetime
from price import find_instance, find_instance_workload, find_lowest_price, find_three_choices
from deployment import deployment


# Command to run: "python -m app.unit_tests"
# Set flag to 1 for optimized way
# Set flag to 2 for the unoptimized way


# ** NOTE *** test_flag is in price.py due to import error


# ------------------------------------------------------------------------------------
#                                     FIND_INSTANCE
# ------------------------------------------------------------------------------------
# find_instance_results = []
#
# # TEST 1
# start = datetime.now().microsecond / 1000
# find_instance(800, 0)
# end = datetime.now().microsecond / 1000
# final = end - start
# find_instance_results.append(final)
# print("--------------------------")
# print("         FIND_INSTANCE    ")
# print("--------------------------")
# print(" -------- TEST 1 --------")
# print("Total time: " + str(final))
#
# # TEST 2
# start = datetime.now().microsecond / 1000
# find_instance(800, 0)
# end = datetime.now().microsecond / 1000
# final = end - start
# find_instance_results.append(final)
# print(" -------- TEST 2 --------")
# print("Total time: " + str(final))
#
# # TEST 3
# start = datetime.now().microsecond / 1000
# find_instance(800, 0)
# end = datetime.now().microsecond / 1000
# final = end - start
# find_instance_results.append(final)
# print(" -------- TEST 3 --------")
# print("Total time: " + str(final))
#
# # TEST 4
# start = datetime.now().microsecond / 1000
# find_instance(800, 0)
# end = datetime.now().microsecond / 1000
# final = end - start
# find_instance_results.append(final)
# print(" -------- TEST 4 --------")
# print("Total time: " + str(final))
#
# # ------------------------------------------------------------------------------------
# #                                  FIND_INSTANCE_WORKLOAD
# # ------------------------------------------------------------------------------------
# find_workload_results = []
#
# # TEST 1
# start = datetime.now().microsecond / 1000
# find_instance_workload('ml')
# end = datetime.now().microsecond / 1000
# final = end - start
# find_workload_results.append(final)
#
# print("--------------------------")
# print("         FIND_WORKLOAD    ")
# print("--------------------------")
#
# print(" -------- TEST 1 --------")
# print("Total time: " + str(final))
#
# # TEST 2
# start = datetime.now().microsecond / 1000
# find_instance_workload('gp')
# end = datetime.now().microsecond / 1000
# final = end - start
# find_workload_results.append(final)
#
# print(" -------- TEST 2 --------")
# print("Total time: " + str(final))
#
# # TEST 3
# start = datetime.now().microsecond / 1000
# find_instance_workload('im')
# end = datetime.now().microsecond / 1000
# final = end - start
# find_workload_results.append(final)
#
# print(" -------- TEST 3 --------")
# print("Total time: " + str(final))
#
# # TEST 4
# start = datetime.now().microsecond / 1000
# find_instance_workload('ml')
# end = datetime.now().microsecond / 1000
# final = end - start
# find_workload_results.append(final)
#
# print(" -------- TEST 4 --------")
# print("Total time: " + str(final))
#
# print("--------------------------")
# print("        FINAL RESULTS     ")
# print("--------------------------")
# print(find_instance_results)
# print(find_workload_results)


# ------------------------------------------------------------------------------------
#                                    FULL DEPLOYMENT TEST
# ------------------------------------------------------------------------------------

# # TEST 1
# start = datetime.now().microsecond / 1000
# instance_options = find_instance(800, 0)
# node = instance_options[0]
# deployment(node, 'linux', 'test1')
# end = datetime.now().microsecond / 1000
# final = end - start
# print(" -------- TEST 1 --------")
# print("Total time: " + str(final))

# TEST 2
start = datetime.now().microsecond / 1000
instance_options = find_instance(800, 0)
node = instance_options[1][2]
deployment(node, 'linux', 'test2')
end = datetime.now().microsecond / 1000
final = end - start
print(" -------- TEST 2 --------")
print("Total time: " + str(final))


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






