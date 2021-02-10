<template>
	<div>
	<div v-if="scale" :class="{isOpened: scale}" >
		<b-button @click="scale = false" class="align-self-end">Закрыть</b-button>
	<div class="d-flex flex-row justify-content-center p-3">		
	<figure class="w-50">
      	<figcaption>Фото профиля</figcaption>
	      <b-img-lazy :src='this.$props.prevue' :alt="this.$props.name"></b-img-lazy>
      </figure>
	  <figure class="w-50">
		<figcaption>Селфи</figcaption>
	      <b-img-lazy :src='this.$props.selfie' :alt="this.$props.name"></b-img-lazy>			
	  </figure>	
	</div>
	</div>

	<b-card class=" m-2"
			style="max-width:380px"
			nogutters
	>
      <div class="d-flex flex-row justify-center align-center" @click="scale = scale ? false : true">
      <figure class="w-50 mx-1">
      	<figcaption>Фото профиля</figcaption>
	      <b-img-lazy :src='this.$props.prevue' style="max-height:270px;max-width:186px" class="w-100" :alt="this.$props.name"></b-img-lazy>
      </figure>
	  <figure class="w-50 mx-1">
		<figcaption>Селфи</figcaption>
	      <b-img-lazy :src='this.$props.selfie' class="w-100" :alt="this.$props.name"></b-img-lazy>			
	  </figure>
      </div>
      <div class='d-flex flex-row justify-content-end'>
	  <b-button-group class="mr-2">
	  	<b-button @click='verify' class='p-0 shieldButton actionsButtons' size="sm">
	  		<font-awesome-icon icon="user-shield" class="m-3 p-0"/>
	  	</b-button>
	  	<b-button @click="decline" class='p-0 deniedButton actionsButtons' size="sm">
	  		<font-awesome-icon icon="window-close" class="m-3 p-0"/>
	  	</b-button>
	  </b-button-group>
	  	<b-button @click="scale = true" class='p-0 openPhotoButton actionsButtons' size="sm" ><font-awesome-icon icon="eye" class="m-3 p-0"/></b-button>
      </div>
      <p style="color:#e48800;fontSize:12px;margin:10px 0"><font-awesome-icon icon="clock" style="marginRight:5px" />Заявка,{{createdTime}}</p>
      <div class="d-flex flex-row justify-content-between align-center">
      	<div class="d-flex flex-row justify-content-start">
	      	<b-avatar :src='this.$props.prevue' square size="48px"></b-avatar>
	      	<div class="d-flex flex-column ml-2" style="fontSize:12px">
		      <p style="color:#005AF0;fontWeight:bold;">{{this.$props.name}}<span style="color:lightgrey;marginLeft:3px;">({{this.$props.years}})</span></p>
		      <p style="color:grey">{{this.$props.city}}</p>
		      <span class="indicator" :style="{backgroundColor: online === true  ?  '#6DBB4A' : null }"></span>
	      	</div>
      	</div>
      	<b-button-group class="float-right">
      		<b-button @click="banAcc" class="p-0 actionsButtons d-flex align-items-center banAccountButton" size="sm">
      			<font-awesome-icon icon="portrait" class="mr-0 ml-2 my-1 p-0" /><font-awesome-icon icon="ban" class="mx-1"/>
      		</b-button>
      		<b-button @click="banDev" class="p-0 actionsButtons d-flex align-items-center banDeviceButton" size="sm">
      			<font-awesome-icon icon="mobile-alt" class="mr-0 ml-2 my-1 p-0"/><font-awesome-icon icon="ban" class="mx-1"/>
      		</b-button>
      	</b-button-group>
      </div>
    </b-card>
    </div>
</template>
<style lang="scss" scoped>
	figcaption{
		font-weight:thin;
		text-align:center;
		color:gray;
	}
	.actionsButtons{
		border:none;
	}
	.shieldButton{
		background-color:#6DBB4A;
	}
	.deniedButton{
		background-color:#E48800;
	}
	.openPhotoButton{
		background-color:#41CAC0;
	}
	.banAccountButton{
		background-color:#E48800;
	}
	.banDeviceButton{
		background-color:#EC6459;
	}
	.isOpened{
		display:flex;
		flex-direction:column;
		align-items:center;
		background-color:white;
		position:absolute;
		z-index:100;
		top:0;
		right:0;
		left:0;
		bottom:0;
		margin:auto;
		padding:20px;
		text-align:center;
		img{

			display:inline-block;
			max-width:90%;
			height:auto;
			margin:auto;
		}
	}
	.indicator{
		display:inline-block;
		width:10px;
		height:10px;
		border-radius:50%;
	}
	p{
		margin:0;
	}
</style>
<script>
	export default{
		name:'UserCard',
		data(){
			return{
				scale:false,
			}
		},
		props:{
			name:{
				type:String,
				default:()=>'',
			},
			prevue:{
				type:String,
				dafault:()=>'',
			},
			selfie:{
				type:String,
				dafault:()=>'',	
			},
			id:{
				type:Number,
				dafault:()=>Number,	
			},
			years:{
				type:Number,
				default:()=>Number,
			},
			created:{
				type:String,
				default:()=>'',
			},
			city:{
				type:String,
				default:()=>'',	
			},
			i:{
				type:Number,
				dafault:()=>Number,
			}
		},
		methods:{
			verify(){
				let id = this.$props.id
				let userIndex = this.$props.i
				this.$store.dispatch('verificate',{id,userIndex});
			},
			decline(){
				let id = this.$props.id
				let userIndex = this.$props.i
				this.$store.dispatch('decline',{id,userIndex});	
			},
			banAcc(){
				let id = this.$props.id
				let userIndex = this.$props.i
				this.$store.dispatch('banAccount',{id,userIndex});
			},
			banDev(){
				let id = this.$props.id
				let userIndex = this.$props.i
				this.$store.dispatch('banDevice',{id,userIndex});
			},
		},
		computed:{
			createdTime(){
				let dateTime = this.$props.created;
				let formated = dateTime.split(' ');
				let formattedDate =  formated[0].replace(/-/gi, '.');
				return formattedDate + " " + formated[1];
			},
			bannedDevice(){
				 this.$props.id === this.$store.state.bannedDevces.find((this.$props.id)) ? true : false ;
			},
			online(){
				let random = Math.floor(Math.random() * 2);
				if (random > 0) {
					return true;
				}else{
					return false;
				}
			},
		}
	}
</script>