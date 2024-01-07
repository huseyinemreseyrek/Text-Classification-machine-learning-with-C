import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
w1_adam_train_accuracy = []
w1_adam_test_accuracy = []
w1_adam_time = []
w1_adam_iteration = []
w1_adam_loss = []

# with open("w1_ADAM_values.txt", 'r') as dosya:
  
#     for satir in dosya:
        
#         if "Train Accuracy:" in satir and "Test Accuracy:" in satir:
#             train_accuracy = float(satir.split("Train Accuracy:")[1].split(" ")[1])
#             test_accuracy = float(satir.split("Test Accuracy:")[1].split(" ")[1])
#             epoch = int(satir.split("ADAM Epoch:")[1].split(" ")[1])
#             time = float(satir.split("ADAM Time:")[1].split(" ")[1])
#             loss = float(satir.split("Loss:")[1].split(" ")[1])
#             w1_adam_train_accuracy.append(train_accuracy)
#             w1_adam_test_accuracy.append(test_accuracy)
#             w1_adam_iteration.append(epoch)
#             w1_adam_time.append(time)
#             w1_adam_loss.append(loss)

# w1_GD_train_accuracy = []
# w1_GD_test_accuracy = []
# w1_GD_time = []
# w1_GD_iteration = []
# w1_GD_loss = []

# with open("w1_Gradient_values.txt", 'r') as dosya:
  
#     for satir in dosya:
        
#         if "Train Accuracy:" in satir and "Test Accuracy:" in satir:
#             train_accuracy = float(satir.split("Train Accuracy:")[1].split(" ")[1])
#             test_accuracy = float(satir.split("Test Accuracy:")[1].split(" ")[1])
#             epoch = int(satir.split("Gradient Epoch:")[1].split(" ")[1])
#             time = float(satir.split("Gradient Time:")[1].split(" ")[1])
#             loss = float(satir.split("Loss:")[1].split(" ")[1])
#             w1_GD_train_accuracy.append(train_accuracy)
#             w1_GD_test_accuracy.append(test_accuracy)
#             w1_GD_iteration.append(epoch)
#             w1_GD_time.append(time)
#             w1_GD_loss.append(loss)

# w1_SGD_train_accuracy = []
# w1_SGD_test_accuracy = []
# w1_SGD_time = []
# w1_SGD_iteration = []
# w1_SGD_loss = []

# with open("w1_SGD_values.txt", 'r') as dosya:
  
#     for satir in dosya:
        
#         if "Train Accuracy:" in satir and "Test Accuracy:" in satir:
#             train_accuracy = float(satir.split("Train Accuracy:")[1].split(" ")[1])
#             test_accuracy = float(satir.split("Test Accuracy:")[1].split(" ")[1])
#             epoch = int(satir.split("SGD Epoch:")[1].split(" ")[1])
#             time = float(satir.split("SGD Time:")[1].split(" ")[1])
#             loss = float(satir.split("Loss:")[1].split(" ")[1])
#             w1_SGD_train_accuracy.append(train_accuracy)
#             w1_SGD_test_accuracy.append(test_accuracy)
#             w1_SGD_iteration.append(epoch)
#             w1_SGD_time.append(time)
#             w1_SGD_loss.append(loss)
# w1_SGD_test_accuracy = [val * 100 for val in w1_SGD_test_accuracy]
# w1_GD_test_accuracy = [val * 100 for val in w1_GD_test_accuracy]
# w1_adam_test_accuracy = [val * 100 for val in w1_adam_test_accuracy]
# w1_SGD_train_accuracy = [val * 100 for val in w1_SGD_train_accuracy]
# w1_GD_train_accuracy = [val * 100 for val in w1_GD_train_accuracy]
# w1_adam_train_accuracy = [val * 100 for val in w1_adam_train_accuracy]

# fig = plt.figure(figsize=(18, 9))
# plt.plot(w1_adam_time, w1_adam_train_accuracy, label='ADAM Train Accuracy', marker='o',markersize=4)
# plt.plot(w1_adam_time, w1_adam_test_accuracy, label='ADAM Test Accuracy', marker='o',linestyle = '--',markersize=4)
# plt.plot(w1_GD_time, w1_GD_train_accuracy, label='GD Train Accuracy', marker='*',markersize=8)
# plt.plot(w1_GD_time, w1_GD_test_accuracy, label='GD Test Accuracy', marker='*',linestyle = '--',markersize=8,color = 'blue')
# plt.plot(w1_SGD_time, w1_SGD_train_accuracy, label='SGD Train Accuracy', marker='D',markersize=4)
# plt.plot(w1_SGD_time, w1_SGD_test_accuracy, label='SGD Test Accuracy', marker='D',linestyle = '--',markersize=4)
# plt.xlabel('Time',fontsize=20)
# plt.ylabel('Accuracy(%)',fontsize=20)
# plt.title('Train and Test Accuracy Over Time for Different Optimization Algorithms',fontsize=20)
# plt.legend(loc='lower right')
# plt.show()
# plt.close()

# fig = plt.figure(figsize=(18, 9))
# plt.plot(w1_adam_iteration, w1_adam_train_accuracy, label='ADAM Train Accuracy', marker='o',markersize=4)
# plt.plot(w1_adam_iteration, w1_adam_test_accuracy, label='ADAM Test Accuracy', marker='o',linestyle = '--',markersize=4)
# plt.plot(w1_GD_iteration, w1_GD_train_accuracy, label='GD Train Accuracy', marker='*',markersize=8)
# plt.plot(w1_GD_iteration, w1_GD_test_accuracy, label='GD Test Accuracy', marker='*',linestyle = '--',markersize=8,color = 'blue')
# plt.plot(w1_SGD_iteration, w1_SGD_train_accuracy, label='SGD Train Accuracy', marker='D',markersize=4)
# plt.plot(w1_SGD_iteration, w1_SGD_test_accuracy, label='SGD Test Accuracy', marker='D',linestyle = '--',markersize=4)
# plt.xlabel('Iteration',fontsize=20)
# plt.ylabel('Accuracy(%)',fontsize=20)
# plt.title('Train and Test Accuracy at Each Iteration for Different Optimization Algorithms',fontsize=20)
# plt.legend(loc='lower right')
# plt.show()
# plt.close()

