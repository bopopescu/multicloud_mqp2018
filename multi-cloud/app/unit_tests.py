from datetime import datetime
from price import find_instance, find_instance_workload, print_all_valid_instances
from deployment import deployment, get_node, destroy, gce_destroy_all
from libcloud.pricing import invalidate_pricing_cache, set_pricing


# Command to run: "python -m app.unit_tests"
# Set flag to 1 for optimized way
# Set flag to 2 for the unoptimized way


# ** NOTE *** test_flag is in price.py due to import error

# ------------------------------------------------------------------------------------
#                                     FIND_INSTANCE
# ------------------------------------------------------------------------------------
find_instance_results = []

# TEST 1
start = datetime.now()
instance, top_three, valid_instances = find_instance(800, 0)
end = datetime.now()
delta = end - start
final = int(delta.total_seconds() * 1000)
find_instance_results.append(final)
print("--------------------------")
print("         FIND_INSTANCE    ")
print("--------------------------")
print(" -------- TEST 1 --------")
print("Total time: " + str(final))
print_all_valid_instances(top_three)

# # TEST 2
# start = datetime.now()
# instance, top_three, valid_instances = find_instance(16000, 0)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# find_instance_results.append(final)
# print(" -------- TEST 2 --------")
# print("Total time: " + str(final))
# print_all_valid_instances(top_three)

#
# # TEST 3
# start = datetime.now()
# instance, top_three, valid_instances = find_instance(800, 0)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# find_instance_results.append(final)
# print(" -------- TEST 3 --------")
# print("Total time: " + str(final))
# print_all_valid_instances(top_three)
#
#
# # TEST 4
# start = datetime.now()
# instance, top_three, valid_instances = find_instance(800, 0)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# find_instance_results.append(final)
# print(" -------- TEST 4 --------")
# print("Total time: " + str(final))
# print_all_valid_instances(top_three)
#
#
# # TEST 5
# start = datetime.now()
# instance, top_three, valid_instances = find_instance(800, 0)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# find_instance_results.append(final)
# print(" -------- TEST 5 --------")
# print("Total time: " + str(final))
# print_all_valid_instances(top_three)
#
#
# # TEST 6
# start = datetime.now()
# instance, top_three, valid_instances = find_instance(800, 0)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# find_instance_results.append(final)
# print(" -------- TEST 6 --------")
# print("Total time: " + str(final))
# print_all_valid_instances(top_three)
#
#
# # TEST 7
# start = datetime.now()
# instance, top_three, valid_instances = find_instance(800, 0)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# find_instance_results.append(final)
# print(" -------- TEST 7 --------")
# print("Total time: " + str(final))
# print_all_valid_instances(top_three)
#
#
# # TEST 8
# start = datetime.now()
# instance, top_three, valid_instances = find_instance(800, 0)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# find_instance_results.append(final)
# print(" -------- TEST 8 --------")
# print("Total time: " + str(final))
# print_all_valid_instances(top_three)
#
#
# # TEST 9
# start = datetime.now()
# instance, top_three, valid_instances = find_instance(800, 0)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# find_instance_results.append(final)
# print(" -------- TEST 9 --------")
# print("Total time: " + str(final))
# print_all_valid_instances(top_three)
#
#
# # TEST 10
# start = datetime.now()
# instance, top_three, valid_instances = find_instance(800, 0)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# find_instance_results.append(final)
# print(" -------- TEST 10 --------")
# print("Total time: " + str(final))
# print_all_valid_instances(top_three)


