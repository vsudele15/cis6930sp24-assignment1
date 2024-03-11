__Name: Vaidehi Sudele__
__ASSIGNMENT DESCRIPTION:__ THIS IS ASSIGNMENT 1 IN THE CIS6930 DATA ENGINEERING COURSE. THIS ASSIGNMENT FOCUSES ON READCTING SENSITIVE INFORMATION SUCH AS NAMES, DATES, PHONES, ADDRESSE FROM A GIVEN TEXT FILE. A TEXT FILE I GIVEN AS INPUT WITH SOME FLAGS AND THE PROGRAM GIVES OUTPUT AS A FILE WITH EXTENSION .censored 

__REQUIREMENTS:__
- Python 3.11
- pipenv
__RUNNING INSTRUCTIONS:__
1. Clone the repository

2. Navigate to the project directory:

3. Install dependencies using Pipenv: pipenv install

__COMMAND TO RUN:__
pipenv run python censoror.py --input '*.txt' \
                    --names --dates --phones --address\
                    --output 'files/' \
                    --stats stderr
__BUGS AND ASSUMPTIONS:__

__FUNCTION DESCRIPTION:__ (1.) redact_dates(text, nlp): This function takes two parameters: text, which is the input text containing dates to be redacted, and nlp, which is a spaCy NLP pipeline object initialized with a model that includes entity recognition capabilities. The function processes the input text using the provided spaCy NLP pipeline to identify entities. It then iterates through each identified entity and checks if its label is "DATE". If it is, the function replaces the text of that entity with a series of black bars (█) of the same length. Finally, it returns the redacted text.

(2.) redact_phones(text, nlp): The given function takes 2 parameters text and nlp. It processes the input text using the provided spaCy NLP pipeline (nlp), which tokenizes the text and identifies entities such as phone numbers. Then, it iterates through each identified entity and checks if its label is "PHONE". If it is, the function replaces the text of that entity with a series of black bars (█) of the same length. Finally, it returns the redacted text.

(3.) redact_addresses(text, nlp): This function takes two parameters: text and nlp. It processes the input text using the provided spaCy NLP pipeline (nlp), which tokenizes the text and identifies entities such as addresses. Then, it iterates through each identified entity and checks if its label is "ADDRESS". If it is, the function replaces the text of that entity with a series of black bars (█) of the same length. Finally, it returns the redacted text.

(4.) redact_names(text, nlp): This function also takes two parameters, text and nlp. It proceses the input text using the provided spaCy NLP pipeline (nlp), which tokenizes the text and identifies entities such as addresses. Then, it iterates through each identified entity and checks if its label is "NAMES". If it is, the function replaces the text of that entity with a series of black bars (█) of the same length. Finally, it returns the redacted text.

(5.) redact_text(text, nlp, args): This function takes three parameters: text, nlp, and args. It processes the input text using the provided spaCy NLP pipeline (nlp) and redacts specified entities based on the command-line arguments (args). The args parameter is expected to be an argparse Namespace object containing boolean flags indicating which entities to redact. It iterates through each specified entity type and calls the corresponding redaction function (redact_dates, redact_phones, redact_addresses, redact_names) if the corresponding flag is set to True in args. Finally, it returns the redacted text.

(6.) process_file(input_file, args): This function processes an input file specified by input_file, reads its content, then redacts sensitive information using the redact_text function based on the specified redaction options provided in the args argument. After redacting the text, it writes the redacted text to an output file, with the same filename but with a .censored extension, in the directory specified by args.output. If an error occurs during file processing, such as failing to read the input file or encountering an exception during redaction, it prints an error message indicating the filename and the nature of the error.

(7.) main(): The main function serves as the entry point of the script. It parses command-line arguments using the argparse module, specifying options such as input files, output directory, and types of information to redact (dates, phone numbers, addresses, names). It then checks if the required input and output options are specified. Next, it searches for input files matching the specified pattern using glob.glob. If no input files are found, it prints a message and exits. It creates the output directory if it doesn't already exist. Finally, it iterates over each input file, passing it to the process_file function for redaction.