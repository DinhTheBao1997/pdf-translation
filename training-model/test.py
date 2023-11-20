import pandas as pd
from sklearn.model_selection import train_test_split
import klib
from google.colab import drive
import matplotlib.pyplot as plt
import numpy as np
import torch
from torch import optim
from transformers import AdamW, AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import get_linear_schedule_with_warmup
from transformers import T5Tokenizer, MT5ForConditionalGeneration
from tqdm.notebook import tqdm as tqdm_notebook_
from scipy.signal import savgol_filter
import random
import copy
import os

drive.mount('/content/drive')

df = pd.read_csv('/content/drive/MyDrive/xnli15.tsv', sep='\t')
print('Shape of the Dataframe: ', df.shape)
display(df.head())

# Display the column headers represening each language
print(df.columns)

# Modify the structure of the dataframe for the required downstream task
data_prep = [] 
for col in df.columns:
  for row in df[col]:
    data_prep.append([row, col])

dataframe = pd.DataFrame(data_prep, columns=['input_text','target_text'])
display(dataframe)

# Data cleaning 
dataframe=klib.data_cleaning(dataframe)
dataframe=dataframe.drop_duplicates(subset='input_text', keep=False)

# Adding prefix text to the input, which helps the model to understand the fine-tuning task objective
dataframe['input_text'] = ' '+dataframe['input_text'] 
display(dataframe)

# Visualizing the distribution of the examples in each language
dataframe['target_text'].hist(bins=len(df.columns))

train_val_df, test_df = train_test_split(dataframe, test_size=0.21, random_state=42)
train_df, eval_df = train_test_split(train_val_df, test_size=0.24, random_state=42)
print('Training dataset shape: ', train_df.shape)
print('Validation dataset shape: ', eval_df.shape)
print('Testing dataset shape: ', test_df.shape)

model_repo = 'google/mt5-small'
model_path = '/content/drive/MyDrive/fine-tuned_mt5/'

tokenizer = AutoTokenizer.from_pretrained(model_repo)
model = MT5ForConditionalGeneration.from_pretrained(model_repo)
model = model.cuda()

len(tokenizer.vocab)

print(model.config.max_length)

LANG_TOKEN_MAPPING = {
    'identify language': ''
}
special_tokens_dict = {'additional_special_tokens': list(LANG_TOKEN_MAPPING.values())}
special_tokens_dict

tokenizer.all_special_tokens

model.config.vocab_size

token_len = []

for row in dataframe['input_text']:
  input_ids = tokenizer.encode(row, return_tensors='pt').cuda()
  token_len.append(len(input_ids[0]))

token_len.sort(reverse=True)

plt.figure(figsize=(6, 4),tight_layout=True, dpi=80)
plt.hist(token_len)
plt.xlabel('input token ids length')
plt.ylabel('frequency')
# plt.savefig('/content/gdrive/My Drive/ip_tokens_len.jpg')


label_len = []

for row in dataframe['target_text']:
  input_ids = tokenizer.encode(row, return_tensors='pt').cuda()
  label_len.append(len(input_ids[0]))
  

label_len.sort(reverse=True)

plt.figure(figsize=(6, 4),tight_layout=True, dpi=80)
plt.hist(label_len)
plt.xlabel('target token ids length')
plt.ylabel('frequency')

# Large input sequence length makes the training computationally very intensive
# Choose a decent value by analyzing the histogram above
max_inp_seq_len = 40
max_tar_seq_len = 3

# function to encode a given string and return token ids

def encode_str(text, tokenizer, seq_len):  
  """ Tokenize, pad to max length and encode to ids 
      Returns tensor with token ids """
  input_ids = tokenizer.encode(
      text=text,
      return_tensors = 'pt',
      padding = 'max_length',
      truncation = True,
      max_length = seq_len)

  return input_ids[0]

# Testing the encode_str function

print(train_df['input_text'].iloc[0])
t1 = encode_str(train_df['input_text'].iloc[0],tokenizer,max_inp_seq_len)
print(t1)
tokens = tokenizer.convert_ids_to_tokens(t1)
print(tokens)

# Visualizing how the target texts are tokenized

uniq_lab = dataframe['target_text'].unique()
for uni in uniq_lab:
  t1 = encode_str(uni,tokenizer,max_tar_seq_len)
  tokens = tokenizer.convert_ids_to_tokens(t1)
  print('Input ID: ',t1,', Tokens: ', tokens,', Decoded text: ',tokenizer.decode(t1))

# function to encode a given row from the dataset, containing 'input_text' and 'target_text'
# returns input and target token ids