# # ------------------------------------------------------------------------------------
# #                                  FIND_INSTANCE_WORKLOAD
# # ------------------------------------------------------------------------------------
# find_workload_results = []
#
# # TEST 1
# start = datetime.now()
# instance, top_three, valid_instances = find_instance_workload('ml')
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# find_workload_results.append(final)
# print("--------------------------")
# print("         FIND_WORKLOAD    ")
# print("--------------------------")
#
# print(" -------- TEST 1 --------")
# print("Total time: " + str(final))
# print_all_valid_instances(top_three)
#
#
# # TEST 2
# start = datetime.now()
# instance, top_three, valid_instances = find_instance_workload('ml')
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# find_workload_results.append(final)
# print(" -------- TEST 2 --------")
# print("Total time: " + str(final))
# print_all_valid_instances(top_three)
#
#
# # TEST 3
# start = datetime.now()
# instance, top_three, valid_instances = find_instance_workload('ml')
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# find_workload_results.append(final)
# print(" -------- TEST 3 --------")
# print("Total time: " + str(final))
# print_all_valid_instances(top_three)
#
#
# # TEST 4
# start = datetime.now()
# instance, top_three, valid_instances = find_instance_workload('ml')
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# find_workload_results.append(final)
# print(" -------- TEST 4 --------")
# print("Total time: " + str(final))
# print_all_valid_instances(top_three)
#
#
# # TEST 5
# start = datetime.now()
# instance, top_three, valid_instances = find_instance_workload('ml')
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# find_workload_results.append(final)
# print(" -------- TEST 5 --------")
# print("Total time: " + str(final))
# print_all_valid_instances(top_three)
#
#
# # TEST 6
# start = datetime.now()
# instance, top_three, valid_instances = find_instance_workload('ml')
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# find_workload_results.append(final)
# print(" -------- TEST 6 --------")
# print("Total time: " + str(final))
# print_all_valid_instances(top_three)
#
#
# # TEST 7
# start = datetime.now()
# instance, top_three, valid_instances = find_instance_workload('ml')
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# find_workload_results.append(final)
# print(" -------- TEST 7 --------")
# print("Total time: " + str(final))
# print_all_valid_instances(top_three)
#
# # TEST 8
# start = datetime.now()
# instance, top_three, valid_instances = find_instance_workload('ml')
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# find_workload_results.append(final)
# print(" -------- TEST 8 --------")
# print("Total time: " + str(final))
# print_all_valid_instances(top_three)
#
#
# # TEST 9
# start = datetime.now()
# instance, top_three, valid_instances = find_instance_workload('ml')
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# find_workload_results.append(final)
# print(" -------- TEST 9 --------")
# print("Total time: " + str(final))
# print_all_valid_instances(top_three)
#
#
# # TEST 10
# start = datetime.now()
# instance, top_three, valid_instances = find_instance_workload('ml')
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# find_workload_results.append(final)
# print(" -------- TEST 10 --------")
# print("Total time: " + str(final))
# print_all_valid_instances(top_three)
#
#
# print("--------------------------")
# print("        FINAL RESULTS     ")
# print("--------------------------")
# print(find_instance_results)
# print(find_workload_results)


