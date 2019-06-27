<template>
<div id="app">
<div class="container">
<div class="header">
 <div class="row">
 <div class="four columns">
 <img alt="GNU Health Federation" src="./assets/logo-gnu-health-federation.png" class="u-max-full-width">
</div>
<div id="nav" class="eight columns">
 <ul class="u-pull-right">
 <span v-if=this.$store.state.authenticated>
 <li>  <router-link to="/" v-on:click.native="logout()"
                    tag="button" class="ghbuttondark"
                    replace>Logout</router-link> </li></span>
   <span v-else>
 <li><router-link to="/">Home</router-link></li>
 <li><router-link to="/about">About</router-link> </li>
 <li><router-link to="/login" tag="button"
                    class="ghbuttondark">Login</router-link> </li>
 </span>
 </ul>
</div>
</div>
</div>
</div>  

        <!-- Show the entry page ("Home") -->
   
    <router-view/>
    <div class="container text-center">
    <div class="footer">
    <p><small>GNU Health (c) GNU Solidario GPL v3+ </small></p>
    </div>
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
  margin-top: 20px;
  color: #007191;
}

.header {

    border-bottom: 1px solid #bedfe4;
    margin-bottom: 8px;
    }

#nav ul li {
 display: inline;
 margin: 0 20px 0 0;
 margin-bottom: 130px;
}

#nav ul li:last-child {

 margin: 0;

}

#nav a {
   font-weight: bold;
   color: #007191;
   text-decoration: none;
   text-transform: uppercase;
   font-size: 14px;
   text-decoration: none;
}
 
#nav a:hover {
    text-decoration: underline;
}

#nav a.router-link-exact-active {
    color: #00acc6;
}

.ghbuttondark {
    border: none;
    color: white;
    border-radius: 20px;
    background: #00acc6;
    border: 1px solid #00acc6;
    text-transform: uppercase;
    padding-left: 25px;
    padding-right: 25px;
    font-size: 14px;
    font-weight: bold;
    cursor: pointer;
}

.ghbuttondark:hover, .ghbuttondark:focus, .ghbuttondark:active {

    background: #00acc6;
    border-color: #ffffff;
 
}

.footer {
    border-top: 1px solid #bedfe4;
}


.greybutton {
    background: #95b5bc;
    color: #ffffff;
    border-color: #95b5bc;
}

.greybutton:hover, .greybutton:focus, .greybutton:active   {
    background: #95b5bc;
    border-color: #ffffff;
}

table tr:nth-child(even) {
    background: #ffffff;
    }
table tr:nth-child(odd) {
    background: #ecf2f3;
    }

</style>