<template>
    <div>
        <div class="leftmenu">
            <router-link to="/demographics">Demographics</router-link>
            <router-link to="/accounts">Accounts</router-link>
        </div>
    </div>
</template>
<script>

export default {
    name: "Leftmenu",
}
</script>

<style>
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
</style>
