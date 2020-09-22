# Spam or Ham classifier

The goal of this project is to build a spam or ham classifier and use it for classifing new messages through a telegram bot where the user can insert a message and receive the result of the classification.
The dataset used is avaible here: [dataset](https://www.kaggle.com/uciml/sms-spam-collection-dataset) and in the following notebook: [here](https://colab.research.google.com/drive/1rAQg8OOVOhZLY3gREc_ryeLPrzt1c0Ou?usp=sharing) is reported the first phase which has the goal of analyzing the dataset composition, apply preprocessing operation in the dataset and then train two different family of classifier.

- One classifier family is build with MultinomialNB classifier and they differ each other for the alpha value.
- The other classifier family is a SVM and they differ each other for the C value. DISCLAIMER: the time required for build the entire family is high

The classifier used for the Telegram bot is the SVM classifier which has obtained overall better results in the valuation phase.  

## File description
- bot.py: In this file the behavior of the bot is defined, the bot has two commands /start that allow the user to insert text for being classified, /cancel that terminate the current session. When a message is classified the bot allow the user to rate the prediction if it's correct or not, the data is collected in a csv file for build a user dataset
- preprocess.py: Here are defined all the functions that preprocess the text.
- classification.py: In this part the precomputed train features and the classifier are loaded. The new record that needs to be classified is then converted is trasformed with vectorized and his label class predicted
- spamhamclassifier.py: Is the notebook converted in py file, for computing the dataset with the same version of sklearn

## Modules
The project requires the following modules in order to be runned:
- joblib
- nltk
- sklearn
- pandas
- python-telegram-bot

Also you need to specify your private telegram key in a secrets.json file.

To run the bot just run 'bot.py' using python
