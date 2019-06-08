<template>
    <form @submit.prevent="validateLoginForm">
        <div id="login">
            <input type="text" name="thalamus_server"
                v-model="authinfo.thalamus_server"
                v-validate="'required'"
                :class = '{required: IsEmpty}' />
            <input type="text" name="federation_acct" v-model="authinfo.federation_acct"
                placeholder="Federation ID" v-validate="'required|min:9|max:16'" />
            <input type="password" name="password" v-model="authinfo.password"
                placeholder="Password" v-on:keyup.enter="validateLoginForm()"
                v-validate="'required|min:6|max:16'" />

            <button type="button" v-on:click="validateLoginForm()">Login</button>
        </div>
    </form>
</template>


<script>
import axios from 'axios';

    export default {
        name: 'Login',
        data() {
            return {
                authinfo: {
                    thalamus_server: this.$default_thalamus_server,
                    federation_acct: "",
                    password: ""
                },
                stderr: []
            }
        },
        computed: {
            // Check that the server field is not empty
            IsEmpty () {
            const empty = this.authinfo.thalamus_server.length == 0
            return empty ? true : false
            }
        },

        methods: {

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
                    url: this.authinfo.thalamus_server + "/login",

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
            },

            validateLoginForm() {
                this.$validator.validateAll().then((result) => {
                    if (result) {
                        this.thalamus_login ();
                    }
                    else {
                        alert('Please check the errors in the form');
                    }
                });
            }

        }
    }

</script>
