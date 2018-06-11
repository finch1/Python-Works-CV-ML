import tensorflow as tf 
import pandas as pd 
from sklearn.preprocessing import MinMaxScaler

# load training data set from CSV file
training_data_df = pd.read_csv("D:\\Ex_Files_Building_Deep_Learning_Apps\\03\\sales_data_training.csv", dtype=float)

# pull out columns for X ( data to train with) and Y ( value to predict)
# axis=1 parameter tells it we want to drop a column not a row
# .values to get back the result as an array
X_training =  training_data_df.drop('total_earnings', axis = 1).values
Y_training =  training_data_df[['total_earnings']].values

# load testing data set from CSV file
test_data_df = pd.read_csv("D:\\Ex_Files_Building_Deep_Learning_Apps\\03\\sales_data_test.csv", dtype=float)

X_test =  training_data_df.drop('total_earnings', axis = 1).values
Y_test =  training_data_df[['total_earnings']].values

# all data needs to be scaled to a small range like 0 to 1 for the NN to 
# work well. Create scalers for the inputs and outputs
X_scaler = MinMaxScaler(feature_range=(0,1))
Y_scaler = MinMaxScaler(feature_range=(0,1))

# scale both the training inputs and outputs
X_scaled_training = X_scaler.fit_transform(X_training)
Y_scaled_training = Y_scaler.fit_transform(Y_training)

# it is very important that the training and test data are scaled with the same scaler
X_scaled_testing = X_scaler.transform(X_test)
Y_scaled_testing = Y_scaler.transform(Y_test)

print(X_scaled_testing.shape)
print(Y_scaled_testing.shape)

print("Note: Y values where scaled by multiplying by {:.10f} and adding {:.4f}".format(Y_scaler.scale_[0], Y_scaler.min_[0]))

# define model parameters
learning_rate = 0.001
training_epochs = 100
display_step = 5

# define how many inputs and outputs are in our neural network
number_of_inputs = 9
number_of_outputs = 1

# define how many neurons we want in each layer of our neural net
nodes_layer1 = 50
nodes_layer2 = 100
nodes_layer3 = 50

# Section one: define the layers of the neural net itself
"""Variable scopes functions are similar to python functions.
Any variable we create within this scope will automatically get a prefix of input to their name
internally in TF. Everything within the same scope will be grouped together within the diagram"""
# input layer
with tf.variable_scope('input'):
    """NN should accept nine floats as input for making predictions each time.
    placeholder objects args(what type of tensor to accept,
                             size or shape of tensor to expect=(
                             None = NN can mix up batches of any size,
                             expect nine values for each record in the batch))    """
    X = tf.placeholder(tf.float32, shape=(None, number_of_inputs))

# layer 1
with tf.variable_scope('layer1'):
    weights = # for each connection between each node and node in previous layer
    biases = tf.get_variable(name="biases1", ) # variable holds value over time
    layer_1_output = # activation function that outputs the result of the layer