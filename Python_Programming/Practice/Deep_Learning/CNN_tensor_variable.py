import tensorflow as tf

weight = tf.Variable(5.0)

print("Initial weight value : ", weight.numpy())

weight.assign(10.0)
print("Updated weight value : ", weight.numpy())

weight.assign_add(2.5)
print("Updated weight value : ", weight.numpy())

weight.assign_sub(1.5)
print("Updated weight value : ", weight.numpy())

# Initial weight value :  5.0
# Updated weight value :  10.0
# Updated weight value :  12.5
# Updated weight value :  11.5
