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
        <button class='ghbutton'
            v-on:click="update_demographics_chart()">Analytics</button>

        <div v-if="render_charts">
            <table class="u-full-width">
                <canvas id="gender-chart"></canvas>
            </table>
        </div>

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
// Import Axios library
import axios from 'axios';
// Import Chart.js library
import Chart from 'chart.js';

// Import chart templates
import GenderChartTemplate from '../charts/chart-templates.js'

import Leftmenu from '@/components/Leftmenu.vue'

export default {
    name: "Demographics",

    data() {
        return {
            render_form:false,
            render_charts:false,
            people: [],
            pfields: [],
            axios_errors: [],
            GenderChart: GenderChartTemplate,
        }
    },

    components: {
      Leftmenu
    },

    methods: {
        update_demographics_chart() {
            // Reset the array
            this.GenderChart.data.datasets[0].data.splice(0,2);

            this.render_form = false;
            this.render_charts = true;

            // TODO: Automate info from this.people
            this.GenderChart.data.datasets[0].data.push(12,65);
            this.demographics_analytics('gender-chart', this.GenderChart);
        },

        // Create the Chart with updated data
        demographics_analytics(context, chartData) {
            this.gchart= new Chart(context, {
                type: chartData.type,
                data: chartData.data,
                options: chartData.options,
            });
        },

        demographics() {
            // Using Axios
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
            .then(response => {this.people = response.data; return response.data;})
            .catch(e => { this.axios_errors.push(e)} );
        },

        toggle_form () {
            this.render_form = !this.render_form;
            this.render_charts = false;

            if (this.render_form == true) {
                this.demographics();
            }
        },

    },

}
</script>