# ------------------------------------------------------------------------------------
#                                    FULL DEPLOYMENT TEST
# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
#                                     AWS DEPLOYMENT TESTS
# ------------------------------------------------------------------------------------
# print("--------------------------")
# print("      AWS Deployments     ")
# print("--------------------------")
#
# full_aws_ids = []
#
# # TEST 1
# start = datetime.now()
# instance_options = find_instance(800, 0)
# node = instance_options[0]
# deployed_node = deployment(node, 'rhel', 'test1')
# full_aws_ids.append(deployed_node)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# user_node = get_node("Amazon", deployed_node.id)
# while user_node[0].state == 'pending':
#     user_node = get_node("Amazon", deployed_node.id)
# final2 = datetime.now()
# delta2 = final2 - end
# ready_time = int(delta2.total_seconds() * 1000)
# print(" -------- TEST 1 --------")
# print("Total time for deployment: " + str(final))
# print("Total time until ready: " + str(ready_time))
#
#
# # TEST 2
# start = datetime.now()
# instance_options = find_instance(800, 0)
# node = instance_options[0]
# deployed_node = deployment(node, 'rhel', 'test2')
# full_aws_ids.append(deployed_node)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# user_node = get_node("Amazon", deployed_node.id)
# while user_node[0].state == 'pending':
#     user_node = get_node("Amazon", deployed_node.id)
# final2 = datetime.now()
# delta2 = final2 - end
# ready_time = int(delta2.total_seconds() * 1000)
# print(" -------- TEST 2 --------")
# print("Total time for deployment: " + str(final))
# print("Total time until ready: " + str(ready_time))
#
# # TEST 3
# start = datetime.now()
# instance_options = find_instance(800, 0)
# node = instance_options[0]
# deployed_node = deployment(node, 'rhel', 'test3')
# full_aws_ids.append(deployed_node)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# user_node = get_node("Amazon", deployed_node.id)
# while user_node[0].state == 'pending':
#     user_node = get_node("Amazon", deployed_node.id)
# final2 = datetime.now()
# delta2 = final2 - end
# ready_time = int(delta2.total_seconds() * 1000)
# print(" -------- TEST 3 --------")
# print("Total time for deployment: " + str(final))
# print("Total time until ready: " + str(ready_time))
#
# # TEST 4
# start = datetime.now()
# instance_options = find_instance(800, 0)
# node = instance_options[0]
# deployed_node = deployment(node, 'rhel', 'test4')
# full_aws_ids.append(deployed_node)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# user_node = get_node("Amazon", deployed_node.id)
# while user_node[0].state == 'pending':
#     user_node = get_node("Amazon", deployed_node.id)
# final2 = datetime.now()
# delta2 = final2 - end
# ready_time = int(delta2.total_seconds() * 1000)
# print(" -------- TEST 4 --------")
# print("Total time for deployment: " + str(final))
# print("Total time until ready: " + str(ready_time))
#
# # TEST 5
# start = datetime.now()
# instance_options = find_instance(800, 0)
# node = instance_options[0]
# deployed_node = deployment(node, 'rhel', 'test5')
# full_aws_ids.append(deployed_node)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# user_node = get_node("Amazon", deployed_node.id)
# while user_node[0].state == 'pending':
#     user_node = get_node("Amazon", deployed_node.id)
# final2 = datetime.now()
# delta2 = final2 - end
# ready_time = int(delta2.total_seconds() * 1000)
# print(" -------- TEST 5 --------")
# print("Total time for deployment: " + str(final))
# print("Total time until ready: " + str(ready_time))
#
# # TEST 6
# start = datetime.now()
# instance_options = find_instance(800, 0)
# node = instance_options[0]
# deployed_node = deployment(node, 'rhel', 'test6')
# full_aws_ids.append(deployed_node)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# user_node = get_node("Amazon", deployed_node.id)
# while user_node[0].state == 'pending':
#     user_node = get_node("Amazon", deployed_node.id)
# final2 = datetime.now()
# delta2 = final2 - end
# ready_time = int(delta2.total_seconds() * 1000)
# print(" -------- TEST 6 --------")
# print("Total time for deployment: " + str(final))
# print("Total time until ready: " + str(ready_time))
#
# # TEST 7
# start = datetime.now()
# instance_options = find_instance(800, 0)
# node = instance_options[0]
# deployed_node = deployment(node, 'rhel', 'test7')
# full_aws_ids.append(deployed_node)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# user_node = get_node("Amazon", deployed_node.id)
# while user_node[0].state == 'pending':
#     user_node = get_node("Amazon", deployed_node.id)
# final2 = datetime.now()
# delta2 = final2 - end
# ready_time = int(delta2.total_seconds() * 1000)
# print(" -------- TEST 7 --------")
# print("Total time for deployment: " + str(final))
# print("Total time until ready: " + str(ready_time))
#
# # TEST 8
# start = datetime.now()
# instance_options = find_instance(800, 0)
# node = instance_options[0]
# deployed_node = deployment(node, 'rhel', 'test8')
# full_aws_ids.append(deployed_node)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# user_node = get_node("Amazon", deployed_node.id)
# while user_node[0].state == 'pending':
#     user_node = get_node("Amazon", deployed_node.id)
# final2 = datetime.now()
# delta2 = final2 - end
# ready_time = int(delta2.total_seconds() * 1000)
# print(" -------- TEST 8 --------")
# print("Total time for deployment: " + str(final))
# print("Total time until ready: " + str(ready_time))
#
# # TEST 9
# start = datetime.now()
# instance_options = find_instance(800, 0)
# node = instance_options[0]
# deployed_node = deployment(node, 'rhel', 'test9')
# full_aws_ids.append(deployed_node)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# user_node = get_node("Amazon", deployed_node.id)
# while user_node[0].state == 'pending':
#     user_node = get_node("Amazon", deployed_node.id)
# final2 = datetime.now()
# delta2 = final2 - end
# ready_time = int(delta2.total_seconds() * 1000)
# print(" -------- TEST 9 --------")
# print("Total time for deployment: " + str(final))
# print("Total time until ready: " + str(ready_time))
#
# # TEST 10
# start = datetime.now()
# instance_options = find_instance(800, 0)
# node = instance_options[0]
# deployed_node = deployment(node, 'rhel', 'test10')
# full_aws_ids.append(deployed_node)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# user_node = get_node("Amazon", deployed_node.id)
# while user_node[0].state == 'pending':
#     user_node = get_node("Amazon", deployed_node.id)
# final2 = datetime.now()
# delta2 = final2 - end
# ready_time = int(delta2.total_seconds() * 1000)
# print(" -------- TEST 10 --------")
# print("Total time for deployment: " + str(final))
# print("Total time until ready: " + str(ready_time))
#
#
# for i in full_aws_ids:
#     destroy("Amazon", i)

# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
#                                     GCP DEPLOYMENT TEST
# ------------------------------------------------------------------------------------
# print("--------------------------")
# print("      GCE Deployments     ")
# print("--------------------------")
#
# full_node_list = []
#
# # TEST 1
# start = datetime.now()
# instance_options = find_instance(800, 0)
# node = instance_options[1][2]
# deployed_node = deployment(node, 'linux', 'test1')
# full_node_list.append(deployed_node)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# flag = 1
# user_node = get_node("Google", deployed_node.name)
# while user_node.state == 'pending':
#     user_node = get_node("Google", deployed_node.name)
#     flag = 2
# if flag == 1:
#     ready_time = final
# else:
#     final2 = datetime.now().second
#     ready_time = final2 - final
# print(" -------- TEST 1 --------")
# print("Total time: " + str(final))
# print("Time until ready: " + str(ready_time))
#
# # TEST 2
# start = datetime.now()
# instance_options = find_instance(800, 0)
# node = instance_options[1][2]
# deployed_node = deployment(node, 'linux', 'test2')
# full_node_list.append(deployed_node)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# flag = 1
# user_node = get_node("Google", deployed_node.name)
# while user_node.state == 'pending':
#     user_node = get_node("Google", deployed_node.name)
#     flag = 2
# if flag == 1:
#     ready_time = final
# else:
#     final2 = datetime.now().second
#     ready_time = final2 - final
# print(" -------- TEST 2 --------")
# print("Total time: " + str(final))
# print("Time until ready: " + str(ready_time))
#
# # TEST 3
# start = datetime.now()
# instance_options = find_instance(800, 0)
# node = instance_options[1][2]
# deployed_node = deployment(node, 'linux', 'test3')
# full_node_list.append(deployed_node)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# flag = 1
# user_node = get_node("Google", deployed_node.name)
# while user_node.state == 'pending':
#     user_node = get_node("Google", deployed_node.name)
#     flag = 2
# if flag == 1:
#     ready_time = final
# else:
#     final2 = datetime.now().second
#     ready_time = final2 - final
# print(" -------- TEST 3 --------")
# print("Total time: " + str(final))
# print("Time until ready: " + str(ready_time))
#
# # TEST 4
# start = datetime.now()
# instance_options = find_instance(800, 0)
# node = instance_options[1][2]
# deployed_node = deployment(node, 'linux', 'test4')
# full_node_list.append(deployed_node)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# flag = 1
# user_node = get_node("Google", deployed_node.name)
# while user_node.state == 'pending':
#     user_node = get_node("Google", deployed_node.name)
#     flag = 2
# if flag == 1:
#     ready_time = final
# else:
#     final2 = datetime.now().second
#     ready_time = final2 - final
# print(" -------- TEST 4 --------")
# print("Total time: " + str(final))
# print("Time until ready: " + str(ready_time))
#
# # TEST 5
# start = datetime.now()
# instance_options = find_instance(800, 0)
# node = instance_options[1][2]
# deployed_node = deployment(node, 'linux', 'test5')
# full_node_list.append(deployed_node)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# flag = 1
# user_node = get_node("Google", deployed_node.name)
# while user_node.state == 'pending':
#     user_node = get_node("Google", deployed_node.name)
#     flag = 2
# if flag == 1:
#     ready_time = final
# else:
#     final2 = datetime.now().second
#     ready_time = final2 - final
# print(" -------- TEST 5 --------")
# print("Total time: " + str(final))
# print("Time until ready: " + str(ready_time))
#
# # TEST 6
# start = datetime.now()
# instance_options = find_instance(800, 0)
# node = instance_options[1][2]
# deployed_node = deployment(node, 'linux', 'test6')
# full_node_list.append(deployed_node)
#
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# flag = 1
# user_node = get_node("Google", deployed_node.name)
# while user_node.state == 'pending':
#     user_node = get_node("Google", deployed_node.name)
#     flag = 2
# if flag == 1:
#     ready_time = final
# else:
#     final2 = datetime.now().second
#     ready_time = final2 - final
# print(" -------- TEST 6 --------")
# print("Total time: " + str(final))
# print("Time until ready: " + str(ready_time))
#
# # TEST 7
# start = datetime.now()
# instance_options = find_instance(800, 0)
# node = instance_options[1][2]
# deployed_node = deployment(node, 'linux', 'test7')
# full_node_list.append(deployed_node)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# flag = 1
# user_node = get_node("Google", deployed_node.name)
# while user_node.state == 'pending':
#     user_node = get_node("Google", deployed_node.name)
#     flag = 2
# if flag == 1:
#     ready_time = final
# else:
#     final2 = datetime.now().second
#     ready_time = final2 - final
# print(" -------- TEST 7 --------")
# print("Total time: " + str(final))
# print("Time until ready: " + str(ready_time))
#
# # TEST 8
# start = datetime.now()
# instance_options = find_instance(800, 0)
# node = instance_options[1][2]
# deployed_node = deployment(node, 'linux', 'test8')
# full_node_list.append(deployed_node)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# flag = 1
# user_node = get_node("Google", deployed_node.name)
# while user_node.state == 'pending':
#     user_node = get_node("Google", deployed_node.name)
#     flag = 2
# if flag == 1:
#     ready_time = final
# else:
#     final2 = datetime.now().second
#     ready_time = final2 - final
# print(" -------- TEST 8 --------")
# print("Total time: " + str(final))
# print("Time until ready: " + str(ready_time))
#
# # TEST 9
# start = datetime.now()
# instance_options = find_instance(800, 0)
# node = instance_options[1][2]
# deployed_node = deployment(node, 'linux', 'test9')
# full_node_list.append(deployed_node)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# flag = 1
# user_node = get_node("Google", deployed_node.name)
# while user_node.state == 'pending':
#     user_node = get_node("Google", deployed_node.name)
#     flag = 2
# if flag == 1:
#     ready_time = final
# else:
#     final2 = datetime.now().second
#     ready_time = final2 - final
# print(" -------- TEST 9 --------")
# print("Total time: " + str(final))
# print("Time until ready: " + str(ready_time))
#
# # TEST 10
# start = datetime.now()
# instance_options = find_instance(800, 0)
# node = instance_options[1][2]
# deployed_node = deployment(node, 'linux', 'test10')
# full_node_list.append(deployed_node)
# end = datetime.now()
# delta = end - start
# final = int(delta.total_seconds() * 1000)
# flag = 1
# user_node = get_node("Google", deployed_node.name)
# while user_node.state == 'pending':
#     user_node = get_node("Google", deployed_node.name)
#     flag = 2
# if flag == 1:
#     ready_time = final
# else:
#     final2 = datetime.now().second
#     ready_time = final2 - final
# print(" -------- TEST 10 --------")
# print("Total time: " + str(final))
# print("Time until ready: " + str(ready_time))
#
# gce_destroy_all(full_node_list)
# ------------------------------------------------------------------------------------






