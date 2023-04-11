# PyPeerReview-Matching

Python script to facilitate matching reviewers with entrants (i.e., reviewees), using CSV-formatted input files. Both the entrants.csv and reviewers.csv are 4 column files that contain a) the name (first and last), b) their email, c) the methods that they are experts in, and d) their research topics. The reviewers.csv can also have additional columns at the end containing their history of review participation, whose column headers must include the word "Round" for filtering purposes and values as 'yes' or 'no'.

A 2 column, semicolon separated taxonomy.csv file is included for suggestions on values for topics and methods.

The entrants.csv and reviewers.csv can be generated using a spreedsheet program.

Running the notebook will resuting a the creation of matching_results.csv.

<p align="center">
  <img src="sankey.png" width="350" title="hover text"><br>
  Figure 1. An illustration of resulting matching for 10 entrants, each requiring<br>3 reviews and each reviewer being responsible for performing 3.
</p>

#### Known Bug
  Depending on the numbers (i.e., number of reviewers, entrants, and how many reviews should be done), **the script can result in a reviewer obtaining the same entrant twice**. To check this sort the results dataframe by both the reviewers and by the entrants and do a visual inspection. Until this is solved, please check the results and hand edit where needed.

##### Input and Flags:
1) reviewers CSV file (; seperated)
2) entrants CSV file (; seperated)
3) use_history - 'True' or 'False'
4) reviewer_responsibility - number of reviews to be done by each reviewer
5) entrant_needed_reviews - number of reviews need for each entrant

##### Output:
1) CSV formatted file of matchings (; seperated), including itemized and total matching scores.
2) prints to screen the suggested best matchings

##### Library Dependencies:
1) Pandas

##### Structure of input CSV files:
The structure and examples of the entrants.csv nd reviewers.csv input files can be found below.The "Methods" and "Topics" can be several entries that are seperated by a comma. For the reviewers.csv, it is assumed that the last columns are the histories of their participation (i.e., 'yes' or 'no'). These are provided in a column whose header name include the word 'Round' (see example).

##### Contact:
Karl N. Kirschner<br>
Department of Computer Science<br>
University of Applied Sciences Bonn-Rhein-Sieg<br>
Grantham-Allee 20<br>
53757 Sankt Augustin - Germany<br>

Email: k.n.kirschner _at_ gmail.com

##### Contribution:
Concept: Kirschner<br>
Coding and structure:  Jiang, Daniel and Bitterling, Robert (prototype); Kirschner

<hr style="height:30px"> 

#### entrants.csv example file:
Name;Email;Methods;Topics<br>
Zoowee Blubberworth;zb@fakemail.com;Mathematics, md;viruses, Security<br>
Flufffy Gloomkins;fg@fakemail.com;md, Statistics;Virtual Reality, proteins<br>
etc.

#### reviewers.csv example file:
Name;Email;Methods;Topics;Round 2016;Round  2017;Round  2018;Round  2019<br>
Peafy Doodoofish;pd@fakemail.com;Numerical Algorithms, Statistical Mechanics, Infrared, Python;Security, Viruses, Virtual Reality, Carbohydrates;No; No; Yes; No<br>
Peawee Pimplehair;pp@fakemail.com;Numerical Algorithms, Bioinformatics, NMR, Raman;Methods Development, Virtual Reality, DNA, Viruses;Yes; Yes; No; No<br>
Chewlu Boogerbrain;cb@fakemail.com;Basis Sets, Statistical Mechanics, Molecular Dynamics, Bioinformatics;Security, Virtual Reality, Methods Development, Protein;No; No; No; No<br>
Eggster HoboSmittens;eh@fakemail.com;Infrared, Machine Learning, NMR, Raman;Security, Carbohydrates, Viruses, DNA;Yes; Yes; Yes; Yes<br>
etc.

#### matching_results.csv:
Reviewer Name;Entrant Name;Itemized Score [topics, methods, reviewer's history];Total Score<br>
Fartmoo PimpleFadden;Flapberry Fudgewhistle;['1.000', '1.000', 0];2.0<br>
Fartmoo PimpleFadden;Buritt Noseface;['0.500', '0.500', 0];1.0<br>
Fartmoo PimpleFadden;Peaberry Wigglewhistle;['1.000', '0.000', 0];1.0<br>
Ratspitz Noodlehill;Buritt Noseface;['0.500', '0.500', 0];1.0<br>
Ratspitz Noodlehill;Peaberry Wigglewhistle;['0.500', '0.500', 0];1.0<br>
Ratspitz Noodlehill;Trashwee Sockborn;['0.500', '0.500', 0];1.0<br>
etc.

#### taxonomy.csv:
Topics;Methods<br>
admet;cg<br>
aerosols;bioinformatics<br>
agriculture and food;cheminformatics<br>
analytical;dft<br>
atmospheric;docking<br>
...<br>
viruses;<br>
waste and recycling;<br>
water;<br>
zwitterions;<br>


### Sources:
- Fake names obtained from: https://www.imagineforest.com/blog/funny-name-generator/
- The Sankey illustration was made using https://github.com/riley-x/SankeyFlow.git
