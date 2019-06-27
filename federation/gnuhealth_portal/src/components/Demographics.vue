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
        <button class='ghbutton'
            v-on:click="toggle_form()">Show users</button>
        <div v-if="render_form">
            <table class="u-full-width">
                <th>ID</th><th>Name</th><th>Lastname</th><th>Gender</th><th>DoB</th>
                <th>Marital Status</th><th>Profession</th><th>Active</th>
                <tr v-for="person in people" v-bind:key="person.id">
                    <td > {{ person[0].id }} </td>
                    <td > {{ person[0].name }} </td>
                    <td > {{ person[0].lastname }} </td>
                    <td > {{ person[0].gender }} </td>
                    <td > {{ person[0].dob }} </td>
                    <td > {{ person[0].marital_status }} </td>
                    <td > {{ person[0].profession }} </td>
                    <td > {{ person[0].active }} </td>
                </tr>
            </table>
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
    name: "Demographics",
    // Data
    data() {
        return {
            render_form:false,
            people: [],
            pfields: [],
            axios_errors: [],
        }
    },

    components: {
      Leftmenu
    },

    // Using Axios 
    methods: {
        demographics () {
            axios({
                headers: {
                    'Content-Type': 'application/json',
                },
                method: 'get',
                url: this.$store.state.credentials.thalamus_server + "/people",
                auth: {
                    username: this.$store.state.credentials.fedacct,
                    password: this.$store.state.credentials.password
                },
            })
            .then(response => {this.people = response.data})
            .catch(e => { this.axios_errors.push(e)} );
        },
        toggle_form () {
            this.render_form = !this.render_form;
            if (this.render_form == true) {
                this.demographics();
            }
        }

    },
}
</script>
