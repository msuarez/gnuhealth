<template>
<div id="workplace">
    <div id="leftmenu">
        <button v-on:click='demographics'>
            Demographics
        </button>
    </div>

    <div id="mainarea">
        <div id="restable">
            <table border="1px">
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

    <div id="stderror">
        <ul>
            <li v-for="error of errors" v-bind:key="error.id">
            {{error.message}}
            </li>
        </ul>
    </div>

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
            pfields: [],
            errors: [],
        }
    },
    // Using Axios 

    methods: {
        demographics () {
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
        font-weight: bold;
        text-align: left;
    }
    
    #leftmenu {
    font-weight: bold;
    width: 150px;
    float: left;
    }
    
    #mainarea {
        border: 1px solid #CCCCCC;
        padding: 20px;
        margin-top: 10px;
        background-color: white;
        width: 75%;
        float: right;
    }

    #restable {
        td, tr, th {
            border: 1px solid black;
            padding: 15px;
        }
    }
</style>
