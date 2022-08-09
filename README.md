## Installation

1. Clone the repo 

2. Run `conda env create -f environment.yml && conda activate slurmgui`

3. Set the password with `python reset_password.py <your password>`

4. Open `config.json` and set the default account (your project account number)

## Usage

1. Start the app with `python main.py`

2. Go to `https://127.0.0.1:5000/`. Log in and go to "slurm"

3. In the "Jobs" block, click new to open the form for submitting jobs. Fill out the form and click "submit" to submit the job to slurm.

![image](resource/new.png)

