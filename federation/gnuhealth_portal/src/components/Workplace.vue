<template>
  <div id="workplace">

        <button v-on:click='search_people'>
            Federation Accounts
        </button>
        <table>
            <tr v-for="person in people" v-bind:key="person.id">
                <td> {{ person }} </td>
            </tr>
        </table>
        
        <ul>
            <li v-for="error of errors" v-bind:key="error.id">
            {{error.message}}
            </li>
        </ul>


</div>
</template>

<script>
import axios from 'axios';


export default {
    name: "Workplace",
    // Datos
    data() {
        return {
            people: [],
            errors: [],
        }
    },
    // Using Axios 

    methods: {
        search_people () {
            axios({
                headers: {
                    'Content-Type': 'application/json',
                },
                method: 'get',
                url: this.$thalamus_server + "/people",
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

<style scoped>
    #workplace {
        background-color: #FFFFFF;
        border: 1px solid #CCCCCC;
        padding: 20px;
        margin-top: 10px;
    }
</style>
