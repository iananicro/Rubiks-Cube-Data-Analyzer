Description
-----
This program was my Final Project for my ITS462 Application Integration from December 2023.

<img width="400" alt="image" src="https://github.com/user-attachments/assets/995b809d-77fd-4a87-bc16-294a08a4cf8f">

Rubik's Cube Data Analyzer is a Python and XML based program that let's the user view various information about a specified Rubik's Cube
data set. The first two options are console application based and allow you to view...
- Solve ID
- Time
- Scramble
- Date of Solve
<img width="500" alt="image" src="https://github.com/user-attachments/assets/c39e56dc-96d2-468b-bdcb-69da741a2965">

Along with the standard console application based information viewing, with the help of Matploblib, you can view charts of...
- Overall Information
<img width="400" alt="image" src="https://github.com/user-attachments/assets/c75d8c45-2eba-493f-8cf1-f01c5a491045">
<img width="400" alt="image" src="https://github.com/user-attachments/assets/b0e69bc1-0c32-44ea-9eb5-412b6ba8ef70">

- Start vs. End information
<img width="400" alt="image" src="https://github.com/user-attachments/assets/5f463579-b348-41ae-b2ad-0196bde28653">
<img width="400" alt="image" src="https://github.com/user-attachments/assets/721eb53b-622c-4a28-b76d-2e2a562286f9">

- Solve Range Information
<img width="400" alt="image" src="https://github.com/user-attachments/assets/cd83abbf-34ec-4c6e-bd0a-0bf7ed83201f">
<img width="400" alt="image" src="https://github.com/user-attachments/assets/bb2c55a4-58ef-49a1-86b2-3975b1f12353">



Dataset Explanation
-----
The dataset that I used compiles data from thousands of different Rubik’s Cube solves, including the solve ID, solve time, scramble and date solved. 

This dataset contains information beginning on 7 September 2020, and ending on 23 August 2021. It would’ve contained a few thousand more solves up to around October of 2023, but unfortunately it was not backed up.

This dataset has about 37,000 lines of code with about 6,200 solves. You can always add onto this dataset by doing more solves. 

This dataset was created through features on CSTimer.net to collect the ID, time, scramble, date, etc., but all that information was inputted through my actual Rubik’s Cube solves. This is my own conducted data.

Data Conclusions
---------------
Based of the findings, we can conclude that a majority of my solves are within the 25 to 30 second (33.63%) and 30 to 35 second range (33.04%). 
Solves between 35 and 40 seconds (16.58%) and 20 to 25 seconds (10.78%) are also relatively common. 
There are results for 10 to 15 seconds (0.05%) and 50 to 55 seconds (0.02%), but they’re so uncommon and rare they don’t even show up on the graph. 
From this conclusion, you can reason that I on average solve around 31 seconds.
There is other functions that this Python program does, such as allowing you to view information based off of specific solves (queried through time or solve ID), but these three gives us the best conclusions about the data set.

