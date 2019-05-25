<template>
  <div id="app">
    <div id="nav">
    <span v-if=this.$store.state.authenticated>
        <router-link to="/" v-on:click.native="logout()" 
            replace>Logout </router-link>
    </span>
    <span v-else>
        <router-link to="/">Home</router-link> |
        <router-link to="/login">Login </router-link> |
        <router-link to="/about">About</router-link>
    </span>
    <!-- Show the entry page ("Home") -->
    <router-view/>
    <br/>
    </div>
  </div>
</template>

<script>
    export default {
        name: 'App',
        mounted() {
            if(!this.$store.state.authenticated) {
                this.$router.replace({ name: "home" });
            }
        },
        methods: {
            logout() {
                // call the vuex mutation function to reset user credentials
                this.$store.commit('reset_credentials');
            }
        }
    }
</script>

<style>
#app {
  font-family: Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #51717e;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #51717e;
}

#nav a.router-link-exact-active {
  color: #08a8b3;
}
</style>
