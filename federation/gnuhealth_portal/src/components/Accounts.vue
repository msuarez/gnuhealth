<template>
<div class="container">
<div class="row">
<div class="three columns">
    <div>
        <leftmenu/>
    </div>
</div>
<div class="nine columns">
    <div class="mainarea mt-4">
    <div class="ghtopbar">
        <button class="ghbutton"
            v-on:click.prevent="set_active_form(new_acct=true,edit_acct=false)">New</button>

        <button class="ghbutton"
            v-on:click.prevent="set_active_form(new_acct=false,edit_acct=true)">Edit</button>
    </div>
        <div v-if="render_new_acct" id="new_account">
            <form id="new_fed_account" @submit.prevent="validateCreateForm">
            <div class="row">
                    <div class="six columns">
                    <label>Account<span class="red">*</span></label>
                    <!-- ************* NOTE *************
                        This applies only to the account field, where we
                        need to force uppercase always.
                        We can not use v-model or CSS on input field
                        so, we use toUpperCase method directly
                    -->
                    <input class="u-full-width" type="text" 
                        :value="account_id.toUpperCase()"
                        placeholder="Federation Account" name="account_id"
                        v-validate="'required'"
                        @input="account_id = $event.target.value.toUpperCase()"/>
                    </div>
                    <div class="six columns">
                        <label class="hide-sm">&nbsp;</label>
                        <button class="ghbutton greybutton"
                            v-on:click.prevent="generate_fedid">Generate</button>
                    </div>
                    </div>
                    <div class="row">
                    <div class="six columns">
                        <label>Name</label>
                        <input class="u-full-width" type="text" name="name"
                            v-model="account_info.name"
                            placeholder="First"/>
                    </div>
                    <div class="six columns">
                    <label class="hide-sm">&nbsp;</label>
                    <input class="u-full-width" type="text" name="lastname"
                        v-model="account_info.lastname"
                        placeholder="Last"/>
                    </div>
                    </div>
                     <div class="row">
                    <div class="six columns">
                    <label>Gender & DoB</label>
                    <select class="mr-4" name="gender"
                        v-model="account_info.gender"
                        v-validate="'required'">
                        <option v-for="option in goptions"
                            v-bind:key="option.value">
                                {{ option.value }}
                        </option>
                    </select>
                    <input type="date" name="dob" v-model="account_info.dob"
                        placeholder="Date of Birth" />
                      </div>
                      </div>
                    <div class="row">
                        <div class="six columns">
                            <label>Password</label>
                            <input class="u-full-width" type="password"
                                name="password" placeholder="Password"
                                v-model="account_info.password" ref="password"
                                v-validate="'required'"/>
                        </div>
                        <div class="six columns">
                            <label class="hide-sm">&nbsp;</label>
                            <input class="u-full-width" type="password"
                                name="pass_confirm"
                                placeholder="Confirm password"
                                v-model="pass_confirm" data-vv-as="password"
                                v-validate="'required|confirmed:password'"/>
                        </div>
                    </div>
                    <div class="row">
                        <div class="six columns">
                            <label>Roles<span class="red">*</span></label>
                            <input class="u-full-width" type="text" name="roles"
                                v-model="account_info.roles"
                                v-validate="'required'"/>
                        </div>
                        <div class="six columns">
                            <label class="hide-sm">&nbsp;</label>
                            <label class="u-pull-left mr-4">
                            <input type="checkbox" name="active"
                                v-model="account_info.active"/>
                            <span class="label-body">Active</span>	
                            </label>
                            <label>
                            <input type="checkbox" name="deceased"
                                v-model="account_info.deceased"/>
                            <span class="label-body">Deceased</span>
                            </label>
                        </div>
                    </div>
                <button class="ghbutton"
                    v-on:click.prevent="validateCreateForm">Create</button>
            </form>
        </div>

<!-- Edit account form -->

        <div v-if="render_edit_acct" id="edit_account">
            <form id="edit_fed_account" @submit.prevent="validateCreateForm">
                <ul class="gh-form">
                        <div class="row">
                        <div class="six columns">
                        <label>Account<span class="red">*</span></label>
                        <input class="u-full-width" type="search" :value="account_id.toUpperCase()"
                            placeholder="Federation Account" name="account_id"
                            v-validate="'required'"
                            @input="account_id = $event.target.value.toUpperCase()"/>
                        </div>
                        <div class="six columns">
                        <label class="hide-sm">&nbsp;</label>
                        <button class="ghbutton"
                        v-on:click.prevent="validateEditForm">Search</button>
                        </div>
                        </div>
                </ul>
            </form>
        </div>

    </div>
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
            render_new_acct: false,
            render_edit_acct: false,
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
        set_active_form (new_acct, edit_acct) {
            this.render_new_acct = new_acct
            this.render_edit_acct = edit_acct
        },

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
                alert("User created SUCCESSFULLY !");
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

        search_federation_account () {
            axios({
                headers: {
                    'Content-Type': 'application/json',
                },
                method: 'get',
                url: this.$store.state.credentials.thalamus_server +
                    '/people/' + this.account_id,
                auth: {
                    username: this.$store.state.credentials.fedacct,
                    password: this.$store.state.credentials.password
                },

            })
            .then(response => {this.accounts = response.data})
            .catch(e => { this.axios_errors.push(e)} );
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

        validateCreateForm() {
            this.$validator.validateAll().then((result) => {
                if (result) {
                    this.create_federation_account ();
                }
                else {
                    alert('Please check the errors in the form');
                }
            });
        },

        validateEditForm() {
            this.$validator.validateAll().then((result) => {
                if (result) {
                    this.search_federation_account ();
                }
                else {
                    alert('Please check the errors in the form');
                }
            });
        }

    },
}
</script>
