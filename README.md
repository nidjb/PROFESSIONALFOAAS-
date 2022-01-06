### Project: FOAAS SERVICE IN PROFESSIONAL ENVIRONMENT FOR EMPLOYEE
##### CLASS PROJECT -GROUP -FALL 2021 -WEB BACK-END ENGINEERING
--------------------------------------------------------
### GOAL(PURPOSE): 
Engineers have been posting rude messages on internal company chats using sites like FOAAS (content warning: profanity). HR director is concerned that this behavior may create a hostile work environment, will affect recruiting, and could expose the company to legal liability.

To meet the requirements of the director, this project will build a new version of the FOAAS service built with language suitable to the professional environment, but which still provides the original HTML pages.

--------------------------------------------------
####  Project Detail
On the basis of the user's request, the service will retrieve an unprofessional response from the URL (from [FOAAS](https://foaas.com/)) and display the original FOOAS response with language suitable for a professional environment by passing the unprofessional message through PurgoMalum (https://www.purgomalum.com).

------------------------------------------------------
#### PROJECT REQUIRE MODULES (from python)
* http.server
* http.client
* socketserver
* json
* urllib.parse
-----------------------------------------------------
#### project Structure
~~~bash
 ProfessionalversionofFOAAS
 |
 |-- redact.py
 |-- server.py
 |-- README.md
 ~~~
-------------------------------------------------
#### How to test an example run for this project:

##### FOR PART -1 - RUNNING PROJECT IN COMMAND LINE
1. Open up a command-line terminal, and navigate to the directory in which `redact.py` is saved.
2. Run the command:
            python3 redact.py

            This should display a message stating:
            Usage: redact URL

        *A path can be specified by following the path formats listed on [FOAAS](https://foaas.com/)
         Example:

         python3 redact.py /because/ProfAvery

3. The terminal will display redacted message in the intended format (outlined in the code).

##### FOR PART-2 -RUNNING server.py
1. Open up a command-line terminal, and navigate to the directory in which `server.py` is saved.
2. We can now run the command:

    python3 server.py

    The command-line terminal will display a prompt informing the user what PORT is in use. **In our project the port we are using is 8000** (defined in `server.py`).

3. Navigate to the local host site, indicating the path to see the message from FOAAS service without curse words.
    example we would use:

        http://localhost:8000/because/ProfAvery



---------------------------------------------------------
##### Student INFORMATION -FALL 2021 -WEB BACK-END ENGINEERING
Nidhi Shah (project lead)
Priyanka Kadam
Robert Nguyen
