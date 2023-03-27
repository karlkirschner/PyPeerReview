# PyPeerReview
Python script to facilitate matching reviewers with entrants (i.e., reviewees), using CSV-formatted input files (4 column, semicolon separated) that contain a) the name (First and Last), b) their email, c) the methods that they are experts in, and d) their research topics.

#### entrants.csv:

Name; Email; Methods; Topics<br>
Zoowee Blubberworth; zoowee_blubberworth@somewhere.edu; QM, MD, MM; metals, proteins, method devel<br>
Flufffy Gloomkins; flufffy_gloomkins@somewhere.edu; DFT, ML; phrama, solvents, ionic liquids, spectroscopy<br>

#### reviewers.csv:
Name; Email; Methods; Topics<br>
Sockborn Peaberry; sockborn_peaberry@somewhere.edu; QM; spectroscopy, pharama<br>
Wigglewhistle Eggster; wigglewhistl_eggster@somewhere.edu; DFT, ML; metals<br>
