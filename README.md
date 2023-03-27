# PyPeerReview
Python script to facilitate matching reviewers with entrants (i.e., reviewees), using CSV-formatted input files (semicolon separated) that contain the name (First and Last), their email, the methods that they are experts in, and their research topics.

entrants.csv:
Name; Email; Methods; Topics
Zoowee Blubberworth; zoowee_blubberworth@somewhere.edu; QM, MD, MM; metals, proteins, method devel
Flufffy Gloomkins; flufffy_gloomkins@somewhere.edu; DFT, ML; phrama, solvents, ionic liquids, spectroscopy

reviewers.csv:
Name; Email; Methods; Topics
Noseface Peaberry; noseface_peaberry@somewhere.edu; QM; spectroscopy, pharama
Wigglewhistle Trashwee; wigglewhistl_trashwee@somewhere.edu; DFT, ML; metals
