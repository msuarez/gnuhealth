<template>
<div>
    <div class="leftmenu">
        <tr><td>
            <a href='#' v-on:click='toggle_form()'>Accounts</a>
        </td></tr>
    </div>
    <div v-if="render_form" class="mainarea">
        <div id="new_account">
            <form id="new_fed_account">
            <label>Federation Account</label>
            <input type="text" name="account_id" v-model="account_id" />
            <br/>
            <input type="text" name="name" v-model="account_info.name" />
            <input type="text" name="lastname" v-model="account_info.lastname" />
            <br/>
            <input type="password" name="password" v-model="account_info.password" />
            <input type="text" name="roles" v-model="account_info.roles" />           
            <button type="button" v-on:click="create_federation_account()">New account</button>
            </form>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';


export default {
    name: "Accounts",
    // Data
    data() {
        return {
            render_form:false,
            account_id: "",
            account_info: {
                name: "",
                lastname: "",
                password: "" ,
                roles: ["end_user"],
                active: true
            }
        }
    },
    // Using Axios 
    methods: {
        create_federation_account () {
            axios({
                headers: {
                    'Content-Type': 'application/json',
                },
                method: 'post',
                url: this.$store.state.credentials.thalamus_server + "/people/" + this.account_id,
                auth: {
                    username: this.$store.state.credentials.fedacct,
                    password: this.$store.state.credentials.password
                },
                data: {
                    id: this.account_id,
                    data: this.account_info
                    },
            })
            .then(response => {this.people = response.data})
            .catch(e => { console.log(e)} );
        },
        toggle_form () {
            this.render_form = !this.render_form;
        }
 
    },
}
</script>

<style>
    .restable {
        table, td, tr, th {
            border: 1px solid black;
            padding: 15px;
        }
    }
</style>
