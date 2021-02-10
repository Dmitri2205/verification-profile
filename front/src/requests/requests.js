import axios from 'axios';

const dataRequests = (url,type,data)=>{
	return new Promise((resolve,reject)=>{
		axios({method:type,url,data}).then((response)=>{
			resolve(response.data);
		})
		.catch((error)=>{
			reject(error);
		});
	});
}
export default dataRequests;