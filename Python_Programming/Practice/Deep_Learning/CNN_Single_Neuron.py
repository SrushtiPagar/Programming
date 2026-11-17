import tensorflow as tf

inputs = tf.constant([1.0,2.0,3.0])

weights = tf.constant([0.5,-0.2,0.8])

bias = tf.constant(0.1)

weights_sum = tf.reduce_sum(inputs * weights) + bias

print("Inputs : ",inputs.numpy)
print("Weights : ", weights.numpy)
print("bias : ",bias.numpy)

print("Weighted sum : ",weights_sum.numpy)

output = tf.sigmoid(weights_sum)

print("Output : ",output.numpy()) 