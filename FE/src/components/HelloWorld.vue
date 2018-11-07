<template>
  <div class="hello">
    <input v-model='name'>
    <button @click='doLogin'>登陆</button>
    <button @click='doLogout'>登出</button>
  </div>
</template>

<script>
import { login, logout } from '../getData'
export default {
  name: 'HelloWorld',
  data () {
    return {
      name: '',
    }
  },
  methods:{
    doLogin(){
      let params = {
        username: this.name
      }
      login(params,(res)=>{
        console.log(res)
      })
    },
    doLogout(){
      logout('',(res)=>{
        console.log(res)
      })
    }
  },
  mounted(){
    
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