def encode_row(row, tokenizer, seq_inp_len, seq_tar_len):
  """Encode input and tagret texts from single row"""
  """Returns input and output token ids"""
  input_text = row['input_text']
  target_text = row['target_text']

  if input_text is None or target_text is None:
    return None

  input_token_ids = encode_str(
      input_text, tokenizer, seq_inp_len)
  
  target_token_ids = encode_str(
      target_text, tokenizer, seq_tar_len)

  return input_token_ids, target_token_ids

# function to encode a single batch and return input and output batch token ids

def encode_batch(batch, tokenizer):
  """Encode a single batch"""
  """Returns input and output batch token ids"""
  inputs = []
  targets = []
  for index, row in batch.iterrows():
    #gets input and output tocken ids
    formatted_data = encode_row(
        row, tokenizer, max_inp_seq_len, max_tar_seq_len)
#    print("i/o tocken ids:",formatted_data)    
    if formatted_data is None:
      continue
    
    input_ids, target_ids = formatted_data
    #unsqueeze(input, dim) returns a new tensor with a dimension of size one inserted at the specified position
    inputs.append(input_ids.unsqueeze(0))
    targets.append(target_ids.unsqueeze(0))
#  print('squeezed tocken ids:',inputs)
  
#Concatenate the given sequence of seq tensors in the given dimension    
  batch_input_ids = torch.cat(inputs).cuda()
  batch_target_ids = torch.cat(targets).cuda()

  return batch_input_ids, batch_target_ids

# function to create a generator object to generate batches of data

def data_generator(dataset, tokenizer, batch_size=32):
  """"generates batches"""
  #shuffle the data
  dataset=dataset.sample(frac=1).reset_index(drop=True)

  for i in range(0, len(dataset), batch_size):
    raw_batch = dataset[i:i+batch_size]
    yield encode_batch(raw_batch, tokenizer)

# Testing data generator

data_gen = data_generator(train_df, tokenizer, 8)
data_batch = next(data_gen)
#print('data_batch:',data_batch)
print('Input shape:', data_batch[0].shape)
print('Output shape:', data_batch[1].shape)

# defining the parameters required for fine-tuning

n_epochs = 1
train_batch_size = 16
eval_batch_size = 8
lr = 5e-4 

n_batches = int(np.ceil(len(train_df) / train_batch_size)) 
total_steps = n_epochs * n_batches 
n_warmup_steps = int(total_steps * 0.01) 

val_freq = np.ceil(10*eval_batch_size*n_batches/len(eval_df))*2
while val_freq%5 != 0:
  val_freq += 1
val_freq = round(val_freq)

print_freq = val_freq

checkpoint_freq = np.ceil(n_batches/10)
while checkpoint_freq%100 != 0:
  checkpoint_freq -= 1
checkpoint_freq = round(checkpoint_freq)

print('Total Training Steps(Batches) per Epoch: '+str(n_batches))
print('Printing & Validation Frequency: '+str(val_freq))
print('Checkpoint Saving Frequency: '+str(checkpoint_freq))

# Optimizer
optimizer = AdamW(model.parameters(), lr=lr)
# Create a schedule with a learning rate that decreases linearly from the initial lr set in the optimizer to 0, 
# after a warmup period during which it increases linearly from 0 to the initial lr set in the optimizer.
# Warmup is a way to reduce the primacy effect of the early training examples.
scheduler = get_linear_schedule_with_warmup(
    optimizer, n_warmup_steps, total_steps)

# list to store the training and validation losses 

losses = []
val_losses = []

# function to evaluate the model during training at a given frequency

def eval_model(model, val_generator_object, max_iters=6):
  """evaluate the model on small validation data"""
  
  eval_losses = []
  for i, (input_batch, label_batch) in enumerate(val_generator_object):
    if i >= max_iters:
      break

    model_out = model.forward(
        input_ids = input_batch,
        labels = label_batch)
    eval_losses.append(model_out.loss.item()) 

  return np.mean(eval_losses)

# fine-tuning the model and save the checkpoints

