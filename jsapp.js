const spawn = require('child_process').spawn;

//const childpython = spawn('python',['--version']);
const childpython = spawn('python',['collective_sorter.py','filter','posting.txt','datas']);

//instead of posting.txt put your job posting and instead of datas put the location of folder with all resumes

//Arguements- collective_sorter.py <Operation_to_Perform(filter/categorize)> <category(categorize)//Job_posting.txt(filter)> <folder_path with all resumes>
//Note add job posting when filtering by resume and name of the category while categorizing


childpython.stdout.on('data',(data)=>{
	console.log("stdout : "+data);

});