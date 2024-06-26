
//const childpython = spawn('python',['--version']);


//instead of posting.txt put your job posting and instead of datas put the location of folder with all resumes

//Arguements- collective_sorter.py <Operation_to_Perform(filter/categorize)> <category(categorize)//Job_posting.txt(filter)> <folder_path with all resumes>
//Note add job posting when filtering by resume and name of the category while categorizing
const input_data = [
	{
		"_id": "665f75dbc5ba4a1556347577",
		"applicationId": "665f75c6c5ba4a15563474d4",
		"appliedBy": {
			"_id": "664fd8aae035e952e0edc119",
			"email": "keshugarg927@gmail.com",
			"password": "$2b$10$xEZQ6mum.dMACsixxHnToOKh.DA14Xhxw7eR/n.u4UGi7sxaLuQ5G",
			"type": "student",
			"credits": 974,
			"verified": true,
			"resume": [
				"665f7902c5ba4a15563476e4"
			],
			"pic": "https://res.cloudinary.com/di2jxskci/image/upload/v1717342463/eazeplace/dwgetslrabe8xpjwotmv.jpg",
			"resumeInterships": [
				{
					"title": "a",
					"company": "a",
					"description": "a",
					"startDate": "2024-06-04T18:30:00.000Z",
					"status": true,
					"endDate": "2024-06-09T18:30:00.000Z",
					"verified": true,
					"internId": "73b4c35c6a8253b02b258ce1045aae31",
					"_id": "665cae3806dd6625ab4e5819"
				},
				{
					"title": "hdf",
					"company": "hdf",
					"description": "dfj",
					"startDate": "2024-06-19T18:30:00.000Z",
					"status": true,
					"endDate": "2024-06-04T18:30:00.000Z",
					"verified": true,
					"internId": "141fe0ac4491c6e43cbb3f7f766b4592",
					"_id": "665e3cc9291f48966d490bf4"
				},
				{
					"title": "gdf",
					"company": "hd",
					"description": "jd",
					"startDate": "2024-06-26T18:30:00.000Z",
					"status": true,
					"endDate": "2024-06-19T18:30:00.000Z",
					"verified": true,
					"internId": "6a09510cdfcce19beca57f818df59f0e",
					"_id": "665e3cd4291f48966d490ebf"
				},
				{
					"title": "asd",
					"company": "asd",
					"description": "asd",
					"startDate": "2024-06-08T18:30:00.000Z",
					"status": true,
					"endDate": "2024-06-17T18:30:00.000Z",
					"verified": true,
					"internId": "41150cd94880002713dd90bae8dbd335",
					"_id": "665ca558f5961e1f79b6e0d6"
				},
				{
					"title": "SDE",
					"company": "FaceBook",
					"description": "AEF",
					"startDate": "2024-06-11T18:30:00.000Z",
					"status": true,
					"endDate": "2024-06-09T18:30:00.000Z",
					"verified": true,
					"internId": "e709edd70d299c34d4ca3fb6bb85f400",
					"_id": "665e6097474b6617523984c5"
				},
				{
					"title": "",
					"company": "afs",
					"description": "",
					"startDate": null,
					"status": true,
					"endDate": null,
					"verified": true,
					"internId": "74ee902d7f7c8297be289a9a1a10c5de",
					"_id": "665e6124474b6617523997b4"
				},
				{
					"title": "qwe",
					"company": "qwe",
					"description": "qwe",
					"startDate": "2024-06-08T18:30:00.000Z",
					"status": true,
					"endDate": "2024-06-10T18:30:00.000Z",
					"verified": true,
					"internId": "64a5cb8be8e9e00bd3b7d9bb060d44c0",
					"_id": "665ca567f5961e1f79b6e325"
				}
			],
			"resumeProjects": [
				{
					"title": "ML Engineer",
					"status": true,
					"company": "frfe",
					"description": "Prepared and maintained technical data, reports, documentation, and briefings and created presentations to communicate information to various departments.",
					"startDate": "2002-02-01T18:30:00.000Z",
					"endDate": "2004-04-03T18:30:00.000Z",
					"verified": true,
					"projectId": "517ba1b161064f29c246ebfc8f957486",
					"_id": "6656129dc2d503766cd0ce32"
				},
				{
					"title": "Data scientist ",
					"status": true,
					"company": "Facebook",
					"description": "Created a model to suggest friends",
					"endDate": "2024-02-04T18:30:00.000Z",
					"verified": true,
					"projectId": "fa8650247ab0fb985bcfb2d46403b46c",
					"_id": "6655bd94c2d503766cd0bad5"
				},
				{
					"title": "Product manager",
					"status": true,
					"company": "Facebook",
					"description": "Analyze all current product improvement plans to identify any potential synergies, avoiding duplication of effort and implementing a new feature for a fraction of the cost.",
					"startDate": "2012-12-11T18:30:00.000Z",
					"endDate": "2003-03-02T18:30:00.000Z",
					"verified": true,
					"projectId": "765e3c5f9b0acd275e50acffd5af3534",
					"_id": "665611c3c2d503766cd0c758"
				},
				{
					"title": "af",
					"status": true,
					"company": "ads",
					"description": "sadg",
					"startDate": "2012-11-28T18:30:00.000Z",
					"endDate": "2024-06-09T18:30:00.000Z",
					"verified": true,
					"projectId": "b39b59f6adbea9e6069b08b9fc966d19",
					"_id": "665e60d9474b661752398bb0"
				}
			],
			"createdAt": "2024-05-24T00:00:42.086Z",
			"updatedAt": "2024-06-04T21:54:49.100Z",
			"__v": 0,
			"branch": "Civil Engineering",
			"collegeId": "https://res.cloudinary.com/di2jxskci/image/upload/v1717342471/eazeplace/ryuibxh5h5yxhawywc6c.png",
			"firstName": "keshav",
			"gitHub": "Github",
			"institute": "iit",
			"lastName": "Garg",
			"linkedIn": "Linkedin",
			"mobile": "8888",
			"program": "Btech",
			"year": "2026",
			"title": "Mr"
		},
		"type": "intern",
		"status": "applied",
		"coverLetter": "wet",
		"assesmentSolution": "",
		"resume": null,
		"createdAt": "2024-06-04T20:15:23.603Z",
		"updatedAt": "2024-06-04T20:15:23.603Z",
		"__v": 0
	},
	{
		"_id": "66608dccbedc7389f8aba254",
		"applicationId": "665f75c6c5ba4a15563474d4",
		"appliedBy": {
			"_id": "665ee71eb0becc1a575e421a",
			"email": "keshav@keshav",
			"password": "$2b$10$18PgE/bWvSwJoD4CYDLkv.05MaPbKe302KC5BX/B1CMLePulBLhUK",
			"type": "student",
			"credits": 8782,
			"verified": true,
			"resume": [
				"665ee75db0becc1a575e4226"
			],
			"pic": "https://res.cloudinary.com/di2jxskci/image/upload/v1717495621/eazeplace/mnvoqa4na6um4xeh84wx.png",
			"resumeInterships": [],
			"resumeProjects": [],
			"createdAt": "2024-06-04T10:06:22.499Z",
			"updatedAt": "2024-06-05T16:09:48.253Z",
			"__v": 0,
			"branch": "Civil Engineering",
			"collegeId": "https://res.cloudinary.com/di2jxskci/image/upload/v1717495625/eazeplace/d9z9zc0b4eo8a3ic2hsd.png",
			"firstName": "Keshav",
			"institute": "IITR",
			"lastName": "Garg",
			"mobile": "8295645119",
			"program": "Btech",
			"title": "Mr",
			"year": "2026"
		},
		"type": "intern",
		"status": "applied",
		"coverLetter": "m ,",
		"assesmentSolution": "",
		"resume": {
			"_id": "665ee75db0becc1a575e4226",
			"name": "Keshav Garg",
			"email": "keshav@keshav",
			"pic": "https://res.cloudinary.com/di2jxskci/image/upload/v1717495621/eazeplace/mnvoqa4na6um4xeh84wx.png",
			"branch": "Civil Engineering",
			"year": 2026,
			"user": "665ee71eb0becc1a575e421a",
			"resumeName": "gkujb",
			"areasOfInterest": [],
			"achievements": [],
			"skills": [],
			"verified": false,
			"proof": [],
			"internships": [],
			"academics": [
				{
					"graduationYear": 2026,
					"institute": "IIT Roorkee",
					"degree": "Civil",
					"major": "Civil",
					"cgpa": 10,
					"tenthSchool": "Keshav Garg",
					"tenthPercentage": 96,
					"tenthYear": 2020,
					"twelfthSchool": "Keshav Garg",
					"twelfthPercentage": 93,
					"twelfthYear": 2022,
					"instituteVerified": true,
					"tenthVerified": true,
					"twelfthVerified": true,
					"_id": "665ee774b0becc1a575e42a4"
				}
			],
			"projects": [],
			"extraCurriculars": [],
			"__v": 0
		},
		"createdAt": "2024-06-05T16:09:48.252Z",
		"updatedAt": "2024-06-05T16:09:48.252Z",
		"__v": 0
        }
]
const spawn = require('child_process').spawn;

const childpython = spawn('python',['collective_sorter.py','posting.txt',input_data]);

childpython.stdout.on('data',(data)=>{

	console.log(typeof(data));
});