# fig = plt.figure(figsize=(18, 9))
# plt.plot(w1_adam_time, w1_adam_loss, label='ADAM Total Loss', marker='o',markersize=4)
# plt.plot(w1_GD_time, w1_GD_loss, label='GD Total Loss', marker='*',markersize=8)
# plt.plot(w1_SGD_time, w1_SGD_loss, label='SGD Total Loss', marker='D',markersize=4)
# plt.xlabel('Time',fontsize=20)
# plt.ylabel('Total Loss(MSE)',fontsize=20)
# plt.title('Total Loss Over Time for Different Optimization Algorithms',fontsize=20)
# plt.legend(loc='upper right')
# plt.show()
# plt.close()

# fig = plt.figure(figsize=(18, 9))
# plt.plot(w1_adam_iteration, w1_adam_loss, label='ADAM Total Loss', marker='o',markersize=4)
# plt.plot(w1_GD_iteration, w1_GD_loss, label='GD Total Loss', marker='*',markersize=8)
# plt.plot(w1_SGD_iteration, w1_SGD_loss, label='SGD Total Loss', marker='D',markersize=4)
# plt.xlabel('Iteration',fontsize=20)
# plt.ylabel('Total Loss(MSE)',fontsize=20)
# plt.title('Total Loss at Each Iteration for Different Optimization Algorithms',fontsize=20)
# plt.legend(loc='upper right')
# plt.show()
# plt.close()

# w2_adam_train_accuracy = []
# w2_adam_test_accuracy = []
# w2_adam_time = []
# w2_adam_iteration = []
# w2_adam_loss = []

# with open("w2_ADAM_values.txt", 'r') as dosya:
  
#     for satir in dosya:
        
#         if "Train Accuracy:" in satir and "Test Accuracy:" in satir:
#             train_accuracy = float(satir.split("Train Accuracy:")[1].split(" ")[1])
#             test_accuracy = float(satir.split("Test Accuracy:")[1].split(" ")[1])
#             epoch = int(satir.split("ADAM Epoch:")[1].split(" ")[1])
#             time = float(satir.split("ADAM Time:")[1].split(" ")[1])
#             loss = float(satir.split("Loss:")[1].split(" ")[1])
#             w2_adam_train_accuracy.append(train_accuracy)
#             w2_adam_test_accuracy.append(test_accuracy)
#             w2_adam_iteration.append(epoch)
#             w2_adam_time.append(time)
#             w2_adam_loss.append(loss)

# w2_GD_train_accuracy = []
# w2_GD_test_accuracy = []
# w2_GD_time = []
# w2_GD_iteration = []
# w2_GD_loss = []

# with open("w2_Gradient_values.txt", 'r') as dosya:
  
#     for satir in dosya:
        
#         if "Train Accuracy:" in satir and "Test Accuracy:" in satir:
#             train_accuracy = float(satir.split("Train Accuracy:")[1].split(" ")[1])
#             test_accuracy = float(satir.split("Test Accuracy:")[1].split(" ")[1])
#             epoch = int(satir.split("Gradient Epoch:")[1].split(" ")[1])
#             time = float(satir.split("Gradient Time:")[1].split(" ")[1])
#             loss = float(satir.split("Loss:")[1].split(" ")[1])
#             w2_GD_train_accuracy.append(train_accuracy)
#             w2_GD_test_accuracy.append(test_accuracy)
#             w2_GD_iteration.append(epoch)
#             w2_GD_time.append(time)
#             w2_GD_loss.append(loss)

# w2_SGD_train_accuracy = []
# w2_SGD_test_accuracy = []
# w2_SGD_time = []
# w2_SGD_iteration = []
# w2_SGD_loss = []

# with open("w2_SGD_values.txt", 'r') as dosya:
  
#     for satir in dosya:
        
#         if "Train Accuracy:" in satir and "Test Accuracy:" in satir:
#             train_accuracy = float(satir.split("Train Accuracy:")[1].split(" ")[1])
#             test_accuracy = float(satir.split("Test Accuracy:")[1].split(" ")[1])
#             epoch = int(satir.split("SGD Epoch:")[1].split(" ")[1])
#             time = float(satir.split("SGD Time:")[1].split(" ")[1])
#             loss = float(satir.split("Loss:")[1].split(" ")[1])
#             w2_SGD_train_accuracy.append(train_accuracy)
#             w2_SGD_test_accuracy.append(test_accuracy)
#             w2_SGD_iteration.append(epoch)
#             w2_SGD_time.append(time)
#             w2_SGD_loss.append(loss)
# w2_SGD_test_accuracy = [val * 100 for val in w2_SGD_test_accuracy]
# w2_GD_test_accuracy = [val * 100 for val in w2_GD_test_accuracy]
# w2_adam_test_accuracy = [val * 100 for val in w2_adam_test_accuracy]
# w2_SGD_train_accuracy = [val * 100 for val in w2_SGD_train_accuracy]
# w2_GD_train_accuracy = [val * 100 for val in w2_GD_train_accuracy]
# w2_adam_train_accuracy = [val * 100 for val in w2_adam_train_accuracy]

# fig = plt.figure(figsize=(18, 9))
# plt.plot(w2_adam_time, w2_adam_train_accuracy, label='ADAM Train Accuracy', marker='o',markersize=4)
# plt.plot(w2_adam_time, w2_adam_test_accuracy, label='ADAM Test Accuracy', marker='o',linestyle = '--',markersize=4)
# plt.plot(w2_GD_time, w2_GD_train_accuracy, label='GD Train Accuracy', marker='*',markersize=8)
# plt.plot(w2_GD_time, w2_GD_test_accuracy, label='GD Test Accuracy', marker='*',linestyle = '--',markersize=8,color = 'blue')
# plt.plot(w2_SGD_time, w2_SGD_train_accuracy, label='SGD Train Accuracy', marker='D',markersize=4)
# plt.plot(w2_SGD_time, w2_SGD_test_accuracy, label='SGD Test Accuracy', marker='D',linestyle = '--',markersize=4)
# plt.xlabel('Time',fontsize=20)
# plt.ylabel('Accuracy(%)',fontsize=20)
# plt.title('Train and Test Accuracy Over Time for Different Optimization Algorithms',fontsize=20)
# plt.legend(loc='lower right')
# plt.show()
# plt.close()

