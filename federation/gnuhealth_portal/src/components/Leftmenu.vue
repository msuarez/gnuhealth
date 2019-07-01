<template>
    <div>
        <div class="leftmenu u-full-width">
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
        margin-top: 15px;
        margin-bottom: 25px;
        float: left;
        border: 1px;
        font-size: 17px;
        padding: 15px;
        background-color: #cfdee0;
        border-radius: 4px;
    }

    .leftmenu a {
        background-color: #cfdee0;
        display: block;
        color: inherit;
        padding: 12px;
        text-decoration: none;
        text-align: left;
        font-weight: bold;
        margin-bottom: 4px;
    }
     
    .leftmenu a::before {
        border-style: solid;
        border-width: 0.13em 0.13em 0 0;
        content: '';
        display: inline-block;
        height: 0.35em;
        position: relative;
        top: 0.55em;
        vertical-align: top;
        width: 0.35em;
        left: 0;
        transform: rotate(45deg);
        margin-right:5px;
    }


    .leftmenu a:hover { 
        background-color: #00acc6; 
        border-radius: 4px;
        color: #ffffff;
    }

    div.leftmenu a:hover {
    
        color: #ffffff;
    }

    div.leftmenu a.router-link-exact-active {
        color: #ffffff;
        background-color: #00acc6;
        border-radius: 4px;
    }

</style>
