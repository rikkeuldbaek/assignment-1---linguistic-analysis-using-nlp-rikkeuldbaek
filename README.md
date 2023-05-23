[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10145290&assignment_repo_type=AssignmentRepo)

# **Assignment 1 - Extracting linguistic features using spaCy**
## **Cultural Data Science - Language Analytics**
#### Author: Rikke Uldbæk (202007501)
#### Date: 15th of February 2023

<br>

# **1.1 GitHub link**
The following link is a link to the GitHub repository of assignment 1 in the course Language Analytics (F23.147201U021.A). Within the GitHub repository all necessary code are provided to reproduce the results of the assignment.

https://github.com/rikkeuldbaek/assignment-1-linguistic-analysis-using-nlp-rikkeuldbaek

<br>

# **1.2 Description**
In this assignment I have used ```spaCy``` to extract linguistic information from *The Uppsala Student English corpus (USE)* dataset. For this assignment I have written a script which does the following: Loop over each text file (essay) in the data folder, extract the relative frequency of Nouns, Verbs, Adjective, and Adverbs per 10,000 words and count the total number of unique named entities of three types: persons (PER), locations (LOC), and organizations (ORGS). This linguistic information is extracted for each sub-folder (a1, a2, a3, etc.) and saved in a table. 


<br>

# **1.3 Data**
*The Uppsala Student English corpus (USE)* dataset is a corpus consisting of 1,489 essays written by 440 Swedish university students of English. These 1,489 essays are written at three levels: first term, second term and third term. First term essays are located within the sub-folders a1, a2, a3, a4, a5, second term essays are located within the sub-folders b1, b2, b3, b4, b5, b6, b7, b8, and the third term essays are located in the c1 sub-folder. The total number of words is 1,221,265, making the average length of the written essay 820 words (Kyto et al. 2003). 

<br>

# **1.4 Repository Structure**
The table below presents the required folder structure of this assignment.

Folder|Description|content|
|---|---|---|
| ```in```|Stores the folder ```USEcorpus``` containing all subfolders of essays|```USEcorpus```|
|```out```|Stores extracted linguistic information from each subfolder| a1.txt, a2.txt, a3.txt, a4.txt, a5.txt, b1.txt, b2.txt, b3.txt, b4.txt, b5.txt, b6.txt, b7.txt, b8.txt, and c1.txt|
|```src```|Stores the linguistic information extration script|```LA_assignment1_ru.py```|


<br>

# **1.5 Usage and Reproducibility**
## **1.5.1 Prerequisites** 
In order for the user to be able to run the code, please make sure to have bash and python 3 installed on the used device. The code has been written and tested with Python 3.9.2 on a Linux operating system. In order to run the provided code for this assignment, please follow the instructions below.

<br>

## **1.5.2 Setup Instructions** 
**1) Clone the repository**
```python
git clone https://github.com/rikkeuldbaek/assignment-1-linguistic-analysis-using-nlp-rikkeuldbaek
 ```

 **2) Setup** <br>
Setup virtual environment (```LA1_env```), install packages and load the ```spaCy``` model.
```python
bash setup.sh
```
<br>

## **1.5.3 Run the script** 
Please execute the command below in the terminal to run the ```LA_assignment1_ru.py``` script and produce the described results (information extraction).
```python
bash run.sh
```

However, for the user to change the folder of data (if needed) please specify this in the ```run.sh``` script:
```python
python3 src/LA_assignment1_ru.py --folder_name
```
In this exercise the ```folder_name``` is ```USEcorpus```. ```USEcorpus``` is a subfolder within the folder ```in``` which reffers to my folder structure. The user of the code, can specify their own ```folder_name```, if they want to extract linguistic information from other data files. Please take note of the required folder structure if doing so. 

<br>

## **1.5.4 Script arguments**

The ```LA_assignment1_ru.py``` takes the following arguments:
|Argument|Type|Default|
|---|---|---|
|--folder_name|str|"USEcorpus"|


<br>


# **1.6 Results**
The results consists of 14 .csv files which are all located in the folder ```out```. Please navigate to that folder to inspect the results. A preview of sub-folder a1 looks like this: 


|Filename|RelFreq ADJ|RelFreq NOUN|RelFreq ADV|RelFreq VERB|Unique PER|Unique LOC|Unique ORG|
|---|---|---|---|---|---|---|---|
|0176.a1.txt|649.06|1408.14|682.07|1243.12|0|0|1|
|3040.a1.txt|940.17|1168.09|655.27|1737.89|0|0|0|
|2044.a1.txt|556.99 |1398.96|595.85|1450.78|1|0|0|
|etc||||||||

<br>

# **Resources**

Kyto, M. D. of E. S., Axelsson, M. W., & Berglund, Y. (2003). The Uppsala Student English Corpus (USE). https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457

[The Uppsala Student English Corpus (USE) - dataset](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457)