# fig = plt.figure(figsize=(18, 9))
# plt.plot(w2_adam_iteration, w2_adam_train_accuracy, label='ADAM Train Accuracy', marker='o',markersize=4)
# plt.plot(w2_adam_iteration, w2_adam_test_accuracy, label='ADAM Test Accuracy', marker='o',linestyle = '--',markersize=4)
# plt.plot(w2_GD_iteration, w2_GD_train_accuracy, label='GD Train Accuracy', marker='*',markersize=8)
# plt.plot(w2_GD_iteration, w2_GD_test_accuracy, label='GD Test Accuracy', marker='*',linestyle = '--',markersize=8,color = 'blue')
# plt.plot(w2_SGD_iteration, w2_SGD_train_accuracy, label='SGD Train Accuracy', marker='D',markersize=4)
# plt.plot(w2_SGD_iteration, w2_SGD_test_accuracy, label='SGD Test Accuracy', marker='D',linestyle = '--',markersize=4)
# plt.xlabel('Iteration',fontsize=20)
# plt.ylabel('Accuracy(%)',fontsize=20)
# plt.title('Train and Test Accuracy at Each Iteration for Different Optimization Algorithms',fontsize=20)
# plt.legend(loc='lower right')
# plt.show()
# plt.close()

# fig = plt.figure(figsize=(18, 9))
# plt.plot(w2_adam_time, w2_adam_loss, label='ADAM Total Loss', marker='o',markersize=4)
# plt.plot(w2_GD_time, w2_GD_loss, label='GD Total Loss', marker='*',markersize=8)
# plt.plot(w2_SGD_time, w2_SGD_loss, label='SGD Total Loss', marker='D',markersize=4)
# plt.xlabel('Time',fontsize=20)
# plt.ylabel('Total Loss(MSE)',fontsize=20)
# plt.title('Total Loss Over Time for Different Optimization Algorithms',fontsize=20)
# plt.legend(loc='upper right')
# plt.show()
# plt.close()

# fig = plt.figure(figsize=(18, 9))
# plt.plot(w2_adam_iteration, w2_adam_loss, label='ADAM Total Loss', marker='o',markersize=4)
# plt.plot(w2_GD_iteration, w2_GD_loss, label='GD Total Loss', marker='*',markersize=8)
# plt.plot(w2_SGD_iteration, w2_SGD_loss, label='SGD Total Loss', marker='D',markersize=4)
# plt.xlabel('Iteration',fontsize=20)
# plt.ylabel('Total Loss(MSE)',fontsize=20)
# plt.title('Total Loss at Each Iteration for Different Optimization Algorithms',fontsize=20)
# plt.legend(loc='upper right')
# plt.show()
# plt.close()

# w3_adam_train_accuracy = []
# w3_adam_test_accuracy = []
# w3_adam_time = []
# w3_adam_iteration = []
# w3_adam_loss = []

# with open("w3_ADAM_values.txt", 'r') as dosya:
  
#     for satir in dosya:
        
#         if "Train Accuracy:" in satir and "Test Accuracy:" in satir:
#             train_accuracy = float(satir.split("Train Accuracy:")[1].split(" ")[1])
#             test_accuracy = float(satir.split("Test Accuracy:")[1].split(" ")[1])
#             epoch = int(satir.split("ADAM Epoch:")[1].split(" ")[1])
#             time = float(satir.split("ADAM Time:")[1].split(" ")[1])
#             loss = float(satir.split("Loss:")[1].split(" ")[1])
#             w3_adam_train_accuracy.append(train_accuracy)
#             w3_adam_test_accuracy.append(test_accuracy)
#             w3_adam_iteration.append(epoch)
#             w3_adam_time.append(time)
#             w3_adam_loss.append(loss)

# w3_GD_train_accuracy = []
# w3_GD_test_accuracy = []
# w3_GD_time = []
# w3_GD_iteration = []
# w3_GD_loss = []

# with open("w3_Gradient_values.txt", 'r') as dosya:
  
#     for satir in dosya:
        
#         if "Train Accuracy:" in satir and "Test Accuracy:" in satir:
#             train_accuracy = float(satir.split("Train Accuracy:")[1].split(" ")[1])
#             test_accuracy = float(satir.split("Test Accuracy:")[1].split(" ")[1])
#             epoch = int(satir.split("Gradient Epoch:")[1].split(" ")[1])
#             time = float(satir.split("Gradient Time:")[1].split(" ")[1])
#             loss = float(satir.split("Loss:")[1].split(" ")[1])
#             w3_GD_train_accuracy.append(train_accuracy)
#             w3_GD_test_accuracy.append(test_accuracy)
#             w3_GD_iteration.append(epoch)
#             w3_GD_time.append(time)
#             w3_GD_loss.append(loss)

# w3_SGD_train_accuracy = []
# w3_SGD_test_accuracy = []
# w3_SGD_time = []
# w3_SGD_iteration = []
# w3_SGD_loss = []

# with open("w3_SGD_values.txt", 'r') as dosya:
  
#     for satir in dosya:
        
#         if "Train Accuracy:" in satir and "Test Accuracy:" in satir:
#             train_accuracy = float(satir.split("Train Accuracy:")[1].split(" ")[1])
#             test_accuracy = float(satir.split("Test Accuracy:")[1].split(" ")[1])
#             epoch = int(satir.split("SGD Epoch:")[1].split(" ")[1])
#             time = float(satir.split("SGD Time:")[1].split(" ")[1])
#             loss = float(satir.split("Loss:")[1].split(" ")[1])
#             w3_SGD_train_accuracy.append(train_accuracy)
#             w3_SGD_test_accuracy.append(test_accuracy)
#             w3_SGD_iteration.append(epoch)
#             w3_SGD_time.append(time)
#             w3_SGD_loss.append(loss)
# w3_SGD_test_accuracy = [val * 100 for val in w3_SGD_test_accuracy]
# w3_GD_test_accuracy = [val * 100 for val in w3_GD_test_accuracy]
# w3_adam_test_accuracy = [val * 100 for val in w3_adam_test_accuracy]
# w3_SGD_train_accuracy = [val * 100 for val in w3_SGD_train_accuracy]
# w3_GD_train_accuracy = [val * 100 for val in w3_GD_train_accuracy]
# w3_adam_train_accuracy = [val * 100 for val in w3_adam_train_accuracy]

