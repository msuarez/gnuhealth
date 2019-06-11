<template>
<div>
    <div>
        <leftmenu/>
    </div>

    <div class="mainarea">
        <div id="new_account">
            <form id="new_fed_account">
            <ul class="gh-form">
                <li>
                <label>Account<span class="red">*</span></label>
                <input type="text" name="account_id" v-model="account_id"
                    placeholder="Federation Account" required />
                </li>
                <li>
                <label>Name</label>
                <input type="text" name="name" v-model="account_info.name"
                    placeholder="First"/>
                <input type="text" name="lastname" v-model="account_info.lastname"
                    placeholder="Last"/>
                </li>
                <li>
                <label>Password<span class="red">*</span></label>
                <input type="password" name="password"
                    v-model="account_info.password" />
                </li>
                <li>
                <label>Roles<span class="red">*</span></label>
                <input type="text" name="roles" v-model="account_info.roles"
                    required />
                <li/>
                <li>
                <button class="ghbutton"
                    v-on:click="create_federation_account()">Create</button>
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
                    "/people/" + this.account_id,
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
