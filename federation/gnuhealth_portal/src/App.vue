<template>
  <div id="app">
    <div id="nav">
        <span v-if=this.$store.state.authenticated>
            <div class="upper-right">
                <router-link to="/" v-on:click.native="logout()"
                    tag="button" class="ghbuttondark"
                    replace>Logout</router-link>
            </div>
        </span>
        <span v-else>
            <router-link to="/">Home</router-link> |
            <router-link to="/about">About</router-link>
            <div class="upper-right">
                <router-link to="/login" tag="button"
                    class="ghbuttondark">Login</router-link>
            </div>
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
    .required {
        background: #51717e;
    }

.ghbutton {
    border: none;
    background: #00bec6;
    padding: 5px 15px;
    color: white;
    border-radius: 20px;
    margin-right: 10px;
}

// Buttons

.ghbuttondark {
    border: none;
    background: #276777;
    padding: 5px 15px;
    color: white;
    border-radius: 20px;
    margin-right: 10px;
}

.upper-right {
    float: right;
}

// Forms

.gh-form {
    margin:10px auto;
    max-width: 400px;
    padding: 20px 12px 10px 20px;
    font: 13px;
    text-align: left;
}
.gh-form li {
    padding: 0;
    display: block;
    list-style: none;
    margin: 10px 0 0 0;
}

.gh-form label{
    margin:0 0 3px 0;
    padding:0px;
    display:block;
}
.gh-form input[type=text],
.gh-form input[type=date],
.gh-form input[type=datetime],
.gh-form input[type=number],
.gh-form input[type=search],
.gh-form input[type=time],
.gh-form input[type=url],
.gh-form input[type=email],
textarea,
select{
    box-sizing: border-box;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    border:1px solid #BEBEBE;
    padding: 7px;
    margin:0px;
    -webkit-transition: all 0.30s ease-in-out;
    -moz-transition: all 0.30s ease-in-out;
    -ms-transition: all 0.30s ease-in-out;
    -o-transition: all 0.30s ease-in-out;
    outline: none;
}
.gh-form input[type=text]:focus,
.gh-form input[type=date]:focus,
.gh-form input[type=datetime]:focus,
.gh-form input[type=number]:focus,
.gh-form input[type=search]:focus,
.gh-form input[type=time]:focus,
.gh-form input[type=url]:focus,
.gh-form input[type=email]:focus,
.gh-form textarea:focus, 
.gh-form select:focus{
    -moz-box-shadow: 0 0 8px #00bec6;
    -webkit-box-shadow: 0 0 8px #00bec6;
    box-shadow: 0 0 8px #00bec6;
    border: 1px solid #00bec6;
}
.gh-form .field-divided{
    width: 49%;
}

.gh-form .field-long{
    width: 100%;
}
.gh-form .field-select{
    width: 100%;
}
.gh-form .field-textarea{
    height: 100px;
}
.gh-form .red{
    color:red;
}
</style>