# fig = plt.figure(figsize=(18, 9))
# plt.plot(w3_adam_time, w3_adam_train_accuracy, label='ADAM Train Accuracy', marker='o',markersize=4)
# plt.plot(w3_adam_time, w3_adam_test_accuracy, label='ADAM Test Accuracy', marker='o',linestyle = '--',markersize=4)
# plt.plot(w3_GD_time, w3_GD_train_accuracy, label='GD Train Accuracy', marker='*',markersize=8)
# plt.plot(w3_GD_time, w3_GD_test_accuracy, label='GD Test Accuracy', marker='*',linestyle = '--',markersize=8,color = 'blue')
# plt.plot(w3_SGD_time, w3_SGD_train_accuracy, label='SGD Train Accuracy', marker='D',markersize=4)
# plt.plot(w3_SGD_time, w3_SGD_test_accuracy, label='SGD Test Accuracy', marker='D',linestyle = '--',markersize=4)
# plt.xlabel('Time',fontsize=20)
# plt.ylabel('Accuracy(%)',fontsize=20)
# plt.title('Train and Test Accuracy Over Time for Different Optimization Algorithms',fontsize=20)
# plt.legend(loc='lower right')
# plt.show()
# plt.close()

# fig = plt.figure(figsize=(18, 9))
# plt.plot(w3_adam_iteration, w3_adam_train_accuracy, label='ADAM Train Accuracy', marker='o',markersize=4)
# plt.plot(w3_adam_iteration, w3_adam_test_accuracy, label='ADAM Test Accuracy', marker='o',linestyle = '--',markersize=4)
# plt.plot(w3_GD_iteration, w3_GD_train_accuracy, label='GD Train Accuracy', marker='*',markersize=8)
# plt.plot(w3_GD_iteration, w3_GD_test_accuracy, label='GD Test Accuracy', marker='*',linestyle = '--',markersize=8,color = 'blue')
# plt.plot(w3_SGD_iteration, w3_SGD_train_accuracy, label='SGD Train Accuracy', marker='D',markersize=4)
# plt.plot(w3_SGD_iteration, w3_SGD_test_accuracy, label='SGD Test Accuracy', marker='D',linestyle = '--',markersize=4)
# plt.xlabel('Iteration',fontsize=20)
# plt.ylabel('Accuracy(%)',fontsize=20)
# plt.title('Train and Test Accuracy at Each Iteration for Different Optimization Algorithms',fontsize=20)
# plt.legend(loc='lower right')
# plt.show()
# plt.close()

# fig = plt.figure(figsize=(18, 9))
# plt.plot(w3_adam_time, w3_adam_loss, label='ADAM Total Loss', marker='o',markersize=4)
# plt.plot(w3_GD_time, w3_GD_loss, label='GD Total Loss', marker='*',markersize=8)
# plt.plot(w3_SGD_time, w3_SGD_loss, label='SGD Total Loss', marker='D',markersize=4)
# plt.xlabel('Time',fontsize=20)
# plt.ylabel('Total Loss(MSE)',fontsize=20)
# plt.title('Total Loss Over Time for Different Optimization Algorithms',fontsize=20)
# plt.legend(loc='upper right')
# plt.show()
# plt.close()

# fig = plt.figure(figsize=(18, 9))
# plt.plot(w3_adam_iteration, w3_adam_loss, label='ADAM Total Loss', marker='o',markersize=4)
# plt.plot(w3_GD_iteration, w3_GD_loss, label='GD Total Loss', marker='*',markersize=8)
# plt.plot(w3_SGD_iteration, w3_SGD_loss, label='SGD Total Loss', marker='D',markersize=4)
# plt.xlabel('Iteration',fontsize=20)
# plt.ylabel('Total Loss(MSE)',fontsize=20)
# plt.title('Total Loss at Each Iteration for Different Optimization Algorithms',fontsize=20)
# plt.legend(loc='upper right')
# plt.show()
# plt.close()

# w4_adam_train_accuracy = []
# w4_adam_test_accuracy = []
# w4_adam_time = []
# w4_adam_iteration = []
# w4_adam_loss = []

# with open("w4_ADAM_values.txt", 'r') as dosya:
  
#     for satir in dosya:
        
#         if "Train Accuracy:" in satir and "Test Accuracy:" in satir:
#             train_accuracy = float(satir.split("Train Accuracy:")[1].split(" ")[1])
#             test_accuracy = float(satir.split("Test Accuracy:")[1].split(" ")[1])
#             epoch = int(satir.split("ADAM Epoch:")[1].split(" ")[1])
#             time = float(satir.split("ADAM Time:")[1].split(" ")[1])
#             loss = float(satir.split("Loss:")[1].split(" ")[1])
#             w4_adam_train_accuracy.append(train_accuracy)
#             w4_adam_test_accuracy.append(test_accuracy)
#             w4_adam_iteration.append(epoch)
#             w4_adam_time.append(time)
#             w4_adam_loss.append(loss)

# w4_GD_train_accuracy = []
# w4_GD_test_accuracy = []
# w4_GD_time = []
# w4_GD_iteration = []
# w4_GD_loss = []

# with open("w4_Gradient_values.txt", 'r') as dosya:
  
#     for satir in dosya:
        
#         if "Train Accuracy:" in satir and "Test Accuracy:" in satir:
#             train_accuracy = float(satir.split("Train Accuracy:")[1].split(" ")[1])
#             test_accuracy = float(satir.split("Test Accuracy:")[1].split(" ")[1])
#             epoch = int(satir.split("Gradient Epoch:")[1].split(" ")[1])
#             time = float(satir.split("Gradient Time:")[1].split(" ")[1])
#             loss = float(satir.split("Loss:")[1].split(" ")[1])
#             w4_GD_train_accuracy.append(train_accuracy)
#             w4_GD_test_accuracy.append(test_accuracy)
#             w4_GD_iteration.append(epoch)
#             w4_GD_time.append(time)
#             w4_GD_loss.append(loss)

# w4_SGD_train_accuracy = []
# w4_SGD_test_accuracy = []
# w4_SGD_time = []
# w4_SGD_iteration = []
# w4_SGD_loss = []

# with open("w4_SGD_values.txt", 'r') as dosya:
  
#     for satir in dosya:
        
#         if "Train Accuracy:" in satir and "Test Accuracy:" in satir:
#             train_accuracy = float(satir.split("Train Accuracy:")[1].split(" ")[1])
#             test_accuracy = float(satir.split("Test Accuracy:")[1].split(" ")[1])
#             epoch = int(satir.split("SGD Epoch:")[1].split(" ")[1])
#             time = float(satir.split("SGD Time:")[1].split(" ")[1])
#             loss = float(satir.split("Loss:")[1].split(" ")[1])
#             w4_SGD_train_accuracy.append(train_accuracy)
#             w4_SGD_test_accuracy.append(test_accuracy)
#             w4_SGD_iteration.append(epoch)
#             w4_SGD_time.append(time)
#             w4_SGD_loss.append(loss)
# w4_SGD_test_accuracy = [val * 100 for val in w4_SGD_test_accuracy]
# w4_GD_test_accuracy = [val * 100 for val in w4_GD_test_accuracy]
# w4_adam_test_accuracy = [val * 100 for val in w4_adam_test_accuracy]
# w4_SGD_train_accuracy = [val * 100 for val in w4_SGD_train_accuracy]
# w4_GD_train_accuracy = [val * 100 for val in w4_GD_train_accuracy]
# w4_adam_train_accuracy = [val * 100 for val in w4_adam_train_accuracy]