for epoch_idx in range(n_epochs):
  # generate batch data
  train_generator = data_generator(train_df, tokenizer, train_batch_size)
  val_generator = data_generator(eval_df, tokenizer, eval_batch_size)
                
  for batch_idx, (input_batch, label_batch) in tqdm_notebook_(enumerate(train_generator), total=n_batches):
    #zeroes all the gradients before the calculation
    optimizer.zero_grad()

    # Forward pass
    model_out = model.forward(input_ids = input_batch, labels = label_batch)

    # Calculate loss
    loss = model_out.loss
    # loss.item() gets the scalar value held in the loss.  item() turns a Tensor into a Python number
    losses.append(loss.item())
    #backpropagation - computing the gradient of the loss function with respect to each weight
    loss.backward()
    # updating weights to minimize loss
    optimizer.step()
    #You call scheduler.step() every batch, right after optimizer.step(), to update the learning rate.
    scheduler.step()

    # Print training update info
    # At an interval of print_freq or val_freq
    if (batch_idx + 1) % print_freq == 0:
      #average loss for the last 'print_freq' batches
      avg_loss = np.mean(losses[-print_freq:])
      val_loss = eval_model(model, val_generator)
      print('Epoch: {} | Step: {} | Avg. train loss: {:.3f} | Avg. val loss: {:.3f} | lr: {}'.format(
          epoch_idx+1, batch_idx+1, avg_loss, val_loss, scheduler.get_last_lr()[0]))
      val_losses.append(val_loss)
      

    # save the model for every 'checkpoint_freq' steps
    if (batch_idx + 1) % checkpoint_freq == 0:      
      torch.save(model.state_dict(), os.path.join(model_path+ 'Step-{}_checkpoint_lang_pred.pt'.format(batch_idx + 1)))

torch.save(model.state_dict(), os.path.join(model_path+ 'Step-{}_checkpoint_lang_pred.pt'.format(batch_idx + 1)))

if not os.path.exists('/content/drive/MyDrive/Loss'):
  os.mkdir('/content/drive/MyDrive/Loss')

pd.DataFrame(losses).to_csv("/content/drive/MyDrive/Loss/train_loss.csv")
pd.DataFrame(val_losses).to_csv("/content/drive/MyDrive/Loss/val_loss.csv")

print(losses)
print(val_losses)

pd.DataFrame(losses).to_csv("/content/drive/MyDrive/Loss/train_loss.csv")
pd.DataFrame(val_losses).to_csv("/content/drive/MyDrive/Loss/val_loss.csv")

train_loss_= pd.read_csv('/content/drive/MyDrive/Loss/train_loss.csv', index_col=0)
val_loss_= pd.read_csv('/content/drive/MyDrive/Loss/val_loss.csv', index_col=0)


# visualizing the training and validation losses

# Actual training loss with low opacity
fig = plt.figure(figsize=(10, 5), dpi=80)
plt.plot(train_loss_, alpha=0.15, color='orange')

# smoothening the training loss
# window size is chosen depending upon the amount of smoothening required
window = 11
order = 1
y_ = savgol_filter(train_loss_['0'], window, order)
plt.plot(y_, color='orange', label='Training loss (smoothened)')

# Validation loss
val_loss_df = copy.deepcopy(val_loss_) 
val_loss_df.index = (val_loss_.index+1)*val_freq
plt.plot(val_loss_df, label='Validation loss')

plt.legend(loc="upper right")
plt.xlabel('Steps')

# save the plot if needed
# fig.savefig('/content/gdrive/MyDrive/Loss/Loss_Plot.png', dpi=fig.dpi)

def test_model(test_df, tokenizer, wrong_prediction, max_iter):

  max_test_iters = max_iter
  correct_predictions = 0

  for _ in range(max_test_iters):
    num = random.randint(0,len(test_df['input_text'])-1)
    test = test_df.iloc[num]

    input_ids = encode_str(text = test['input_text'], tokenizer = tokenizer, seq_len = 40)
    input_ids = input_ids.unsqueeze(0).cuda()

    #print('Truncated input text:', tokenizer.convert_tokens_to_string(
    #  tokenizer.convert_ids_to_tokens(input_ids[0])))

    output_tokens = model.generate(input_ids, num_beams=10, num_return_sequences=1, length_penalty = 1, no_repeat_ngram_size=2)
    # print(output_tokens)
    for token_set in output_tokens:
      prediction = tokenizer.decode(token_set,skip_special_tokens=True)
      if prediction == test['target_text']:
        correct_predictions += 1
      else:
        wrong_prediction.append([test['input_text'], test['target_text'], prediction])

  return correct_predictions/max_test_iters, wrong_prediction

# test the model on multiple batches to find average test accuracy.
# wrong predictions are saved to 'wrong_predictions.csv' file for further analysis.

Test_acc_values = []
wrong_pred = []
test_n_batches = 200
print('Model testing on test dataset: \n')
for _ in tqdm_notebook_(range(test_n_batches)):
  acc, wrong_pred = test_model(test_df, tokenizer, wrong_pred, max_iter=50)
  Test_acc_values.append(acc)


print('Avg. Test Accuracy: {:.4f}'.format(np.mean(Test_acc_values))) 
wrong_pred_df = pd.DataFrame (wrong_pred, columns = ['Input_text', 'True_target', 'Predicted'])
wrong_pred_df.to_csv("/content/drive/MyDrive/wrong_predictions.csv")
