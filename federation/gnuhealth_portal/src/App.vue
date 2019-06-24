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
        <br/>
    </div>
    <router-view/>
    <div class="footer">
    <p><small>GNU Health (c) GNU Solidario GPL v3+ </small></p>
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
    color: #007191;
    padding: 30px;
    padding-top:0px;
    }
    #nav {
    padding-top:30px;
    padding-bottom:30px;
    }

    div#app div#nav {
    background-image: url(assets/logo-gnu-health-federation.png);
    background-repeat: no-repeat;
    background-position: 0px center;
    }

    div#nav {
    border-bottom: 1px solid #bedfe4;

    }
    div#app div#nav span {
    float:right;
    }

    div#app div#nav span a {
    text-transform: uppercase;
    font-size: 14px;
    text-decoration: none;
    }

    div#app div#nav span a:last-of-type {
    margin-right: 50px;
    }

    #nav a {
    font-weight: bold;
    color: #007191;
    }

    #nav a.router-link-exact-active {
    color: #00acc6;
    }
    .required {
        background: #51717e;
    }

    .footer {
    clear:both;
    border-top: 1px solid #bedfe4;
    }

/* Buttons */


.ghbutton {
    border: none;
    background: #007191;
    padding: 8px 25px;
    color: white;
    border-radius: 4px;
    margin-right: 10px;
    font-size: 14;
}


.greybutton {
    background: #95b5bc;
}



.ghbuttondark {
    border: none;
    padding: 5px 15px;
    color: white;
    border-radius: 20px;
    margin-right: 10px;
    background: #00acc6;
    text-transform: uppercase;
    padding-left: 25px;
    padding-right: 25px;
    font-size: 14px;
    font-weight: bold;
    cursor: pointer;
}

.upper-right {
    float: right;
}

/* Forms */

.gh-form {
    margin: 0px;
    padding: 0px;
    font-size: 14px;
    text-align: left;
}
.gh-form li {
    padding: 0;
    list-style: none;
    margin: 10px 0 0 0;
}

.gh-form label{
    margin:0 0 3px 0;
    padding:0px;
    display:inline-block;
}

.gh-form input[type=text],
.gh-form input[type=date],
.gh-form input[type=datetime],
.gh-form input[type=number],
.gh-form input[type=password],
.gh-form input[type=search],
.gh-form input[type=time],
.gh-form input[type=url],
.gh-form input[type=email],
textarea,
select{
    box-sizing: border-box;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    border:1px solid #cfdee0;
    padding: 7px;
    margin:2px;
    -webkit-transition: all 0.30s ease-in-out;
    -moz-transition: all 0.30s ease-in-out;
    -ms-transition: all 0.30s ease-in-out;
    -o-transition: all 0.30s ease-in-out;
    outline: none;
    border-radius: 4px;
    color:#007191;
    margin-right: 12px;
}
.gh-form input[type=text]:focus,
.gh-form input[type=date]:focus,
.gh-form input[type=datetime]:focus,
.gh-form input[type=number]:focus,
.gh-form input[type=password]:focus,
.gh-form input[type=search]:focus,
.gh-form input[type=time]:focus,
.gh-form input[type=url]:focus,
.gh-form input[type=email]:focus,
.gh-form textarea:focus,
.gh-form select:focus{
    -moz-box-shadow: 0 0 8px #00acc6;
    -webkit-box-shadow: 0 0 8px #00acc6;
    box-shadow: 0 0 8px #00acc6;
    border: 1px solid #00acc6;
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

table.restable {
    border-bottom: 1px solid #bedfe4;
    border-top: 1px solid #bedfe4;
    margin-top: 25px;
    width: 100%;
    border-collapse: collapse;
}

table.restable th {
    border-bottom: 1px solid #bedfe4;
    text-transform: uppercase;
    font-size: 12px;
    padding-top:10px;
    padding-bottom: 10px;
}

table.restable td {
    padding: 6px;
}

table.restable tr:nth-child(even) {
    background: #ffffff;
    }
table.restable tr:nth-child(odd) {
    background: #ecf2f3;
    }

</style>
