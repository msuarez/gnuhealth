<template>
    <div id="login">
        <input type="text" name="federation_acct" v-model="authinfo.federation_acct" placeholder="Federation ID" />
        <input type="password" name="password" v-model="authinfo.password" placeholder="Password" />
        <button type="button" v-on:click="login()">Login</button>
    </div>
</template>


<script>
import axios from 'axios';

    export default {
        name: 'Login',
        data() {
            return {
                authinfo: {
                    federation_acct: "",
                    password: ""
                },
                login_url: this.$thalamus_server + "/login",
                errors: []
            }
        },
        methods: {
            login() {
                // Check that both user and password fields are not empy
                if(this.authinfo.federation_acct != "" && this.authinfo.password != "") {
                    // Login to Thalamus
                    this.thalamus_login ();
                    } 
                    else {
                        alert("Enter Federation ID and password");
                    }
                },
                
            set_authenticated () {
                    // call the vuex mutation function to store the user credentials
                    this.$store.commit('set_credentials', this.authinfo);
                    // redirect to the "Workplace" component
                    this.$router.replace({ name: "workplace" });
                    
                },
            
            /* Connects to the Thalamus server */
            thalamus_login () {
                axios({
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    method: 'get',
                    url: this.login_url,
                    auth: {
                        username: this.authinfo.federation_acct,
                        password: this.authinfo.password
                    },
                })
                // Use arrow functions within the .then block 
                .then((response) => {
                    console.log ("User Autenthicated:", this.authinfo.federation_acct,
                                 response.data);
                    this.set_authenticated ();
                    }
                )
                .catch((response) => {
                    console.log ("Wrong credentials from:", this.authinfo.federation_acct,
                                 response.data);
                    alert("Access denied");
                }
                )
            }
        }
    }
    
</script>

