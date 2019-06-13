<template>
<div>
    <div>
        <leftmenu/>
    </div>

    <div class="mainarea">
        <div id="new_account">
            <form id="new_fed_account" @submit.prevent="validateForm">
            <ul class="gh-form">
                <li>
                    <label>Account<span class="red">*</span></label>
                    <!-- ************* NOTE *************
                        This applies only to the account field, where we
                        need to force uppercase always.

                        We can not use v-model or CSS on input field
                        so, we use toUpperCase method directly
                    -->
                    <input type="text" :value="account_id.toUpperCase()"
                        placeholder="Federation Account" name="account_id"
                        v-validate="'required'"
                        @input="account_id = $event.target.value.toUpperCase()"/>
                    <button class="ghbutton"
                        v-on:click="generate_fedid()">Generate</button>

                </li>
                <li>
                    <label>Name</label>
                    <input type="text" name="name" v-model="account_info.name"
                        placeholder="First"/>
                    <input type="text" name="lastname" v-model="account_info.lastname"
                        placeholder="Last"/>
                </li>
                <li>
                    <label>Gender</label>
                    <select name="gender" v-model="account_info.gender"
                        v-validate="'required'">
                        <option v-for="option in goptions"
                            v-bind:key="option.value">
                                {{ option.value }}
                        </option>
                    </select>
                    <input type="date" name="dob" v-model="account_info.dob"
                        placeholder="Date of Birth" />

                <li>
                    <label>Password<span class="red">*</span></label>
                    <input type="password" name="password"
                        v-model="account_info.password"
                        v-validate="'required'"/>

                    <input type="password" name="pass_confirm"
                        placeholder="confirm password"
                        v-model="pass_confirm" v-validate="'required'"/>
                </li>
                <li>
                    <label>Roles<span class="red">*</span></label>
                    <input type="text" name="roles" v-model="account_info.roles"
                        v-validate="'required'"/>
                <li/>
                <li>
                <button class="ghbutton"
                    v-on:click.prevent="create_federation_account">Create</button>
                </li>
                </ul>
            </form>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';
import Leftmenu from '@/components/Leftmenu.vue'

export default {
    name: "Accounts",
    // Data
    data() {
        return {
            account_id: "",
            account_info: {
                gender:'',
                name: "",
                lastname: "",
                password: "" ,
                roles: ["end_user"],
                dob: "",
                active: true,
                deceased: false
            },
            // local variables not to be passed
            pass_confirm: "",
            goptions: [
                    { text: 'Gender', value: '' },
                    { text: 'Male', value: 'm' },
                    { text: 'Female', value: 'f' }
                ],
        }
    },

    components: {
      Leftmenu
    },

    // Using Axios
    methods: {
        create_federation_account () {
            axios({
                headers: {
                    'Content-Type': 'application/json',
                },
                method: 'post',
                url: this.$store.state.credentials.thalamus_server +
                    '/people/' + this.account_id,
                auth: {
                    username: this.$store.state.credentials.fedacct,
                    password: this.$store.state.credentials.password
                },
                data: this.account_info

            })
            .then((response) => {
                console.log ("User created:",
                    this.account_id, this.account_info,
                    response.data);
                }
            )
            .catch((response) => {
                console.log ("Error creating the user:",
                    this.account_id, this.account_info,
                    response.data);
                alert("User creation failed !");
            }
            )
        },

        /**
            # Add a default random string in the ref field.
            # The STRSIZE constant provides the length of the PUID
            # The format of the PUID is XXXNNNXXX
        */
        generate_fedid() {
            const STRSIZE = 9;
            var letter;
            const alphabet = "ABCDEFGHIJKLMNPQRSTUVWXYZ";
            var x;
            var puid = this.$store.state.country_code ;

            for (x = 0; x < STRSIZE; x++){
                if ( x < 3 || x > 5 ) {
                    letter = Math.floor(Math.random() * alphabet.length)
                    puid += alphabet.charAt(letter)
                }
                else {
                    puid += Math.floor(Math.random()*10)
                }
            }
            this.account_id = puid;
        },

        validateForm() {
            this.$validator.validateAll().then((result) => {
                if (result) {
                    this.create_federation_account ();
                }
                else {
                    alert('Please check the errors in the form');
                }
            });
        }
    },
}
</script>
