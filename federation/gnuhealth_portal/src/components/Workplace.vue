<template>
<div id="workplace">

    <demographics/>
    <accounts/>
    
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

import Demographics from '@/components/Demographics.vue'
import Accounts from '@/components/Accounts.vue'

export default {
    name: "Workplace",
    components: {
        Demographics,
        Accounts
    }

}
</script>

<style>
    #workplace {
        text-align: left;
    }
    
    .leftmenu {
    font-weight: bold;
    width: 150px;
    float: left;
    }
    
    .mainarea {
        border: 1px solid #CCCCCC;
        padding: 20px;
        margin-top: 10px;
        background-color: white;
        width: 75%;
        float: right;
    }

</style>
