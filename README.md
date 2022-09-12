# ppt-translator-regional-lang
Translates English PowerPoint Presentations (.pptx) to Hindi, Tamil or Marathi

## Requirements
* Python 3.7 or above (can be downloaded from [here](https://www.python.org/downloads/))
* The below Python Libraries can be installed with the below commands in Command Prompt/Termninal/Powershell
  1. [requests](https://pypi.org/project/requests/)
  
  `pip install requests`
  
  2. [python-pptx](https://pypi.org/project/python-pptx/)
  
  `pip install python-pptx`


## Usage
1. Keep app.py and translator.py in the same directory.
2. Put the PPT to be translated in the same directory.
3. Open Command Prompt/Termninal/Powershell and navigate to the diretory of the code files (.py)
4. Type the below command
  
  `py app.py [name_of_your_ppt_file.pptx] [name_of_new_ppt_file.pptx] [hin|tam|mar]`
  
  Last Argument is for destination language:
  * hin for Hindi
  * tam for Tamil
  * mar for Marathi
  
Example Use Case:

`py app.py test.pptx new_test.pptx hin`
