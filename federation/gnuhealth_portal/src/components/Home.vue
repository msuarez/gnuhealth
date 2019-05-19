<template>
  <div class="home">
    <img alt="GNU Health Federation" src="../assets/logo.png">
    <Welcome msg="Welcome to GNU Health"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Welcome from '@/components/Welcome.vue'

export default {
  name: 'home',
  components: {
    Welcome
  }
}
</script>
