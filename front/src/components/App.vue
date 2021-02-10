<template>
  <div>
    <div v-if="loadingStatus"><h1>Загрузка</h1><b-spinner variant="primary" label="Text Centered"></b-spinner></div>
    <div v-if="!loadingStatus" 
         class="d-flex flex-row justify-content-center flex-wrap py-2"
    >
      <UserCard v-for=" (item,index) in users" 
                :key="index"
                :name="item.user.name"
                :prevue="item.photo_prev"
                :selfie="item.selfie_prev"
                :years="item.user.years"
                :id="item.user.user_id"
                :i="index"
                :created="item.created_at"
                :city="item.user.city"
      />  
    </div>
    

  </div>
</template>
<script>
import UserCard from './UserCard';
import {mapState} from 'vuex';  
  export default{
    name:'App',
    components:{
      UserCard,
    },
    data(){
      return {
      }
    },
    methods:{
      getUsersFromStore(){
        return this.$store.state.users;
      }
    },
    computed:{
       users(){
          return this.$store.state.users;
       }, 
       loadingStatus(){
          return this.$store.state.isLoading;
       },
    },
    mounted(){
      this.$store.dispatch('getUsersData');
    },
  }
</script>