# fig = plt.figure(figsize=(18, 9))
# plt.plot(w4_adam_time, w4_adam_train_accuracy, label='ADAM Train Accuracy', marker='o',markersize=4)
# plt.plot(w4_adam_time, w4_adam_test_accuracy, label='ADAM Test Accuracy', marker='o',linestyle = '--',markersize=4)
# plt.plot(w4_GD_time, w4_GD_train_accuracy, label='GD Train Accuracy', marker='*',markersize=8)
# plt.plot(w4_GD_time, w4_GD_test_accuracy, label='GD Test Accuracy', marker='*',linestyle = '--',markersize=8,color = 'blue')
# plt.plot(w4_SGD_time, w4_SGD_train_accuracy, label='SGD Train Accuracy', marker='D',markersize=4)
# plt.plot(w4_SGD_time, w4_SGD_test_accuracy, label='SGD Test Accuracy', marker='D',linestyle = '--',markersize=4)
# plt.xlabel('Time',fontsize=20)
# plt.ylabel('Accuracy(%)',fontsize=20)
# plt.title('Train and Test Accuracy Over Time for Different Optimization Algorithms',fontsize=20)
# plt.legend(loc='lower right')
# plt.show()
# plt.close()

# fig = plt.figure(figsize=(18, 9))
# plt.plot(w4_adam_iteration, w4_adam_train_accuracy, label='ADAM Train Accuracy', marker='o',markersize=4)
# plt.plot(w4_adam_iteration, w4_adam_test_accuracy, label='ADAM Test Accuracy', marker='o',linestyle = '--',markersize=4)
# plt.plot(w4_GD_iteration, w4_GD_train_accuracy, label='GD Train Accuracy', marker='*',markersize=8)
# plt.plot(w4_GD_iteration, w4_GD_test_accuracy, label='GD Test Accuracy', marker='*',linestyle = '--',markersize=8,color = 'blue')
# plt.plot(w4_SGD_iteration, w4_SGD_train_accuracy, label='SGD Train Accuracy', marker='D',markersize=4)
# plt.plot(w4_SGD_iteration, w4_SGD_test_accuracy, label='SGD Test Accuracy', marker='D',linestyle = '--',markersize=4)
# plt.xlabel('Iteration',fontsize=20)
# plt.ylabel('Accuracy(%)',fontsize=20)
# plt.title('Train and Test Accuracy at Each Iteration for Different Optimization Algorithms',fontsize=20)
# plt.legend(loc='lower right')
# plt.show()
# plt.close()

# fig = plt.figure(figsize=(18, 9))
# plt.plot(w4_adam_time, w4_adam_loss, label='ADAM Total Loss', marker='o',markersize=4)
# plt.plot(w4_GD_time, w4_GD_loss, label='GD Total Loss', marker='*',markersize=8)
# plt.plot(w4_SGD_time, w4_SGD_loss, label='SGD Total Loss', marker='D',markersize=4)
# plt.xlabel('Time',fontsize=20)
# plt.ylabel('Total Loss(MSE)',fontsize=20)
# plt.title('Total Loss Over Time for Different Optimization Algorithms',fontsize=20)
# plt.legend(loc='upper right')
# plt.show()
# plt.close()

# fig = plt.figure(figsize=(18, 9))
# plt.plot(w4_adam_iteration, w4_adam_loss, label='ADAM Total Loss', marker='o',markersize=4)
# plt.plot(w4_GD_iteration, w4_GD_loss, label='GD Total Loss', marker='*',markersize=8)
# plt.plot(w4_SGD_iteration, w4_SGD_loss, label='SGD Total Loss', marker='D',markersize=4)
# plt.xlabel('Iteration',fontsize=20)
# plt.ylabel('Total Loss(MSE)',fontsize=20)
# plt.title('Total Loss at Each Iteration for Different Optimization Algorithms',fontsize=20)
# plt.legend(loc='upper right')
# plt.show()
# plt.close()

# w5_adam_train_accuracy = []
# w5_adam_test_accuracy = []
# w5_adam_time = []
# w5_adam_iteration = []
# w5_adam_loss = []

# with open("w5_ADAM_values.txt", 'r') as dosya:
  
#     for satir in dosya:
        
#         if "Train Accuracy:" in satir and "Test Accuracy:" in satir:
#             train_accuracy = float(satir.split("Train Accuracy:")[1].split(" ")[1])
#             test_accuracy = float(satir.split("Test Accuracy:")[1].split(" ")[1])
#             epoch = int(satir.split("ADAM Epoch:")[1].split(" ")[1])
#             time = float(satir.split("ADAM Time:")[1].split(" ")[1])
#             loss = float(satir.split("Loss:")[1].split(" ")[1])
#             w5_adam_train_accuracy.append(train_accuracy)
#             w5_adam_test_accuracy.append(test_accuracy)
#             w5_adam_iteration.append(epoch)
#             w5_adam_time.append(time)
#             w5_adam_loss.append(loss)

# w5_GD_train_accuracy = []
# w5_GD_test_accuracy = []
# w5_GD_time = []
# w5_GD_iteration = []
# w5_GD_loss = []

# with open("w5_Gradient_values.txt", 'r') as dosya:
  
#     for satir in dosya:
        
#         if "Train Accuracy:" in satir and "Test Accuracy:" in satir:
#             train_accuracy = float(satir.split("Train Accuracy:")[1].split(" ")[1])
#             test_accuracy = float(satir.split("Test Accuracy:")[1].split(" ")[1])
#             epoch = int(satir.split("Gradient Epoch:")[1].split(" ")[1])
#             time = float(satir.split("Gradient Time:")[1].split(" ")[1])
#             loss = float(satir.split("Loss:")[1].split(" ")[1])
#             w5_GD_train_accuracy.append(train_accuracy)
#             w5_GD_test_accuracy.append(test_accuracy)
#             w5_GD_iteration.append(epoch)
#             w5_GD_time.append(time)
#             w5_GD_loss.append(loss)

