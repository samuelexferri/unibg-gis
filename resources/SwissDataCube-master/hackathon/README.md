# SDC Hackathon 11-13 April 2018
Info & registration: http://www.swissdatacube.org/index.php/2018/03/07/opengeneva-hackathon-sdc-sdg/

## News 1 [April 3]
1. We will start on Wednesday April 11 at 9:00. The event will finish on Friday April 13 at 17:00.
2. The venue will be at the "Centre Universitaire d’Informatique”, 7 route de Drize, 1227 Carouge. You can find access information on the following page: http://cui.unige.ch/en/contact/planaccessglobal/
3. We will have a dedicated GitHub repository available at: https://github.com/GRIDgva/SwissDataCube/tree/master/hackathon
4. Currently, we are working with our NASA colleagues to prepare a Virtual Machine with all the necessary material to work with. As soon as it will be ready, we will send you the link to download and install it.

## News 2 [April 6]
The rooms for our Hackathon will be the following 301-2 [April 11]; 322-3 [April 12-13]

1. We will start on Wednesday April 11 at 9:00. The event will finish on Friday April 13 at 17:00.
2. The venue will be at the "Centre Universitaire d’Informatique”, 7 route de Drize, 1227 Carouge. You can find access information on the following page: http://cui.unige.ch/en/contact/planaccessglobal/
3. Regarding Logistics, Organization & Schedule, all information can be found in the following document:
	https://owncloud.unepgrid.ch/index.php/s/bRkAiVLuTiCvH3P
4. Code repository: https://github.com/GRIDgva/SwissDataCube/tree/master/hackathon
5. Document repository:  https://owncloud.unepgrid.ch/index.php/s/g7sxb0Obwu6cW7d 
6. Project documentation (will be available early next week): http://swissdatacube.sparkboard.com 
7. A Virtual Machine with all the necessary software is available. It should be installed before the hackathon! All instructions are available at:
	https://github.com/GRIDgva/SwissDataCube/tree/master/hackathon
8. A repository of useful scientific articles is available at: https://owncloud.unepgrid.ch/index.php/s/AEcywqhftORz5Fa

## News 3 [April 10]
We are really happy to welcome you tomorrow for the beginning of our hackathon.
We will meet at 9:00 the Centre Universitaire d’Informatique (CUI) Battle - Building A, 7 route de Drize, 1227 Carouge.
You can find further information on how to reach the Battelle Campus at: http://cui.unige.ch/en/contact/planaccessglobal/
The room will be: 301-2 (third floor)

To organise and document our work, we have set up a dedicated sparkboard. Please register at: https://swissdatacube.sparkboard.com

Regarding the logistics:
- food & beverage during the day (coffee break; lunch) are offered by the University of Geneva/CUI. Thanks to them
- lunch will be served at the Battelle Campus Cafeteria
- we will have a coffee machine and a boiler for teas and coffees
- If you stay in the building to work over night, just be careful to inform the security (we will inform them)
- Accomodation: Open Geneva Festival can offer free dormitory facilities in civil protection bunkers (with Internet access) each night between 11th and 16th of April 2018. The bunker is located in Meyrin, Geneve and there are 50 spots each night available on first-come-first-served basis. The registration for the accommodation service will be open on 10th of April 2018 at 12:00 at the following link: https://goo.gl/forms/ndchcoZ8DRGJIuFg1.

Do not forget that tomorrow from 6 pm - 7:30pm we will have also the conference “GIS for Good”: https://www.eventbrite.fr/e/billets-conference-gis-for-good-global-to-local-44670677198

That’s all for the moment and we are really looking forward to meet you all tomorrow and have fun together :-)

## Swiss Data Cube Virtual Machine
1. You need first to install Virtual Box: https://www.virtualbox.org
2. Then download the SDC VM at: https://owncloud.unepgrid.ch/index.php/s/tsmakvA29MIx1UZ
3. Import the downloaded OVA file in Virtual Box (Import Appliance)
4. Download and mount the virtual data disk [available soon]
5. In order to bypass firewall issue in Linux and Mac OS change the guest SSH port to 3022
```
Settings > Network > Advanced > Port Forwarding > Change SSH Host Port from 222 to 3022 > OK > OK
```

The VM is a minimial installation with no data (just the OS, the UI, and the notebook server).

Data are available on a separate virtual data disk which can be mounted to the VM.

The VM is configured with 2 vCPUs and 2 GB RAM.
```
username: localuser/password: localuser1234
```
Start the VM in Headless mode.

Connect to the VM using SSH (terminal or Putty) in order to allow copy/paste.
```
ssh -p 3022 localuser@localhost
```

To start the User Interface (http://localhost:8000/), type the following command line:
```
sudo service data_cube_ui restart 
```
To start the Jupyter Notebook (http://localhost:8888), type the following command line:
```
tmux new -s dcNotebook
source /home/localuser/Datacube/datacube_env/bin/activate
cd /home/localuser/Datacube/data_cube_notebooks
jupyter notebook
```
tmux is a terminal multiplexer, allowing a user to access multiple separate terminal sessions inside a single terminal window or remote terminal session. It is useful for dealing with multiple programs from a command-line interface, and for separating programs from the Unix shell that started the program.
Type the following commands to test how to interact with tmux sessions.
```
Ctrl+b > d # to leave a session without stopping its process
tmux ls # to list the active tmux sessions (you should get something starting with "dcNotebook: 1 windows (created ...")
tmux attach -t dcNotebook # to enter the session you just closed
exit # to stop and close the session you are in (it will interrupt all its processes)
```
This way you can use a single terminal and jump in tmux sessions to see Jupyter Notebook activity.
