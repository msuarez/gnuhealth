<template>
<div>
    <div class="leftmenu">
        <button v-on:click='demographics'>
            Demographics
        </button>
    </div>
    <div class="mainarea">
          
    <div v-if="render_form">
        <table class="restable">
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
</template>

<script>
import axios from 'axios';


export default {
    name: "Demographics",
    // Data
    data() {
        return {
            render_form:false,
            people: [],
            pfields: [],
            errors: [],
        }
    },
    // Using Axios 
    methods: {
        demographics () {
            this.render_form = true,
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
            .catch(e => { this.errors.push(e)} );
        },
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