# w5_SGD_train_accuracy = []
# w5_SGD_test_accuracy = []
# w5_SGD_time = []
# w5_SGD_iteration = []
# w5_SGD_loss = []

# with open("w5_SGD_values.txt", 'r') as dosya:
  
#     for satir in dosya:
        
#         if "Train Accuracy:" in satir and "Test Accuracy:" in satir:
#             train_accuracy = float(satir.split("Train Accuracy:")[1].split(" ")[1])
#             test_accuracy = float(satir.split("Test Accuracy:")[1].split(" ")[1])
#             epoch = int(satir.split("SGD Epoch:")[1].split(" ")[1])
#             time = float(satir.split("SGD Time:")[1].split(" ")[1])
#             loss = float(satir.split("Loss:")[1].split(" ")[1])
#             w5_SGD_train_accuracy.append(train_accuracy)
#             w5_SGD_test_accuracy.append(test_accuracy)
#             w5_SGD_iteration.append(epoch)
#             w5_SGD_time.append(time)
#             w5_SGD_loss.append(loss)
# w5_SGD_test_accuracy = [val * 100 for val in w5_SGD_test_accuracy]
# w5_GD_test_accuracy = [val * 100 for val in w5_GD_test_accuracy]
# w5_adam_test_accuracy = [val * 100 for val in w5_adam_test_accuracy]
# w5_SGD_train_accuracy = [val * 100 for val in w5_SGD_train_accuracy]
# w5_GD_train_accuracy = [val * 100 for val in w5_GD_train_accuracy]
# w5_adam_train_accuracy = [val * 100 for val in w5_adam_train_accuracy]

# fig = plt.figure(figsize=(18, 9))
# plt.plot(w5_adam_time, w5_adam_train_accuracy, label='ADAM Train Accuracy', marker='o',markersize=4)
# plt.plot(w5_adam_time, w5_adam_test_accuracy, label='ADAM Test Accuracy', marker='o',linestyle = '--',markersize=4)
# plt.plot(w5_GD_time, w5_GD_train_accuracy, label='GD Train Accuracy', marker='*',markersize=8)
# plt.plot(w5_GD_time, w5_GD_test_accuracy, label='GD Test Accuracy', marker='*',linestyle = '--',markersize=8,color = 'blue')
# plt.plot(w5_SGD_time, w5_SGD_train_accuracy, label='SGD Train Accuracy', marker='D',markersize=4)
# plt.plot(w5_SGD_time, w5_SGD_test_accuracy, label='SGD Test Accuracy', marker='D',linestyle = '--',markersize=4)
# plt.xlabel('Time',fontsize=20)
# plt.ylabel('Accuracy(%)',fontsize=20)
# plt.title('Train and Test Accuracy Over Time for Different Optimization Algorithms',fontsize=20)
# plt.legend(loc='lower right')
# plt.show()
# plt.close()

# fig = plt.figure(figsize=(18, 9))
# plt.plot(w5_adam_iteration, w5_adam_train_accuracy, label='ADAM Train Accuracy', marker='o',markersize=4)
# plt.plot(w5_adam_iteration, w5_adam_test_accuracy, label='ADAM Test Accuracy', marker='o',linestyle = '--',markersize=4)
# plt.plot(w5_GD_iteration, w5_GD_train_accuracy, label='GD Train Accuracy', marker='*',markersize=8)
# plt.plot(w5_GD_iteration, w5_GD_test_accuracy, label='GD Test Accuracy', marker='*',linestyle = '--',markersize=8,color = 'blue')
# plt.plot(w5_SGD_iteration, w5_SGD_train_accuracy, label='SGD Train Accuracy', marker='D',markersize=4)
# plt.plot(w5_SGD_iteration, w5_SGD_test_accuracy, label='SGD Test Accuracy', marker='D',linestyle = '--',markersize=4)
# plt.xlabel('Iteration',fontsize=20)
# plt.ylabel('Accuracy(%)',fontsize=20)
# plt.title('Train and Test Accuracy at Each Iteration for Different Optimization Algorithms',fontsize=20)
# plt.legend(loc='lower right')
# plt.show()
# plt.close()

# fig = plt.figure(figsize=(18, 9))
# plt.plot(w5_adam_time, w5_adam_loss, label='ADAM Total Loss', marker='o',markersize=4)
# plt.plot(w5_GD_time, w5_GD_loss, label='GD Total Loss', marker='*',markersize=8)
# plt.plot(w5_SGD_time, w5_SGD_loss, label='SGD Total Loss', marker='D',markersize=4)
# plt.xlabel('Time',fontsize=20)
# plt.ylabel('Total Loss(MSE)',fontsize=20)
# plt.title('Total Loss Over Time for Different Optimization Algorithms',fontsize=20)
# plt.legend(loc='upper right')
# plt.show()
# plt.close()


# fig = plt.figure(figsize=(18, 9))
# plt.plot(w5_adam_iteration, w5_adam_loss, label='ADAM Total Loss', marker='o',markersize=4)
# plt.plot(w5_GD_iteration, w5_GD_loss, label='GD Total Loss', marker='*',markersize=8)
# plt.plot(w5_SGD_iteration, w5_SGD_loss, label='SGD Total Loss', marker='D',markersize=4)
# plt.xlabel('Iteration',fontsize=20)
# plt.ylabel('Total Loss(MSE)',fontsize=20)
# plt.title('Total Loss at Each Iteration for Different Optimization Algorithms',fontsize=20)
# plt.legend(loc='upper right')
# plt.show()
# plt.close()

##################################################################
with open("w1_GD_parameters.txt", "r") as dosya:
    satirlar = dosya.readlines()

vektorler = []

for satir in satirlar:
    vektor = np.array(list(map(float, satir.split())))
    vektorler.append(vektor)
vektorler = np.array(vektorler)


tsne = TSNE(n_components=2, random_state=42, perplexity=3)
vektorler_tsne = tsne.fit_transform(vektorler)
start_point1 = vektorler_tsne[0]
end_point1 = vektorler_tsne[-1]
###############################################################

with open("w2_GD_parameters.txt", "r") as dosya1:
    satirlar = dosya1.readlines()


vektorler2 = []

for satir in satirlar:
    vektor = np.array(list(map(float, satir.split())))
    vektorler2.append(vektor)
vektorler2 = np.array(vektorler2)

tsne2 = TSNE(n_components=2, random_state=42, perplexity=3)
vektorler_tsne2 = tsne2.fit_transform(vektorler2)

