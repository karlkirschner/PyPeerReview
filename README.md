# PyPeerReview
Python script to facilitate matching reviewers with entrants (i.e., reviewees), using CSV-formatted input files

(4 column, semicolon separated) that contain a) the name (first and last), b) their email, c) the methods that they are experts in, and d) their research topics.

#### entrants.csv:
Name;Email;Methods;Topics<br>
Zoowee Blubberworth;zb@fakemail.com;Mathematics, md;viruses, Security<br>
Flufffy Gloomkins;fg@fakemail.com;md, Statistics;Virtual Reality, proteins<br>


#### reviewers.csv:
Name;Email;Methodologies;Topics;2016;2017;2018;2019<br>
Peafy Doodoofish;pd@fakemail.com;Numerical Algorithms, Statistical Mechanics, Infrared, Python;Security, Viruses, Virtual Reality, Carbohydrates;No; No; Yes; No<br>
Peawee Pimplehair;pp@fakemail.com;Numerical Algorithms, Bioinformatics, NMR, Raman;Methods Development, Virtual Reality, DNA, Viruses;Yes; Yes; No; No<br>
Chewlu Boogerbrain;cb@fakemail.com;Basis Sets, Statistical Mechanics, Molecular Dynamics, Bioinformatics;Security, Virtual Reality, Methods Development, Protein;No; No; No; No<br>
Eggster HoboSmittens;eh@fakemail.com;Infrared, Machine Learning, NMR, Raman;Security, Carbohydrates, Viruses, DNA;Yes; Yes; Yes; Yes<br>



Sources:
Fake names obtained from: https://www.imagineforest.com/blog/funny-name-generator/
