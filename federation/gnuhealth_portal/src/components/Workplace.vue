<template>
<div>
    <leftmenu/>
</div>
</template>

<script>
import Leftmenu from '@/components/Leftmenu.vue'

export default {
    name: "Workplace",

    components: {
        Leftmenu
    },

}
</script>

<style>
    #workplace {
        text-align: left;
        background-color: white;
    }

    .mainarea {
        margin-top: 40px;
        margin-bottom:50px;
        background-color: white;
        width: 75%;
        display: inline-block;
        text-align: left;
        float: right;
        border-left: 1px solid #bedfe4;
        padding-left: 35px;



    }
</style>