start_point2 = vektorler_tsne2[0]
end_point2 = vektorler_tsne2[-1]


####################################################################


with open("w3_GD_parameters.txt", "r") as dosya2:
    satirlar = dosya2.readlines()

vektorler3 = []

for satir in satirlar:
    vektor = np.array(list(map(float, satir.split())))
    vektorler3.append(vektor)
vektorler3 = np.array(vektorler3)

tsne3 = TSNE(n_components=2, random_state=42, perplexity=3)
vektorler_tsne3 = tsne3.fit_transform(vektorler3)
start_point3 = vektorler_tsne3[0]
end_point3 = vektorler_tsne3[-1]
###################################################################


with open("w4_GD_parameters.txt", "r") as dosya3:
    satirlar = dosya3.readlines()

vektorler4 = []

for satir in satirlar:
    vektor = np.array(list(map(float, satir.split())))
    vektorler4.append(vektor)
vektorler4 = np.array(vektorler4)

tsne4 = TSNE(n_components=2, random_state=42, perplexity=3)
vektorler_tsne4 = tsne4.fit_transform(vektorler4)
start_point4 = vektorler_tsne4[0]
end_point4 = vektorler_tsne4[-1]
######################################################################################

with open("w5_GD_parameters.txt", "r") as dosya4:
    satirlar = dosya4.readlines()

vektorler5 = []

for satir in satirlar:
    vektor = np.array(list(map(float, satir.split())))
    vektorler5.append(vektor)
vektorler5 = np.array(vektorler5)

tsne5 = TSNE(n_components=2, random_state=42, perplexity=3)
vektorler_tsne5 = tsne5.fit_transform(vektorler5)
start_point5 = vektorler_tsne5[0]
end_point5 = vektorler_tsne5[-1]

#############################################################################################

plt.scatter(vektorler_tsne[:, 0], vektorler_tsne[:, 1], label='w1_GD', color = 'blue')
plt.scatter(start_point1[0], start_point1[1], color='blue', marker='*', s=350)
plt.scatter(end_point1[0], end_point1[1], color='blue', marker='x', s=350)

plt.scatter(vektorler_tsne2[:, 0], vektorler_tsne2[:, 1], color = "yellow", label = 'w2_GD')
plt.scatter(start_point2[0], start_point2[1], color='yellow', marker='*', s=350)
plt.scatter(end_point2[0], end_point2[1], color='yellow', marker='x', s=350)

plt.scatter(vektorler_tsne3[:, 0], vektorler_tsne3[:, 1], color = "red", label = 'w3_GD')
plt.scatter(start_point3[0], start_point3[1], color='red', marker='*', s=350)
plt.scatter(end_point3[0], end_point3[1], color='red', marker='x', s=350)

plt.scatter(vektorler_tsne4[:, 0], vektorler_tsne4[:, 1], color = "black", label = 'w4_GD')
plt.scatter(start_point4[0], start_point4[1], color='black', marker='*', s=350)
plt.scatter(end_point4[0], end_point4[1], color='black', marker='x', s=350)

plt.scatter(vektorler_tsne5[:, 0], vektorler_tsne5[:, 1], color = "purple", label = 'w5_GD')
plt.scatter(start_point5[0], start_point5[1], color='purple', marker='*', s=350)
plt.scatter(end_point5[0], end_point5[1], color='purple', marker='x', s=350)
text = "*: Initial point\nx: Ending point"
plt.text(max(vektorler_tsne[:, 0]+10), min(vektorler_tsne[:, 1]-6), text, fontsize=15, ha='right', va='bottom')
plt.title('t-SNE Visualization with Different Initial W Values for Gradient Descent')
plt.legend(loc = 'upper left')
plt.show()

##############################################################################################################

with open("w1_SGD_parameters.txt", "r") as dosya:
    satirlar = dosya.readlines()

vektorler = []

for satir in satirlar:
    vektor = np.array(list(map(float, satir.split())))
    vektorler.append(vektor)
vektorler = np.array(vektorler)


tsne = TSNE(n_components=2, random_state=42, perplexity=20)
vektorler_tsne = tsne.fit_transform(vektorler)
start_point1 = vektorler_tsne[0]
end_point1 = vektorler_tsne[-1]
###############################################################

with open("w2_SGD_parameters.txt", "r") as dosya1:
    satirlar = dosya1.readlines()


vektorler2 = []

for satir in satirlar:
    vektor = np.array(list(map(float, satir.split())))
    vektorler2.append(vektor)
vektorler2 = np.array(vektorler2)

tsne2 = TSNE(n_components=2, random_state=42, perplexity=20)
vektorler_tsne2 = tsne2.fit_transform(vektorler2)

start_point2 = vektorler_tsne2[0]
end_point2 = vektorler_tsne2[-1]


####################################################################


with open("w3_SGD_parameters.txt", "r") as dosya2:
    satirlar = dosya2.readlines()

vektorler3 = []

for satir in satirlar:
    vektor = np.array(list(map(float, satir.split())))
    vektorler3.append(vektor)
vektorler3 = np.array(vektorler3)

tsne3 = TSNE(n_components=2, random_state=42, perplexity=20)
vektorler_tsne3 = tsne3.fit_transform(vektorler3)
start_point3 = vektorler_tsne3[0]
end_point3 = vektorler_tsne3[-1]
###################################################################


with open("w4_SGD_parameters.txt", "r") as dosya3:
    satirlar = dosya3.readlines()

vektorler4 = []

for satir in satirlar:
    vektor = np.array(list(map(float, satir.split())))
    vektorler4.append(vektor)
vektorler4 = np.array(vektorler4)

tsne4 = TSNE(n_components=2, random_state=42, perplexity=20)
vektorler_tsne4 = tsne4.fit_transform(vektorler4)
start_point4 = vektorler_tsne4[0]
end_point4 = vektorler_tsne4[-1]
######################################################################################

with open("w5_SGD_parameters.txt", "r") as dosya4:
    satirlar = dosya4.readlines()

vektorler5 = []

for satir in satirlar:
    vektor = np.array(list(map(float, satir.split())))
    vektorler5.append(vektor)
vektorler5 = np.array(vektorler5)

tsne5 = TSNE(n_components=2, random_state=42, perplexity=20)
vektorler_tsne5 = tsne5.fit_transform(vektorler5)
start_point5 = vektorler_tsne5[0]
end_point5 = vektorler_tsne5[-1]

#############################################################################################

