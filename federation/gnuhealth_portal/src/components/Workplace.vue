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
        margin-top: 50px;
        background-color: white;
        width: 75%;
        display: inline-block;
        float: right;
    }
</style>
