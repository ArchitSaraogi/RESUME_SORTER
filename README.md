##This is a manual to integrate the python project into your website

1> How a user must operate it:
	a>The program has two operational modes 'filter' and 'categorize'


	b>User must select one and give it a system variable


	c>User must also pass the complete location of the job posting text file and the location of the folder in the commmand line as system arguements





	COMMAND LINE INPUT:

	python collective_sorter.py <Operation_to_Perform(filter/categorize)> <category(categorize)//Job_posting.txt(filter)> <folder_path with all resumes>



	
	d>The abaove steps will be valid for all cases where there is a job posting given already in form of a text file.

	e>In case of absence of any job posting or in order to categorize the resumes under one category you must use the 'categorize' function and pass in the category in the second system arguement 

EXAMPLE:
 case i> filter
  python collective_sorter.py filter posting.txt datas
 case ii> categorize
  python collective_sorter.py categorize ACCOUNTANT datas

OUTPUT:
filter: A python dictionary / A JS object will be the format of the output with all resumes in order of their similarity with job requirement


categorize: A python dictionary / A JS object will be the format of the output with only those resumes which match the job category



INTEGRATION INTO JAVA SCRIPT(NODE JS):


create a class childpython that will pass all of the required system arguements 
eg1: const childpython = spawn('python',['collective_sorter.py','filter','posting.txt','datas']);
eg2: const childpython = spawn('python',['collective_sorter.py','categorize','ACCOUNTANT','datas']);


the output will be stored in the sample_object variable as shown in the jsapp.js program


NOTE** : All locations system variables 2,4 should be complete locations and not just the file name unless it is directly under the same folder like in this case

 TROUBLESHOOTING:


 Error Arguement Missing: Arguements- collective_sorter.py <Operation_to_Perform(filter/categorize)> <category(categorize)//Job_posting.txt(filter)> <folder_path with all resumes>

 Note: Contents modified this Readme is no longer valid
 

 you perhaps forgot to entry all 4 of the required system arguements as the program demanded