plt.scatter(vektorler_tsne[:, 0], vektorler_tsne[:, 1], label='w1_SGD', color = 'blue')
plt.scatter(start_point1[0], start_point1[1], color='blue', marker='*', s=350)
plt.scatter(end_point1[0], end_point1[1], color='blue', marker='x', s=350)

plt.scatter(vektorler_tsne2[:, 0], vektorler_tsne2[:, 1], color = "yellow", label = 'w2_SGD')
plt.scatter(start_point2[0], start_point2[1], color='yellow', marker='*', s=350)
plt.scatter(end_point2[0], end_point2[1], color='yellow', marker='x', s=350)

plt.scatter(vektorler_tsne3[:, 0], vektorler_tsne3[:, 1], color = "red", label = 'w3_SGD')
plt.scatter(start_point3[0], start_point3[1], color='red', marker='*', s=350)
plt.scatter(end_point3[0], end_point3[1], color='red', marker='x', s=350)

plt.scatter(vektorler_tsne4[:, 0], vektorler_tsne4[:, 1], color = "black", label = 'w4_SGD')
plt.scatter(start_point4[0], start_point4[1], color='black', marker='*', s=350)
plt.scatter(end_point4[0], end_point4[1], color='black', marker='x', s=350)

plt.scatter(vektorler_tsne5[:, 0], vektorler_tsne5[:, 1], color = "purple", label = 'w5_SGD')
plt.scatter(start_point5[0], start_point5[1], color='purple', marker='*', s=350)
plt.scatter(end_point5[0], end_point5[1], color='purple', marker='x', s=350)
text = "*: Initial point\nx: Ending point"
plt.text(max(vektorler_tsne[:, 0]+3), min(vektorler_tsne[:, 1]-7), text, fontsize=15, ha='right', va='bottom')
plt.title('t-SNE Visualization with Different Initial W Values for SGD')
plt.legend(loc = 'upper left')
plt.show()

#####################################################################################################################

with open("w1_ADAM_parameters.txt", "r") as dosya:
    satirlar = dosya.readlines()

vektorler = []

for satir in satirlar:
    vektor = np.array(list(map(float, satir.split())))
    vektorler.append(vektor)
vektorler = np.array(vektorler)


tsne = TSNE(n_components=2, random_state=42, perplexity=20)
vektorler_tsne = tsne.fit_transform(vektorler)
start_point1 = vektorler_tsne[0]
end_point1 = vektorler_tsne[-1]
###############################################################

with open("w2_ADAM_parameters.txt", "r") as dosya1:
    satirlar = dosya1.readlines()


vektorler2 = []

for satir in satirlar:
    vektor = np.array(list(map(float, satir.split())))
    vektorler2.append(vektor)
vektorler2 = np.array(vektorler2)

tsne2 = TSNE(n_components=2, random_state=42, perplexity=20)
vektorler_tsne2 = tsne2.fit_transform(vektorler2)

start_point2 = vektorler_tsne2[0]
end_point2 = vektorler_tsne2[-1]


####################################################################


with open("w3_ADAM_parameters.txt", "r") as dosya2:
    satirlar = dosya2.readlines()

vektorler3 = []

for satir in satirlar:
    vektor = np.array(list(map(float, satir.split())))
    vektorler3.append(vektor)
vektorler3 = np.array(vektorler3)

tsne3 = TSNE(n_components=2, random_state=42, perplexity=20)
vektorler_tsne3 = tsne3.fit_transform(vektorler3)
start_point3 = vektorler_tsne3[0]
end_point3 = vektorler_tsne3[-1]
###################################################################


with open("w4_ADAM_parameters.txt", "r") as dosya3:
    satirlar = dosya3.readlines()

vektorler4 = []

for satir in satirlar:
    vektor = np.array(list(map(float, satir.split())))
    vektorler4.append(vektor)
vektorler4 = np.array(vektorler4)

tsne4 = TSNE(n_components=2, random_state=42, perplexity=20)
vektorler_tsne4 = tsne4.fit_transform(vektorler4)
start_point4 = vektorler_tsne4[0]
end_point4 = vektorler_tsne4[-1]
######################################################################################

with open("w5_ADAM_parameters.txt", "r") as dosya4:
    satirlar = dosya4.readlines()

vektorler5 = []

for satir in satirlar:
    vektor = np.array(list(map(float, satir.split())))
    vektorler5.append(vektor)
vektorler5 = np.array(vektorler5)

tsne5 = TSNE(n_components=2, random_state=42, perplexity=20)
vektorler_tsne5 = tsne5.fit_transform(vektorler5)
start_point5 = vektorler_tsne5[0]
end_point5 = vektorler_tsne5[-1]

#############################################################################################

plt.scatter(vektorler_tsne[:, 0], vektorler_tsne[:, 1], label='w1_ADAM', color = 'blue')
plt.scatter(start_point1[0], start_point1[1], color='blue', marker='*', s=350)
plt.scatter(end_point1[0], end_point1[1], color='blue', marker='x', s=350)

plt.scatter(vektorler_tsne2[:, 0], vektorler_tsne2[:, 1], color = "yellow", label = 'w2_ADAM')
plt.scatter(start_point2[0], start_point2[1], color='yellow', marker='*', s=350)
plt.scatter(end_point2[0], end_point2[1], color='yellow', marker='x', s=350)

plt.scatter(vektorler_tsne3[:, 0], vektorler_tsne3[:, 1], color = "red", label = 'w3_ADAM')
plt.scatter(start_point3[0], start_point3[1], color='red', marker='*', s=350)
plt.scatter(end_point3[0], end_point3[1], color='red', marker='x', s=350)

plt.scatter(vektorler_tsne4[:, 0], vektorler_tsne4[:, 1], color = "black", label = 'w4_ADAM')
plt.scatter(start_point4[0], start_point4[1], color='black', marker='*', s=350)
plt.scatter(end_point4[0], end_point4[1], color='black', marker='x', s=350)

plt.scatter(vektorler_tsne5[:, 0], vektorler_tsne5[:, 1], color = "purple", label = 'w5_ADAM')
plt.scatter(start_point5[0], start_point5[1], color='purple', marker='*', s=350)
plt.scatter(end_point5[0], end_point5[1], color='purple', marker='x', s=350)
text = "*: Initial point\nx: Ending point"
plt.text(max(vektorler_tsne[:, 0]+7), min(vektorler_tsne[:, 1]-2), text, fontsize=15, ha='right', va='bottom')
plt.title('t-SNE Visualization with Different Initial W Values for ADAM Algorithm')
plt.legend(loc = 'upper left')
plt.show()
