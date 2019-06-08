<template>
<div id="workplace">
    <demographics/>
    <accounts/>
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
        background-color: white;
    }

    .leftmenu {
        float: left;
        border: 1px;
        font-size: 12px;
        width: 200px;
    }

    .leftmenu a {
        background-color: #eee;
        display: block;
        color: black;
        padding: 12px;
        text-decoration: none;
    }
    .leftmenu a:hover { background-color: #ccc; }

    .leftmenu a.active {
        background-color: #4CAF50;
        color: white;
    }

    .mainarea {
        margin-top: 50px;
        background-color: white;
        width: 75%;
        float: right;
    }
</style>
