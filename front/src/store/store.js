import Vue from 'vue';
import Vuex from 'vuex';
import dataRequests from "../requests/requests";

Vue.use(Vuex)

export default new Vuex.Store({
	state:{
		isLoading:true,
		apiHost:'http://127.0.0.1:5000/',
		apiUrl:'api/v1/verification-profile/',
		users:null,
		verificated:[],
		declined:[],
		banned:[],
		bannedDevices:[],
	},
	getters:{
		isLoading:state=>{
			return state.isLoading;
		},
		getUsers:state=>{
			return state.users;
		}
	},
	actions:{
		async getUsersData(ctx){
		dataRequests(this.state.apiHost + this.state.apiUrl + 'get-data','GET',null)
			.then((value)=>{
				ctx.commit('getUserData',value.data);
			})
			.finally(()=>{
				ctx.commit('loadingState',false);
			});
		},
		async verificate(ctx,payload){
			 dataRequests(this.state.apiHost + this.state.apiUrl + 'verification','POST',{"user_id":payload.id})
			.then((value)=>{
				if (value.status === 'ok') {
				ctx.commit('verificate',payload);
				}
			});
		},
		async decline(ctx,payload){
			dataRequests(this.state.apiHost + this.state.apiUrl + 'cancel-verification','POST',{"user_id":payload.id})
			.then((value)=>{
				if (value.status === 'ok') {
				ctx.commit('decline',payload);
				}
			});
		},
		async banAccount(ctx,payload){
			dataRequests(this.state.apiHost + this.state.apiUrl + 'ban-acc','POST',{"user_id":payload.id})
			.then((value)=>{
				if (value.status === 'ok') {
				ctx.commit('banAccount',payload);
				}
			});
		},
		async banDevice(ctx,payload){
			 dataRequests(this.state.apiHost + this.state.apiUrl + 'ban-dev','POST',{"user_id":payload.id})
			.then((value)=>{
				if (value.status === 'ok') {
				ctx.commit('banDevice',payload);
				}
			}) 
		},
	},
	mutations:{
		getUserData(state,data){
			state.users = data;
		},
		loadingState(state,value){
			state.isLoading = value;
		},
		verificate(state,payload){
			state.verificated.push(payload.id);
			state.users.splice(payload.userIndex,1);
		},
		decline(state,payload){
			state.declined.push(payload.id);
			state.users.splice(payload.userIndex,1);
		},
		banAccount(state,payload){
			state.banned.push(payload.id);
			state.users.splice(payload.userIndex,1);
		},
		banDevice(state,payload){
			state.bannedDevices.push(payload.id);
			state.users.splice(payload.userIndex,1);
		},
	},
})