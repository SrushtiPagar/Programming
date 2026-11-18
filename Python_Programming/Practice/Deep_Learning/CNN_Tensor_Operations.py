import tensorflow as tf

tensor1 = tf.constant([10,20,30])
tensor2 = tf.constant([1,2,3])

addition = tf.add(tensor1, tensor2)
print("Addition is : ",addition)


subtraction = tf.subtract(tensor1, tensor2)
print("Subtraction is : ",subtraction)


multiplication = tf.multiply(tensor1, tensor2)
print("multiplication is : ",multiplication)

division = tf.divide(tensor1, tensor2)
print("division is : ",division)

division = tf.divide(tensor1, tensor2)
print("division is : ",division)

square = tf.square(tensor1)
print("square is : ",square)

sum = tf.reduce_sum(tensor1)
print("Reduced sum is : ",sum)

mean = tf.reduce_mean(tensor1)
print("mean sum is : ",mean)

# Addition is :  tf.Tensor([11 22 33], shape=(3,), dtype=int32)
# Subtraction is :  tf.Tensor([ 9 18 27], shape=(3,), dtype=int32)
# multiplication is :  tf.Tensor([10 40 90], shape=(3,), dtype=int32)
# division is :  tf.Tensor([10. 10. 10.], shape=(3,), dtype=float64)
# division is :  tf.Tensor([10. 10. 10.], shape=(3,), dtype=float64)
# square is :  tf.Tensor([100 400 900], shape=(3,), dtype=int32)
# Reduced sum is :  tf.Tensor(60, shape=(), dtype=int32)
# mean sum is :  tf.Tensor(20, shape=(), dtype=int32)